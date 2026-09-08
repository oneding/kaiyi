import React, { useState } from "react";
import { THEMES, getMonthTheme, DEFAULT_MONTH } from "./config/themes.js";
import HomePage from "./components/HomePage.jsx";
import TaskModal from "./components/TaskModal.jsx";
import Creator from "./components/Creator.jsx";
import SharePage from "./components/SharePage.jsx";

const STEPS = [
  { n: 1, label: "品牌首页" },
  { n: 2, label: "月度任务" },
  { n: 3, label: "模板创作" },
  { n: 4, label: "一键分享" },
];

export default function App() {
  const [month, setMonth] = useState(DEFAULT_MONTH);
  const [stage, setStage] = useState("home"); // home | creator | share
  const [taskOpen, setTaskOpen] = useState(false);
  const [photo, setPhoto] = useState(null);
  const [frameType, setFrameType] = useState("route");
  const [generated, setGenerated] = useState(null);
  const [toast, setToast] = useState("");

  const theme = getMonthTheme(month);

  const activeStep = taskOpen ? 2 : stage === "home" ? 1 : stage === "creator" ? 3 : 4;

  const showToast = (msg) => {
    setToast(msg);
    clearTimeout(showToast._t);
    showToast._t = setTimeout(() => setToast(""), 2200);
  };

  const changeMonth = (m) => {
    setMonth(Number(m));
    setStage("home");
    setTaskOpen(false);
    setPhoto(null);
    setGenerated(null);
    showToast(`已切换至${getMonthTheme(Number(m)).name}主题`);
  };

  const start = () => {
    setTaskOpen(false);
    setStage("creator");
  };

  const moveToShare = (img) => {
    setGenerated(img);
    setStage("share");
  };

  return (
    <div className="app-shell">
      <div className="topbar">
        <div className="brand">
          <span className="mark">K</span>
          <span>KAIYI</span>
        </div>
        <div className="month-picker">
          <span>{theme.name}主题</span>
          <select value={month} onChange={(e) => changeMonth(e.target.value)}>
            {THEMES.map((t) => (
              <option key={t.month} value={t.month}>
                {t.month}月 · {t.title}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="steps">
        {STEPS.map((s) => {
          const cls =
            activeStep === s.n
              ? "active"
              : activeStep > s.n
              ? "done"
              : "";
          return (
            <div key={s.n} className={"step " + cls}>
              <div className="dot">{activeStep > s.n ? "✓" : s.n}</div>
              <div className="label">{s.label}</div>
            </div>
          );
        })}
      </div>

      {(stage === "home" || taskOpen) && (
        <HomePage
          theme={theme}
          onJoin={() => setTaskOpen(true)}
          onPickMonth={(m) => changeMonth(m)}
        />
      )}
      {stage === "creator" && (
        <Creator
          theme={theme}
          photo={photo}
          setPhoto={setPhoto}
          frameType={frameType}
          setFrameType={setFrameType}
          onShare={moveToShare}
          onBack={() => setStage("home")}
          showToast={showToast}
        />
      )}
      {stage === "share" && (
        <SharePage
          theme={theme}
          generated={generated}
          onRedo={() => setStage("creator")}
          showToast={showToast}
        />
      )}

      {taskOpen && (
        <TaskModal theme={theme} onClose={() => setTaskOpen(false)} onStart={start} />
      )}

      {toast && <div className="toast">{toast}</div>}
    </div>
  );
}
