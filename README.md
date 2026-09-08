# KAIYI · 分享你的目的地 H5

一个基于 **Vite + React** 的移动端 H5 活动页：每月一套主题与模板，用户上传照片 → 套用 3 款 3:4 相框 → 生成图片 → 分享到 **Instagram / Facebook**。支持部署到 **Vercel**。

## 流程

1. 品牌首页（月度主题、JOIN NOW）
2. 月度任务弹窗（挑战说明、START）
3. 模板创作（选相框 + 相机/相册上传 + GENERATE）
4. 一键分享（下载 / 复制文案 / 系统分享 / FB / IG）

## 主题与模板

- **12 个月主题**：`src/config/themes.js`，每月含标题、标语、话题标签、品牌色、季节图标、明信片纸色。
- **3 款相框**：路线打卡、旅行明信片、车窗视角（`src/components/FramePreview.jsx`）。
- **差异化**：每月相框大字文案（`theme.copy`）与季节图标（`StampIcon`，内联 SVG，截图安全）随月份变化；明信片背景用每月纸色。
- 顶部下拉框或**首页全年画廊**（横滑 12 月卡片）可切换任意月份，实时预览该月主题与配色。

## PWA

已内置 `public/manifest.webmanifest` 与 `icon.svg`，移动端浏览器可“添加到主屏幕”作为独立 App 打开。

## 本地运行

```bash
npm install
npm run dev      # 默认 http://localhost:5174
```

## 生产构建

```bash
npm run build    # 输出到 dist/
npm run preview
```

## 部署到 Vercel

已包含 `vercel.json`（framework=vite，outputDirectory=dist，SPA 重写）。

**方式一：Vercel CLI**

```bash
npm i -g vercel
vercel            # 首次登录后按提示，框架选 Vite，一键部署
```

**方式二：Git 集成**

1. 推送代码到 GitHub / GitLab。
2. Vercel → New Project → 导入仓库，框架自动识别为 Vite。
3. 直接 Deploy。

部署后，H5 的分享链接会读取 `window.location.origin` 作为 Facebook 分享地址。

## 分享实现说明

- **系统一键分享**：优先调用 Web Share API（`navigator.share({files})`），移动端会弹出系统分享面板，可直接选 Instagram / Facebook App。
- **Instagram / Facebook**：不支持的浏览器回退为「下载图片 + 打开对应平台」，用户粘贴文案与话题标签后上传。
- **复制文案**：复制含 `#KaiyiLifeInMotion`、`#主题标签` 与 @KAIYI 的完整文案。

## 目录结构

```
kaiyi-h5/
├── index.html
├── vite.config.js
├── vercel.json
├── package.json
└── src/
    ├── main.jsx
    ├── App.jsx
    ├── config/themes.js       # 12 个月度主题 + 3 款相框说明
    ├── components/
    │   ├── HomePage.jsx       # 品牌首页（含全年主题画廊）
    │   ├── TaskModal.jsx      # 月度任务弹窗
    │   ├── Creator.jsx        # 模板创作
    │   ├── FramePreview.jsx   # 3:4 相框渲染（预览/生成共用）
    │   ├── StampIcon.jsx      # 12 个主题线性 SVG 图标
    │   └── SharePage.jsx      # 一键分享
    ├── lib/
    │   ├── generate.js        # html2canvas 截图 + 文件读取
    │   └── media.js           # 各月主题背景图
    └── styles/app.css
```
