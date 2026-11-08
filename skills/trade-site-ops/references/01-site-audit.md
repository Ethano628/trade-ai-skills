# 站点体检清单

每条问题写进 `ops/audit-YYYY-MM-DD.md`，格式：

| # | 部分 | 问题 | 严重度 | 位置 | 怎么改 | 改完看哪个数 |
|---|---|---|---|---|---|---|

严重度：**P0** 阻止收录或直接丢询盘 / **P1** 影响排名或信任 / **P2** 优化项。

静态站先跑体检脚本（只用 Python 标准库）。在项目根运行，脚本路径按 skill 安装位置换：

```
python3 .claude/skills/trade-site-ops/scripts/audit_static_site.py site > ops/audit-YYYY-MM-DD.md
# 可选：--domain https://www.yourbrand.com   --banned "a,b"   --banned-file ops/banned-phrases.txt
```

它列出机器能查的问题：title/description（长度不计 `[TODO: …]`）、H1、canonical、Open Graph、图片 alt/尺寸、JSON-LD、死链、孤立页、禁用说法（默认 No.1 / best in the world / guaranteed / FDA approved 等，可追加）、sitemap 漏列或多列、robots.txt、llms.txt 链接，以及三类占位（`[TODO…]`、`{{…}}`、`example.com`，HTML 注释不计）。下面没被脚本覆盖的项（面包屑、内容质量、事实、实体一致性、转化）人工判断。

## 一、技术（能不能被抓、被收录、被理解）

**P0 级先查**
- [ ] 全站或重要页误加了 `noindex`（meta robots 或 HTTP 头）
- [ ] robots.txt 屏蔽了重要目录、CSS/JS，或误屏蔽 Googlebot/Bingbot
- [ ] 首页、产品页返回非 200；有大量 404 或跳转链
- [ ] canonical 指向错误地址（指向首页、指向测试域名、指向 http）
- [ ] 没有 sitemap，或 sitemap 里是 404/noindex/跳转网址
- [ ] 询价表单提交不了、邮件收不到（见 07-conversion）

**P1**
- [ ] 每页唯一 title（约 50–60 字符）和 description（约 140–155 字符）；重复的列出来
- [ ] 每页一个 H1，且包含该页目标词
- [ ] http/https、www/非 www 只有一个可访问版本（其余 301）
- [ ] 结构化数据：首页 Organization（+WebSite）、产品页 Product + BreadcrumbList、FAQ 用 FAQPage；JSON 能解析；FAQPage 问答和页面可见文字一致；没有编造的评价/评分
- [ ] 内链：每个商业页至少被 3 个页面链到；没有孤立页；锚文本描述性
- [ ] 图片：alt 描述性；单张不过大；有 width/height
- [ ] 手机端：无横向溢出、按钮可点、字号可读
- [ ] 速度：用 PageSpeed Insights（免费）测首页和一个产品页，记 LCP、CLS、INP；明显差的列原因（大图、阻塞脚本、字体）
- [ ] 薄内容/近似页：多个页面只换了一个词、内容几乎一样 → 合并
- [ ] 标签页、作者页、站内搜索结果页、空分类页：不该被收录的加 noindex 并移出 sitemap
- [ ] llms.txt 存在且和网站一致；robots.txt 没误屏蔽 AI 爬虫（除非用户有意）

**P2**
- [ ] Open Graph 完整；favicon
- [ ] 面包屑
- [ ] 404 页有用（带导航）
- [ ] 外部链接打开方式、无失效外链

## 二、内容（买家能不能在这里做决定）
- [ ] 首屏一句话说清"谁、做什么、给谁"
- [ ] 每个产品页有 HTML 规格表、可定制项、条款（MOQ/样品/交期/付款/港口/回复时效）、FAQ、询价 CTA
- [ ] 答案先行：段落第一句就是结论
- [ ] 每个数字、认证、客户名能在事实卡找到证据；没有 No.1/leading/best 这类无证据说法
- [ ] 没有中式英语套话（"Welcome to our website"、"high quality and competitive price"）
- [ ] 每页对应一个目标词，没有两页抢同一个词（同一个词 GSC 里两个网址轮流出现 = 自相残杀）
- [ ] 有没有"问题词"内容（买家选型、比较、规格、安装、标准）——常被 AI 答案引用

## 三、实体和信任
- [ ] 公司名、品牌、地址、电话、邮箱：网站各页、结构化数据、llms.txt、LinkedIn/YouTube/目录页完全一致
- [ ] About 页有真实工厂照片/视频、成立时间、团队（已确认的）
- [ ] 证书有图、写清标准和机构；检测报告可下载或可索取
- [ ] 有真实联系人（名字、职务）更好
- [ ] 第三方主页数量（LinkedIn 公司页、YouTube、行业目录、B2B 平台店铺）——0 个是 P1

## 四、询盘转化
见 `07-conversion.md`，体检时至少查：每个商业页有 CTA、表单真实提交通过、邮箱明文可见、回复时效写了且做得到、有 "How did you find us?" 字段。

## 体检报告结尾
- **最重要的 3 个问题**（按对询盘的影响排）
- **AI 已修复**（列文件和改动，怎么撤回）
- **需要用户本人做**（导出数据、提供证据、后台操作）
- **进本周计划的项**
