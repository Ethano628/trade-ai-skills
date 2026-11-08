# GEO：让 ChatGPT 等 AI 答案提到你

GEO（生成式引擎优化）= 让 ChatGPT、Gemini、Perplexity、Copilot、谷歌 AI 概览等在回答买家问题时提到你、引用你的页面。它和 SEO 是同一套基本功，多三件事：**被引用的写法、去 AI 常引用的地方露脸、实体信息一致**。

## 一、监测（每周，`ops/geo-log.md`）

1. 定一个**固定采购问题集**（10–20 个），用买家口吻，覆盖：
   - 找供应商："Who are reliable manufacturers of 304 stainless kitchen racks in China?"（示例）
   - 比较："304 vs 316 stainless steel for kitchen racks, which is better for humid climates?"
   - 选型/规格："What load capacity should a commercial kitchen wall rack have?"
   - 采购流程："What is a typical MOQ for OEM kitchen racks?"
2. 每周在 2–3 个 AI 助手（开联网搜索）里问同一批问题，记：

| 日期 | 问题 | AI | 提到我们？ | 引用了哪些网址 | 引用的页面有什么我们没有 | 动作 |
|---|---|---|---|---|---|---|

3. 答案会波动，看几周的比例变化，不看单次。

## 二、被引用的内容写法
- 开头一两句直接给答案，带数字、单位、条件。
- 规格、对比、条款用表格；问题用 H2 或 FAQ。
- 写出处（标准编号、检测机构、数据来源），作者/公司信息清楚。
- 有原创信息：测试数据、实拍、真实案例（经同意）、买家常见问题的统计。
- 每个"AI 没提到我们"的问题，都应该有一个页面（或页面里一节）直接回答它。

## 三、去 AI 常引用的地方露脸
- 看监测里 AI 反复引用的第三方站（行业目录、论坛、问答、视频、媒体）——这就是外链和站外露脸的优先清单（接 `06-backlinks-pr.md`）。
- 在这些地方用真人账号、以厂家身份真实回答问题，链接只在有用时放。
- YouTube 视频（工厂、工艺、安装、测试）常被引用，标题和描述写清品牌和产品。

## 四、实体一致（F6）
- 公司英文名、品牌、地址、电话、邮箱、网址在：网站每页页尾、About、Organization 结构化数据、llms.txt、LinkedIn 公司页、YouTube、行业目录、B2B 平台店铺——**逐字一致**。
- Organization 的 `sameAs` 列出所有真实第三方主页。
- 品牌名独特（造词）更容易被 AI 识别为一个实体。

## 五、技术前提
- 被 Bing 收录（ChatGPT 搜索等依赖它），Bing Webmaster 提交 sitemap。
- robots.txt 不屏蔽 AI 搜索爬虫（如 OAI-SearchBot、PerplexityBot、GPTBot、ClaudeBot、Google-Extended，按用户意愿决定）。
- llms.txt 给出站点摘要和关键页面，内容和网站一致。
- 重要内容在 HTML 里，不藏在图片、PDF 或需要点击才加载的脚本里。

## 六、过关标准
- 固定问题集每周有记录。
- 每个没提到我们的问题都有对应动作（补页、补 FAQ、去某个第三方站露脸），并进周计划。
- 实体信息一致性清单全绿。
