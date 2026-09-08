import React, { useRef, useState } from "react";
import FramePreview from "./FramePreview.jsx";
import { FRAME_INFO, FRAME_TYPES } from "../config/themes.js";
import { getThemeBg, THUMBS } from "../lib/media.js";
import { captureFrame, fileToDataUrl } from "../lib/generate.js";

export default function Creator({
  theme,
  photo,
  setPhoto,
  frameType,
  setFrameType,
  onShare,
  onBack,
  showToast,
}) {
  const inputRef = useRef(null);
  const frameRef = useRef(null);
  const pendingMode = useRef("album");
  const [busy, setBusy] = useState(false);

  const src = photo || getThemeBg(theme.month);

  const pickMedia = (mode) => {
    pendingMode.current = mode;
    const input = inputRef.current;
    if (!input) return;
    if (mode === "camera") {
      // 打开相机
      input.setAttribute("capture", "environment");
    } else {
      // 打开相册：必须移除 capture，否则 iOS/部分安卓会强制拉起相机
      input.removeAttribute("capture");
    }
    if (!mode) input.removeAttribute("capture");
    input.value = "";
    input.click();
  };

  const onFile = async (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    try {
      const url = await fileToDataUrl(file);
      setPhoto(url);
      showToast("照片已添加");
    } catch {
      showToast("读取图片失败");
    }
  };

  const generate = async () => {
    if (!frameRef.current) return;
    setBusy(true);
    try {
      const dataUrl = await captureFrame(frameRef.current);
      onShare(dataUrl);
    } catch (err) {
      console.error(err);
      showToast("生成失败，请检查图片或重试");
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="creator">
      <div className="sec-title">CHOOSE A 3:4 FRAME</div>

      <div className="frame-row">
        {FRAME_TYPES.map((type, i) => {
          const info = FRAME_INFO[type];
          return (
            <div
              key={type}
              className={"frame-opt" + (frameType === type ? " sel" : "")}
              onClick={() => setFrameType(type)}
            >
              <div
                className="thumb"
                style={{ backgroundImage: `url(${THUMBS[i]})` }}
              >
                <span className="badge">{info.no}</span>
              </div>
              <div className="cap">
                <div className="n">{info.name}</div>
                <div className="d">{info.desc}</div>
              </div>
            </div>
          );
        })}
      </div>

      <div className="media">
        <div ref={frameRef}>
          <FramePreview theme={theme} frameType={frameType} src={src} />
        </div>
      </div>

      <div className="media-actions">
        <button className="btn ghost media-btn" onClick={() => pickMedia("camera")}>
          📷 CAMERA
        </button>
        <button className="btn ghost media-btn" onClick={() => pickMedia("album")}>
          🖼 ALBUM
        </button>
      </div>

      <input
        ref={inputRef}
        type="file"
        accept="image/*"
        style={{ display: "none" }}
        onChange={onFile}
      />

      <button className="btn dark" onClick={generate} disabled={busy}>
        {busy ? "生成中…" : "GENERATE"}
      </button>

      <button
        className="btn ghost"
        onClick={onBack}
        style={{ marginTop: 12, marginBottom: 0 }}
      >
        ← 返回
      </button>
      <div className="footnote">
        {theme.name}主题 · {theme.hashtags[0]} · {theme.hashtags[1]}
      </div>
    </div>
  );
}
