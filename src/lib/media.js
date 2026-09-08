// 各月主题背景图 —— 完全本地生成（SVG 渐变 data URL），不依赖任何外网 CDN。
// 优点：无跨域问题、无网络加载失败、html-to-image 截图稳定，部署后电脑/手机打开一定可用。

import { THEMES } from "../config/themes.js";

// 用主题色生成一张近似「风景感」的渐变底图（SVG），输出为 data URL。
// 视觉上带一点光斑/山影层次，避免纯色显得单调。
function gradientDataUrl(accent, bg) {
  const g = [
    `<svg xmlns="http://www.w3.org/2000/svg" width="720" height="960" viewBox="0 0 720 960">`,
    `<defs>`,
    `<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">`,
    `<stop offset="0%" stop-color="${accent}"/>`,
    `<stop offset="55%" stop-color="${bg}"/>`,
    `<stop offset="100%" stop-color="#07090e"/>`,
    `</linearGradient>`,
    `<radialGradient id="glow" cx="0.72" cy="0.22" r="0.5">`,
    `<stop offset="0%" stop-color="#ffffff" stop-opacity="0.32"/>`,
    `<stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>`,
    `</radialGradient>`,
    `</defs>`,
    `<rect width="720" height="960" fill="url(#sky)"/>`,
    `<circle cx="520" cy="170" r="150" fill="url(#glow)"/>`,
    // 远处山影
    `<path d="M0 620 L140 500 L280 600 L420 470 L580 610 L720 520 L720 960 L0 960 Z" fill="#000" fill-opacity="0.22"/>`,
    `<path d="M0 720 L180 590 L360 700 L540 560 L720 680 L720 960 L0 960 Z" fill="#000" fill-opacity="0.30"/>`,
    // 前景
    `<rect width="720" height="960" fill="#000" fill-opacity="0.06"/>`,
    `</svg>`,
  ].join("");
  return "data:image/svg+xml;utf8," + encodeURIComponent(g);
}

export const getThemeBg = (month) => {
  const t = THEMES[(month - 1 + THEMES.length) % THEMES.length];
  return gradientDataUrl(t.accent, t.bg);
};

// 相框缩略图 —— 也改为本地渐变，避免外网图片加载失败导致白块
export const THUMBS = [
  gradientDataUrl("#b6ff3b", "#1a2a20"),
  gradientDataUrl("#1f8f9d", "#12262e"),
  gradientDataUrl("#f7a83c", "#2a1a10"),
];
