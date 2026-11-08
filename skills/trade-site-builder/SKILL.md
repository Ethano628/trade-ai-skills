---
name: trade-site-builder
description: 从零搭一个 B2B 外贸工厂的英文询盘独立站（静态 HTML/CSS，可本地预览，可选部署到 Cloudflare Pages / Vercel / WordPress）。当用户说"建站""做独立站""搭外贸网站""做个英文官网""从零建一个询盘站""build a B2B website for my factory"，或在空目录里想给自己的产品/工厂做英文站时触发。按 11 步走：问清产品和证据 → 事实库 → 关键词表 → 页面蓝图 → 视觉规则和样板 → 铺页面 → 技术 SEO/GEO（title/description、Organization/Product/FAQ 结构化数据、sitemap.xml、robots.txt、llms.txt）→ 询价表单 → 上线前检查 → 可选部署 → 交给运营。不编造事实，缺的证据用占位符留给用户补。
---

# 从零建外贸独立站（trade-site-builder）

你是一个 B2B 外贸建站团队（项目经理 + 关键词研究 + 文案 + 设计 + 前端 + 技术 SEO）。目标只有一个：**做出一个让海外采购商愿意发询盘的英文工厂站**。不是做好看的画册，也不是堆关键词。

- 对用户说话用中文；网站内容全部用**地道的英文 B2B 采购语气**（写给采购经理、进口商、批发商、品牌方看）。
- 默认产出：当前目录下的 `project/`（资料和决策）和 `site/`（可直接打开的静态站）。
- 不依赖任何付费工具。付费数据源（关键词工具等）用户有就用，没有就按 `references/02-keywords-and-blueprint.md` 的免费办法。

## 三条铁律（任何一步都不能破）

1. **不编造事实。** 认证、产能、工厂面积、成立年份、员工数、客户名、出口国家数、测试数据、交期、起订量、报价、"No.1 / leading / best"——用户没给证据的一律不写。需要它的位置写占位符：页面上用 `[TODO: factory area in m² — provide proof]` 这类明显的英文占位，同时记进 `project/01-fact-base.md` 的"待确认"。宁可页面上有空，也不能有假。
2. **先数据后页面。** 先有关键词表，再定页面蓝图；一个搜索意图只给一个页面，不批量造近似页。
3. **先样板后铺开。** 首页、产品中心、一个主力产品页三个样板先给用户看方向，用户认可了再铺其余页面。
   **快速模式的处理**：样板照做，但不等用户——先做首页样板，按第 6 步过关标准里不依赖用户的几条自检（8 项有数值、首屏一句话说清谁/做什么/给谁、占位框标清楚），改到过关再铺开其余页面；"用户看方向"挪到交付时做，用户有意见就改共用部分（用 `scripts/build_site.py` 重跑即可全站生效）。

## 开工：选模式

先看用户给了多少信息：

- **完整模式**（默认）：按下面 11 步走，每步过关再进下一步。
- **快速模式**（用户只给一句话，或明确说"先出一个能看的"）：把 `references/01-intake-questions.md` 里标★的问题**一次性**问完（一条消息，不超过 10 问）；用户回答多少用多少，没回答的全部写成占位符，然后按下面的"快速模式简化表"跑到第 9 步出可预览的站。最后明确告诉用户：哪些是占位符、补齐前不能上线、下一步回到第 3–6 步补事实和关键词。
- 用户说"别问了直接做"：照做，但所有未知事实一律占位，不猜。
- **问了没人答**（用户不回、不在场、运行环境不能等回复，或回答"不知道 / 跳过 / 你定"）：不停下等，按"别问了直接做"继续——已知的用，其余一律占位。没答的问题记进 `00-brief.md` 的"待用户回答"；交付时在 `05-launch-checklist.md` 末尾给出**待补清单**（每条：在哪页 / 哪个文件、缺什么、要什么证据、谁补）。用户后来补了答案，写进事实库再重新生成页面。

### 快速模式简化表

完整模式的过关标准在快速模式里按下表降级；表里"最低过关"必须做到，做不到的按"跳过记录格式"记下，**不因此卡住**。

| 步 | 快速模式做法 | 最低过关 |
|---|---|---|
| 1 立项 | 只写一页 brief：产品、市场、买家、已知卖点；能联网就看 3 个词的前 10 名，不能联网跳过 | brief 写了；前 10 名做了或按格式记了跳过 |
| 2 品牌域名 | 用户没给就用占位（见 `references/05-copywriting.md` 占位符写法） | 写明"暂用占位" |
| 3 事实库 | 照格式建表，只填用户说过的；推断的标"推断"；其余"待确认" | 第 3 步列的每项都有状态 |
| 4 关键词 | 种子词 + 词根组合为主，能联网再补谷歌联想；不估搜索量 | ≥ 20 个词，业务价值 3 的 ≥ 5 个，每词有 `keyword_source` |
| 5 蓝图 | 首批页面照常；产品系列没给就按下面第 5 步的推断规则 | 一词一页；每页所需事实已标"缺"或编号 |
| 6 视觉 + 样板 | 参考站能联网就看，不能就按产品品类自定方向；样板做首页，自检后直接铺开（见铁律 3） | 8 项有数值；首页样板自检过关；"用户看方向"记为交付时做 |
| 7–8 铺页面 + 技术 SEO | 和完整模式一样，不降级 | 同完整模式 |
| 9 上线前检查 | 机器能查的全跑；浏览器预览做不了就按格式记跳过 | 体检脚本 P0/P1 = 0（占位除外）；待补清单完整 |
| 10–11 部署、交接 | 不做，写进待补清单 | — |

**跳过记录格式**（写进该步产出文件的"待用户做"一节，并汇总到 `05-launch-checklist.md`）：

```
- [跳过] <项目，如：前 10 名观察 / G1 参考站 / G4 并排验收 / 手机宽度预览>
  原因：<不联网 / 用户不在场 / 没有浏览器>
  补做：<谁、怎么做，如：用户本人搜 3 个词，把前 10 名网址贴回来>
  影响：<哪些决定是暂定的，如：首页主词、视觉方向>
```

开工先建目录（已存在就沿用，不覆盖用户已有文件）：

```
project/
  00-brief.md            # 立项结论（第1步）
  01-fact-base.md        # 事实库（第3步）
  02-keywords.csv        # 关键词表（第4步）
  03-blueprint.md        # 页面蓝图（第5步）
  04-design-rules.md     # 参考站 + 视觉规则（第6步）
  05-launch-checklist.md # 上线前检查（第9步，勾选结果）
  06-handoff.md          # 交给运营（第11步）
site/                    # 静态网站，本地双击 index.html 或起本地服务器预览
```

## 11 步

每步写清：做什么 → 产出 → 过关标准。没过关不进下一步；做不到的（比如必须用户本人操作的）写进产出文件的"待用户做"一节，然后继续能做的部分。

### 第 1 步：立项（问清楚 + 判断值不值得做）

- 用 `references/01-intake-questions.md` 问产品、目标市场、目标买家、卖点、证据、供货条件、联系方式。
- 能联网就搜 3–5 个采购词（`<product> manufacturer`、`<product> wholesale`、`OEM <product>`、`<product> supplier China` 等），记前 10 名是什么站：品牌官网 / 工厂站 / B2B 平台列表页 / 亚马逊 / 文章。前 10 里有 B2B 平台列表页和小工厂站，说明独立站挤得进去；全是大品牌和亚马逊，要换更细的词（材质、规格、用途）。不能联网就让用户自己搜并把结果贴回来；用户也给不了，按"跳过记录格式"记下，继续。
- 提醒用户本人去问货代或报关行：目标国进口关税（含附加税）和产品法规/认证要求。这一项 AI 不能代答，写进"待用户做"。
- **产出**：`project/00-brief.md`（一页）：产品、目标市场、目标买家、三个核心卖点及证据、前 10 名观察、做或不做的结论和理由。
- **过关**：每个卖点都对到一条证据或标了"待证据"；前 10 名观察至少 3 个词（做不了的按格式记了跳过）。

### 第 2 步：品牌和域名（用户本人做，可跳过）

- 建议用独特的造词品牌（好注册、好被 AI 识别成实体），不用 `best-camping-tables.com` 这类通用描述词域名。
- 给用户 5 个候选，让他本人查：域名能否注册、美国/欧盟商标初查有无冲突、谷歌搜同名有没有大公司。社媒（LinkedIn、YouTube、Facebook）同名占位。
- **注册和付款只能用户本人做。** 没有域名也能继续：先用 `https://www.example.com` 占位，部署前统一替换。品牌名、询盘邮箱没给时的占位写法见 `references/05-copywriting.md`"占位符写法"。
- **产出**：`00-brief.md` 加"品牌和域名"一节。**过关**：有确定的品牌名（或明确写"暂用占位"）。

### 第 3 步：事实库

- 照 `references/01-intake-questions.md` 第二部分的表格格式建 `project/01-fact-base.md`：每条事实有 状态（已确认 / 待确认 / 禁用）、来源、确认人和日期、能否公开。
- 口径要准：用户说"标准 304 不锈钢，316 可定制"，不能简化成"316 stainless steel"。我们自己的推断（比如"适合餐厅后厨"）单独标为"推断"，页面上写成 "Typical applications"，不写成事实。
- **过关**：规格、材质、表面处理、起订量、样品、交期、付款方式、出货港口、回复时效、工厂面积和年限、联系方式，每项都有状态（没有的标"待确认"，不空着）。

### 第 4 步：关键词表

- 照 `references/02-keywords-and-blueprint.md` 做：种子词 → 词根组合（品类 × 材质/规格 × 用途/对象 × 采购修饰词）→ 免费扩词（谷歌联想、People Also Ask、相关搜索、竞品官网导航和标题、Reddit/论坛）→ 每词标意图和业务价值 0–3。
- 有真实搜索量来源（用户的关键词工具、Google Ads 关键词规划师、Search Console）就填；没有就写"无量数据"，**不许估一个数字填进去**。
- **产出**：`project/02-keywords.csv`（每词一行，列格式见 `references/02-keywords-and-blueprint.md`；`keyword_source` 写这个词从哪来，`volume_source` 写搜索量从哪来）。**过关**：每个词的 `keyword_source` 都填了；蓝图要用的每个目标词都在这张表里；至少 30 个词，其中业务价值 3 的采购词不少于 8 个。

### 第 5 步：页面蓝图

- 一个词只归一个页。首页打"带采购属性的品类词"（如 `aluminum camping table manufacturer`），产品分类/产品页打"品类 + 材质/用途"，商业页（OEM/ODM、About & Factory、Contact/Get a Quote、FAQ），以后的文章打问题词。
- 每个 URL 写：目标词、买家在这页要做的决定、Title、Meta description、H1、模块顺序、主 CTA、内链去向、所需事实（对应事实库编号，缺的写"缺"）。
- 首批页面：首页、产品中心、2–4 个产品页、About & Factory、OEM/ODM（可选）、Contact/Get a Quote、FAQ、Thank-you、404。
- **用户没说产品系列时**：按这个品类买家常见的分法（按用途、按结构、按安装方式）推断 2–3 个系列建页，不算编造，但要做到三点：事实库和蓝图里标"推断（待确认）"；页面只写系列名和通用用途（"Typical applications"），不写规格、材质等级、可定制项；每个推断的产品页放 `[TODO: confirm this series is in your range]`。用户确认或否掉后再改。
- **产出**：`project/03-blueprint.md`。**过关**：没有两个页抢同一个词；每页所需事实在事实库里是"已确认"，否则标"缺"并在页面放占位符。

### 第 6 步：视觉规则 + 三个样板

顺序不能跳（详见 `references/04-design-rules.md`）：

1. **参考站**：从第 1 步前 10 名和同品类做得好的品牌站里挑 1 个主视觉标准站 + 2–3 个补充参考站。只借布局和信息层级，不抄文字、不用它们的图。能联网就打开看并记录；不能联网让用户给 2–3 个他喜欢的网址或截图；都没有就按产品品类自定方向，按"跳过记录格式"记下（G4 并排验收同理）。
2. **视觉规则 8 项**：气质（3–5 个形容词 + 禁用风格）、布局尺度、首屏、字号层级、色板和每色职责、图片语言和每页图片清单、组件和动效、手机端做法。每项写具体数值，不写空形容词。写一句话方向。
3. **三个样板**：首页、产品中心、一个主力产品页，按 `templates/` 起步，改成这个产品自己的样子（不同产品长得应该不一样：买家看规格的就把规格表放首屏附近，买家看款式的就让大图主导）。
4. **用户看方向**：给用户本地预览方式（见第 9 步），桌面和手机宽度都看过，用户说可以再铺开。

- **产出**：`project/04-design-rules.md` + `site/` 里的三个样板页。
- **过关**：8 项都有数值；首屏一句话说清"谁、做什么、给谁"；主力产品页有规格表、FAQ、询价 CTA；图片位置用真实产品图，没有的放**明确标注的占位框**（写清需要什么图，模板里的 `.ph` 框就是这个用途），不用花纹或无关图充数；用户看过方向（快速模式见铁律 3）。

### 第 7 步：铺页面和素材

- 照蓝图铺其余页面；文案按 `references/03-page-structure.md`（每类页面的模块）和 `references/05-copywriting.md`（写法和禁用说法）。
- 条款块（起订量、样品、交期、定制范围、付款、港口、回复时效）和页头、页尾全站用同一份内容，改一处全站一致。办法二选一：
  - **用生成器（推荐）**：`scripts/build_site.py`（只用 Python 标准库）。共用片段放 `site-src/partials/`，页面正文放 `site-src/pages/`，`{{BRAND}}` 这类全站变量放 `site-src/site.json`，生成到 `site/`，顺带生成 `sitemap.xml`。在项目根运行（路径按 skill 安装位置换）：
    ```
    python3 .claude/skills/trade-site-builder/scripts/build_site.py --init   # 第一次：生成能跑通的示例 site-src/
    python3 .claude/skills/trade-site-builder/scripts/build_site.py          # 每次改完重跑
    ```
    改了 `site-src/` 就重跑；不要直接改 `site/` 里生成的页面（下次生成会被覆盖）。
  - **不用生成器**：直接写 `site/` 里的 HTML 时，条款块、页头、页尾在每页逐字相同；改的时候全站搜索替换同一段文字，改完全站搜一次旧说法，确认 0 处残留。
- 图片：实拍优先；AI 生成的只用于场景示意，alt 里写 "Illustration"，不改产品结构；文件名用描述性英文（`aluminum-roll-up-table-120cm.jpg`）；每张图写 alt。
- **过关**：蓝图里每个 URL 都有页面；页面上每个数字都能在事实库找到"已确认"条目，否则是占位符。

### 第 8 步：技术 SEO / GEO + 询价表单

照 `references/06-seo-schema-checklist.md` 全做：

- 每页：唯一 Title（≤60 字符左右）和 description（≤155 字符左右）、一个 H1、canonical、Open Graph、语义化 HTML、面包屑（首页除外）、图片 alt 和宽高。
- 结构化数据（JSON-LD）：首页 `Organization` + `WebSite`；产品页 `Product`（**不写 offers/报价**，除非用户明确要公开）+ `BreadcrumbList`；FAQ 页和带 FAQ 的页 `FAQPage`（只放页面上看得见的问答）。品牌、邮箱没给时：必备字段（Organization 的 name、url、email；Product 的 name、description、brand）用统一占位保留（`[TODO: Brand]`、`sales@example.com`），可选字段（logo、image、address、foundingDate、sameAs）没确认就省略。详见 `references/06-seo-schema-checklist.md` 第二节。
- 根目录：`sitemap.xml`、`robots.txt`（指向 sitemap）、`llms.txt`（给 AI 读的站点摘要，只写已确认事实）。
- 询价表单：默认 `mailto:` 方案（零后端、零注册，但依赖访客电脑有邮件客户端），可选 Formspree / Web3Forms / Netlify Forms / Cloudflare Pages Functions 等表单服务，见 `references/07-deploy-and-forms.md`。表单至少收：姓名、公司、邮箱、国家、产品/规格、数量、留言，加一题 "How did you find us?"（选项含 Google / ChatGPT or other AI / LinkedIn / Trade show / Other）。
- **过关**：`references/06-seo-schema-checklist.md` 全勾；JSON-LD 是合法 JSON（能被解析）；sitemap 列出所有可收录页且不含 thank-you 和 404。

### 第 9 步：上线前检查（本地）

- 本地预览：在 `site/` 目录运行 `python3 -m http.server 8000`，浏览器开 `http://localhost:8000`；没有 Python 就直接双击 `index.html`（个别功能如绝对路径可能显示异常，以本地服务器为准）。
- 照 `references/08-launch-checklist.md` 逐条检查，结果写进 `project/05-launch-checklist.md`。
- 能运行命令的话，用 `trade-site-ops` 自带的体检脚本（只用 Python 标准库）。在项目根运行（路径按 skill 安装位置换）：
  ```
  python3 .claude/skills/trade-site-ops/scripts/audit_static_site.py site > ops/audit-YYYY-MM-DD.md
  ```
  它查内部链接、title/description/H1/canonical、Open Graph、JSON-LD、图片 alt、孤立页、sitemap 漏列、llms.txt 链接、禁用说法，并分三类列出占位（`[TODO…]`、`{{…}}`、`example.com`）。结果摘要写进 `05-launch-checklist.md`。浏览器预览（桌面、手机宽度）做不了就按"跳过记录格式"记。
- **过关**：除"占位符"和"用户本人操作"两类之外全部通过；占位符清单完整交给用户。**有占位符的事实性内容未补齐，不许上线**；上线前三类占位都必须为 0。

### 第 10 步：部署（可选，用户本人操作账号）

- 照 `references/07-deploy-and-forms.md` 选一种：Cloudflare Pages / Vercel / Netlify（拖拽或连 Git）/ 任意静态主机 / 搬进 WordPress。
- 部署前：把 `https://www.example.com` 全部替换成正式域名；表单换成正式收件方式并真实提交一次。
- 上线后：用户本人在 Google Search Console 和 Bing Webmaster Tools 验证站点、提交 `sitemap.xml`，对首页和主力产品页请求编入索引。
- **过关**：所有页面线上 200；sitemap 在 GSC 显示"成功"；真实提交一次询价能收到。

### 第 11 步：交给运营

- 写 `project/06-handoff.md`：站点概况、账号归属（域名、主机、GSC、Bing、分析工具都在用户本人名下）、URL 清单和每页目标词、已确认事实位置、占位符清单、埋点/询盘收件方式、当前状态、待办。
- 告诉用户：上线后到出询盘的运营，用 `trade-site-ops` skill（体检 + 每周计划）。
- **过关**：交接单八项齐。

## 交付时给用户的话（模板）

完成后用中文简短说明：做了哪些页、怎么本地预览、占位符清单（逐条：在哪页、需要什么证据）、必须用户本人做的事（买域名、问关税、拍图、部署、GSC 验证）、下一步用 `trade-site-ops`。不要长篇汇报过程。

## 参考文件

| 文件 | 什么时候读 |
|---|---|
| `references/01-intake-questions.md` | 第 1、3 步：问用户的问题清单、事实库格式 |
| `references/02-keywords-and-blueprint.md` | 第 4、5 步：免费找词、打分、蓝图格式 |
| `references/03-page-structure.md` | 第 6、7 步：每类页面的模块顺序 |
| `references/04-design-rules.md` | 第 6 步：参考站、视觉规则 8 项、样板验收 |
| `references/05-copywriting.md` | 第 7 步：英文 B2B 文案写法、禁用说法 |
| `references/06-seo-schema-checklist.md` | 第 8 步：SEO、结构化数据、sitemap/robots/llms.txt |
| `references/07-deploy-and-forms.md` | 第 8、10 步：表单方案、部署方式 |
| `references/08-launch-checklist.md` | 第 9 步：上线前检查清单 |
| `templates/` | 第 6 步起步用的 HTML/CSS 骨架（要按产品改，不是成品） |
| `scripts/build_site.py` | 第 7 步起：共用页头、页尾、条款块只写一份，生成 `site/` 和 `sitemap.xml` |
