import React from "react";
import StampIcon from "./StampIcon.jsx";

// 3:4 相框（360x480）。route=路线打卡 / postcard=旅行明信片 / window=车窗视角
// 该 DOM 同时用于页面预览和 html2canvas 截图，务必保持结构稳定。

const W = 360;
const H = 480;

function RouteFrame({ theme, src }) {
  return (
    <div style={{ position: "absolute", inset: 0, background: "#000" }}>
      <img src={src} alt="" crossOrigin="anonymous"
        style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg, rgba(0,0,0,.45), rgba(0,0,0,0) 30%, rgba(0,0,0,.7) 100%)" }} />
      {/* 顶部主题条 */}
      <div style={{ position: "absolute", top: 0, left: 0, right: 0, background: theme.accent, height: 8 }} />
      <div style={{ position: "absolute", top: 24, left: 24, right: 24 }}>
        <div style={{ color: "#fff", fontWeight: 800, letterSpacing: "0.28em", fontSize: 14 }}>{theme.title}</div>
        <div style={{ color: "rgba(255,255,255,.75)", fontSize: 11, letterSpacing: "0.4em", marginTop: 6 }}>{theme.hashtags[0]}</div>
      </div>
      {/* 路线标记 */}
      <div style={{ position: "absolute", left: 44, top: "40%", height: 130, display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div style={{ width: 12, height: 12, borderRadius: "50%", background: theme.accent, boxShadow: "0 0 0 5px rgba(200,242,74,.25)" }} />
        <div style={{ width: 3, flex: 1, background: theme.accent }} />
        <div style={{ width: 16, height: 16, borderRadius: "50%", border: `3px solid ${theme.accent}`, background: "transparent" }} />
      </div>
      {/* 底部文案 */}
      <div style={{ position: "absolute", bottom: 26, left: 24, right: 24 }}>
        <div style={{ background: theme.accent, height: 20, width: 26, marginBottom: 12 }} />
        <div style={{ color: theme.accent, fontWeight: 900, fontSize: 22, letterSpacing: "0.04em" }}>{theme.copy.stop}</div>
        <div style={{ display: "flex", alignItems: "center", gap: 8, color: "#fff", fontSize: 12, marginTop: 8, letterSpacing: "0.04em" }}>
          <StampIcon name={theme.icon} size={16} color={theme.accent} />
          <span>{theme.hashtags[1]}</span>
        </div>
      </div>
    </div>
  );
}

function PostcardFrame({ theme, src }) {
  return (
    <div style={{ position: "absolute", inset: 0, background: theme.paper, color: "#1c2a2e" }}>
      {/* 顶部标识 */}
      <div style={{ display: "flex", justifyContent: "space-between", padding: "22px 22px 0" }}>
        <div style={{ fontWeight: 800, color: "#1f8f9d", fontSize: 13, letterSpacing: "0.14em" }}>
          KAIYI · <span style={{ textTransform: "uppercase" }}>{theme.name}</span>
        </div>
        <div style={{ width: 40, height: 40, borderRadius: "50%", border: "2px solid #1f8f9d", display: "grid", placeItems: "center", color: "#1f8f9d", fontWeight: 800, fontSize: 14 }}>
          {String(theme.month).padStart(2, "0")}
        </div>
      </div>
      {/* 照片（明信片） */}
      <div style={{ padding: "16px 22px 0" }}>
        <div style={{ border: "1px solid #dfd6c4", boxShadow: "0 8px 22px rgba(0,0,0,.12)", aspectRatio: "3/4.1", overflow: "hidden", background: "#000" }}>
          <img src={src} alt="" crossOrigin="anonymous" style={{ width: "100%", height: "100%", objectFit: "cover" }} />
        </div>
      </div>
      {/* 底部文案 */}
      <div style={{ padding: "16px 22px 0" }}>
        <div style={{ fontSize: 12, letterSpacing: "0.16em", color: "#8a8577", textTransform: "uppercase" }}>{theme.frameLabels.postcard}</div>
        <div style={{ fontWeight: 900, fontSize: 26, marginTop: 4, color: "#1c2a2e", lineHeight: 1.06 }}>{theme.copy.place}</div>
        <div style={{ display: "flex", alignItems: "center", gap: 8, color: "#e07a3f", fontWeight: 800, fontSize: 14, marginTop: 8 }}>
          <StampIcon name={theme.icon} size={18} color="#e07a3f" />
          <span>{theme.hashtags[1]}</span>
        </div>
      </div>
    </div>
  );
}

function WindowFrame({ theme, src }) {
  const bracket = {
    position: "absolute",
    width: 44,
    height: 44,
    borderColor: theme.accent,
  };
  return (
    <div style={{ position: "absolute", inset: 0, background: "#0d0d0d" }}>
      <img src={src} alt="" crossOrigin="anonymous" style={{ width: "100%", height: "100%", objectFit: "cover", opacity: 0.92 }} />
      <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg, rgba(0,0,0,.1), rgba(0,0,0,0) 40%, rgba(0,0,0,.85) 100%)" }} />
      {/* 取景框四角 */}
      <div style={{ position: "absolute", inset: 22, pointerEvents: "none" }}>
        <div style={{ ...bracket, top: 0, left: 0, borderTop: "3px solid", borderLeft: "3px solid", borderColor: theme.accent }} />
        <div style={{ ...bracket, top: 0, right: 0, borderTop: "3px solid", borderRight: "3px solid", borderColor: theme.accent }} />
        <div style={{ ...bracket, bottom: 0, left: 0, borderBottom: "3px solid", borderLeft: "3px solid", borderColor: theme.accent }} />
        <div style={{ ...bracket, bottom: 0, right: 0, borderBottom: "3px solid", borderRight: "3px solid", borderColor: theme.accent }} />
      </div>
      {/* 底部文案 */}
      <div style={{ position: "absolute", bottom: 26, left: 26, right: 26 }}>
        <div style={{ background: theme.accent, height: 20, width: 26, marginBottom: 12 }} />
        <div style={{ color: theme.accent, fontWeight: 900, fontSize: 20, letterSpacing: "0.04em", lineHeight: 1.1 }}>{theme.copy.view}</div>
        <div style={{ display: "flex", alignItems: "center", gap: 8, color: "#fff", fontSize: 12, marginTop: 8 }}>
          <StampIcon name={theme.icon} size={16} color={theme.accent} />
          <span>{theme.hashtags[1]}</span>
        </div>
      </div>
    </div>
  );
}

export default function FramePreview({ theme, frameType, src }) {
  const inner =
    frameType === "postcard" ? (
      <PostcardFrame theme={theme} src={src} />
    ) : frameType === "window" ? (
      <WindowFrame theme={theme} src={src} />
    ) : (
      <RouteFrame theme={theme} src={src} />
    );

  return (
    <div data-frame={frameType} style={{ width: W, height: H, position: "relative", overflow: "hidden", background: "#000", borderRadius: 0 }}>
      {inner}
    </div>
  );
}
