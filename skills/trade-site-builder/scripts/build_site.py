#!/usr/bin/env python3
"""最小静态站生成器（只用 Python 标准库）：页头、页尾、条款块等共用部分只写一份，改一处、重跑，全站一致。

目录约定（默认在项目根的 site-src/，生成到 site/）：
  site-src/
    site.json          全站变量，例如 {"DOMAIN": "https://www.example.com", "BRAND": "[TODO: Brand]", ...}
    partials/*.html    共用片段：head.html、header.html、footer.html、terms.html ……
    pages/**/*.html    每个页面的正文；目录结构 = 网址结构（pages/products/x.html → site/products/x.html）
    static/**          原样复制（assets/、图片、llms.txt、robots.txt……）；.txt 文件里的 {{变量}} 也会替换

JSON-LD 写在页面正文末尾的 <script type="application/ld+json"> 里即可（放 </body> 前也有效），同样能用 {{变量}}。

页面里能用的写法：
  第一行 <!--page {"title": "...", "description": "...", "og_type": "product", "noindex": false} -->
      页面变量（JSON）；生成后这一行会被去掉
  <!-- include: header.html -->   插入 partials/header.html（片段里也可以再 include）
  {{BRAND}}                        先找页面变量，再找 site.json；都没有就原样保留（体检脚本会报出来）
  内置变量：{{ROOT}} 到站点根的相对前缀（"" 或 "../"）、{{PATH}} 页面路径、{{URL}} 页面绝对网址、{{TODAY}}

用法（在项目根运行；路径按你装 skill 的位置换）：
  python3 .claude/skills/trade-site-builder/scripts/build_site.py --init    # 第一次：生成一个能跑的 site-src/ 示例
  python3 .claude/skills/trade-site-builder/scripts/build_site.py           # 生成 site/
  python3 .claude/skills/trade-site-builder/scripts/build_site.py --src site-src --out site

另外自动生成 site/sitemap.xml（列出所有没有 noindex 的页；static/ 里自带 sitemap.xml 时不生成）。
只覆盖它生成的文件，不删除 site/ 里别的东西。
"""
import argparse
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

INCLUDE = re.compile(r"<!--\s*include:\s*([\w./-]+)\s*-->")
VAR = re.compile(r"\{\{\s*([A-Za-z_][\w]*)\s*\}\}")
PAGE_META = re.compile(r"\A\s*<!--page\s+(\{.*?\})\s*-->\s*\n?", re.S)


def expand_includes(text, partials, depth=0):
    if depth > 10:
        sys.exit("include 嵌套超过 10 层，检查是不是互相引用")

    def repl(m):
        f = partials / m.group(1)
        if not f.exists():
            sys.exit(f"找不到片段：{f}")
        return expand_includes(f.read_text(encoding="utf-8"), partials, depth + 1)

    return INCLUDE.sub(repl, text)


def fill(text, vals):
    return VAR.sub(lambda m: str(vals[m.group(1)]) if m.group(1) in vals else m.group(0), text)


def build(src, out):
    cfg = json.loads((src / "site.json").read_text(encoding="utf-8")) if (src / "site.json").exists() else {}
    domain = str(cfg.get("DOMAIN", "https://www.example.com")).rstrip("/")
    today = datetime.date.today().isoformat()
    partials, pages_dir, static = src / "partials", src / "pages", src / "static"
    if not pages_dir.is_dir():
        sys.exit(f"没有 {pages_dir}；第一次用先加 --init")
    out.mkdir(parents=True, exist_ok=True)

    indexable, n = [], 0
    for p in sorted(pages_dir.rglob("*.html")):
        rel = p.relative_to(pages_dir).as_posix()
        text = p.read_text(encoding="utf-8")
        meta = {}
        m = PAGE_META.match(text)
        if m:
            meta = json.loads(m.group(1))
            text = text[m.end():]
        depth = rel.count("/")
        url = domain + "/" + ("" if rel == "index.html" else rel)
        vals = {**cfg, **meta, "ROOT": "../" * depth, "PATH": rel, "URL": url, "TODAY": today}
        vals["ROBOTS"] = '<meta name="robots" content="noindex">' if meta.get("noindex") else ""
        vals["CANONICAL"] = "" if meta.get("noindex") else f'<link rel="canonical" href="{url}">'
        vals.setdefault("og_type", "website")
        html = fill(expand_includes(text, partials), vals)
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        n += 1
        if not meta.get("noindex"):
            indexable.append(url)

    if static.is_dir():
        for f in sorted(static.rglob("*")):
            if f.is_dir():
                continue
            target = out / f.relative_to(static)
            target.parent.mkdir(parents=True, exist_ok=True)
            if f.suffix == ".txt":
                target.write_text(fill(f.read_text(encoding="utf-8"), {**cfg, "TODAY": today}), encoding="utf-8")
            else:
                shutil.copy2(f, target)

    if not (static / "sitemap.xml").exists():
        rows = "\n".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in indexable)
        (out / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "\n</urlset>\n",
            encoding="utf-8")
    print(f"生成 {n} 页 → {out}（sitemap 收录 {len(indexable)} 页）")


# ---------- --init：一个能跑通的最小示例，照着改 ----------
EXAMPLE = {
    "site.json": json.dumps({
        "DOMAIN": "https://www.example.com",
        "BRAND": "[TODO: Brand]",
        "EMAIL": "sales@example.com",
        "EMAIL_TEXT": "[TODO: inquiry email]",
        "ADDRESS": "[TODO: company address in English]",
        "YEAR": str(datetime.date.today().year),
    }, indent=2, ensure_ascii=False) + "\n",
    "partials/head.html": """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{title}}</title>
  <meta name="description" content="{{description}}">
  {{ROBOTS}}
  {{CANONICAL}}
  <meta property="og:type" content="{{og_type}}">
  <meta property="og:title" content="{{title}}">
  <meta property="og:description" content="{{description}}">
  <meta property="og:url" content="{{URL}}">
  <meta property="og:image" content="{{DOMAIN}}/assets/img/og-cover.jpg">
  <link rel="icon" href="{{ROOT}}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{{ROOT}}assets/css/style.css">
</head>
""",
    "partials/header.html": """<body>
  <header class="site-header">
    <div class="container">
      <a class="logo" href="{{ROOT}}index.html">{{BRAND}}</a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
      <nav class="nav" id="nav" aria-label="Main">
        <a href="{{ROOT}}products.html">Products</a>
        <a href="{{ROOT}}contact.html">Contact</a>
        <a class="btn btn--primary" href="{{ROOT}}contact.html">Get a Quote</a>
      </nav>
    </div>
  </header>
""",
    "partials/terms.html": """<div class="table-wrap">
  <table>
    <tbody>
      <tr><th>MOQ</th><td>[TODO: MOQ] — contact us with your spec and we will confirm.</td></tr>
      <tr><th>Samples</th><td>[TODO: sample policy and lead time]</td></tr>
      <tr><th>Lead time</th><td>[TODO: production lead time]</td></tr>
      <tr><th>Payment terms</th><td>[TODO: payment terms]</td></tr>
      <tr><th>Port of loading</th><td>[TODO: port of loading]</td></tr>
      <tr><th>Response time</th><td>[TODO: reply time on business days]</td></tr>
    </tbody>
  </table>
</div>
""",
    "partials/footer.html": """  <footer class="site-footer">
    <div class="container">
      <div><strong>{{BRAND}}</strong><br>{{ADDRESS}}<br><a href="mailto:{{EMAIL}}">{{EMAIL_TEXT}}</a></div>
      <div><a href="{{ROOT}}products.html">Products</a><a href="{{ROOT}}contact.html">Contact</a></div>
      <div><span>© {{YEAR}} {{BRAND}}</span></div>
    </div>
  </footer>
  <div class="mobile-cta"><a class="btn btn--primary" href="{{ROOT}}contact.html">Get a Quote</a></div>
  <script>
    var t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
    t && t.addEventListener('click', function () { var o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o); });
  </script>
</body>
</html>
""",
    "pages/index.html": """<!--page {"title": "[TODO: Category] Manufacturer for Importers | [TODO: Brand]", "description": "[TODO: one sentence on who you are, what you make and for whom.] Request specs and a quote."} -->
<!-- include: head.html -->
<!-- include: header.html -->
  <main class="section"><div class="container">
    <h1>[TODO: who + what + for whom]</h1>
    <p><a href="products.html">View products</a> · <a href="contact.html">Get a quote</a></p>
    <h2>Ordering Terms</h2>
    <!-- include: terms.html -->
  </div></main>
  <script type="application/ld+json">
  {"@context": "https://schema.org", "@graph": [
    {"@type": "Organization", "@id": "{{DOMAIN}}/#org", "name": "{{BRAND}}", "url": "{{DOMAIN}}/", "email": "{{EMAIL}}"},
    {"@type": "WebSite", "@id": "{{DOMAIN}}/#website", "url": "{{DOMAIN}}/", "name": "{{BRAND}}", "publisher": {"@id": "{{DOMAIN}}/#org"}}
  ]}
  </script>
<!-- include: footer.html -->
""",
    "pages/products.html": """<!--page {"title": "Products | [TODO: Brand]", "description": "[TODO: product range in one sentence.] Custom options on request."} -->
<!-- include: head.html -->
<!-- include: header.html -->
  <main class="section"><div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / Products</div>
    <h1>Products</h1>
    <p><a href="products/sample-product.html">[TODO: series name — confirm this series is in your range]</a></p>
  </div></main>
<!-- include: footer.html -->
""",
    "pages/products/sample-product.html": """<!--page {"title": "[TODO: Product] Supplier | [TODO: Brand]", "description": "[TODO: product, key spec, customization, buyer type.] Request a quote.", "og_type": "product"} -->
<!-- include: head.html -->
<!-- include: header.html -->
  <main class="section"><div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="../products.html">Products</a> / [TODO: Product]</div>
    <h1>[TODO: Product with target keyword]</h1>
    <h2>Ordering Terms</h2>
    <!-- include: terms.html -->
    <p><a class="btn btn--primary" href="../contact.html?product=sample-product">Request a Quote for This Product</a></p>
  </div></main>
  <script type="application/ld+json">
  {"@context": "https://schema.org", "@graph": [
    {"@type": "Product", "name": "[TODO: Product]", "description": "[TODO: product description]",
     "brand": {"@type": "Brand", "name": "{{BRAND}}"}, "manufacturer": {"@id": "{{DOMAIN}}/#org"}},
    {"@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "{{DOMAIN}}/"},
      {"@type": "ListItem", "position": 2, "name": "Products", "item": "{{DOMAIN}}/products.html"},
      {"@type": "ListItem", "position": 3, "name": "[TODO: Product]", "item": "{{URL}}"}
    ]}
  ]}
  </script>
<!-- include: footer.html -->
""",
    "pages/contact.html": """<!--page {"title": "Get a Quote | [TODO: Brand]", "description": "Send your product, size and quantity. We reply with questions or a quote."} -->
<!-- include: head.html -->
<!-- include: header.html -->
  <main class="section"><div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / Get a Quote</div>
    <h1>Get a Quote</h1>
    <!-- 询价表单从 templates/contact.html 复制过来 -->
    <p>Email <a href="mailto:{{EMAIL}}">{{EMAIL_TEXT}}</a>.</p>
  </div></main>
<!-- include: footer.html -->
""",
    "pages/404.html": """<!--page {"title": "Page Not Found | [TODO: Brand]", "description": "This page does not exist.", "noindex": true} -->
<!-- include: head.html -->
<!-- include: header.html -->
  <main class="section"><div class="container"><h1>Page not found</h1><p><a href="{{ROOT}}index.html">Back to home</a></p></div></main>
<!-- include: footer.html -->
""",
    "static/robots.txt": "User-agent: *\nAllow: /\n\nSitemap: {{DOMAIN}}/sitemap.xml\n",
    "static/llms.txt": "# {{BRAND}}\n\n> [TODO: one-sentence summary, confirmed facts only]\n\n- [Products]({{DOMAIN}}/products.html)\n- [Get a Quote]({{DOMAIN}}/contact.html)\n",
}


def init(src):
    if src.exists() and any(src.iterdir()):
        sys.exit(f"{src} 已存在且不为空，不覆盖")
    for rel, body in EXAMPLE.items():
        f = src / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(body, encoding="utf-8")
    tpl_assets = Path(__file__).resolve().parent.parent / "templates" / "assets"
    if tpl_assets.is_dir():
        shutil.copytree(tpl_assets, src / "static" / "assets", dirs_exist_ok=True)
    print(f"已生成示例 {src}/；按蓝图改 site.json、partials/、pages/，再不带 --init 运行一次")


def main():
    ap = argparse.ArgumentParser(description="最小静态站生成器：共用片段只写一份")
    ap.add_argument("--src", default="site-src", help="源目录（默认 site-src）")
    ap.add_argument("--out", default="site", help="输出目录（默认 site）")
    ap.add_argument("--init", action="store_true", help="生成一个能跑通的 site-src 示例")
    a = ap.parse_args()
    src, out = Path(a.src).resolve(), Path(a.out).resolve()
    if a.init:
        init(src)
    else:
        build(src, out)


if __name__ == "__main__":
    main()
