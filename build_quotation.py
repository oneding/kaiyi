"""KAIYI 海外营销项目年度报价单生成"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from copy import copy

wb = Workbook()

# ---------- 通用样式 ----------
NAVY = "1F3864"        # 深蓝主色
ACCENT = "2F5496"      # 中蓝
LIGHT_BG = "F2F2F2"    # 浅灰底
HEADER_FILL = PatternFill("solid", start_color=NAVY)
SUBHEADER_FILL = PatternFill("solid", start_color=ACCENT)
TOTAL_FILL = PatternFill("solid", start_color="FFF2CC")
GRAND_FILL = PatternFill("solid", start_color="FCE4D6")
LIGHT_FILL = PatternFill("solid", start_color=LIGHT_BG)

WHITE_BOLD = Font(name="Arial", size=11, bold=True, color="FFFFFF")
TITLE_FONT = Font(name="Arial", size=20, bold=True, color=NAVY)
SUBTITLE_FONT = Font(name="Arial", size=12, bold=True, color=ACCENT)
SECTION_FONT = Font(name="Arial", size=12, bold=True, color="FFFFFF")
BOLD = Font(name="Arial", size=11, bold=True)
NORMAL = Font(name="Arial", size=11)
NOTE_FONT = Font(name="Arial", size=10, italic=True, color="595959")

THIN = Side(style="thin", color="BFBFBF")
MED = Side(style="medium", color=NAVY)
BORDER_ALL = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
BORDER_HEAD = Border(left=THIN, right=THIN, top=MED, bottom=MED)

CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT = Alignment(horizontal="left", vertical="center", wrap_text=True)
RIGHT = Alignment(horizontal="right", vertical="center")

CNY = '"¥"#,##0;("¥"#,##0);-'
CNY_YUAN = '"¥"#,##0.00;("¥"#,##0.00);-'

def merge_and_set(ws, rng, value, font, fill=None, align=None, border=None):
    ws.merge_cells(rng)
    c = ws[rng.split(":")[0]]
    c.value = value
    c.font = font
    if fill: c.fill = fill
    c.alignment = align or CENTER
    if border:
        for row in ws[rng]:
            for cell in row:
                cell.border = border

def set_row_height(ws, row, h):
    ws.row_dimensions[row].height = h

# ============================================================
# Sheet 1: 封面 (Cover)
# ============================================================
cover = wb.active
cover.title = "封面"
cover.sheet_view.showGridLines = False

cover.column_dimensions['A'].width = 4
for col in ['B', 'D', 'F', 'H']:
    cover.column_dimensions[col].width = 14
cover.column_dimensions['C'].width = 14
cover.column_dimensions['E'].width = 14
cover.column_dimensions['G'].width = 14

set_row_height(cover, 1, 14)
set_row_height(cover, 2, 30)
set_row_height(cover, 3, 50)
set_row_height(cover, 4, 28)
set_row_height(cover, 5, 20)

merge_and_set(cover, "B2:H2", "KAIYI · 开瑞汽车", TITLE_FONT, fill=None, align=Alignment(horizontal="center", vertical="center"))
merge_and_set(cover, "B3:H3", "海外营销 H5 项目年度报价单", Font(name="Arial", size=16, bold=True, color="FFFFFF"), fill=HEADER_FILL)
merge_and_set(cover, "B4:H4", "QUOTATION  /  2026–2027", Font(name="Arial", size=11, color="FFFFFF"), fill=SUBHEADER_FILL)

set_row_height(cover, 7, 28)
merge_and_set(cover, "B7:H7", "项 目 概 述", SECTION_FONT, fill=HEADER_FILL, align=Alignment(horizontal="left", vertical="center", indent=1))

overview_rows = [
    ("项目名称", "KAIYI · Share Your Destination 海外品牌营销 H5"),
    ("客户单位", "KAIYI 开瑞汽车（海外事业部）"),
    ("项目周期", "2026 年 9 月 — 2027 年 8 月（12 个月）"),
    ("交付形态", "移动端 H5（Vite + React）+ PC 桌面端响应式适配"),
    ("适配设备", "PC 桌面浏览器（≥ 1024px）+ 移动端（≤ 768px）双端自适应"),
    ("分享渠道", "Facebook · Instagram（系统分享面板带图分享）"),
    ("核心能力", "12 个月度主题自动切换 · 3 款相框模板 · 图片生成 · 一键分享"),
    ("维护模式", "每月 1 套新模板（设计 + 开发 + 上线）"),
    ("文档版本", "V1.1  /  2026-09-08  /  人民币报价 · 含 PC + 移动端"),
]
r = 8
for k, v in overview_rows:
    cover.row_dimensions[r].height = 24
    cover[f"B{r}"] = k
    cover[f"B{r}"].font = BOLD
    cover[f"B{r}"].fill = LIGHT_FILL
    cover[f"B{r}"].alignment = Alignment(horizontal="center", vertical="center")
    cover[f"B{r}"].border = BORDER_ALL
    cover.merge_cells(f"C{r}:H{r}")
    cover[f"C{r}"] = v
    cover[f"C{r}"].font = NORMAL
    cover[f"C{r}"].alignment = LEFT
    for col in ["C", "D", "E", "F", "G", "H"]:
        cover[f"{col}{r}"].border = BORDER_ALL
    r += 1

set_row_height(cover, r + 1, 28)
merge_and_set(cover, f"B{r+1}:H{r+1}", "报 价 汇 总", SECTION_FONT, fill=HEADER_FILL, align=Alignment(horizontal="left", vertical="center", indent=1))

summary = [
    ("A. 一次性设计费", "=报价明细!E5", False),
    ("B. 一次性开发费", "=报价明细!E13", False),
    ("C. 项目管理 / 客户确认", "=报价明细!E18", False),
    ("D. 月度维护费（12 个月）", "=报价明细!E25", False),
    ("E. 托管 / 空间 / 域名（年度）", "=报价明细!E29", False),
    ("F. 运营服务费（年度）", "=报价明细!E34", False),
    ("G. 增值税（6%）", "=ROUND(SUM(B22:B27)*0.06,0)", False),
    ("合计（含税）", "=SUM(B22:B28)", True),
]
r2 = r + 2
for k, v, bold in summary:
    cover.row_dimensions[r2].height = 24
    cover.merge_cells(f"B{r2}:E{r2}")
    cover[f"B{r2}"] = k
    cover[f"B{r2}"].font = BOLD if bold else NORMAL
    cover[f"B{r2}"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    if bold:
        cover[f"B{r2}"].fill = GRAND_FILL
        for col in ["C", "D", "E"]:
            cover[f"{col}{r2}"].fill = GRAND_FILL
    cover.merge_cells(f"F{r2}:H{r2}")
    cover[f"F{r2}"] = v
    cover[f"F{r2}"].font = BOLD if bold else NORMAL
    cover[f"F{r2}"].alignment = RIGHT
    cover[f"F{r2}"].number_format = CNY
    if bold:
        cover[f"F{r2}"].fill = GRAND_FILL
        cover[f"G{r2}"].fill = GRAND_FILL
        cover[f"H{r2}"].fill = GRAND_FILL
    for col in ["B", "C", "D", "E", "F", "G", "H"]:
        cover[f"{col}{r2}"].border = BORDER_ALL
    r2 += 1

merge_and_set(cover, f"B{r2+1}:H{r2+1}",
              "报价有效期：自本报价单签发之日起 30 个自然日    /    报价单位：人民币元（CNY）    /    含 6% 增值税",
              NOTE_FONT, fill=None, align=CENTER)

cover.print_options.horizontalCentered = True
cover.page_setup.orientation = cover.ORIENTATION_LANDSCAPE
cover.page_setup.fitToWidth = 1
cover.page_setup.fitToHeight = 1
cover.sheet_properties.pageSetUpPr.fitToPage = True

# ============================================================
# Sheet 2: 报价明细 (Quotation Detail)
# ============================================================
detail = wb.create_sheet("报价明细")
detail.sheet_view.showGridLines = False

widths = {"A": 6, "B": 32, "C": 22, "D": 8, "E": 16, "F": 38, "G": 14, "H": 18}
for k, w in widths.items():
    detail.column_dimensions[k].width = w

# 表头
detail.row_dimensions[1].height = 32
headers = ["序号", "项目名称", "工作内容 / 交付物", "数量", "单价 (¥)", "说明 / 工艺要点", "计量", "小计 (¥)"]
for i, h in enumerate(headers, start=1):
    c = detail.cell(row=1, column=i, value=h)
    c.font = WHITE_BOLD
    c.fill = HEADER_FILL
    c.alignment = CENTER
    c.border = BORDER_HEAD

def section_row(row, title):
    detail.row_dimensions[row].height = 22
    detail.merge_cells(f"A{row}:H{row}")
    c = detail.cell(row=row, column=1, value=title)
    c.font = SECTION_FONT
    c.fill = SUBHEADER_FILL
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    for col in range(1, 9):
        detail.cell(row=row, column=col).border = BORDER_ALL

def item_row(row, idx, name, content, qty, unit_price, desc, measure, formula_total=True):
    detail.row_dimensions[row].height = 36
    vals = [idx, name, content, qty, unit_price, desc, measure]
    for i, v in enumerate(vals, start=1):
        c = detail.cell(row=row, column=i, value=v)
        c.font = NORMAL
        c.alignment = LEFT if i in (2, 3, 6) else CENTER
        c.border = BORDER_ALL
    # 小计列：使用公式
    cell = detail.cell(row=row, column=8, value=f"=D{row}*E{row}")
    cell.font = NORMAL
    cell.alignment = RIGHT
    cell.number_format = CNY
    cell.border = BORDER_ALL
    # 单价列也格式化
    detail.cell(row=row, column=5).number_format = CNY

# --- A. 设计 ---
section_row(2, "A. 一次性设计费（Design）")
design_items = [
    ("主题视觉系统设计", "12 个月主题色板、字体、版式风格指南（Design Guideline）", 1, 30000, "逐月差异化，确保全年品牌调性一致", "套"),
    ("相框模板设计", "3 款相框 × 12 个月 = 36 款原创版式（路线打卡 / 旅行明信片 / 车窗视角）", 36, 1200, "每款含 PC + 移动端双端 3:4 出图样式 + 月度文案 + 装饰图标", "款"),
    ("SVG 图标系统", "12 个季节 / 主题线性图标（currentColor）", 12, 600, "可在 html2canvas / html-to-image 安全截图", "个"),
    ("PWA 应用图标", "icon.svg + icon-maskable.svg + 启动画面", 1, 3000, "支持添加到主屏幕 / 桌面图标", "套"),
    ("品牌首页 / 任务弹窗视觉", "首页主视觉 12 套 + 任务弹窗 12 套视觉稿", 24, 800, "PC + 移动端双端布局，含文案层级、按钮态、动效指引", "套"),
]
r = 3
for i, it in enumerate(design_items, start=1):
    item_row(r, i, *it)
    r += 1
# A 小计
detail.row_dimensions[r].height = 24
detail.merge_cells(f"B{r}:G{r}")
detail.cell(row=r, column=2, value="A 小计（一次性设计费）").font = BOLD
detail.cell(row=r, column=2).alignment = Alignment(horizontal="right", vertical="center", indent=1)
detail.cell(row=r, column=2).fill = TOTAL_FILL
detail.cell(row=r, column=8, value=f"=SUM(H3:H{r-1})").font = BOLD
detail.cell(row=r, column=8).alignment = RIGHT
detail.cell(row=r, column=8).number_format = CNY
detail.cell(row=r, column=8).fill = TOTAL_FILL
for col in range(1, 9):
    detail.cell(row=r, column=col).border = BORDER_ALL
detail.cell(row=r, column=1).fill = TOTAL_FILL
detail.cell(row=r, column=1).border = BORDER_ALL

# --- B. 开发 ---
b_start = r + 2
section_row(b_start, "B. 一次性开发费（Development）")
b_items = [
    ("H5 主框架开发", "Vite + React + PC/移动端响应式适配 + Vercel 全球托管", 1, 25000, "PC 桌面（≥1024px）+ 移动端（≤768px）双端自适应，PWA Manifest、Service Worker、Lighthouse 95+", "套"),
    ("四大流程页面", "品牌首页 / 月度任务弹窗 / 模板创作 / 一键分享", 4, 4500, "PC + 移动端双端适配，含路由、状态管理、断点响应式", "页"),
    ("图片生成与系统分享", "html-to-image 截图 + Web Share API（带文件）+ FB/IG 面板调起", 1, 12000, "支持 Facebook / Instagram App 一键带图分享", "套"),
    ("月度主题引擎", "12 个月主题切换 + 全年主题画廊 + 每月差异化文案注入", 1, 8000, "数据驱动：themes.js 一处维护全局生效", "套"),
    ("PWA / 缓存 / 离线", "离线访问、添加到主屏、桌面图标、安装提示", 1, 5000, "提升海外用户访问体验", "套"),
]
r = b_start + 1
for i, it in enumerate(b_items, start=1):
    item_row(r, i, *it)
    r += 1
# B 小计
detail.row_dimensions[r].height = 24
detail.merge_cells(f"B{r}:G{r}")
detail.cell(row=r, column=2, value="B 小计（一次性开发费）").font = BOLD
detail.cell(row=r, column=2).alignment = Alignment(horizontal="right", vertical="center", indent=1)
detail.cell(row=r, column=2).fill = TOTAL_FILL
detail.cell(row=r, column=8, value=f"=SUM(H{b_start+1}:H{r-1})").font = BOLD
detail.cell(row=r, column=8).alignment = RIGHT
detail.cell(row=r, column=8).number_format = CNY
detail.cell(row=r, column=8).fill = TOTAL_FILL
for col in range(1, 9):
    detail.cell(row=r, column=col).border = BORDER_ALL
detail.cell(row=r, column=1).fill = TOTAL_FILL
detail.cell(row=r, column=1).border = BORDER_ALL

# --- C. 客户确认 / 项目管理 ---
c_start = r + 2
section_row(c_start, "C. 项目管理与客户确认（PM & UAT）")
c_items = [
    ("需求梳理 / 方案设计", "业务调研、用户旅程、信息架构、流程图", 1, 6000, "输出 PRD / 原型 / 验收标准", "套"),
    ("客户确认 / 版本评审", "三轮视觉 + 功能评审会（含会议纪要、修订意见落地）", 3, 3000, "保障上线即验收通过", "轮"),
    ("UAT 验收与上线", "测试用例、回归测试、生产部署、域名备案支持", 1, 6000, "覆盖 12 个月度主题上线", "次"),
]
r = c_start + 1
for i, it in enumerate(c_items, start=1):
    item_row(r, i, *it)
    r += 1
detail.row_dimensions[r].height = 24
detail.merge_cells(f"B{r}:G{r}")
detail.cell(row=r, column=2, value="C 小计（项目管理 / 客户确认）").font = BOLD
detail.cell(row=r, column=2).alignment = Alignment(horizontal="right", vertical="center", indent=1)
detail.cell(row=r, column=2).fill = TOTAL_FILL
detail.cell(row=r, column=8, value=f"=SUM(H{c_start+1}:H{r-1})").font = BOLD
detail.cell(row=r, column=8).alignment = RIGHT
detail.cell(row=r, column=8).number_format = CNY
detail.cell(row=r, column=8).fill = TOTAL_FILL
for col in range(1, 9):
    detail.cell(row=r, column=col).border = BORDER_ALL
detail.cell(row=r, column=1).fill = TOTAL_FILL
detail.cell(row=r, column=1).border = BORDER_ALL

# --- D. 月度维护 ---
d_start = r + 2
section_row(d_start, "D. 月度维护费（按月续约 · 12 个月）")
d_items = [
    ("每月新模板设计", "1 套新相框版式（含 3:4 出图 + 文案 + 图标）", 12, 5000, "保持月度内容新鲜度", "月"),
    ("主题内容更新", "月度标题、标语、话题标签、品牌色、文案", 12, 3000, "数据驱动更新 themes.js 一处生效", "月"),
    ("上线部署 / 回归", "新模板上线 + 回归测试 + 旧模板兼容性检查", 12, 2000, "确保零中断发布", "月"),
]
r = d_start + 1
for i, it in enumerate(d_items, start=1):
    item_row(r, i, *it)
    r += 1
detail.row_dimensions[r].height = 24
detail.merge_cells(f"B{r}:G{r}")
detail.cell(row=r, column=2, value="D 小计（月度维护 × 12 月）").font = BOLD
detail.cell(row=r, column=2).alignment = Alignment(horizontal="right", vertical="center", indent=1)
detail.cell(row=r, column=2).fill = TOTAL_FILL
detail.cell(row=r, column=8, value=f"=SUM(H{d_start+1}:H{r-1})").font = BOLD
detail.cell(row=r, column=8).alignment = RIGHT
detail.cell(row=r, column=8).number_format = CNY
detail.cell(row=r, column=8).fill = TOTAL_FILL
for col in range(1, 9):
    detail.cell(row=r, column=col).border = BORDER_ALL
detail.cell(row=r, column=1).fill = TOTAL_FILL
detail.cell(row=r, column=1).border = BORDER_ALL

# --- E. 托管 / 空间 / 域名 ---
e_start = r + 2
section_row(e_start, "E. 托管 / 空间 / 域名（年度）")
e_items = [
    ("Vercel Pro 托管", "全球 CDN · 自动 HTTPS · 预览部署 · 99.99% SLA", 1, 2400, "覆盖海外多区域访问", "年"),
    ("域名注册 / 维护", ".com / .life / .moto 等海外品牌域名", 1, 500, "首年注册 + WHOIS 隐私保护", "年"),
    ("SSL / DNS 配置", "证书托管 + DNS 解析优化", 1, 0, "Vercel 自动签发，含在托管费内", "年"),
]
r = e_start + 1
for i, it in enumerate(e_items, start=1):
    item_row(r, i, *it)
    r += 1
detail.row_dimensions[r].height = 24
detail.merge_cells(f"B{r}:G{r}")
detail.cell(row=r, column=2, value="E 小计（托管 / 空间 / 域名）").font = BOLD
detail.cell(row=r, column=2).alignment = Alignment(horizontal="right", vertical="center", indent=1)
detail.cell(row=r, column=2).fill = TOTAL_FILL
detail.cell(row=r, column=8, value=f"=SUM(H{e_start+1}:H{r-1})").font = BOLD
detail.cell(row=r, column=8).alignment = RIGHT
detail.cell(row=r, column=8).number_format = CNY
detail.cell(row=r, column=8).fill = TOTAL_FILL
for col in range(1, 9):
    detail.cell(row=r, column=col).border = BORDER_ALL
detail.cell(row=r, column=1).fill = TOTAL_FILL
detail.cell(row=r, column=1).border = BORDER_ALL

# --- F. 运营服务 ---
f_start = r + 2
section_row(f_start, "F. 运营服务费（年度）")
f_items = [
    ("内容运营支持", "话题策划、文案润色、多语言适配（含英 / 西 / 阿）", 12, 1500, "覆盖海外三大主要市场", "月"),
    ("数据监控 / 月报", "UV / 分享率 / 月度活跃 / 转化漏斗 + 报告", 12, 1500, "每月 1 份数据报告 + 优化建议", "月"),
    ("客户活动支持", "节日 / 营销节点 / 联合活动素材快速响应", 4, 3000, "每季度 1 次专项活动", "次"),
]
r = f_start + 1
for i, it in enumerate(f_items, start=1):
    item_row(r, i, *it)
    r += 1
detail.row_dimensions[r].height = 24
detail.merge_cells(f"B{r}:G{r}")
detail.cell(row=r, column=2, value="F 小计（运营服务）").font = BOLD
detail.cell(row=r, column=2).alignment = Alignment(horizontal="right", vertical="center", indent=1)
detail.cell(row=r, column=2).fill = TOTAL_FILL
detail.cell(row=r, column=8, value=f"=SUM(H{f_start+1}:H{r-1})").font = BOLD
detail.cell(row=r, column=8).alignment = RIGHT
detail.cell(row=r, column=8).number_format = CNY
detail.cell(row=r, column=8).fill = TOTAL_FILL
for col in range(1, 9):
    detail.cell(row=r, column=col).border = BORDER_ALL
detail.cell(row=r, column=1).fill = TOTAL_FILL
detail.cell(row=r, column=1).border = BORDER_ALL

# --- 总计 ---
total_row = r + 2
detail.row_dimensions[total_row].height = 30
detail.merge_cells(f"A{total_row}:G{total_row}")
detail.cell(row=total_row, column=1, value="项目总计（含税前 · 不含增值税）").font = Font(name="Arial", size=12, bold=True, color="FFFFFF")
detail.cell(row=total_row, column=1).fill = HEADER_FILL
detail.cell(row=total_row, column=1).alignment = Alignment(horizontal="right", vertical="center", indent=1)
detail.cell(row=total_row, column=8, value=f"=H6+H11+H15+H19+H22+H25").font = Font(name="Arial", size=12, bold=True, color="FFFFFF")
detail.cell(row=total_row, column=8).fill = HEADER_FILL
detail.cell(row=total_row, column=8).alignment = RIGHT
detail.cell(row=total_row, column=8).number_format = CNY
for col in range(1, 9):
    detail.cell(row=total_row, column=col).border = BORDER_HEAD

# 小计行号参考（封面已引用）
# A=5, B=11, C=15, D=19, E=22, F=25（按上方行号实际计算并写入固定值也可）
# 用 SUMIFS 公式更稳健
# 但为简单起见，直接写引用公式：
# 我们需要确认小计行实际位置，封面已经引用了 E5/E13/E18/E25/E29/E34，对应的小计应是：
# A: 第5行, B: 第11行, C: 第15行, D: 第19行, E: 第22行, F: 第25行
# 让我们重设这些为绝对引用
# 实际写入的小计行号为：6, 11, 15, 19, 22, 25
# 修正封面引用

# 更新封面公式的引用（基于实际小计行号）
cover_formulas = {
    22: "=报价明细!H6",   # A
    23: "=报价明细!H11",  # B
    24: "=报价明细!H15",  # C
    25: "=报价明细!H19",  # D
    26: "=报价明细!H22",  # E
    27: "=报价明细!H25",  # F
}
for row, f in cover_formulas.items():
    cell = cover[f"F{row}"]
    cell.value = f
    cell.font = NORMAL

detail.print_options.horizontalCentered = True
detail.page_setup.orientation = detail.ORIENTATION_LANDSCAPE
detail.page_setup.fitToWidth = 1
detail.page_setup.fitToHeight = 0
detail.sheet_properties.pageSetUpPr.fitToPage = True

# ============================================================
# Sheet 3: 月度计划 (Monthly Plan)
# ============================================================
plan = wb.create_sheet("月度计划")
plan.sheet_view.showGridLines = False

pwidths = {"A": 6, "B": 12, "C": 22, "D": 22, "E": 18, "F": 26}
for k, w in pwidths.items():
    plan.column_dimensions[k].width = w

plan.row_dimensions[1].height = 30
ph = ["月份", "主题", "核心话题 / Hashtag", "相框模板版本", "上线日期", "维护项"]
for i, h in enumerate(ph, start=1):
    c = plan.cell(row=1, column=i, value=h)
    c.font = WHITE_BOLD
    c.fill = HEADER_FILL
    c.alignment = CENTER
    c.border = BORDER_HEAD

months = [
    (9, "Share Your Destination", "#KaiyiLifeInMotion · #ShareYourDestination", "v1.0（首发 3 款）", "2026-09-15", "首发上线 + 客户验收"),
    (10, "Autumn Colors", "#AutumnColors · #KaiyiLifeInMotion", "v1.1（新增 1 款）", "2026-10-15", "月度新模板 + 主题更新"),
    (11, "Misty Lake", "#MistyLake · #KaiyiLifeInMotion", "v1.2", "2026-11-15", "月度新模板 + 主题更新"),
    (12, "Winter Wonderland", "#WinterWonderland", "v1.3", "2026-12-15", "节日活动支持"),
    (1, "New Year Drive", "#NewYearDrive", "v1.4", "2027-01-15", "新年活动专题"),
    (2, "Valentine Ride", "#ValentineRide", "v1.5", "2027-02-14", "情人节专题"),
    (3, "Spring Bloom", "#SpringBloom", "v1.6", "2027-03-15", "春日主题"),
    (4, "Cherry Road", "#CherryRoad", "v1.7", "2027-04-15", "樱花季专题"),
    (5, "Coastal Drift", "#CoastalDrift", "v1.8", "2027-05-15", "海岸线主题"),
    (6, "Desert Light", "#DesertLight", "v1.9", "2027-06-15", "沙漠光线主题"),
    (7, "Highland Pass", "#HighlandPass", "v2.0", "2027-07-15", "高地穿越 + 半年度回顾"),
    (8, "Sunset Mile", "#SunsetMile", "v2.1", "2027-08-15", "年度收官 + 数据复盘"),
]
r = 2
for m in months:
    plan.row_dimensions[r].height = 28
    for i, v in enumerate(m, start=1):
        c = plan.cell(row=r, column=i, value=v)
        c.font = NORMAL
        c.alignment = CENTER if i in (1, 5) else LEFT
        c.border = BORDER_ALL
        if i == 2:
            c.font = BOLD
    r += 1

# 月度合计
plan.row_dimensions[r + 1].height = 24
plan.merge_cells(f"A{r+1}:E{r+1}")
c = plan.cell(row=r+1, column=1, value="12 个月维护 + 运营 · 小计")
c.font = BOLD
c.alignment = Alignment(horizontal="right", vertical="center", indent=1)
c.fill = TOTAL_FILL
cell = plan.cell(row=r+1, column=6, value=f"=报价明细!H19+报价明细!H25")
cell.font = BOLD
cell.fill = TOTAL_FILL
cell.alignment = RIGHT
cell.number_format = CNY
for col in range(1, 7):
    plan.cell(row=r+1, column=col).border = BORDER_ALL

plan.print_options.horizontalCentered = True
plan.page_setup.orientation = plan.ORIENTATION_LANDSCAPE
plan.page_setup.fitToWidth = 1
plan.sheet_properties.pageSetUpPr.fitToPage = True

# ============================================================
# Sheet 4: 服务条款 (Terms)
# ============================================================
terms = wb.create_sheet("服务条款")
terms.sheet_view.showGridLines = False

twidths = {"A": 4, "B": 22, "C": 70}
for k, w in twidths.items():
    terms.column_dimensions[k].width = w

terms.row_dimensions[1].height = 36
terms.merge_cells("A1:C1")
c = terms.cell(row=1, column=1, value="服 务 条 款 与 付 款 说 明")
c.font = Font(name="Arial", size=16, bold=True, color="FFFFFF")
c.fill = HEADER_FILL
c.alignment = CENTER

terms_data = [
    ("条款类别", "具体内容"),
    ("项目周期", "本项目合同周期为 12 个月，自双方签署之日起生效，到期前 30 日协商续约。"),
    ("交付物清单", "（1）H5 主程序（含源码，PC + 移动端双端响应式）；（2）12 套主题视觉稿；（3）36 款相框模板；（4）月度维护 12 次；（5）Vercel 全球托管 + 域名；（6）月度数据报告 × 12。"),
    ("一次性付款", "A + B + C 项合计一次性付款 50%，项目启动 5 个工作日内支付；上线验收后 30 日内支付 50% 尾款。"),
    ("月度付款", "D + F 项按月支付，每月 5 日前开具上月发票并收款；E 项年度费用首次部署时一次性支付。"),
    ("知识产权", "项目交付物的著作权归乙方所有；甲方拥有本项目专属永久使用权；乙方可在作品集中展示。"),
    ("客户配合", "甲方应在 5 个工作日内反馈确认意见；超期未反馈视为默认通过确认。每自然月最多发起 2 次模板修订。"),
    ("维保范围", "免费维保期 12 个月，含 Bug 修复、依赖升级、安全补丁；新功能 / 新主题属月度维护范围。"),
    ("变更管理", "需求变更需双方书面确认；超出原范围的工作量按 1,500 元 / 人天单独计费。"),
    ("数据合规", "项目遵守 GDPR 与目标市场数据法规；用户上传图片仅本地处理，不上传服务器。"),
    ("终止条款", "任意一方可提前 30 日书面通知终止合同；已交付部分按比例结算，未交付部分退还未发生款项。"),
    ("争议解决", "本协议适用中华人民共和国法律；争议提交项目所在地人民法院诉讼解决。"),
    ("报价有效期", "自签发之日起 30 个自然日内有效。"),
]
r = 2
for i, (k, v) in enumerate(terms_data):
    terms.row_dimensions[r].height = 32
    cell_k = terms.cell(row=r, column=2, value=k)
    cell_v = terms.merge_cells(f"C{r}:C{r}")
    cell_v_obj = terms.cell(row=r, column=3, value=v)
    if i == 0:
        cell_k.font = WHITE_BOLD
        cell_v_obj.font = WHITE_BOLD
        cell_k.fill = HEADER_FILL
        cell_v_obj.fill = HEADER_FILL
        cell_k.alignment = CENTER
        cell_v_obj.alignment = CENTER
    else:
        cell_k.font = BOLD
        cell_k.fill = LIGHT_FILL
        cell_k.alignment = Alignment(horizontal="center", vertical="center")
        cell_v_obj.font = NORMAL
        cell_v_obj.alignment = LEFT
    for col in (2, 3):
        terms.cell(row=r, column=col).border = BORDER_ALL
    terms.cell(row=r, column=1).border = BORDER_ALL
    r += 1

terms.print_options.horizontalCentered = True
terms.page_setup.orientation = terms.ORIENTATION_LANDSCAPE
terms.page_setup.fitToWidth = 1
terms.sheet_properties.pageSetUpPr.fitToPage = True

# ============================================================
# Sheet 5: 联系信息 (Contact)
# ============================================================
contact = wb.create_sheet("联系信息")
contact.sheet_view.showGridLines = False

cwidths = {"A": 4, "B": 20, "C": 40, "D": 4, "E": 20, "F": 40}
for k, w in cwidths.items():
    contact.column_dimensions[k].width = w

contact.row_dimensions[1].height = 36
contact.merge_cells("A1:F1")
c = contact.cell(row=1, column=1, value="联  系  方  式")
c.font = Font(name="Arial", size=16, bold=True, color="FFFFFF")
c.fill = HEADER_FILL
c.alignment = CENTER

contact.row_dimensions[3].height = 28
contact.merge_cells("B3:C3")
contact.cell(row=3, column=2, value="委托方（甲方）").font = Font(name="Arial", size=12, bold=True, color="FFFFFF")
contact.cell(row=3, column=2).fill = SUBHEADER_FILL
contact.cell(row=3, column=2).alignment = CENTER
contact.merge_cells("E3:F3")
contact.cell(row=3, column=5, value="受托方（乙方）").font = Font(name="Arial", size=12, bold=True, color="FFFFFF")
contact.cell(row=3, column=5).fill = SUBHEADER_FILL
contact.cell(row=3, column=5).alignment = CENTER

contacts_left = [
    ("客户单位", "KAIYI 开瑞汽车"),
    ("联系人", "海外事业部"),
    ("邮箱", "marketing@KAIYI-global.com"),
    ("电话", "+86 10-XXXX XXXX"),
    ("地址", "北京市朝阳区 XX 大厦"),
]
contacts_right = [
    ("服务商", "彩讯科技股份有限公司"),
    ("联系人", "项目商务部"),
    ("邮箱", "biz@caixun.com"),
    ("电话", "+86 10-XXXX XXXX"),
    ("地址", "深圳市南山区 XX 大厦"),
]

for i, (k, v) in enumerate(contacts_left):
    r = 4 + i
    contact.row_dimensions[r].height = 24
    contact.cell(row=r, column=2, value=k).font = BOLD
    contact.cell(row=r, column=2).fill = LIGHT_FILL
    contact.cell(row=r, column=2).alignment = Alignment(horizontal="center", vertical="center")
    contact.cell(row=r, column=2).border = BORDER_ALL
    contact.cell(row=r, column=3, value=v).font = NORMAL
    contact.cell(row=r, column=3).alignment = Alignment(horizontal="left", vertical="center", indent=1)
    contact.cell(row=r, column=3).border = BORDER_ALL

for i, (k, v) in enumerate(contacts_right):
    r = 4 + i
    contact.row_dimensions[r].height = 24
    contact.cell(row=r, column=5, value=k).font = BOLD
    contact.cell(row=r, column=5).fill = LIGHT_FILL
    contact.cell(row=r, column=5).alignment = Alignment(horizontal="center", vertical="center")
    contact.cell(row=r, column=5).border = BORDER_ALL
    contact.cell(row=r, column=6, value=v).font = NORMAL
    contact.cell(row=r, column=6).alignment = Alignment(horizontal="left", vertical="center", indent=1)
    contact.cell(row=r, column=6).border = BORDER_ALL

contact.row_dimensions[10].height = 24
contact.merge_cells("B10:F10")
c = contact.cell(row=10, column=2, value="感谢您的信任，期待携手共创 KAIYI 海外品牌新篇章！")
c.font = Font(name="Arial", size=12, bold=True, italic=True, color=NAVY)
c.alignment = CENTER

contact.print_options.horizontalCentered = True
contact.page_setup.orientation = contact.ORIENTATION_LANDSCAPE
contact.page_setup.fitToWidth = 1
contact.sheet_properties.pageSetUpPr.fitToPage = True

# 保存
output = "C:/Users/zyd/WorkBuddy/2026-09-08-08-07-16/kaiyi-h5/kaiyi-quotation.xlsx"
wb.save(output)
print(f"Saved: {output}")