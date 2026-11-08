# 上线前检查清单

复制到 `project/05-launch-checklist.md` 逐条勾，写结果和发现的问题。分四类：事实 / 页面 / 询盘 / 技术。

## 事实
- [ ] 全站搜 `[TODO`、`{{`、`example.com`：三样都 = 0（上线前必须）；本地预览阶段列出完整待补清单给用户
- [ ] 页面上每个数字、认证、客户名都能在事实库找到"已确认"条目
- [ ] 没有禁用说法（No.1 / leading / best / guaranteed / 无证据的认证和环保声明；体检脚本会查默认列表，可追加）
- [ ] 没有公开报价数字（除非用户明确决定公开）
- [ ] 图片上的文字（含 AI 生成图）逐字核过；AI 示意图 alt 含 "Illustration"
- [ ] 公司名、品牌、地址、邮箱全站一致

## 页面
- [ ] 蓝图里每个 URL 都有页面，导航能到达所有主要页
- [ ] 首屏一句话说清谁、做什么、给谁
- [ ] 每个产品页有规格表（HTML 表格）、FAQ、询价 CTA
- [ ] 条款块全站一致
- [ ] 桌面（约 1440px）和手机（约 390px）都看过：不横向溢出、按钮可点、字号可读、手机底部 Get a Quote 按钮每页都在（没有浏览器就按 SKILL.md"跳过记录格式"记）
- [ ] 每页至少 2 条内链，没有死链，没有孤立页（没有任何页链到它）
- [ ] 占位图全部替换成真实图或 AI 示意图（上线前）

## 询盘
- [ ] 表单字段：姓名、公司、邮箱、国家、产品、数量、留言、How did you find us?
- [ ] 真实提交一次：邮件到、内容完整、能回复
- [ ] 提交后跳到 thank-you 页（表单服务方案）或打开邮件客户端（mailto 方案）
- [ ] 页面上有明文邮箱作为后备；WhatsApp 链接（如有）格式 `https://wa.me/<国际区号号码>` 能打开
- [ ] 回复时效承诺写了就能做到

## 技术
- [ ] 每页唯一 title、description、一个 H1、canonical（绝对地址、正式域名）
- [ ] JSON-LD 全部能解析；首页 Organization+WebSite，产品页 Product+BreadcrumbList，FAQ 页 FAQPage
- [ ] sitemap.xml 列全可收录页，不含 thank-you/404；robots.txt 指向 sitemap，没误屏蔽
- [ ] llms.txt 存在，内容和网站一致
- [ ] thank-you、404 有 noindex
- [ ] 图片有 alt/width/height，单张一般不超过约 300KB；首屏以外 lazy
- [ ] favicon 存在
- [ ] HTTPS（部署后）；http 和非 www/www 只保留一个版本（部署后在主机设置跳转）

## 可自动跑的检查（能执行命令时）
用 `trade-site-ops` 自带的体检脚本，在项目根运行（脚本路径按 skill 安装位置换，常见是 `.claude/skills/`、`~/.claude/skills/` 或 `~/.codex/skills/`）：

```
python3 .claude/skills/trade-site-ops/scripts/audit_static_site.py site > ops/audit-YYYY-MM-DD.md
```

它查：title/description/H1/canonical（缺失、重复、长度，长度不计 `[TODO: …]`）、Open Graph、JSON-LD 解析、图片 alt/尺寸、死链、孤立页、禁用说法、sitemap 漏列或多列、robots.txt、llms.txt 链接，并分三类列出占位。没装 trade-site-ops 时，至少手工跑一遍：解析每段 JSON-LD、检查每个 `href`/`src` 指向的本地文件存在、`grep -rnE "\[TODO|\{\{|example\.com" site/`。

## 待补清单（快速模式和"问了没人答"时必填，放本文件末尾）

| # | 在哪（页面 / 文件） | 缺什么 | 要什么证据 | 谁补 |
|---|---|---|---|---|

跳过的检查（前 10 名、参考站、并排验收、手机预览等）按 SKILL.md"跳过记录格式"列在这里。
