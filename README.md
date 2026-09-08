# KAIYI · Share Your Destination 海外营销 H5

> **KAIYI 开瑞汽车 海外品牌年度营销项目交付包**
>
> 基于 **Vite + React** 的响应式 H5 活动站，每月一套原创主题与相框模板，用户上传照片 → 套用 3 款 3:4 相框 → 生成图片 → 分享到 **Instagram / Facebook**。
>
> **支持设备**：PC 桌面浏览器（≥ 1024px）+ 移动端（≤ 768px）双端自适应。
>
> **部署**：Vercel 全球托管，自动 HTTPS、全球 CDN、99.99% SLA。
>
> **项目周期**：2026 年 9 月 — 2027 年 8 月（12 个月）。
>
> **年度总额**：人民币 ¥58,000（不含税）/ ¥61,480（含 6% 增值税）—— 详见 §10 报价结构。

---

## 一、核心能力（对照报价单六大板块）

### A. 设计（按月拆解 12 期 · 总额 ¥28,000）
- **9 月（启动月 ¥3,800）**：品牌视觉系统全套（色板/字体/SVG图标库/PWA图标/风格指南）+ 3 款首发相框模板。
- **10–8 月（11 期 × ¥2,200 = ¥24,200）**：每月 1 套新相框 + 月度主题色 + 文案 + 装饰图标。
- 月度差异化文案与图标通过 `themes.js` 数据驱动更新，全年视觉基底稳定、内容常新。

### B. 一次性开发费（¥15,000）
- **H5 主框架**：Vite + React + Vercel 全球托管，PC + 移动端双端自适应响应式。
- **四大流程页面**：品牌首页 / 月度任务弹窗 / 模板创作 / 一键分享。
- **图片生成与系统分享**：`html-to-image`（替代已停止维护的 html2canvas）+ Web Share API 带文件，移动端调起系统分享面板（FB / IG App）。
- **月度主题引擎**：12 月切换 + 全年主题画廊 + 每月差异化文案注入。
- **PWA / 缓存 / 离线**：Service Worker、添加到主屏、桌面图标。

### C. 客户确认与项目管理（¥1,500）
- 需求梳理、UAT 验收、版本评审、上线部署支持。

### D. 月度运营与维护（12 个月 × ~¥667/月 = ¥8,000）
- 月度主题内容更新（标题 / Hashtag / 品牌色微调 / 文案润色）。
- 上线部署 / 回归测试 / 兼容性检查 / Bug 修复。
- 节日 / 营销节点快速响应素材（4 个重大节点）。

### E. 托管 / 空间 / 域名（¥1,500 / 年）
- Vercel Pro 托管（全球 CDN · 自动 HTTPS · 预览部署 · 99.99% SLA）。
- `.com` 等海外品牌域名注册 + WHOIS 隐私保护。

### F. 运营服务（¥4,000 / 年）
- 内容运营支持 / 数据监控月报 / 客户活动支持（4 次）。

---

## 二、四步核心流程

1. **品牌首页** —— 月度主题大图 + JOIN NOW（顶部下拉 / 顶部横滑画廊可切换 1–12 月任意主题）
2. **月度任务弹窗** —— TOPIC / UGC / RULES / HASHTAGS / AWARDS 说明 + START
3. **模板创作** —— 选 3:4 相框 → 📷相机 / 🖼相册 上传 → GENERATE
4. **一键分享** —— 下载图片 / 复制文案 / 系统一键分享（带图） / 打开 FB / 打开 IG

---

## 三、技术栈

| 层 | 选型 |
|---|---|
| 框架 | React 18 + Vite 5 |
| UI | 原生 CSS（无第三方 UI 库）+ SVG 图标系统 |
| 图片生成 | html-to-image（toPng, pixelRatio=2） |
| 分享 | Web Share API（带文件）+ Facebook Sharer 回退 |
| PWA | manifest.webmanifest + Service Worker |
| 托管 | Vercel（自动识别 Vite） |

---

## 四、本地运行

```bash
npm install
npm run dev          # 默认 http://localhost:5174（已 host=0.0.0.0，局域网可访问）
npm run build        # 输出到 dist/
npm run preview      # 本地预览生产构建
```

---

## 五、部署到 Vercel（分步指引）

### 方式一：Git 集成（推荐）
1. 推送代码到 GitHub：`git push origin main`
2. 登录 https://vercel.com → **Add New Project** → 导入 `oneding/kaiyi` 仓库
3. 框架自动识别为 **Vite**，直接点 **Deploy**
4. 首次部署约 1–2 分钟；之后每次 push 自动触发重新部署
5. 部署完成后 Vercel 提供 `xxx.vercel.app` 域名（可在 Settings → Domains 绑定自有域名）

### 方式二：Vercel CLI
```bash
npm i -g vercel
vercel login
vercel                 # 首次部署，按提示确认框架 Vite
vercel --prod          # 后续部署到生产环境
```

> **配置说明**：`vercel.json` 已包含 `framework: vite`、`outputDirectory: dist`、SPA 重写规则，无需额外配置。

### 部署后必检项
- [ ] PC 桌面浏览器（≥ 1024px）打开：首页布局、画廊、相框、生成是否正常
- [ ] 移动端浏览器（iOS Safari / Android Chrome）打开：布局、相机 / 相册（ALBUM）、系统分享面板
- [ ] Web Share API 需 HTTPS（Vercel 自动满足）
- [ ] Lighthouse 性能 ≥ 95（PWA + 全球 CDN）

---

## 六、月度维护流程（持续 12 个月）

每月 15 日为月度模板上线日（D-1 上线 / D-15 完成回访）。

| 节点 | 工作 | 输出 |
|---|---|---|
| 月初 D+1 | 客户反馈上月数据、提出本月主题方向 | 月度需求 |
| 月初 D+3 | 设计师交付新相框模板视觉稿（PC + 移动端） | 设计稿 |
| 月初 D+7 | 客户视觉确认 + 文案确认 | 确认稿 |
| 月初 D+10 | 开发落地 + 主题数据更新 + 回归 | 预发布版 |
| 月初 D+12 | 客户 UAT 验收 | 验收意见 |
| 月初 D+15 | 正式上线 + 数据报告 | 上线报告 |

每月维护明细请见报价单 Sheet「月度计划」。

---

## 七、12 个月营销日历

| 月份 | 主题 | 重点营销节点 / 节日 |
|---|---|---|
| 9 月 | Share Your Destination（启动） | 项目首发 / 柏林 IAA 等车展 |
| 10 月 | Autumn Colors | 万圣节（10/31） |
| 11 月 | Misty Lake | 黑五 / 网一（11 月底） |
| 12 月 | Winter Wonderland | 圣诞（12/25）/ 跨年（12/31） |
| 1 月 | New Year Drive | 新年 / CES 国际消费电子展（1/7-10） |
| 2 月 | Valentine Ride | 情人节（2/14） |
| 3 月 | Spring Bloom | 国际妇女节 / 春分 |
| 4 月 | Cherry Road | 樱花季 / 地球日（4/22） |
| 5 月 | Coastal Drift | 母亲节 / 欧洲夏日度假季启动 |
| 6 月 | Desert Light | 父亲节 / 北半球夏季 |
| 7 月 | Highland Pass | 暑期出行高峰 / 半年度品牌回顾 |
| 8 月 | Sunset Mile | 七夕（中国）/ 年度收官数据复盘 |

---

## 八、目录结构

```
kaiyi-h5/
├── index.html
├── vite.config.js
├── vercel.json                    # Vercel 部署配置
├── package.json
├── kaiyi-quotation.xlsx           # 项目年度报价单（5 个 Sheet · ¥58,000 不含税）
├── build_quotation.py             # 报价单生成脚本（openpyxl）
└── src/
    ├── main.jsx
    ├── App.jsx                    # 全局状态、阶段切换
    ├── config/themes.js           # 12 个月度主题 + 3 款相框说明
    ├── components/
    │   ├── HomePage.jsx           # 品牌首页（含全年主题画廊）
    │   ├── TaskModal.jsx          # 月度任务弹窗
    │   ├── Creator.jsx            # 模板创作
    │   ├── FramePreview.jsx       # 3:4 相框渲染（预览/生成共用）
    │   ├── StampIcon.jsx          # 12 个主题线性 SVG 图标
    │   └── SharePage.jsx          # 一键分享（FB / IG / 系统面板）
    ├── lib/
    │   ├── generate.js            # html-to-image 截图（已弃用 html2canvas）
    │   └── media.js               # 本地 SVG 渐变背景（已移除 Unsplash 外网依赖）
    └── styles/app.css
```

---

## 九、关键决策记录（避免重复踩坑）

- ❌ **html2canvas**：已停止维护，对现代 CSS / SVG 支持差、跨域易失败。**改用 html-to-image**。
- ❌ **Unsplash 远程背景图**：公司 / 手机网络访问不稳定，且跨域污染 canvas。**改用本地 SVG 渐变（dataURL）**。
- ✅ **ALBUM 必须 `removeAttribute("capture")`**：`setAttribute("capture", "")` 在 iOS 上仍会强制拉起相机。
- ✅ **Git 推送**：在沙箱环境下使用 `git -c credential.helper= -c credential.helper=store push origin main`（清空 helper 链、只用 store 凭据）。

---

## 十、报价单与总额

| 板块 | 金额 | 备注 |
|---|---|---|
| A. 设计费（12 月度） | ¥28,000 | 9 月 ¥3,800 + 10-8 月 11 期 × ¥2,200 |
| B. 一次性开发费 | ¥15,000 | 主框架/四大流程/图片分享/PWA |
| C. 客户确认/PM | ¥1,500 | 需求 / 评审 / UAT |
| D. 月度运营与维护 | ¥8,000 | 12 × ~¥667 |
| E. 托管/域名（年度） | ¥1,500 | Vercel Pro + 域名 |
| F. 运营服务（年度） | ¥4,000 | 内容运营 / 月报 |
| **小计（不含税）** | **¥58,000** | 严格年度封顶 |
| 增值税（6%） | ¥3,480 | |
| **合计（含税）** | **¥61,480** | |

详见同级文件 `kaiyi-quotation.xlsx`（5 个 Sheet：封面 / 报价明细 / 月度计划 / 服务条款 / 联系信息）。

### 付款节奏
- **B + C 项** 一次性付款 100%，项目启动 5 个工作日内支付
- **A 项** 设计费按月分期付款，每月 5 日前开具上月发票并收款
- **D + F 项** 按月支付，每月 5 日前开具上月发票并收款
- **E 项** 年度费用首次部署时一次性支付
