# 外贸 AI 获客 skill

给中国外贸工厂和外贸人用的两个 AI skill，装进 **Claude Code** 或 **Codex** 就能用：

| skill | 干什么 | 一句话 |
|---|---|---|
| [`trade-site-builder`](skills/trade-site-builder/SKILL.md) | 从零建外贸独立站 | 在空文件夹里，AI 问清你的产品和证据，做出一个能本地预览的英文 B2B 询盘站（首页、产品页、关于工厂、询价表单、FAQ，带基本 SEO 和结构化数据） |
| [`trade-site-ops`](skills/trade-site-ops/SKILL.md) | 独立站运营到出询盘 | 对一个已有网站做体检，出本周运营计划；之后按周跑：关键词和选题、写内容、收录和 GSC、GEO（让 ChatGPT 等 AI 提到你）、外链、询盘转化、周报 |

方法来自真实建站和运营过程的复盘，拿走就能用。

## 适合谁
- 有产品、想做海外 B2B 询盘、不想先花一大笔钱找建站公司的工厂老板和外贸业务员
- 已经有独立站但没询盘、不知道每周该干什么的人
- 帮工厂建站/代运营、想把流程标准化的服务商

不适合：B2C 零售店铺（Shopify 卖货那种）、想"一键生成几百个页面刷排名"的人——这套方法明确不干这个。

## 怎么装

先把这个仓库下载到本地（`git clone` 或下载 ZIP 解压）。

**Claude Code**（二选一）：
```bash
# 所有项目都能用
mkdir -p ~/.claude/skills && cp -r skills/trade-site-builder skills/trade-site-ops ~/.claude/skills/
# 只在某个项目里用
mkdir -p 你的项目/.claude/skills && cp -r skills/trade-site-builder skills/trade-site-ops 你的项目/.claude/skills/
```

**Codex**：
```bash
mkdir -p ~/.codex/skills && cp -r skills/trade-site-builder skills/trade-site-ops ~/.codex/skills/
```

装好后重启 Claude Code / Codex。说"建站""做独立站""体检我的网站""出本周运营计划"等会自动触发，也可以直接点名："用 trade-site-builder……"。

## 5 分钟跑通

1. 新建一个空文件夹，在里面打开 Claude Code 或 Codex。
2. 说一句：

```
用 trade-site-builder 快速模式，给我的工厂建一个英文询盘站。我们做不锈钢厨房挂架，卖给美国的进口商和亚马逊品牌卖家。
```

3. AI 会一次性问你不超过 10 个问题（答不上的可以跳过，它会留占位符，不会编）。
4. 做完后预览：

```bash
cd site
python3 -m http.server 8000
# 浏览器打开 http://localhost:8000
```

5. 网站有了之后，试第二个 skill：

```
用 trade-site-ops 给 site/ 做一次体检，出本周计划。
```

> 上面例子里的产品只是示例。换成你自己的产品就行。

## 目录说明

```
README.md
LICENSE
skills/
  trade-site-builder/
    SKILL.md                 # 11 步建站流程：每步做什么、产出、过关标准
    references/              # 问题清单和事实库、关键词和蓝图、页面结构、设计规则、
                             # 英文文案、SEO/结构化数据、表单和部署、上线前检查
    templates/               # 基础 HTML/CSS 骨架（首页、产品页、询价页）
    scripts/
      build_site.py          # 最小静态站生成器：页头、页尾、条款块只写一份（只用 Python 标准库）
  trade-site-ops/
    SKILL.md                 # 地基六件事、选题六列、每周冲刺、默认"体检 + 本周计划"
    references/              # 体检清单、关键词和主题地图、写作和事实卡、收录和 GSC、
                             # GEO、外链和公关、询盘转化、周报月报模板
    scripts/
      audit_static_site.py   # 静态站机器体检（只用 Python 标准库）
examples/
  README.md                  # 示例站说明（虚构产品，跑通测试生成）
```

## 核心规矩（两个 skill 都守）
- **不编造事实**：认证、产能、客户名、报价、"No.1"——你没给证据的一律不写，页面上留 `[TODO: …]` 占位，补齐前不许上线。
- **先数据后页面**：先有关键词表再定页面，一个搜索意图一个页面，不批量造近似页。
- **不依赖付费工具**：默认用免费办法（Google Search Console、Bing Webmaster、谷歌搜索联想、竞品官网观察、PageSpeed Insights）；Semrush、Ahrefs 等付费工具是"有就用"。
- **对外动作你本人做**：买域名、注册账号、部署、发外链、回客户，由你操作；AI 写稿、给步骤。

## 限制
- 生成的是**静态站**，适合 10–50 页的工厂询盘站；要几百个 SKU 的在线目录、多语言、会员系统，需要再接 CMS 或开发。
- 图片要你自己提供（实拍最好）；没有图时页面上是标注清楚的占位框。
- 默认询价表单是 `mailto:`，依赖访客电脑有邮件客户端；正式上线建议换成表单服务（文档里有步骤）。
- 关税、法规、认证要求 AI 不能代答，要问你的货代或报关行。
- 不承诺排名和询盘数字。SEO/GEO 见效通常以月计。
- AI 的输出要你过目：尤其是事实和对客户的说法。

## 答疑和交流
- **本仓库不提供免费答疑**，Issue 里的使用咨询不保证回复。
- 想交流、看实操视频：关注抖音 / B站 **Ethan亦凡**，社群入口见主页。
- 发现 bug 或方法上的错误，欢迎提 Issue 或 PR（写清复现步骤）。

## 已知问题（下一版改）

- 建站和运营两个 skill 同一天各跑一次体检，都会写 `ops/audit-日期.md`，后跑的会覆盖先跑的；需要两份时手动改名。
- "H1 含目标词"目前到运营 skill 才检查，建站阶段的上线清单还没查。
- `build_site.py --init` 示例、联系页模板和文案参考里的占位写法、页尾条款块还有几处不完全一致。
- 404 页放在子路径下时相对链接会错；部署在域名根目录没问题。
- 没确认能不能做 OEM 时 OEM 页怎么写、欧洲市场用美式还是英式拼写，还没有规则。
- 运营 skill 默认网站已经上线；本地还没上线的站，体检里"没域名、没收录"会被标成 P0，这是正常提醒。

`examples/demo-site/` 是用虚构产品（竹制砧板，卖欧洲）在干净目录里用快速模式实测跑出来的，所有 `[TODO: …]` 都是故意留给你补的占位符。预览：`cd examples/demo-site && python3 -m http.server 8000`。

## 推荐配合使用（第三方，本仓库不收录其内容）
| 名称 | 用途 | 出处 |
|---|---|---|
| Firecrawl skills / CLI | 抓取竞品网站、批量读页面，做竞品和外链研究时省事 | https://github.com/firecrawl/skills 、https://github.com/firecrawl/cli |
| Anthropic 官方 skills（如 frontend-design） | 提升页面视觉设计质量 | https://github.com/anthropics/skills |

第三方 skill 的许可证和使用条款以各自出处为准。

## 许可证
[MIT](LICENSE) © 2026 Ethan亦凡
