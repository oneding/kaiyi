import React from "react";

export default function TaskModal({ theme, onClose, onStart }) {
  const rows = [
    { k: "TOPIC", v: `${theme.title} — 分享你本月主题下的一段旅程与目的` },
    {
      k: "UGC",
      v: "上传 1+ 张原创照片或视频，配一句话目的地故事。",
    },
    {
      k: "RULES",
      v: "发布至个人公开账号并@品牌官方账号。",
    },
    {
      k: "HASHTAGS",
      v: `${theme.hashtags[0]}  ${theme.hashtags[1]}`,
    },
    {
      k: "AWARDS",
      v: "Official Choice + Popularity Award 官方选择奖 & 人气奖。",
    },
  ];
  return (
    <div className="modal" onClick={onClose}>
      <div className="sheet" onClick={(e) => e.stopPropagation()}>
        <div
          style={{
            textAlign: "center",
            color: "var(--accent)",
            fontWeight: 800,
            letterSpacing: "0.2em",
            fontSize: "12px",
            textTransform: "uppercase",
          }}
        >
          {theme.name} Challenge
        </div>
        <h2>{theme.title}</h2>
        <div className="sub">{theme.tagline}</div>
        <div className="task-rows">
          {rows.map((r) => (
            <div className="task-row" key={r.k}>
              <div className="k">{r.k}</div>
              <div className="v">{r.v}</div>
            </div>
          ))}
        </div>
        <button className="btn" onClick={onStart}>
          START
        </button>
      </div>
    </div>
  );
}
