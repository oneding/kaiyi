import React, { useRef } from "react";
import { getThemeBg } from "../lib/media.js";
import { THEMES } from "../config/themes.js";
import StampIcon from "./StampIcon.jsx";

export default function HomePage({ theme, onJoin, onPickMonth }) {
  const bg = getThemeBg(theme.month);
  const gridRef = useRef(null);

  const pick = (m) => {
    if (onPickMonth) {
      onPickMonth(m);
      gridRef.current &&
        gridRef.current
          .querySelector(`[data-m="${m}"]`)
          ?.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    }
  };

  return (
    <div className="home">
      <div className="featured">
        <div>
          <div className="t">FEATURED WORKS</div>
          <div className="s">View selected stories</div>
        </div>
        <div className="arrow">›</div>
      </div>

      {/* 全年主题画廊 */}
      <div className="gallery">
        <div className="g-head">
          <span className="g-title">12 MONTHS · 12 STORIES</span>
          <span className="g-hint">左右滑动切换月份</span>
        </div>
        <div className="g-strip" ref={gridRef}>
          {THEMES.map((t) => (
            <div
              key={t.month}
              data-m={t.month}
              className={"g-card" + (t.month === theme.month ? " cur" : "")}
              onClick={() => pick(t.month)}
            >
              <div className="g-no">{String(t.month).padStart(2, "0")}</div>
              <div className="g-thumb" style={{ background: `linear-gradient(160deg, ${t.bg}, #05070c)` }}>
                <span className="g-stamp">
                  <StampIcon name={t.icon} size={34} color={t.accent} />
                </span>
                <span className="g-title-abs">{t.title}</span>
              </div>
              <div className="g-meta" style={{ color: t.accent }}>
                {t.name}
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="hero">
        <div
          className="bg"
          style={{
            backgroundImage: `linear-gradient(180deg, ${theme.bg}55, ${theme.bg}cc), url(${bg})`,
          }}
        />
        <div className="scrim" />
        <div className="month-tag">{theme.name} · {theme.season}</div>
        <div className="content">
          <div className="brand-lg">KAIYI</div>
          <h1>{theme.title}</h1>
          <div className="tagline">{theme.tagline}</div>
          <div className="hashtag">{theme.hashtags[1]}</div>
          <button className="btn" onClick={onJoin}>
            JOIN NOW
          </button>
        </div>
      </div>
    </div>
  );
}
