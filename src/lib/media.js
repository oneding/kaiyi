// 各月主题背景图（Unsplash 直链），加载失败时回落到纯渐变
const BG = [
  "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800", // Jan 公路
  "https://images.unsplash.com/photo-1502877338535-766e1452684a", // Feb 樱花-车
  "https://images.unsplash.com/photo-1470770841072-f978cf4d019e", // Mar 湖山
  "https://images.unsplash.com/photo-1519501025264-65ba15a82390", // Apr 城市夜景
  "https://images.unsplash.com/photo-1507525428034-b723cf961d3e", // May 海岸
  "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b", // Jun 山脉
  "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee", // Jul 公路旅行
  "https://images.unsplash.com/photo-1547234935-80c7145ec969", // Aug 沙漠
  "https://images.unsplash.com/photo-1473973266408-ed4e27abdd47", // Sep 秋山日落
  "https://images.unsplash.com/photo-1469474968028-56623f02e42e", // Oct 秋色
  "https://images.unsplash.com/photo-1439066615861-d1af74d74000", // Nov 湖泊
  "https://images.unsplash.com/photo-1483664852095-d6cc6870702d", // Dec 雪境
];

export const getThemeBg = (month) => BG[(month - 1 + BG.length) % BG.length];

// 相框缩略图
export const THUMBS = [
  "https://images.unsplash.com/photo-1473973266408-ed4e27abdd47",
  "https://images.unsplash.com/photo-1502877338535-766e1452684a",
  "https://images.unsplash.com/photo-1506905925346-21bda4d32df4",
];
