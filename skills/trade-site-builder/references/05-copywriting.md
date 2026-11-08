# 英文 B2B 文案写法

读者是海外采购经理、进口商、品牌方。他们赶时间、怕踩坑、要证据。文案的任务是让他快速判断"这家能不能做、靠不靠谱、怎么联系"。

## 写法
1. **答案先行**：每个区块第一句就给结论，再给条件和证据。
   - ✗ *We are a professional manufacturer with many years of experience dedicated to quality...*
   - ✓ *We make aluminum camping tables to your size and packaging spec. Samples ship in [TODO: days] days.*
2. **具体胜过形容**：写数字、单位、条件（已确认的）。"thick" → "1.2 mm wall thickness"。
3. **买家视角**：多用 you/your（your brand, your spec, your market），少用 we are the best。
4. **短句短段**：一段 2–3 句；规格和条款用表格或列表。
5. **一个页面一个主 CTA**：Get a Quote / Request Samples / Send Your Drawing，动词开头。
6. **自然用词**：目标词放进 Title、H1、首段、一个 H2、图片 alt 各一次即可，不堆砌。
7. **地道英文**：美式拼写为默认（color, aluminum），目标市场是英联邦就统一英式。避免中式英语套话（"Welcome to our website"、"high quality and competitive price"、"win-win cooperation"）。

## 禁用说法（除非有一手证据）
- No.1 / leading / top / best / largest / world-class
- 认证名、检测结论、"FDA approved"、"CE certified"（没文件不写；有文件也写准确：哪项标准、哪个机构）
- 客户名、品牌 Logo 墙（没有客户书面同意不放）
- 产能、面积、员工数、年份、出口国家数（没确认不写）
- 具体报价数字（默认不公开，用 "Request a quote"）
- "100% quality guaranteed"、"lowest price" 这类无法兑现的承诺
- 环保/安全类声明（food-safe、eco-friendly、lead-free）必须有检测依据

## 占位符写法
英文页面用明显的方括号，便于全站搜索：
- `[TODO: factory area in m² — provide proof]`
- `[TODO: certificate name + issuing body]`
- `[TODO: photo — packaging line]`

品牌、联系方式没给时统一这样写（全站、结构化数据、llms.txt 一致，方便一次替换）：

| 缺什么 | 页面文字 | 链接 / 结构化数据里 |
|---|---|---|
| 品牌名 | `[TODO: Brand]` | JSON-LD `"name": "[TODO: Brand]"` |
| 询盘邮箱 | `[TODO: inquiry email]` | `mailto:sales@example.com`；JSON-LD `"email": "sales@example.com"`；表单 `data-to="sales@example.com"` |
| 域名 | — | `https://www.example.com` |
| 公司英文名、地址 | `[TODO: company legal name]`、`[TODO: address]` | JSON-LD 里省略 `address` |
| 电话、WhatsApp | 没给就不放，不占位 | — |

上线前全站搜 `[TODO`、`{{`、`example.com` 三样都必须为零（事实性占位必须补齐或删掉该句）；体检脚本会分三类列出来。

## 推断怎么写
AI 根据常识推出的用途、场景，用 "Typical applications include…"、"Commonly used in…"，不写成承诺，也不写成客户案例。

## 示例（虚构品牌 Trailnest，仅示范写法；示例，不是事实）

> **H1**: Aluminum Camping Tables, Made to Your Spec
> **Sub**: Roll up tables, folding camp tables and side tables — with custom sizes, printed logo and retail-ready packaging for importers and outdoor brands.
> **CTA**: Get a Quote · View Products
