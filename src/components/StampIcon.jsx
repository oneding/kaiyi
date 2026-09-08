import React from "react";

// 12 个月度主题线性图标（当前色 currentColor 渲染，可作为 SVG 安全用于 html2canvas 截图）
const PATHS = {
  fireworks: (
    <>
      <path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.8 2.8M15.2 15.2 18 18M18 6l-2.8 2.8M8.8 15.2 6 18" />
      <circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none" />
    </>
  ),
  blossom: (
    <>
      <circle cx="12" cy="7.2" r="2.6" />
      <circle cx="16.7" cy="10.5" r="2.6" />
      <circle cx="14.9" cy="16" r="2.6" />
      <circle cx="9.1" cy="16" r="2.6" />
      <circle cx="7.3" cy="10.5" r="2.6" />
      <circle cx="12" cy="11.7" r="1.5" fill="currentColor" stroke="none" />
    </>
  ),
  sprout: (
    <>
      <path d="M12 21v-8" />
      <path d="M12 13c0-4.2 3-6.6 7-6.6 0 4.2-3 6.6-7 6.6z" />
      <path d="M12 13c0-4.2-3-6.6-7-6.6 0 4.2 3 6.6 7 6.6z" />
    </>
  ),
  city: (
    <>
      <path d="M3 21h18" />
      <path d="M5 21V11h4v10M11 21V7h4v14M17 21v-8h3v8" />
      <path d="M6.5 14h1M6.5 17h1M12.5 12h1M12.5 16h1" />
    </>
  ),
  wave: (
    <>
      <path d="M2 10c2.6-3.6 5.8-3.6 8.4 0s5.8 3.6 8.4 0" />
      <path d="M2 16c2.6-3.6 5.8-3.6 8.4 0s5.8 3.6 8.4 0" />
    </>
  ),
  mountain: (
    <>
      <path d="M3 19 10 7l4 6 3-4 4 10z" />
      <path d="M8 12l2-3 2 3" />
    </>
  ),
  sunset: (
    <>
      <circle cx="12" cy="12" r="4" />
      <path d="M12 4v2M5 12H3M21 12h-2M7 6.5l1.6 1.6M17 6.5l-1.6 1.6" />
      <path d="M2 19h20" />
    </>
  ),
  dune: (
    <>
      <path d="M2 18c5-1 7-9 12-9 4.5 0 6.5 6 8 9" />
      <path d="M2 21h20" />
    </>
  ),
  leaf: (
    <>
      <path d="M6 18C6 10 12 4 20 4c0 8-6 14-14 14z" />
      <path d="M6 18c3-4 7-7 10-9" />
    </>
  ),
  maple: (
    <>
      <path d="M12 3l1.7 3.6 3.6-1-1.6 3.4 3.3 1.6-4.3 1.8.7 3.6-3.4-2-3.4 2 .7-3.6L5 10.6l3.3-1.6-1.6-3.4 3.6 1z" />
      <path d="M12 21v-6" />
    </>
  ),
  mist: (
    <>
      <path d="M3 8h18M5 12h14M4 16h16" />
    </>
  ),
  snowflake: (
    <>
      <path d="M12 3v18M4.8 7.5l14.4 9M19.2 7.5l-14.4 9" />
      <path d="M12 3l-1.5 1.5M12 3l1.5 1.5M12 21l-1.5-1.5M12 21l1.5-1.5" />
    </>
  ),
};

export default function StampIcon({ name = "leaf", size = 24, color = "currentColor", strokeWidth = 1.8 }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke={color}
      strokeWidth={strokeWidth}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      style={{ display: "block" }}
    >
      {PATHS[name] || PATHS.leaf}
    </svg>
  );
}
