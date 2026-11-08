# 关键词表和页面蓝图

## 一、关键词表（免费办法为默认）

### 1. 种子词
从用户的产品名、型号体系、买家常问的问题里取 5–10 个种子词，英文为主，用买家的说法（买家说 "camping table"，工厂内部可能叫"户外折叠桌"，以买家为准）。

### 2. 词根组合
`品类` × `材质/规格/结构` × `用途/对象` × `采购修饰词`

| 维度 | 示例（虚构产品：铝合金折叠露营桌；示例，不是事实） |
|---|---|
| 品类 | camping table, folding table, roll up table, side table |
| 材质/规格 | aluminum, lightweight, adjustable height, 4 person |
| 用途/对象 | camping, RV, picnic, beach, outdoor events |
| 采购修饰词 | manufacturer, supplier, wholesale, OEM, custom, bulk, factory, private label |

### 3. 免费扩词渠道（逐个用，记来源）
| 渠道（`keyword_source` 填这一列的简称） | 怎么用 |
|---|---|
| 种子词（seed） | 用户的产品名、型号、买家原话 |
| AI 词根组合（root-combo） | 按上面四个维度组合出来的词；只说明"可能有人搜"，没验证，业务价值照常打 |
| 谷歌搜索联想（google-suggest） | 在搜索框输入种子词 + 空格 / a–z，记下拉建议（能联网时可直接搜索观察） |
| People Also Ask / 相关搜索（paa / related） | 搜索结果页里的问题和底部相关搜索，问题词留给 FAQ 和文章 |
| 竞品官网（competitor） | 看对手的导航、分类名、页面 Title、FAQ——他们在打什么词 |
| B2B 平台搜索框（b2b-search） | 平台站内搜索联想反映买家常用叫法 |
| Reddit / 行业论坛 / 问答（forum） | 买家真实痛点和比较类问题 |
| Google Trends（trends） | 比较几个叫法谁更常用、有没有季节性 |
| 用户自己的询盘（inquiry） | 买家原话是最好的词，业务价值通常最高 |
| Google Search Console（gsc） | 站上线后最可靠的免费真实数据（展示次数、排名） |
| Google Ads 关键词规划师（ads-planner，可选） | 免费但要有广告账号，只给区间 |
| 付费工具（填工具名，可选） | 有就用，填真实搜索量和难度；没有不影响流程 |

### 4. 每个词打标
`02-keywords.csv` 列：

```
keyword,keyword_source,cluster,intent,business_value_0_3,monthly_volume,volume_source,difficulty,difficulty_source,serp_type,target_url,notes
aluminum camping table manufacturer,root-combo,camping table,find-supplier,3,无量数据,—,—,—,工厂站+B2B平台列表,/,首页主词
roll up table wholesale,google-suggest,roll up table,find-supplier,3,无量数据,—,—,—,—,/products/roll-up-table.html,
how to clean aluminum camping table,paa,care,learn,1,无量数据,—,—,—,文章,(以后的文章),留给运营
```

- **keyword_source**：这个词从哪来（seed / root-combo / google-suggest / paa / related / competitor / b2b-search / forum / inquiry / gsc / ads-planner / 工具名）。SKILL.md 第 4 步"每个词都有来源"指的就是这一列，必须填。
- **volume_source**：搜索量从哪来；没有搜索量就和 monthly_volume 一起写"无量数据 / —"。

- **intent**：learn（了解）/ compare（比较）/ find-supplier（找供应商）/ quote（询价）/ brand（找品牌）。
- **business_value 0–3**：3 = 搜这个词的人会询价（manufacturer/wholesale/OEM/bulk + 品类）；2 = 比较选型；1 = 知识类；0 = 和我们无关（DIY、零售单件、二手）。
- **monthly_volume**：只填真实数据并写来源；没有就写"无量数据"。**不许估数字。**
- **serp_type**：前 10 名主要是什么页（工厂站 / 品牌站 / B2B 平台列表 / 亚马逊 / 文章 / 视频）。决定我们做哪种页才可能上去。

### 5. 优先顺序
业务价值 3 的采购词先做，**哪怕搜索量很小或没数据**——小众 B2B 的通行做法是意图优先于搜索量；再做有量的比较词；纯知识词放最后（容易被 AI 概览直接答掉）。

## 二、页面蓝图（`project/03-blueprint.md`）

### 规则
- **一个词（一个意图）只归一个页**。两个词前 10 名几乎一样，就算同一意图，归同一页。
- 首页 → 带采购属性的品类大词；分类/产品页 → 品类 + 材质/用途；商业页 → OEM/ODM、About & Factory、Contact/Get a Quote、FAQ；问题词 → FAQ 或以后的文章（交给运营）。
- 每页写清"买家在这页要做什么决定"，模块顺序按这个决定排。

### 每个 URL 一节

```markdown
## /products/roll-up-table.html（示例，不是事实）
- 目标词：aluminum roll up table supplier（keywords.csv 第 5 行）
- 次要词：roll up camping table wholesale
- 买家要做的决定：这家能不能按我的尺寸/包装稳定供货？
- Title：Aluminum Roll Up Table Supplier | OEM & Bulk | Trailnest
- Description：Aluminum roll up camping tables for importers and outdoor brands. Custom sizes, logo and OEM packaging. Request specs and a quote.
- H1：Aluminum Roll Up Camping Tables for Wholesale & OEM
- 模块：首屏（大图 + 一句话 + CTA）→ 规格表 → 可定制项 → 应用场景 → 质量和检测 → 条款块 → FAQ → 询价 CTA
- 主 CTA：Request a Quote（带产品名预填）
- 内链：→ 产品中心、→ OEM 页、→ FAQ、→ 相邻产品
- 所需事实：P01、P03、O01（缺）、C01（缺）
```

### 过关检查
- [ ] 没有两个页抢同一个目标词
- [ ] 每个目标词都在 keywords.csv 里，且 `keyword_source` 已填
- [ ] 每页"所需事实"都对到事实库编号；缺的标"缺"，页面放占位
- [ ] 每页都有主 CTA 和至少 2 条内链
