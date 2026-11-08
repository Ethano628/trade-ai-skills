# 模板说明

这是**骨架**，不是成品。AI 在第 6 步按 `project/04-design-rules.md` 改颜色、字号、布局和模块顺序，让每个产品的站长得不一样。

| 文件 | 用途 |
|---|---|
| `assets/css/style.css` | 基础样式；改 `:root` 里的变量就能换色板、字体、宽度 |
| `index.html` | 首页骨架（Organization + WebSite 结构化数据） |
| `product.html` | 产品页骨架，复制到 `site/products/<slug>.html`（Product + BreadcrumbList + FAQPage） |
| `contact.html` | 询价页，默认 mailto，可一键切换表单服务 |

三个模板的页头（导航 + Get a Quote 按钮）、页尾、手机底部按钮（`.mobile-cta`）、Open Graph 五项完全一致，只有资源路径前缀不同（产品页在 `products/` 下，用 `../`）。其余页面（products.html、oem.html、about.html、faq.html、thank-you.html、404.html）照 `references/03-page-structure.md` 用同样的页头页尾生成；`sitemap.xml`、`robots.txt`、`llms.txt` 照 `references/06-seo-schema-checklist.md` 生成。

## 共用部分只写一份：生成器

条款块、页头、页尾要"改一处全站一致"，纯静态 HTML 做不到，用自带的 `../scripts/build_site.py`（只用 Python 标准库）：

1. 在项目根运行 `python3 .claude/skills/trade-site-builder/scripts/build_site.py --init`（路径按 skill 安装位置换），得到一个能跑通的 `site-src/`：`site.json`（全站变量）、`partials/`（head、header、footer、terms 片段）、`pages/`（每页正文）、`static/`（assets、robots.txt、llms.txt，原样复制）。
2. 把这里三个模板拆进去：`<head>` 到 `</head>` 进 `partials/head.html`，页头进 `header.html`，页尾和手机按钮进 `footer.html`，条款表格进 `terms.html`；每页只留 `<main>` 里的内容，第一行写 `<!--page {"title": "...", "description": "..."} -->`，用 `<!-- include: header.html -->` 引片段。资源路径写 `{{ROOT}}assets/...`，生成时自动变成 `""` 或 `"../"`。
3. 不带参数再运行一次，生成 `site/` 和 `sitemap.xml`（不含 noindex 页）。之后只改 `site-src/`，改完重跑。

`{{BRAND}}`、`{{EMAIL}}` 这类变量在 `site.json` 里定义后全站替换；没定义的原样保留，体检脚本会报出来。

不用生成器也可以：条款块、页头、页尾在每页逐字相同，改的时候全站搜索替换，改完再搜一次旧说法确认 0 处。

占位约定：
- `{{…}}`：AI 按蓝图和事实库替换的内容，交付时不应残留。
- `[TODO: …]`：缺事实，等用户提供证据；本地预览可以有，**上线前必须为零**。品牌、邮箱的占位写法见 `references/05-copywriting.md`（`[TODO: Brand]`、`sales@example.com`）。
- `.ph` 灰色斜纹框：图片占位，上线前换成真实图片或标注 Illustration 的示意图。
- `https://www.example.com`：域名占位，部署前全站替换。
