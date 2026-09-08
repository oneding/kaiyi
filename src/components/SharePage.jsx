import React, { useState, useEffect } from "react";

function dataUrlToFile(dataUrl, name) {
  const arr = dataUrl.split(",");
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8 = new Uint8Array(n);
  while (n--) u8[n] = bstr.charCodeAt(n);
  return new File([u8], name, { type: mime });
}

export default function SharePage({ theme, generated, onRedo, showToast }) {
  const [blobUrl, setBlobUrl] = useState("");
  const [canNativeShare, setCanNativeShare] = useState(false);

  const caption = `${theme.title} ${theme.hashtags[0]} ${theme.hashtags[1]} @KAIYI Global — ${theme.tagline}`;
  const shareUrl = window.location.origin + window.location.pathname;

  useEffect(() => {
    if (!generated) return;
    setBlobUrl(generated);
  }, [generated]);

  useEffect(() => {
    const check = () => {
      const f = new File(["x"], "t.png", { type: "image/png" });
      try {
        setCanNativeShare(!!navigator.canShare && navigator.canShare({ files: [f] }));
      } catch {
        setCanNativeShare(false);
      }
    };
    check();
  }, []);

  const download = () => {
    if (!generated) return;
    const a = document.createElement("a");
    a.href = generated;
    a.download = `kaiyi-${theme.month}-${theme.title.toLowerCase().replace(/\s+/g, "-")}.png`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    showToast("已下载，可发布到 Instagram / Facebook");
  };

  const copyCaption = async () => {
    try {
      await navigator.clipboard.writeText(caption);
      showToast("文案已复制");
    } catch {
      showToast("复制失败，请手动复制");
    }
  };

  const openPlatform = (p) => {
    const url =
      p === "instagram"
        ? "https://www.instagram.com/"
        : "https://www.facebook.com/";
    window.open(url, "_blank");
    showToast("已打开，请粘贴文案并上传图片");
  };

  const nativeShare = async () => {
    if (!generated) return;
    try {
      const file = dataUrlToFile(generated, `kaiyi-${theme.month}.png`);
      await navigator.share({
        files: [file],
        title: `KAIYI · ${theme.title}`,
        text: caption,
      });
    } catch (err) {
      if (err && err.name === "AbortError") return;
      download();
    }
  };

  const fbShare = () => {
    const u = encodeURIComponent(shareUrl);
    const q = encodeURIComponent(caption);
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${u}&quote=${q}`, "_blank");
  };

  return (
    <div className="share">
      <div className="ready">Ready to Share</div>

      <div className="preview">
        {generated ? (
          <img src={blobUrl} alt="生成结果" />
        ) : (
          <div style={{ height: 360, display: "grid", placeItems: "center", color: "var(--muted)" }}>
            无生成结果
          </div>
        )}
      </div>

      <div className="cap-box">
        <div className="caption">{caption}</div>
      </div>

      <div className="share-actions">
        <button className="btn share-btn" onClick={download}>
          ⬇ DOWNLOAD
        </button>
        <button className="btn share-btn" style={{ background: "var(--accent)", color: "var(--ink)" }} onClick={copyCaption}>
          COPY CAPTION
        </button>
        {canNativeShare && (
          <button className="btn share-btn" style={{ background: "var(--teal)", color: "#fff" }} onClick={nativeShare}>
            ⇪ 一键分享到系统
          </button>
        )}
        <button className="btn share-btn blue" onClick={fbShare}>
          SHARE TO FACEBOOK
        </button>
        <button className="btn share-btn" style={{ background: "linear-gradient(135deg,#f58529,#dd2a7b,#8134af)", color: "#fff" }} onClick={() => openPlatform("instagram")}>
          SHARE TO INSTAGRAM
        </button>
      </div>

      <button className="btn ghost" onClick={onRedo} style={{ marginTop: 14 }}>
        ← 重新创作
      </button>
      <div className="footnote">
        {theme.hashtags[0]} · {theme.hashtags[1]}
        <br />
        请下载图片或调用系统分享，将其发布至 Instagram / Facebook 并附上话题标签。
      </div>
    </div>
  );
}
