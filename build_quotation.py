"""KAIYI 海外营销项目年度报价单生成
项目总价：人民币 ¥58,000（不含税）
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = Workbook()

# ---------- 通用样式 ----------
NAVY = "1F3864"
ACCENT = "2F5496"
LIGHT_BG = "F2F2F2"
HEADER_FILL = PatternFill("solid", start_color=NAVY)
SUBHEADER_FILL = PatternFill("solid", start_color=ACCENT)
TOTAL_FILL = PatternFill("solid", start_color="FFF2CC")
GRAND_FILL = PatternFill("solid", start_color="FCE4D6")
LIGHT_FILL = PatternFill("solid", start_color=LIGHT_BG)

WHITE_BOLD = Font(name="Arial", size=11, bold=True, color="FFFFFF")
TITLE_FONT = Font(name="Arial", size=20, bold=True, color=NAVY)
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

SUBTOTAL_ROWS = {}

# ============================================================
# Sheet 1: 封面
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
merge_and_set(cover, "B4:H4", "QUOTATION  ·  2026–2027  ·  RMB", Font(name="Arial", size=11, color="FFFFFF"), fill=SUBHEADER_FILL)

set_row_height(cover, 7, 28)
merge_and_set(cover, "B7:H7", "项 目 概 述", SECTION_FONT, fill=HEADER_FILL, align=Alignment(horizontal="left", vertical="center", indent=1))

overview_rows = [
    ("项目名称", "KAIYI · Share Your Destination 海外品牌营销 H5"),
    ("客户单位", "KAIYI 开瑞汽车（海外事业部）"),
    ("项目周期", "2026 年 9 月 — 2027 年 8 月（12 个月）"),
    ("交付形态", "PC + 移动端 H5（Vite + React，响应式适配）+ Vercel 全球托管"),
    ("适配设备", "PC 桌面浏览器（≥ 1024px）+ 移动端（≤ 768px）双端自适应"),
    ("分享渠道", "Facebook · Instagram（系统分享面板带图分享）"),
    ("核心能力", "12 个月度主题切换 · 3 款相框模板 · 图片生成 · 一键分享"),
    ("维护模式", "每月 1 套新模板（设计 + 开发 + 上线）"),
    ("总额", "人民币 ¥58,000（不含税）/ 含税 ¥61,480"),
    ("设计费结构", "A 项设计费按月拆解 12 期 · 启动月 ¥3,800 · 月度项 ¥2,200 · 收官月 ¥2,200"),
    ("文档版本", "V1.3  /  2026-09-08  /  人民币报价"),
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

SUMMARY_START_ROW = r + 3

summary_labels = [
    ("A. 设计费（按月拆解 12 期）", False),
    ("B. 一次性开发费", False),
    ("C. 客户确认 / 项目管理", False),
    ("D. 月度运营与维护", False),
    ("E. 托管 / 域名（年度）", False),
    ("F. 运营服务（年度）", False),
    ("小计（不含税）", True),
    ("G. 增值税（6%）", False),
    ("合计（含税）", True),
]
r2 = SUMMARY_START_ROW
for k, bold in summary_labels:
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
    cover[f"F{r2}"] = 0
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
              "报价有效期：自本报价单签发之日起 30 个自然日    ·    报价单位：人民币元（CNY）    ·    项目年度总额 ¥58,000（不含税）",
              NOTE_FONT, fill=None, align=CENTER)

cover.print_options.horizontalCentered = True
cover.page_setup.orientation = cover.ORIENTATION_LANDSCAPE
cover.page_setup.fitToWidth = 1
cover.page_setup.fitToHeight = 1
cover.sheet_properties.pageSetUpPr.fitToPage = True

# ============================================================
# Sheet 2: 报价明细
# ============================================================
detail = wb.create_sheet("报价明细")
detail.sheet_view.showGridLines = False

widths = {"A": 6, "B": 22, "C": 50, "D": 8, "E": 16, "F": 30, "G": 14, "H": 18}
for k, w in widths.items():
    detail.column_dimensions[k].width = w

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

def item_row(row, idx, name, content, qty, unit_price, desc, measure):
    detail.row_dimensions[row].height = 36
    vals = [idx, name, content, qty, unit_price, desc, measure]
    for i, v in enumerate(vals, start=1):
        c = detail.cell(row=row, column=i, value=v)
        c.font = NORMAL
        c.alignment = LEFT if i in (2, 3, 6) else CENTER
        c.border = BORDER_ALL
    cell = detail.cell(row=row, column=8, value=f"=D{row}*E{row}")
    cell.font = NORMAL
    cell.alignment = RIGHT
    cell.number_format = CNY
    cell.border = BORDER_ALL
    detail.cell(row=row, column=5).number_format = CNY

def subtotal_row(row, label, sum_range_start, sum_range_end):
    detail.row_dimensions[row].height = 24
    detail.merge_cells(f"B{row}:G{row}")
    detail.cell(row=row, column=2, value=label).font = BOLD
    detail.cell(row=row, column=2).alignment = Alignment(horizontal="right", vertical="center", indent=1)
    detail.cell(row=row, column=2).fill = TOTAL_FILL
    detail.cell(row=row, column=8, value=f"=SUM(H{sum_range_start}:H{sum_range_end})").font = BOLD
    detail.cell(row=row, column=8).alignment = RIGHT
    detail.cell(row=row, column=8).number_format = CNY
    detail.cell(row=row, column=8).fill = TOTAL_FILL
    for col in range(1, 9):
        detail.cell(row=row, column=col).border = BORDER_ALL

# --- A. 设计费（按月拆解 12 期 · 总 ¥28,000） ---
section_row(2, "A. 设计费（Design · 按月拆解 12 期 · 总额 ¥28,000）")
months_design = [
    (1, "9 月（启动月）", "品牌视觉系统建立（色板/字体/SVG图标库/PWA图标/风格指南）+ 3 款首发相框模板（路线打卡/旅行明信片/车窗视角）+ PC+移动端双端视觉规范", 3800, "启动重头，建立全年视觉基底"),
    (2, "10 月", "Autumn Colors 主题色 + 1 款新相框 + 月度文案 + 装饰图标", 2200, "逐月新鲜感"),
    (3, "11 月", "Misty Lake 主题色 + 1 款新相框 + 月度文案 + 装饰图标", 2200, "逐月新鲜感"),
    (4, "12 月", "Winter Wonderland 主题色 + 节日专题相框 + 文案 + 图标", 2200, "节日营销支持"),
    (5, "1 月", "New Year Drive 主题色 + 1 款新相框 + 新年文案 + 图标", 2200, "新年活动"),
    (6, "2 月", "Valentine Ride 主题色 + 情人节专题相框 + 文案 + 图标", 2200, "情人节专题"),
    (7, "3 月", "Spring Bloom 主题色 + 春日相框 + 文案 + 图标", 2200, "春日主题"),
    (8, "4 月", "Cherry Road 主题色 + 樱花季专题相框 + 文案 + 图标", 2200, "樱花季专题"),
    (9, "5 月", "Coastal Drift 主题色 + 海岸线相框 + 文案 + 图标", 2200, "海岸线主题"),
    (10, "6 月", "Desert Light 主题色 + 沙漠光线相框 + 文案 + 图标", 2200, "沙漠光线主题"),
    (11, "7 月", "Highland Pass 主题色 + 高地穿越相框 + 文案 + 图标", 2200, "高地穿越 + 半年度回顾"),
    (12, "8 月（收官月）", "Sunset Mile 主题色 + 收官相框 + 文案 + 图标 + 年度专版", 2200, "年度收官 + 数据复盘"),
]
r = 3
for idx, name, content, price, desc in months_design:
    detail.row_dimensions[r].height = 38
    vals = [idx, name, content, 1, price, desc, "月"]
    for j, v in enumerate(vals, start=1):
        c = detail.cell(row=r, column=j, value=v)
        c.font = NORMAL
        c.alignment = LEFT if j in (2, 3, 6) else CENTER
        c.border = BORDER_ALL
    cell = detail.cell(row=r, column=8, value=f"=D{r}*E{r}")
    cell.font = NORMAL
    cell.alignment = RIGHT
    cell.number_format = CNY
    cell.border = BORDER_ALL
    detail.cell(row=r, column=5).number_format = CNY
    r += 1
subtotal_row(r, "A 小计（设计费 · 12 个月度）", 3, r - 1)
SUBTOTAL_ROWS["A"] = r
r += 2

# --- B. 一次性开发费 ---
section_row(r, "B. 一次性开发费（Development）")
b_items = [
    ("H5 主框架开发", "Vite + React + PC/移动端响应式适配 + Vercel 全球托管", 1, 7000, "PC 桌面（≥1024px）+ 移动端（≤768px）双端自适应，PWA Manifest、Lighthouse 95+", "套"),
    ("四大流程页面", "品牌首页 / 月度任务弹窗 / 模板创作 / 一键分享", 4, 1500, "PC+移动端双端适配，含路由、状态管理、断点响应式", "页"),
    ("图片生成与系统分享", "html-to-image 截图 + Web Share API（带文件）+ FB/IG 调起", 1, 1000, "支持 Facebook / Instagram App 一键带图分享", "套"),
    ("月度主题引擎", "12 个月主题切换 + 全年主题画廊 + 每月差异化文案注入", 1, 500, "数据驱动：themes.js 一处维护全局生效", "套"),
    ("PWA / 缓存 / 离线", "离线访问、添加到主屏、桌面图标", 1, 500, "提升海外用户访问体验", "套"),
]
b_start = r + 1
r = b_start
for i, it in enumerate(b_items, start=1):
    item_row(r, i, *it)
    r += 1
subtotal_row(r, "B 小计（一次性开发费）", b_start, r - 1)
SUBTOTAL_ROWS["B"] = r
r += 2

# --- C. 客户确认 / 项目管理 ---
section_row(r, "C. 客户确认与项目管理（UAT & PM）")
c_items = [
    ("需求梳理 / 方案确认", "需求确认、信息架构、流程图、PRD 验收标准", 1, 500, "覆盖 12 个月度主题上线", "套"),
    ("客户评审 / 反馈落地", "两轮视觉 + 功能评审会（含会议纪要、修订意见落地）", 2, 300, "保障上线即验收通过", "轮"),
    ("UAT 验收与上线支持", "回归测试、生产部署协助", 1, 400, "年度上线支持", "次"),
]
c_start = r + 1
r = c_start
for i, it in enumerate(c_items, start=1):
    item_row(r, i, *it)
    r += 1
subtotal_row(r, "C 小计（客户确认 / 项目管理）", c_start, r - 1)
SUBTOTAL_ROWS["C"] = r
r += 2

# --- D. 月度运营与维护 ---
section_row(r, "D. 月度运营与维护费（按月续约 · 12 个月）")
d_items = [
    ("月度主题内容更新", "月度文案润色、话题标签、品牌色微调", 12, 300, "对应 A 板块每月新模板的文案落地", "月"),
    ("上线部署 / 回归测试", "新版上线、回归测试、兼容性检查、Bug 修复", 12, 200, "确保零中断发布，含依赖升级", "月"),
    ("节日 / 营销活动素材", "节日、营销节点的快速响应素材", 4, 500, "覆盖 4 个重大节点（圣诞/情人节/樱花季/年度收官）", "次"),
]
d_start = r + 1
r = d_start
for i, it in enumerate(d_items, start=1):
    item_row(r, i, *it)
    r += 1
subtotal_row(r, "D 小计（月度运营与维护）", d_start, r - 1)
SUBTOTAL_ROWS["D"] = r
r += 2

# --- E. 托管 / 域名 ---
section_row(r, "E. 托管 / 空间 / 域名（年度）")
e_items = [
    ("Vercel Pro 托管", "全球 CDN · 自动 HTTPS · 预览部署 · 99.99% SLA", 1, 1200, "覆盖海外多区域访问", "年"),
    ("域名注册 / 维护", ".com / .life 等海外品牌域名", 1, 300, "首年注册 + WHOIS 隐私保护", "年"),
    ("SSL / DNS 配置", "证书托管 + DNS 解析优化", 1, 0, "Vercel 自动签发，含在托管费内", "年"),
]
e_start = r + 1
r = e_start
for i, it in enumerate(e_items, start=1):
    item_row(r, i, *it)
    r += 1
subtotal_row(r, "E 小计（托管 / 空间 / 域名）", e_start, r - 1)
SUBTOTAL_ROWS["E"] = r
r += 2

# --- F. 运营服务 ---
section_row(r, "F. 运营服务费（年度）")
f_items = [
    ("内容运营支持", "话题策划、文案润色", 12, 200, "服务于月度主题上线", "月"),
    ("数据监控 / 月报", "UV / 分享率 / 月度活跃 + 报告", 12, 100, "每月 1 份数据报告", "月"),
    ("客户活动支持", "节日 / 营销节点快速响应", 4, 100, "4 次专项活动覆盖", "次"),
]
f_start = r + 1
r = f_start
for i, it in enumerate(f_items, start=1):
    item_row(r, i, *it)
    r += 1
subtotal_row(r, "F 小计（运营服务）", f_start, r - 1)
SUBTOTAL_ROWS["F"] = r
r += 2

# --- 项目总计（不含税） ---
total_row = r
detail.row_dimensions[total_row].height = 30
detail.merge_cells(f"A{total_row}:G{total_row}")
detail.cell(row=total_row, column=1, value="项目总计（不含税 · 税前）").font = Font(name="Arial", size=12, bold=True, color="FFFFFF")
detail.cell(row=total_row, column=1).fill = HEADER_FILL
detail.cell(row=total_row, column=1).alignment = Alignment(horizontal="right", vertical="center", indent=1)
sum_refs = "+".join([f"H{SUBTOTAL_ROWS[k]}" for k in ["A","B","C","D","E","F"]])
detail.cell(row=total_row, column=8, value=f"={sum_refs}").font = Font(name="Arial", size=12, bold=True, color="FFFFFF")
detail.cell(row=total_row, column=8).fill = HEADER_FILL
detail.cell(row=total_row, column=8).alignment = RIGHT
detail.cell(row=total_row, column=8).number_format = CNY
SUBTOTAL_ROWS["TOTAL"] = total_row
for col in range(1, 9):
    detail.cell(row=total_row, column=col).border = BORDER_HEAD

# --- 封面汇总回填 ---
labels_keys = ["A", "B", "C", "D", "E", "F"]
for i, key in enumerate(labels_keys):
    row = SUMMARY_START_ROW + i
    cover[f"F{row}"] = f"=报价明细!H{SUBTOTAL_ROWS[key]}"
    cover[f"F{row}"].font = NORMAL
    cover[f"F{row}"].alignment = RIGHT
    cover[f"F{row}"].number_format = CNY

# 小计行 = A..F
subtotal_cover_row = SUMMARY_START_ROW + 6
sum_refs_cover = ",".join([f"F{SUMMARY_START_ROW + i}" for i in range(6)])
cover[f"F{subtotal_cover_row}"] = f"=SUM({sum_refs_cover})"
cover[f"F{subtotal_cover_row}"].font = BOLD
cover[f"F{subtotal_cover_row}"].alignment = RIGHT
cover[f"F{subtotal_cover_row}"].number_format = CNY

# 增值税行 = 小计 * 6%
vat_row = SUMMARY_START_ROW + 7
cover[f"F{vat_row}"] = f"=ROUND(F{subtotal_cover_row}*0.06,0)"
cover[f"F{vat_row}"].font = NORMAL
cover[f"F{vat_row}"].alignment = RIGHT
cover[f"F{vat_row}"].number_format = CNY

# 含税合计
total_cover_row = SUMMARY_START_ROW + 8
cover[f"F{total_cover_row}"] = f"=F{subtotal_cover_row}+F{vat_row}"
cover[f"F{total_cover_row}"].font = BOLD
cover[f"F{total_cover_row}"].alignment = RIGHT
cover[f"F{total_cover_row}"].number_format = CNY

detail.print_options.horizontalCentered = True
detail.page_setup.orientation = detail.ORIENTATION_LANDSCAPE
detail.page_setup.fitToWidth = 1
detail.page_setup.fitToHeight = 0
detail.sheet_properties.pageSetUpPr.fitToPage = True

# ============================================================
# Sheet 3: 月度计划
# ============================================================
plan = wb.create_sheet("月度计划")
plan.sheet_view.showGridLines = False

pwidths = {"A": 6, "B": 12, "C": 22, "D": 22, "E": 18, "F": 16}
for k, w in pwidths.items():
    plan.column_dimensions[k].width = w

plan.row_dimensions[1].height = 30
ph = ["月份", "主题", "核心话题 / Hashtag", "相框模板版本", "上线日期", "设计单价"]
for i, h in enumerate(ph, start=1):
    c = plan.cell(row=1, column=i, value=h)
    c.font = WHITE_BOLD
    c.fill = HEADER_FILL
    c.alignment = CENTER
    c.border = BORDER_HEAD

months = [
    (9, "Share Your Destination", "#KaiyiLifeInMotion · #ShareYourDestination", "v1.0（首发 3 款）", "2026-09-15", 3800),
    (10, "Autumn Colors", "#AutumnColors · #KaiyiLifeInMotion", "v1.1", "2026-10-15", 2200),
    (11, "Misty Lake", "#MistyLake · #KaiyiLifeInMotion", "v1.2", "2026-11-15", 2200),
    (12, "Winter Wonderland", "#WinterWonderland", "v1.3", "2026-12-15", 2200),
    (1, "New Year Drive", "#NewYearDrive", "v1.4", "2027-01-15", 2200),
    (2, "Valentine Ride", "#ValentineRide", "v1.5", "2027-02-14", 2200),
    (3, "Spring Bloom", "#SpringBloom", "v1.6", "2027-03-15", 2200),
    (4, "Cherry Road", "#CherryRoad", "v1.7", "2027-04-15", 2200),
    (5, "Coastal Drift", "#CoastalDrift", "v1.8", "2027-05-15", 2200),
    (6, "Desert Light", "#DesertLight", "v1.9", "2027-06-15", 2200),
    (7, "Highland Pass", "#HighlandPass", "v2.0", "2027-07-15", 2200),
    (8, "Sunset Mile", "#SunsetMile", "v2.1", "2027-08-15", 2200),
]
r = 2
for m in months:
    plan.row_dimensions[r].height = 26
    for i, v in enumerate(m, start=1):
        c = plan.cell(row=r, column=i, value=v)
        c.font = NORMAL
        c.alignment = CENTER if i in (1, 5, 6) else LEFT
        c.border = BORDER_ALL
        if i == 2:
            c.font = BOLD
        if i == 6:
            c.number_format = CNY
    r += 1

plan.row_dimensions[r + 1].height = 24
plan.merge_cells(f"A{r+1}:E{r+1}")
c = plan.cell(row=r+1, column=1, value="12 个月 · 设计费小计")
c.font = BOLD
c.alignment = Alignment(horizontal="right", vertical="center", indent=1)
c.fill = TOTAL_FILL
cell = plan.cell(row=r+1, column=6, value=f"=报价明细!H{SUBTOTAL_ROWS['A']}")
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
# Sheet 4: 服务条款
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
    ("项目总价", "本项目年度总额 ¥58,000（不含税），含税 ¥61,480。其中设计费占 ¥28,000（按月拆解 12 期）。"),
    ("设计费结构", "A 板块设计费按月拆解 12 期：9 月启动月 ¥3,800（含品牌系统基础 + 3 款首发相框），10–8 月月度项 ¥2,200/期，合计 ¥28,000。"),
    ("交付物清单", "（1）H5 主程序（含源码，PC+移动端双端响应式）；（2）12 套主题视觉稿；（3）36 款相框模板；（4）月度维护 12 次；（5）Vercel 全球托管 + 域名；（6）月度数据报告 × 12。"),
    ("一次性付款", "B + C 项合计一次性付款 100%，项目启动 5 个工作日内支付。"),
    ("设计费付款", "A 项设计费按月分期付款，每月 5 日前开具上月发票并收款。"),
    ("月度付款", "D + F 项按月支付，每月 5 日前开具上月发票并收款。"),
    ("年度付款", "E 项年度费用首次部署时一次性支付。"),
    ("知识产权", "项目交付物的著作权归乙方所有；甲方拥有本项目专属永久使用权；乙方可在作品集中展示。"),
    ("客户配合", "甲方应在 5 个工作日内反馈确认意见；超期未反馈视为默认通过确认。每自然月最多发起 2 次模板修订。"),
    ("维保范围", "免费维保期 12 个月，含 Bug 修复、依赖升级、安全补丁；新功能 / 新主题属月度维护范围。"),
    ("数据合规", "项目遵守 GDPR 与目标市场数据法规；用户上传图片仅本地处理，不上传服务器。"),
    ("终止条款", "任意一方可提前 30 日书面通知终止合同；已交付部分按比例结算，未交付部分退还未发生款项。"),
    ("争议解决", "本协议适用中华人民共和国法律；争议提交项目所在地人民法院诉讼解决。"),
    ("报价有效期", "自签发之日起 30 个自然日内有效。"),
]
r = 2
for i, (k, v) in enumerate(terms_data):
    terms.row_dimensions[r].height = 40
    cell_k = terms.cell(row=r, column=2, value=k)
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
# Sheet 5: 联系信息
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

output = "C:/Users/zyd/WorkBuddy/2026-09-08-08-07-16/kaiyi-h5/kaiyi-quotation.xlsx"
wb.save(output)
print(f"Saved: {output}")
print(f"Subtotal rows: {SUBTOTAL_ROWS}")
print(f"Project total before tax should be: 28000+15000+1500+8000+1500+4000 = 58000")
