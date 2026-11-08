# 技术 SEO / GEO 清单

## 一、每页
- [ ] `<html lang="en">`，`<meta charset="utf-8">`，`<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] 唯一 `<title>`：约 50–60 字符，目标词靠前，品牌名放最后
- [ ] 唯一 `<meta name="description">`：约 140–155 字符，写给人看，含目标词和一个行动
- [ ] `<link rel="canonical" href="https://www.example.com/<path>">`（绝对地址，部署前替换域名）
- [ ] Open Graph：`og:title`、`og:description`、`og:type`、`og:url`、`og:image`
- [ ] 只有一个 `<h1>`；H2/H3 层级不跳
- [ ] 语义标签：`<header> <nav> <main> <footer>`，表格用 `<table>`，不用图片代替文字
- [ ] 所有 `<img>` 有描述性 `alt`、`width`、`height`；首屏以外加 `loading="lazy"`
- [ ] 面包屑（首页除外）
- [ ] 内部链接用相对或站内绝对路径，没有死链
- [ ] thank-you、404 加 `<meta name="robots" content="noindex">`

## 二、结构化数据（JSON-LD，放 `<head>` 或 `</body>` 前）

**原则**：只写页面上看得见、事实库里已确认的内容；不写 `aggregateRating`/`review`（除非有真实评价）；`offers` 默认不写。

**缺信息时怎么写**（品牌、邮箱还没定是常态，别把 Organization 删成空壳）：

| 类型 | 必备字段：没确认就用统一占位保留 | 可选字段：没确认就省略 |
|---|---|---|
| Organization | `@id`、`url`（`https://www.example.com/`）、`name`（`[TODO: Brand]`）、`email`（`sales@example.com`） | `logo`（有真实 Logo 文件才加）、`address`、`foundingDate`、`numberOfEmployees`、`sameAs` |
| WebSite | `@id`、`url`、`name`（`[TODO: Brand]`）、`publisher` | — |
| Product | `name`、`description`、`brand`（`{"@type": "Brand", "name": "[TODO: Brand]"}`）、`manufacturer` | `image`（有真实图或标注 Illustration 的图才加）、`material`、`model`（已确认才加） |

占位写法和页面一致（见 `05-copywriting.md`），这样全站一次替换就能补齐；上线前 `[TODO`、`example.com` 必须为 0，体检脚本会报出来。

### 首页：Organization + WebSite（示例，不是事实）
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.example.com/#org",
      "name": "Trailnest (example brand)",
      "url": "https://www.example.com/",
      "logo": "https://www.example.com/assets/img/logo.png",
      "email": "sales@example.com",
      "sameAs": ["https://www.linkedin.com/company/example"]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.example.com/#website",
      "url": "https://www.example.com/",
      "name": "Trailnest (example brand)",
      "publisher": {"@id": "https://www.example.com/#org"}
    }
  ]
}
```
`address`、`foundingDate`、`numberOfEmployees` 已确认才加。`sameAs` 只放真实存在的主页。

### 产品页：Product + BreadcrumbList
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "name": "Aluminum Roll Up Table",
      "image": ["https://www.example.com/assets/img/aluminum-roll-up-table.jpg"],
      "description": "Aluminum roll up camping table, custom sizes and OEM packaging available.",
      "brand": {"@type": "Brand", "name": "Trailnest (example brand)"},
      "manufacturer": {"@id": "https://www.example.com/#org"},
      "material": "Aluminum alloy"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.example.com/"},
        {"@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.example.com/products.html"},
        {"@type": "ListItem", "position": 3, "name": "Roll Up Table", "item": "https://www.example.com/products/roll-up-table.html"}
      ]
    }
  ]
}
```
注意：谷歌的商品富结果通常要求有 offers/评价；B2B 不公开报价时拿不到富结果是正常的，`Product` 仍有助于搜索引擎和 AI 理解实体，不要为了富结果编报价。

### FAQ 页（和带 FAQ 的产品页）：FAQPage
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Do you offer samples?",
     "acceptedAnswer": {"@type": "Answer", "text": "Yes. Contact us with your spec and we will confirm sample lead time."}}
  ]
}
```
问答必须和页面上可见的文字一致。

### 验证
- 本地：用脚本或命令把每段 JSON-LD 解析一遍，不能有语法错误。
- 上线后：Google Rich Results Test、Schema Markup Validator（validator.schema.org）各测首页、一个产品页、FAQ 页。

## 三、根目录文件

### sitemap.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.example.com/</loc><lastmod>2026-01-01</lastmod></url>
  <url><loc>https://www.example.com/products.html</loc><lastmod>2026-01-01</lastmod></url>
</urlset>
```
只列可收录页；不列 thank-you、404、带 noindex 的页；`lastmod` 用真实修改日期。

### robots.txt
```
User-agent: *
Allow: /

Sitemap: https://www.example.com/sitemap.xml
```
不要屏蔽 CSS/JS/图片；不要误屏蔽 AI 爬虫（GPTBot、OAI-SearchBot、PerplexityBot、ClaudeBot、Google-Extended 等），除非用户明确不想被 AI 引用。

### llms.txt（给 AI 读的站点摘要，社区约定格式）
```markdown
# Trailnest (example brand)

> Manufacturer of aluminum camping tables for importers and outdoor brands. Custom sizes, printed logo and OEM packaging.

## Products
- [Roll Up Tables](https://www.example.com/products/roll-up-table.html): roll up tops, custom sizes
- [Folding Camp Tables](https://www.example.com/products/folding-camp-table.html): ...

## Company
- [About & Factory](https://www.example.com/about.html)
- [FAQ](https://www.example.com/faq.html)
- [Get a Quote](https://www.example.com/contact.html)
```
只写已确认事实；和网站、结构化数据说法一致。

## 四、GEO（让 AI 答案能引用）建站时就做的
- 每页开头一句话直接回答"这是什么、给谁、能做什么"。
- 规格、条款、对比用 HTML 表格；FAQ 用问答格式。
- 公司名、品牌、地址、邮箱在全站、结构化数据、llms.txt、第三方主页上**完全一致**。
- 有作者/联系人真名和职务更好（真实的才写）。

## 五、分析和询盘埋点（可选）
- 分析工具任选（Google Analytics 4、Cloudflare Web Analytics、Plausible 等）；GA4 的话询盘提交成功记 `generate_lead` 事件，邮件/WhatsApp 点击可记 `email_click`、`whatsapp_click`。
- 不装分析也能运营：Search Console 看搜索表现，询盘邮箱看结果。
