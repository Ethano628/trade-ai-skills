# 页面结构模板（B2B 工厂询盘站）

原则：每页先回答"买家在这页要做什么决定"，把帮他做决定的东西放上面；每一屏都有去询价的路。下面是起点，按本产品买家的决定调整顺序。

## 全站共用
- **页头**：Logo（链回首页）、导航（Products / OEM & Custom / Factory / FAQ / Contact）、右侧主按钮 "Get a Quote"。手机端折叠菜单，按钮保留。
- **页尾**：公司英文名、地址（已确认才写）、邮箱、WhatsApp（可选）、主要页面链接、版权年份。不放无关友链。
- **条款块**（全站一份）：MOQ · Samples · Lead time · Customization · Payment terms · Port of loading · Response time。缺的写 "Contact us"，不编。
- 页头、页尾、条款块怎么做到"全站一份"：用 `scripts/build_site.py` 的共用片段，或手工逐字复制并全站搜索替换（见 SKILL.md 第 7 步）。
- **手机底部按钮**：每页都有固定在底部的 "Get a Quote"（模板里的 `.mobile-cta`），询价页指向页内表单。
- **面包屑**：首页以外每页都有。

## 首页 `/`
1. **首屏**：一句话说清"谁 + 做什么 + 给谁"（例：*Aluminum camping tables, made to your spec — for importers and outdoor brands.*）；一张真实产品/工厂大图；主 CTA "Get a Quote"，次 CTA "View Products"。
2. **信任条**：3–4 个可证明的点（已确认才放：年份、认证、出口市场、OEM 能力）。没有证据就少放，不凑。
3. **产品系列**：3–6 张卡片，每张：图、系列名、一句关键规格、链接到产品页。
4. **为什么选我们**：3 个卖点，每个配证据（照片、证书、数字）。
5. **OEM / 定制流程**：4–6 步（询价 → 打样 → 确认 → 生产 → 质检 → 出货），每步写时间（已确认才写）。
6. **工厂和质量**：车间/设备/质检照片 + 简短说明，链到 About & Factory。
7. **FAQ 精选**：4–6 条最常见问题，链到 FAQ 页。
8. **询价 CTA 区**：短表单或按钮 + 回复时效。

## 产品中心 `/products.html`
1. H1 + 一段说明（覆盖哪些品类、能定制什么）。
2. 按买家选型维度分组（用途 / 材质 / 结构），每组卡片网格。
3. 选型帮助：一张对比表（系列 × 关键规格）。
4. 定制说明 + CTA。

## 产品页 `/products/<slug>.html`
1. **首屏**：大图（可多图）+ H1 + 3–5 条要点（规格、材质、定制）+ "Request a Quote for this product"。
2. **规格表**：型号、尺寸、材质、厚度、表面、承重、包装——HTML 表格，不做成图片（AI 和搜索引擎读得到）。
3. **可定制项**：尺寸、表面、Logo、包装、颜色。
4. **应用场景**：图 + 短说明（推断的写成 Typical applications）。
5. **质量和检测**：已确认的检测项、质检流程照片。
6. **条款块**。
7. **FAQ**（本产品相关的 4–8 条，进 FAQPage 结构化数据）。
8. **相关产品** + 询价 CTA。

## OEM / 定制页 `/oem.html`（可选，B2B 品牌买家多时做）
定制范围 → 流程和时间 → 打样政策 → 包装和贴标选项 → 起订量说明 → 案例（经客户同意才写，否则写匿名类型如 "a US outdoor gear brand"——也要真实）→ CTA。

## About & Factory `/about.html`
公司简介（谁、哪年、做什么）→ 工厂（面积、产线、设备，已确认才写）→ 质量控制流程 → 认证（附证书图）→ 团队/联系人（可选，有真人照片和名字更可信）→ 出口和展会（已确认才写）→ CTA。

## Contact / Get a Quote `/contact.html`
1. H1 "Get a Quote" + 回复时效。
2. 询价表单（姓名、公司、邮箱、国家、产品、数量、留言、How did you find us?）。
3. 直接联系：邮箱、WhatsApp（可选）、地址。
4. "What happens next"：3 步说明收到询盘后的流程。

## FAQ `/faq.html`
按分类：Ordering（MOQ、样品、付款）/ Product（材质、规格、定制）/ Shipping（交期、港口、包装）/ Quality（检测、售后）。每个答案第一句直接给答案，再补条件。只写已确认事实，不确定的答 "Contact us with your spec and we will confirm."

## Thank-you `/thank-you.html`（noindex）
确认已收到 + 回复时效 + 推荐看看产品页。不进 sitemap。

## 404 `/404.html`（noindex）
简短说明 + 回首页、产品中心、联系的链接。
