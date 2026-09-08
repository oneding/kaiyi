import html2canvas from "html2canvas";

// 将相框 DOM 渲染为高清 PNG 数据 URL
export async function captureFrame(el) {
  const canvas = await html2canvas(el, {
    scale: 2,
    useCORS: true,
    allowTaint: true,
    backgroundColor: "#000000",
    logging: false,
  });
  return canvas.toDataURL("image/png");
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
