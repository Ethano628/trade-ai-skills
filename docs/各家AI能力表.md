# 国内能直接用的 AI 工具能力表（给工厂老板装 skill 用）

> 版本 v1.0 · 查证日期 2026-11-08 · 整理：AI 助手 · 审核：未审
> 依据：各家**官方文档 / 官方帮助中心 / 官方定价页**；第三方文章只作旁证，并标"〔旁证〕"。查不到的写"未核"，不猜。
> 这些产品更新很快，价格和入口以你打开时官方页面为准。

## 先看结论

1. **能原生装 skill（上传 SKILL.md 文件夹或 zip，几乎原样能用）**：豆包电脑版（豆包工作）、腾讯 WorkBuddy、扣子（coze.cn）、千问办公 QwenWork、QoderWork CN、Kimi（Kimi Work 桌面端）、Accio Work；编程类的 TRAE 国内版、腾讯 CodeBuddy、Qoder CN（原通义灵码）也都原生支持。
2. **适合"建智能体 + 传知识文件 + 粘贴指令"**：扣子（智能体编排：人设与回复逻辑 + 知识库）；WorkBuddy 的"资料库"也能放知识文件。其余通用智能体大多是"对话里上传文件 + 装 skill"的用法，没有单独的"系统提示词"框（或未核）。
3. **只能复制粘贴提示词**：DeepSeek 网页版（无 skill、无智能体、文件上传时有时无）；腾讯元宝、智谱清言网页版的 skill 导入未核，按"只能粘贴"对待最稳。
4. **今天就能免费跑通"从零建英文外贸网站（多页 HTML + 预览）"的推荐**：
   - **首选 腾讯 WorkBuddy**：官方文档写明能生成网站应用、右侧预览、说一句"发布"就拿到公网链接；能上传本地技能包；免费版每月 500 积分；国内站点。
   - **次选 豆包电脑版（工作模式）**：官方帮助中心写明能"上传技能"（含 skill.md 文件或文件夹）、能"发布网页应用"；免费版有体验额度。
   - 两者的免费额度够不够做完一整站**未实测**，额度用完就等第二天/下月或换另一家接着做。

---

## 一、办公 / 通用智能体

| 工具 | 装 skill（SKILL.md） | 知识文件 / 知识库 | 自定义指令 | 生成下载文件 / 跑代码 / 网页预览部署 | 海外网络 | 免费额度 | 官方链接 |
|---|---|---|---|---|---|---|---|
| 豆包电脑版（豆包工作） | **支持**。插件·技能·伙伴 → 技能 → + 添加 → 上传技能（文件或文件夹，须含 skill.md 且开头有 YAML 名称和描述） | 对话上传文件；企业版有"企业知识" | 可"与豆包对话新建技能"写指令；单独系统提示词框未核 | 生成文件：是（PPT、表格等，见官方场景）；跑代码：未核；网页：官方场景含"发布网页应用" | 不需要（国内站） | 有免费体验额度，具体数未核；付费 68/200/500 元/月〔旁证〕 | [帮助：使用技能](https://www.doubao.com/work/docs/zh-cn/articles/081010973544-skills) |
| 腾讯 WorkBuddy | **支持**。技能板块 → 添加技能 → 上传技能，拖拽或选择本地技能包 | **资料库**（免费版 5GB）；可接 ima、乐享知识库 | 技能/专家扩展；单独系统提示词框未核 | 生成文件：是；网页：能生成网站应用、右侧预览、"分享"或说"发布"得独立链接 | 不需要（国内站） | 免费体验版每月 500 积分；标准版 99 元/月 | [官网](https://www.workbuddy.cn/) · [技能](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) · [网站发布](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/App-Publishing/Web-App) · [定价](https://www.codebuddy.cn/docs/workbuddy/Pricing) |
| 扣子（coze.cn，原扣子空间 + 开发平台） | **支持**。技能为 SKILL.md 文件夹格式；可"上传技能包"（.skill 或 .zip），扣子 AI 会帮补全格式；桌面端可"从个人设备添加技能" | **知识库**（智能体可挂） | **支持**（智能体"人设与回复逻辑"） | 生成文件：是；扣子编程可开发并部署应用/技能；网页预览部署细节未逐项核 | 不需要（国内站） | 个人免费版每天登录领 1500 积分（当天有效）；进阶版 39.9 元/月；11-12 起新购价格调整 | [技能概述](https://docs.coze.cn/guides_skill_overview) · [技能 FAQ](https://docs.coze.cn/guides_skill_faq) · [对话中用技能](https://docs.coze.cn/cozespace/using_skills) · [套餐升级公告](https://docs.coze.cn/guides_20260119_coze_premium_upgraded) |
| 千问办公 QwenWork（阿里，钉钉体系） | **支持**。扩展 → 技能 → 安装技能，上传 SKILL.md 及辅助文件；也可把仓库链接发给它自动安装 | 网盘；企业知识未逐项核 | 未核 | 生成文件：是（docx/pdf/pptx 内置技能）；官方文档目录有"网页发布" | 不需要 | 有个人版，免费额度未核 | [技能](https://qwenwork.cn/docs/features/skills) · [阿里云帮助](https://help.aliyun.com/zh/qwenwork/skills) |
| 千问 App / 千问电脑版 | 未核（官方说向第三方 Skill 开放，个人上传入口未查到） | 对话上传文件 | 未核 | 未核 | 不需要 | 免费，额度未核 | [千问 AI 平台技能市场](https://www.qianwenai.com/hub/skills) |
| QoderWork CN（阿里，原灵码家族的办公桌面版） | **支持**。扩展 → 技能 → 安装技能，上传 SKILL.md 及辅助文件；或发仓库链接让它装 | 未核 | 未核 | 未核 | 不需要 | 未核 | [技能](https://help.aliyun.com/zh/lingma/qoderwork-cn/user-guide/skills) |
| Kimi（含 Agent / OK Computer、Kimi Work） | **支持**。网页端：贴开源技能的 GitHub 链接安装、或上传文档/对话生成技能；**Kimi Work 桌面端**可上传本地 .zip 或 .md 技能文件 | 对话上传文件（建技能时每次最多 3 个、单个 100MB） | 未核 | Agent 交付物含完整文件、**已部署网页**、可下载 ZIP；一般一次只出一个文件 | 不需要（有大陆人民币价格页） | 免费档 Adagio：Agent 额度约 6 个、并发 1 | [技能](https://www.kimi.com/features/skills) · [Agent 功能与限制](https://www.kimi.com/en/help/agent/agent-features-and-limits) · [会员价格](https://www.kimi.com/zh-cn/help/membership/membership-pricing) |
| Accio Work（阿里国际） | **支持**。Install Local Skill → 选技能所在文件夹；右上角 Upload 可导入技能包 | 处理本地工作区文档；无单独知识库说明 | 未核 | 生成文件：是（表格、报告等）；网页/部署：未写 | 未核（官方未写；排障建议"关 VPN 重试"）；可用阿里国际站账号登录 | 免费每 24 小时 20 credits；新用户一次性 500（7 天）；Pro $19.9/月 | [帮助中心](https://www.accio.com/wow/doc-help-center.html) |
| Accio（采购搜索） | 未核 | 未核 | 未核 | 未核 | 未核 | 未核 | [官网](https://www.accio.com/) |
| 腾讯元宝 | 未核（电脑版有"专业技能"描述，未见用户上传入口） | 对话上传文件；接入 ima 知识库作信源〔旁证〕 | 未核 | Agent 可生成 PPT/Word/Excel/PDF/HTML〔旁证〕 | 不需要 | 免费，额度未核 | [官网](https://yuanbao.tencent.com/) |
| MiniMax Agent | 未核（有技能市场和"技能创建器"，本地上传入口未查到） | 输入框可上传 PDF、PPT、音视频、zip | 未核 | 官方指南：网页类任务完成后给出**网页部署链接**可分享 | 不需要（国内站 minimaxi.com） | 新用户送积分，数额说法不一，未核 | [技能创建器](https://agent.minimaxi.com/skill-creator) |
| 智谱清言 / AutoGLM / AutoClaw（澳龙） | AutoClaw 内置 50+ 技能、有技能市场 ClawHub；本地 SKILL.md 导入步骤未核 | 未核 | 智谱清言有"智能体定制"〔旁证〕，步骤未核 | AutoClaw：文档生成、浏览器自动化；网页部署未核 | 不需要 | 未核 | [AutoClaw](https://autoclaw.zhipuai.cn/) · [智谱清言](https://chatglm.cn/) |

## 二、国内编程类（会用电脑的人用；也能生成网站）

| 工具 | 装 skill | 知识文件 | 自定义指令 | 文件 / 代码 / 网页预览 | 海外网络 | 免费额度 | 官方链接 |
|---|---|---|---|---|---|---|---|
| TRAE 国内版（含 SOLO） | **支持**。设置 → 技能与命令 → 技能 → 创建 → 选全局/项目 → 导入本地技能，上传 SKILL.md 或含它的 .zip | 项目文件即上下文 | 支持（规则） | 写文件、跑代码：是（IDE）；本地预览：是（IDE 常规能力，未逐项核） | 不需要 | 免费版每月 500 积分，2 个云端任务并发；Lite ¥49/月起 | [技能文档](https://docs.trae.cn/ide/skills) · [定价](https://www.trae.cn/pricing) |
| 腾讯 CodeBuddy（国内版） | **支持**。设置页右上角"导入 Skill"；或放 `.codebuddy/skills/` | 项目文件 | 支持 | 写文件、跑代码：是 | 不需要 | 体验版每月 500 积分（与 WorkBuddy 同账号共享） | [Skills 文档](https://www.codebuddy.cn/docs/ide/Features/Skills) · [定价](https://www.codebuddy.cn/docs/workbuddy/Pricing) |
| Qoder CN（原通义灵码，2026-05-20 更名） | **支持**。把技能文件夹拷到 `~/.lingma/skills/{名字}/SKILL.md`（或项目 `.lingma/skills/`），重启后输入 `/` 可见；或用内置 `/create-skill` | 项目文件 | 支持 | 写文件、跑代码：是 | 不需要 | 每日可领 100 Credits（活动页）；专业版首购 19.9 元 | [Skills](https://help.aliyun.com/zh/lingma/qoder-cn/user-guide/skills) · [更名说明](https://help.aliyun.com/zh/lingma/product-overview/introduction-of-lingma) · [文档站](https://docs.qoder.cn/) |
| CodeGeeX（智谱） | 未核 | 未核 | 未核 | IDE 插件，有智能体模式〔旁证〕 | 不需要 | 个人免费〔旁证〕 | [官网](https://codegeex.cn/) |

## 三、只能聊天的

| 工具 | 装 skill | 知识文件 | 自定义指令 | 文件 / 代码 / 网页 | 海外网络 | 免费 | 官方链接 |
|---|---|---|---|---|---|---|---|
| DeepSeek 网页版 / App | 不支持（未见入口） | 专家模式 2026-04 加过文件上传（只识别文字），05-14 因资源紧张下线〔旁证：媒体报道〕；现状未核 | 不支持 | 不能生成下载文件、不能跑代码、不能部署；只能输出代码文本让你自己保存 | 不需要 | 免费 | [官网](https://chat.deepseek.com/) |

---

## 怎么用这张表

- **能装 skill 的**：把本仓库 `skills/` 下某个技能文件夹打成 zip（或直接选文件夹）上传。上传前检查 `SKILL.md` 开头有 `---` 包起来的 `name` 和 `description`，这是各家共同的硬要求（豆包、千问 AI 平台、Kimi API 文档都写了）。
- **只能建智能体的**（扣子智能体）：把 `SKILL.md` 正文贴进"人设与回复逻辑"，`references/` 里的文件上传到知识库。
- **只能聊天的**：每次开新对话，先把 `SKILL.md` 全文贴进去，再提需求。

## 来源清单（查证日期 2026-11-08）

官方：
- 豆包工作帮助中心·使用技能：https://www.doubao.com/work/docs/zh-cn/articles/081010973544-skills
- WorkBuddy 官网：https://www.workbuddy.cn/ ；技能：https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market ；网站应用开发与发布：https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/App-Publishing/Web-App ；定价：https://www.codebuddy.cn/docs/workbuddy/Pricing ；总览：https://www.codebuddy.cn/docs/workbuddy/Overview
- 扣子：技能概述 https://docs.coze.cn/guides_skill_overview ；技能 FAQ https://docs.coze.cn/guides_skill_faq ；在扣子对话中使用技能 https://docs.coze.cn/cozespace/using_skills ；订阅套餐升级 https://docs.coze.cn/guides_20260119_coze_premium_upgraded ；套餐与定价 https://docs.coze.cn/cozespace_coze_billing_overview ；技能商店 https://www.coze.cn/skills
- 千问办公技能：https://qwenwork.cn/docs/features/skills ；https://help.aliyun.com/zh/qwenwork/skills
- 千问 AI 平台技能市场：https://www.qianwenai.com/hub/skills ；发布 Skill：https://platform.qianwenai.com/docs/agent-infra/skills/publish
- QoderWork CN 技能：https://help.aliyun.com/zh/lingma/qoderwork-cn/user-guide/skills
- Qoder CN 技能：https://help.aliyun.com/zh/lingma/qoder-cn/user-guide/skills ；产品介绍（更名）：https://help.aliyun.com/zh/lingma/product-overview/introduction-of-lingma ；文档站：https://docs.qoder.cn/
- Kimi 技能：https://www.kimi.com/features/skills ；Agent 功能与限制：https://www.kimi.com/en/help/agent/agent-features-and-limits ；会员价格：https://www.kimi.com/zh-cn/help/membership/membership-pricing
- Accio Work 帮助中心：https://www.accio.com/wow/doc-help-center.html
- TRAE 技能：https://docs.trae.cn/ide/skills ；定价：https://www.trae.cn/pricing
- CodeBuddy Skills：https://www.codebuddy.cn/docs/ide/Features/Skills
- MiniMax Agent 技能创建器：https://agent.minimaxi.com/skill-creator ；使用指南：https://agent.minimaxi.com/docs/user-guide
- 智谱 AutoClaw：https://autoclaw.zhipuai.cn/

旁证（第三方）：
- 豆包付费档位：https://www.cls.cn/detail/2407871
- 腾讯元宝 Agent 生成文件：https://clawpk.net/tutorials/212-yuanbao-agent-office ；元宝电脑版下载页：https://pc.qq.com/detail/1/detail_36661.html
- DeepSeek 专家模式文件上传下线：https://news.qq.com/rain/a/20260514A06DRX00
- CodeGeeX：https://realpython.com/ref/ai-coding-tools/codegeex/
- 智谱清言 App Store 页：https://apps.apple.com/cn/app/id6450893458

## 修改记录

| 日期 | 版本 | 改了什么 | 为什么 | 谁改的 |
|---|---|---|---|---|
| 2026-11-08 | v1.0 | 首版：17 个工具 × 7 列能力 + 四条结论 | 开源 skill 要说明国内各家 AI 怎么装 | AI 助手 |
