import { toPng } from "html-to-image";

// 将相框 DOM 渲染为高清 PNG 数据 URL
// html-to-image 比 html2canvas 更稳：对 base64 照片、现代 CSS(object-fit/aspect-ratio)、
// 内联 SVG(currentColor) 支持更好，且不会出现 taint 导致 toDataURL 抛 SecurityError 的问题。
export async function captureFrame(el, opts = {}) {
  const dataUrl = await toPng(el, {
    pixelRatio: 2, // 2 倍分辨率，输出约 720x960
    cacheBust: true,
    backgroundColor: "#000000",
    skipAutoScale: false,
    ...opts,
  });
  return dataUrl;
}

// 读取本地图片文件 → dataURL（保证同源，避免 canvas 污染）
export function fileToDataUrl(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

// 把「任意地址的图片」预加载为 dataURL。
// 用于主题背景图（远程 Unsplash）：先拉取并转成 base64，截图时不再依赖外链 CORS。
export async function urlToDataUrl(url) {
  if (!url) return url;
  if (url.startsWith("data:")) return url;
  return new Promise((resolve) => {
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.onload = () => {
      try {
        const canvas = document.createElement("canvas");
        canvas.width = img.naturalWidth;
        canvas.height = img.naturalHeight;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(img, 0, 0);
        resolve(canvas.toDataURL("image/png"));
      } catch (e) {
        // 若跨域被拒，回落到原 URL
        console.warn("urlToDataUrl fallback:", e);
        resolve(url);
      }
    };
    img.onerror = () => resolve(url);
    img.src = url;
  });
}
