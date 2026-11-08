# 询价表单方案 + 部署方式

## 一、询价表单

| 方案 | 要不要后端 | 优点 | 缺点 | 适合 |
|---|---|---|---|---|
| **mailto:（默认）** | 不要 | 零注册、零配置，本地就能演示 | 依赖访客电脑装了邮件客户端；手机网页版邮箱用户可能打不开；无法统计提交 | 演示、起步 |
| Formspree / Web3Forms / Getform 等表单服务（可选） | 不要（第三方代收） | 改一行 `action` 就能用，邮件直达，有垃圾过滤 | 要注册账号；免费档有提交数限制，以各服务官网为准 | 正式上线首选 |
| Netlify Forms（可选） | 不要 | 部署在 Netlify 时加一个属性即可 | 只在 Netlify 上有效 | 用 Netlify 部署 |
| Cloudflare Pages Functions / Vercel Functions（可选） | 要写一个小函数 | 完全自控，可接任意邮件服务 | 要一点开发能力 | 有技术的人 |
| WordPress 表单插件（可选） | WordPress 自带 | 后台可存档 | 要维护 WordPress | 搬进 WordPress 时 |

### mailto 写法（模板默认）
表单 `method="post" action="mailto:sales@example.com" enctype="text/plain"` 在不同浏览器表现不一。模板里的做法更稳：用一小段原生 JS 把表单内容拼成邮件正文，打开 `mailto:` 链接；同时页面上**明文显示邮箱**作为后备（"Or email us directly at …"）。

### 换成表单服务
1. 用户本人在表单服务注册，拿到提交地址（如 `https://formspree.io/f/xxxx`）。
2. 把表单的 `action` 改成该地址、`method="POST"`，去掉 mailto 的 JS（模板里有开关说明）。
3. 提交成功跳转 `thank-you.html`（大多数服务支持 `_next` 或后台设置跳转）。
4. 加简单防垃圾：蜜罐字段（隐藏输入框，有值就丢弃）。

### 无论哪种都要
- 真实提交一次：邮件到了、内容完整、能直接回复给询盘人的邮箱。
- 用户常用邮箱/手机有通知。
- 隐私：表单下方一句 "We only use your details to reply to your inquiry."

## 二、部署（全部可选，账号和付款由用户本人操作）

部署前统一做：
- [ ] 全站把 `https://www.example.com` 换成正式域名（canonical、og:url、JSON-LD、sitemap、robots、llms.txt）
- [ ] 全站搜 `TODO` 为零
- [ ] 表单换成正式方案并测过

### Cloudflare Pages
1. 用户登录 Cloudflare → Workers & Pages → 创建 → Pages → 直接上传 `site/` 文件夹（或连 GitHub 仓库，构建命令留空，输出目录 `site`）。
2. 自定义域名：在项目里添加域名；域名在 Cloudflare 管理时自动配好 DNS 和 HTTPS。
3. `404.html` 放根目录会被自动当作 404 页。

### Vercel
1. 用户登录 Vercel → Add New Project → 导入 Git 仓库（或用 Vercel CLI 在 `site/` 目录部署）。框架选 "Other"，输出目录 `site`。
2. Settings → Domains 添加域名，按提示改 DNS。

### Netlify
登录后把 `site/` 文件夹拖进 Deploys 页面即可；用 Netlify Forms 时给 `<form>` 加 `data-netlify="true"` 和 `name` 属性。

### 任意静态主机 / 对象存储
把 `site/` 里的文件原样上传到网站根目录，确认 HTTPS 已开。

### 搬进 WordPress
适合用户想要后台自己改内容。做法：
1. 用户本人装好 WordPress 和一个轻量主题，**安装期间开"阻止搜索引擎索引"**。
2. 按蓝图建页面，把各页正文搬进去（区块编辑器的"自定义 HTML"块可直接放规格表和 FAQ）。
3. 用 SEO 插件设置每页 Title/description/canonical；结构化数据用插件或在页面里放 JSON-LD（只放一份，别和插件重复）。
4. 表单用表单插件，配 SMTP 发信插件保证邮件不进垃圾箱。
5. 全部检查完再关掉"阻止索引"。

## 三、上线后（用户本人操作）
1. Google Search Console：添加站点（推荐"网域"资源，按提示加 DNS TXT 记录）→ 站点地图里提交完整地址 `https://你的域名/sitemap.xml` → 对首页和主力产品页"请求编入索引"。
2. Bing Webmaster Tools：可从 GSC 一键导入；提交 sitemap。ChatGPT 等 AI 搜索会用到 Bing 的索引，别漏。
3. 企业邮箱建议配好 SPF、DKIM、DMARC，避免回信进垃圾箱（在邮箱服务商后台按指引做）。
