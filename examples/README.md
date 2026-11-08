# 示例

`examples/demo-site/` 会放一个**跑通测试生成的示例站**：在一个空目录里，只给 AI 一句话提示词，用 `trade-site-builder` 快速模式生成，原样提交，不做人工美化。

示例产品是**虚构的**："Lumarack"——一家不锈钢厨房挂架工厂（壁挂置物架、调料架、锅盖架，304 不锈钢，可做 OEM 包装）。品牌、公司、数据全部是编的，不代表任何真实企业；页面上的 `[TODO: …]` 是故意留下的占位，演示"没给证据就不编"。

生成后这里会包含：

```
examples/demo-site/
  project/        # 立项、事实库、关键词表、蓝图、视觉规则、上线检查、交接单
  site/           # 静态英文站：首页、产品中心、产品页、About & Factory、Get a Quote、FAQ、thank-you、404、sitemap.xml、robots.txt、llms.txt
  ops/            # 用 trade-site-ops 对这个站跑一次"体检 + 本周计划"的结果
```

本地预览：

```bash
cd examples/demo-site/site
python3 -m http.server 8000
# 浏览器打开 http://localhost:8000
```

复现用的提示词：

```
用 trade-site-builder 快速模式，给一家虚构的不锈钢厨房挂架工厂（品牌 Lumarack，
目标市场美国和澳洲，买家是进口商和亚马逊品牌卖家）建一个英文询盘站，所有没给的事实一律占位。
```


`demo-site/`：2026-11-08 干净环境复测产出（虚构竹制砧板工厂，快速模式，生成器出的 11 页；占位符故意保留）。
