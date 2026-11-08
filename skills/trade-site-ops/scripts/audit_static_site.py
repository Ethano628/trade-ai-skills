#!/usr/bin/env python3
"""静态站机器体检（只用 Python 标准库）。

用法（在项目根运行；脚本路径按你装 skill 的位置换，常见是 .claude/skills/ 或 ~/.claude/skills/、~/.codex/skills/）：
  python3 .claude/skills/trade-site-ops/scripts/audit_static_site.py site > ops/audit-YYYY-MM-DD.md
  python3 .claude/skills/trade-site-ops/scripts/audit_static_site.py site --domain https://www.yourbrand.com
  python3 .claude/skills/trade-site-ops/scripts/audit_static_site.py site --banned-file ops/banned-phrases.txt

输出 Markdown 到标准输出；体检报告统一存成 ops/audit-YYYY-MM-DD.md（机器结果放在最前，人工补查接在后面）。
检查：title/description（缺失、重复、长度；长度不计 [TODO: …] 占位）、H1 数量、canonical、noindex、
Open Graph、图片 alt/尺寸、JSON-LD 能否解析及类型、本地死链、孤立页（没有任何页链到它）、
禁用说法（默认列表，可用 --banned / --banned-file 追加）、占位（[TODO…]、{{…}}、example.com 分开计数，HTML 注释不算）、
sitemap（列了不存在的页 / 漏列可收录页）、robots.txt、llms.txt 里的站内链接。
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

# 没有一手证据就不能写的说法（不区分大小写；按整词匹配）。用 --banned / --banned-file 追加。
DEFAULT_BANNED = [
    "No.1", "No. 1", "number one", "#1 manufacturer", "best in the world", "world's best", "world-class",
    "world leading", "world-leading", "leading manufacturer", "industry leader", "largest", "top manufacturer",
    "guaranteed", "100% quality", "lowest price", "best price", "FDA approved", "CE certified",
    "food-safe", "food safe", "eco-friendly", "lead-free", "win-win",
]
OG_REQUIRED = ("og:title", "og:description", "og:type", "og:url", "og:image")
TODO_RE = re.compile(r"\[TODO[^\]]*\]")


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.desc, self.canonical, self.robots = "", None, None, ""
        self.h1 = 0
        self.og = set()
        self.text = []
        self._skip = 0
        self.imgs_no_alt, self.imgs_no_size = 0, 0
        self.links = []
        self.jsonld = []
        self._in_title = False
        self._in_ld = False
        self._ld_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (a.get("name") or "").lower()
            if name == "description":
                self.desc = a.get("content") or ""
            elif name == "robots":
                self.robots = (a.get("content") or "").lower()
            prop = (a.get("property") or "").lower()
            if prop.startswith("og:") and (a.get("content") or "").strip():
                self.og.add(prop)
        elif tag == "link" and (a.get("rel") or "").lower() == "canonical":
            self.canonical = a.get("href")
        elif tag == "h1":
            self.h1 += 1
        elif tag == "img":
            if not (a.get("alt") or "").strip():
                self.imgs_no_alt += 1
            if not (a.get("width") and a.get("height")):
                self.imgs_no_size += 1
            if a.get("src"):
                self.links.append(a["src"])
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._in_ld, self._ld_buf = True, []
        if tag in ("script", "style"):
            self._skip += 1
        elif tag == "link" and a.get("href") and (a.get("rel") or "").lower() in ("stylesheet", "icon"):
            self.links.append(a["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._in_ld:
            self._in_ld = False
            self.jsonld.append("".join(self._ld_buf))
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_ld:
            self._ld_buf.append(data)
        if not self._skip:
            self.text.append(data)


def ld_types(obj):
    out = []
    if isinstance(obj, dict):
        t = obj.get("@type")
        if t:
            out += t if isinstance(t, list) else [t]
        for v in obj.values():
            out += ld_types(v)
    elif isinstance(obj, list):
        for v in obj:
            out += ld_types(v)
    return out


def local_target(root, page, href):
    if re.match(r"^(mailto:|tel:|javascript:|data:|#)", href) or "{{" in href:
        return None
    u = urlparse(href)
    if u.scheme in ("http", "https"):
        return None
    path = unquote(u.path)
    if not path:
        return None
    base = root if path.startswith("/") else page.parent
    target = (base / path.lstrip("/")).resolve()
    if target.is_dir():
        target = target / "index.html"
    return target


def strip_comments(text):
    """把 HTML 注释换成等量空行，行号不变。"""
    return re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)


def visible_len(s):
    return len(re.sub(r"\s+", " ", TODO_RE.sub("", s)).strip(" |-–—"))


def load_banned(args):
    words = list(DEFAULT_BANNED)
    if args.banned:
        words += [w.strip() for w in args.banned.split(",") if w.strip()]
    if args.banned_file:
        for line in Path(args.banned_file).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                words.append(line)
    pats = []
    for w in dict.fromkeys(words):
        pre = r"(?<![\w])" if w[0].isalnum() else ""
        post = r"(?![\w])" if w[-1].isalnum() else ""
        pats.append((w, re.compile(pre + re.escape(w) + post, re.I)))
    return pats


def main():
    ap = argparse.ArgumentParser(description="静态站机器体检")
    ap.add_argument("site", help="站点目录，例如 site")
    ap.add_argument("--domain", default="", help="正式域名；给了就检查 canonical 是否都用它")
    ap.add_argument("--banned", default="", help="追加禁用说法，逗号分隔")
    ap.add_argument("--banned-file", default="", help="追加禁用说法的文件，一行一个，# 开头为注释")
    args = ap.parse_args()
    banned = load_banned(args)
    root = Path(args.site).resolve()
    if not root.is_dir():
        sys.exit(f"目录不存在：{root}")

    pages = sorted(p for p in root.rglob("*.html") if "node_modules" not in p.parts)
    issues = []  # (严重度, 页面, 问题)
    titles, descs = defaultdict(list), defaultdict(list)
    todo_hits = []
    ph_count = {"[TODO…]": 0, "{{…}}": 0, "example.com": 0}
    inbound = defaultdict(set)  # 被链页 → 来源页
    indexable = set()

    for p in pages:
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        pp = PageParser()
        pp.feed(text)
        is_util = rel in ("404.html", "thank-you.html")
        if "noindex" not in pp.robots:
            indexable.add(rel)
        t, d = pp.title.strip(), (pp.desc or "").strip()
        if not t:
            issues.append(("P1", rel, "缺 <title>"))
        else:
            titles[t].append(rel)
            if visible_len(t) > 65:
                issues.append(("P2", rel, f"title 偏长（{visible_len(t)} 字符，不计 TODO 占位）"))
        if not d:
            issues.append(("P1", rel, "缺 meta description"))
        else:
            descs[d].append(rel)
            if visible_len(d) > 160:
                issues.append(("P2", rel, f"description 偏长（{visible_len(d)} 字符，不计 TODO 占位）"))
        if not is_util:
            miss = [k for k in OG_REQUIRED if k not in pp.og]
            if miss:
                issues.append(("P2", rel, "缺 Open Graph：" + "、".join(miss)))
        body = " ".join(pp.text) + " " + t + " " + d
        for w, pat in banned:
            n = len(pat.findall(body))
            if n:
                issues.append(("P1", rel, f"禁用说法「{w}」{n} 处（有一手证据才可保留）"))
        if pp.h1 != 1:
            issues.append(("P1", rel, f"H1 数量 = {pp.h1}（应为 1）"))
        if "noindex" in pp.robots and not is_util:
            issues.append(("P0", rel, "页面带 noindex"))
        if is_util and "noindex" not in pp.robots:
            issues.append(("P2", rel, "工具页建议加 noindex"))
        if not pp.canonical and not is_util:
            issues.append(("P1", rel, "缺 canonical"))
        elif pp.canonical and args.domain and not pp.canonical.startswith(args.domain):
            issues.append(("P0", rel, f"canonical 不是正式域名：{pp.canonical}"))
        if pp.imgs_no_alt:
            issues.append(("P1", rel, f"{pp.imgs_no_alt} 张图片缺 alt"))
        if pp.imgs_no_size:
            issues.append(("P2", rel, f"{pp.imgs_no_size} 张图片缺 width/height"))
        types = []
        for raw in pp.jsonld:
            try:
                types += ld_types(json.loads(raw))
            except json.JSONDecodeError as e:
                issues.append(("P1", rel, f"JSON-LD 解析失败：{e.msg}（第 {e.lineno} 行）"))
        if rel == "index.html" and "Organization" not in types:
            issues.append(("P1", rel, "首页缺 Organization 结构化数据"))
        if rel.startswith("products/") and "Product" not in types:
            issues.append(("P2", rel, "产品页缺 Product 结构化数据"))
        for href in set(pp.links):
            tgt = local_target(root, p, href)
            if tgt and not tgt.exists():
                issues.append(("P1", rel, f"死链/缺文件：{href}"))
            elif tgt and tgt.suffix == ".html" and tgt != p.resolve():
                inbound[tgt].add(rel)
        for i, line in enumerate(strip_comments(text).splitlines(), 1):
            kinds = [k for k, hit in (("[TODO…]", "[TODO" in line), ("{{…}}", "{{" in line),
                                      ("example.com", "example.com" in line)) if hit]
            for k in kinds:
                ph_count[k] += 1
            if kinds:
                todo_hits.append(f"{rel}:{i}: {line.strip()[:120]}")

    for p in pages:
        rel = p.relative_to(root).as_posix()
        if rel != "index.html" and rel in indexable and not inbound.get(p.resolve()):
            issues.append(("P2", rel, "孤立页：没有任何页面链到它"))

    for t, ps in titles.items():
        if len(ps) > 1:
            issues.append(("P1", ", ".join(ps), f"title 重复：{t[:60]}"))
    for d, ps in descs.items():
        if len(ps) > 1:
            issues.append(("P1", ", ".join(ps), "description 重复"))

    for name, sev in (("sitemap.xml", "P0"), ("robots.txt", "P1"), ("llms.txt", "P2")):
        if not (root / name).exists():
            issues.append((sev, name, f"缺 {name}"))
    def url_path(u):
        path = urlparse(u).path.lstrip("/") or "index.html"
        return path + "index.html" if path.endswith("/") else path

    sm = root / "sitemap.xml"
    if sm.exists():
        locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", sm.read_text(encoding="utf-8", errors="replace"))
        listed = set()
        for loc in locs:
            path = url_path(loc)
            listed.add(path)
            if not (root / path).exists():
                issues.append(("P1", "sitemap.xml", f"列了不存在的页：{loc}"))
            if path in ("404.html", "thank-you.html") or (path not in indexable and (root / path).exists()):
                issues.append(("P1", "sitemap.xml", f"不应列入（工具页或 noindex）：{loc}"))
        for rel in sorted(indexable - listed - {"404.html", "thank-you.html"}):
            issues.append(("P1", "sitemap.xml", f"漏列可收录页：{rel}"))
    lt = root / "llms.txt"
    if lt.exists():
        for href in re.findall(r"\]\(([^)\s]+)\)", lt.read_text(encoding="utf-8", errors="replace")):
            u = urlparse(href)
            if u.scheme in ("http", "https") and args.domain and not href.startswith(args.domain):
                continue  # 外站链接不查
            if u.scheme in ("http", "https") and not args.domain and "example.com" not in u.netloc:
                continue
            if not (root / url_path(href)).exists():
                issues.append(("P1", "llms.txt", f"链接指向不存在的页：{href}"))
    rb = root / "robots.txt"
    if rb.exists():
        rtxt = rb.read_text(encoding="utf-8", errors="replace")
        if re.search(r"^\s*Disallow:\s*/\s*$", rtxt, re.M):
            issues.append(("P0", "robots.txt", "存在 Disallow: /（可能屏蔽全站，核对所属 User-agent）"))
        if "sitemap" not in rtxt.lower():
            issues.append(("P2", "robots.txt", "未声明 Sitemap"))

    order = {"P0": 0, "P1": 1, "P2": 2}
    issues.sort(key=lambda x: (order[x[0]], x[1]))
    print(f"# 机器体检：{root.name}\n")
    print(f"- 页面数：{len(pages)}")
    for s in ("P0", "P1", "P2"):
        print(f"- {s}：{sum(1 for i in issues if i[0] == s)} 条")
    print(f"- 占位行：{len(todo_hits)} 行（[TODO…] {ph_count['[TODO…]']} 行、{{{{…}}}} {ph_count['{{…}}']} 行、"
          f"example.com {ph_count['example.com']} 行；HTML 注释不计）\n")
    print("| 严重度 | 位置 | 问题 |\n|---|---|---|")
    for s, where, msg in issues:
        print(f"| {s} | {where} | {msg} |")
    if todo_hits:
        print("\n## 占位清单（上线前三类都必须为零；example.com 是域名和邮箱占位）\n")
        for h in todo_hits[:300]:
            print(f"- {h}")
    print("\n> 机器检查只覆盖可自动判断的项；内容质量、事实、实体一致性、转化见 references/01-site-audit.md 人工补查。")


if __name__ == "__main__":
    main()
