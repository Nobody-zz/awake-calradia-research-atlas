# CGEO-MAP-AUD-002｜卡拉迪亚地形图与水系图：数据绘图说明

- 日期：2026-10-23
- 版本：v1.1（浅海与低地标色修正）
- Google Drive 说明文档：[打开](https://docs.google.com/document/d/1MMTodRv647wt4OzmGuKdGWwDRkEDEanBpl6StW63KeQ/edit)
- 地图文件夹：[打开](https://drive.google.com/drive/folders/1eJjV3BJr2AOS3N3_d-6lY8sQHOGSqPVT)
- 地形图：[PNG](https://drive.google.com/file/d/1qRbn2JqQmEFeyZLVZtzwTx3SJIXv37fN/view)
- 水系证据图：[PNG](https://drive.google.com/file/d/1tsx6G2G1EQzBY02rrZ8s0d6tX9suTKlk/view)
- 完整制图包：[ZIP v1.1](https://drive.google.com/file/d/1lFhCTUe_i2IiMK_3wQd9gaqfza5iZu0v/view)

## v1.1 修订摘要

上一版沿用原高程分析图的蓝—青—绿—黄假彩色，导致海域与相对低地视觉上不易区分。本版将海域重编码为深蓝，并在海陆边界内侧加入浅蓝近岸带；陆地改用浅绿低地、绿色中低地/丘陵、赭黄色高地与灰褐色山地高处。两幅地图使用同一套颜色规则，并加入统一图例与海陆边界线。

**重要限定：**浅蓝近岸带是为阅读清晰而设置的制图缓冲区，并非原始测深数据，不代表真实水深。图例中的地形颜色表达原高程可视化的相对色阶，不代表经过米制标定的海拔等级。海陆分割依据已归档高程可视化中的主海色及与图框边缘连通的像素建立，属于基于现有图像的制图分类，不替代从原始 HGHT 数据和水面几何进行独立复算。

## 数据与方法

- 地形底图：`CGEO-MAP-RES-005_双版本同尺度高程图.png` 的原版 `Main_map` 面板，坐标范围为 0–848 游戏场景单位。该图本身是从已解码 HGHT 高程栅格生成的研究可视化；当前工作环境没有原始 4097×4097 高程 PNG，因此本轮对已归档的真实分析图作坐标面板裁切，再进行程序化重着色、地名与图例绘制。未将其伪装成重新读取原始像素后计算的全新 hillshade。
- 海域分类：根据现有可视化中的主海色及与图框边缘的连通关系建立海域掩膜；近岸浅蓝带宽度为 10 个源图像像素，作为视觉区分用的制图参数，不对应测深或海平面以下的真实深度。
- 水系证据：`CGEO-MAP-RES-005_原版河流路径与PHYM7叠加.png` 的河流路径/PHYM 图层可视化，经坐标面板裁切后叠加至同坐标系地形底图。
- 聚落位置：原版 `Modules/SandBox/ModuleData/settlements.xml` 的 `town_*` 实体 `posX`、`posY`，共解析 53 个城镇；地图标注其中分布较有代表性的 25 个（地形图）与 10 个（水系图）。
- 场景坐标与比例尺：比例尺标注为“100 场景单位”，不转换成公里；场景单位到现实长度未校准。

## 水系图的证据边界

图上十条河流线的编号与侧栏对应 `scene.xscene` 内部路径 ID：`river_vlandia`、`river_bat_vla`、`river_bat`、`river_bat_emp`、`river_bat_emp2`、`river_emp_west`、`river_emp_west2`、`river_emp_center`、`river_emp_north`、`river_emp_south`。侧栏中文是便于阅读的研究性描述，不是官方水文专名。路径点的储存顺序不能证明真实水流方向；PHYM `river` 是 terrain layer index，不等于精确河岸边界或完整水面多边形。

## 地形图的证据边界

深蓝表示由现有分析图分类出的海域主体；浅蓝表示近岸制图带；浅绿表示相对低地。浅蓝带宽度为 10 个源图像像素，只是制图参数，不对应真实深度。若要绘制真实浅海/深海分级，必须取得可校准的水深或水面/地形高程数据。图中“北部山地”“西部高地”“中部起伏低地”“东部山地”“南部高地”均为依据图面形态所加的描述性地貌标签，不是官方命名的地理区。聚落中文名是研究用译名，英文官方名称用于回查；未将未经证实的河流、湖泊或山脉专名补画到图上。

## 后续升级

如取得原始 `original_height_mosaic_4097.png`、`warsails_height_mosaic_4097.png`、原版 `scene.xscene` 河流路径控制点及《战帆》`river_triangles.bin` 对应源网格，下一版应从原始数值栅格直接生成 hillshade、等高线与矢量河道，并独立验证海陆边界和水深/水面属性，而不再依赖归档预览图裁切。DLC 与原版必须分别制图，不把不同版本坐标或资源直接混叠。


## v1.2 — 聚落中文地名规范（2026-10-23）

- [聚落中文地名规范表 CSV](CGEO-MAP-RES-014_settlement_chinese_name_register.csv)
- [聚落中文地名规范表 Markdown](CGEO-MAP-RES-014_settlement_chinese_name_register.md)
- [Google Drive CSV](https://drive.google.com/file/d/1-jGBsvgz3Gj6DuxiCAzTKrf6Y7Mi2Avh/view)
- [Google Drive Markdown](https://drive.google.com/file/d/1eo7NEQb4qYJJIxDcCFmvEFTW27YOO76H/view)
- [地图包 v1.2](https://drive.google.com/file/d/1lFhCTUe_i2IiMK_3wQd9gaqfza5iZu0v/view)

当前官方简体中文档案包含聚落地理/百科描述，但未找到可逐一对应全部53个城镇的独立 `Settlements.Settlement.name.*` 中文名称键。地图上不带 † 的中文形式可在官方地理文本中检出；这不等于独立名称键已核实。带 † 的名称是研究暂译，待后续核验。水系、地形底图及其证据边界不变。


## v1.3 地名修订与标签避让（2026-10-23）

- Seonon 改为“肖农”；Epicrotea 改为“厄庇克洛忒亚”，按项目负责人本轮校正采用。当前随档中文语言文件未提供对应独立名称中文键，故规范表明确记录其来源为用户校正，不伪称已由 XML 键直接验证。
- 两张地图改用程序化碰撞检测：对地名标签的候选偏移逐一测试，避开已放置标签、地图内既有地貌/路径文字及地图边界；标签明显偏离锚点时显示细引线。
- 地形/水系底图与原有证据边界不变。


## v1.4 坐标配准纠错（2026-10-23）

复核发现前版《战帆》高程图裁取了双面板图的错误像素区，水域图则错误地假定绘图范围为 0–1040；这会使底图与聚落/港口场景 XY 不重合。现已按原始绘图框像素边界与可见坐标刻度重新裁切和回标，四张地图分别输出到 `卡拉迪亚地理地图_坐标配准修订_v1.5.zip`。原版地形面板与原版河流图按 0–848 场景单位对齐；《战帆》高程面板按 0–1040 对齐；《战帆》水域图按原始坐标刻度回标，不再假定范围为 0–1040。

**证据限制：**《战帆》水域底图仍基于已归档的 Navmesh 绘图 PNG，而非原始 `navmesh.bin` 直接重绘；最终像素级验证需恢复原始 Navmesh 数据与绘图脚本。港口 XY 继续沿用 RES-012 中明确标为候选解释的坐标模型。坐标审计 JSON：`CGEO-MAP-AUD-003_coordinate_registration_audit_v1.5.json`。


## v1.6 — 统一原版配色方案（2026-10-23）

本轮将原版地形图、原版水系图、《战帆》地形图、《战帆》水域—港口图统一为同一视觉色阶：深蓝表示深海/外海，浅蓝表示近岸浅海带，浅绿表示相对低地，绿色表示中低地/丘陵，赭黄表示相对高地/山地。原版水系图仍叠加显式河流路径；《战帆》水域图仍表示导航水域面类型与港口点位，不与原版河流路径混为一类。

- 审计记录：`research/geo/90/EVD/CGEO-MAP-AUD-003_coordinate_palette_audit_v1.6.json`
- 本地交付包文件名：`卡拉迪亚地理地图_原版配色统一修订_v1.6_交付.zip`
- 地名校正继续采用：Seonon = 肖农；Epicrotea = 厄庇克洛忒亚。

配色统一不改变数据来源、坐标范围或证据等级；《战帆》港口 XY 仍按 RES-012 候选坐标模型使用，待原始 navmesh.bin 完成独立配准验证。


### v1.6 配色修订｜Drive 二进制文件已同步（2026-10-23）

Drive 中的原有 PNG 文件 ID 已被 v1.6 成品实际覆盖，并改名标记版本；交付 ZIP 也已覆盖。链接：
- [原版地形图 PNG](https://drive.google.com/file/d/1qRbn2JqQmEFeyZLVZtzwTx3SJIXv37fN/view) — 1,078,557 B
- [原版水系图 PNG](https://drive.google.com/file/d/1tsx6G2G1EQzBY02rrZ8s0d6tX9suTKlk/view) — 1,217,343 B
- [《战帆》地形图 PNG](https://drive.google.com/file/d/1YbF6zMWsnov7e9XBUJmnlTKn7tr0eYHd/view) — 993,198 B
- [《战帆》水域—港口图 PNG](https://drive.google.com/file/d/1O-2VWngB_8sgDQZ1ckOTcb6f1B43gFZY/view) — 1,440,705 B
- [完整交付包 ZIP](https://drive.google.com/file/d/1lFhCTUe_i2IiMK_3wQd9gaqfza5iZu0v/view) — 4,538,085 B

统一配色为深蓝外海、浅蓝近岸、浅绿低地、绿色中低地/丘陵、赭黄高地。原版与《战帆》继续分开记录；《战帆》港口坐标仍受 RES-012 候选坐标解释限制。


## v1.7 配色重制（2026-10-23）

v1.6 的配色结果不合格：低地偏白、海陆边界层次不稳定，且《战帆》地形曾错误地借用导航水域掩膜。v1.7 改为直接依据 RES-005 已解码高程分析面板的色相进行地形重渲染，外海使用较柔和的深蓝，近岸使用浅蓝制图带，低地使用浅鼠尾草绿，中高地采用分级绿，高地采用低饱和赭黄。

- 原版高程面板裁切框：`[186, 71, 855, 740]`，映射到 `0–848` 场景单位。
- 《战帆》高程面板裁切框：`[1054, 71, 1724, 740]`，映射到 `0–1040` 场景单位。
- 不再把《战帆》导航水域掩膜套到高程图上；海域主体从高程面板蓝色分量与图框连通关系识别，近岸带是视觉强调，不代表实测水深。
- 《战帆》水域—港口图仍为导航水域类别图，与原版显式河流 Paths 保持证据类别分离。

四张地图原位更新在 Google Drive：
- [原版地形图 v1.7](https://drive.google.com/file/d/1qRbn2JqQmEFeyZLVZtzwTx3SJIXv37fN/view)
- [原版水系图 v1.7](https://drive.google.com/file/d/1tsx6G2G1EQzBY02rrZ8s0d6tX9suTKlk/view)
- [《战帆》地形图 v1.7](https://drive.google.com/file/d/1YbF6zMWsnov7e9XBUJmnlTKn7tr0eYHd/view)
- [《战帆》水域—港口图 v1.7](https://drive.google.com/file/d/1O-2VWngB_8sgDQZ1ckOTcb6f1B43gFZY/view)
- [Google Drive 制图说明 v1.7](https://docs.google.com/document/d/1MMTodRv647wt4OzmGuKdGWwDRkEDEanBpl6StW63KeQ/edit)


## v1.8 海陆边界恢复（2026-10-23）

v1.7 配色版已撤回：其海陆分类依据高程可视化 RGB 的蓝色色相阈值，但该高程图中蓝色同时表示低海拔地形，不能作为可靠海洋掩膜，导致部分陆地被误判为海域。v1.8 回退到经过坐标配准的 v1.5 地图输出，暂时放弃 v1.7 的重着色；在取得独立有效的海陆分类掩膜并通过逐图目视检查前，不再发布新的配色版。

- 原版地形图：[Drive](https://drive.google.com/file/d/1qRbn2JqQmEFeyZLVZtzwTx3SJIXv37fN/view)
- 原版水系图：[Drive](https://drive.google.com/file/d/1tsx6G2G1EQzBY02rrZ8s0d6tX9suTKlk/view)
- 《战帆》地形图：[Drive](https://drive.google.com/file/d/1YbF6zMWsnov7e9XBUJmnlTKn7tr0eYHd/view)
- 《战帆》水域—港口图：[Drive](https://drive.google.com/file/d/1O-2VWngB_8sgDQZ1ckOTcb6f1B43gFZY/view)
- v1.8 恢复包：[Drive](https://drive.google.com/file/d/1lFhCTUe_i2IiMK_3wQd9gaqfza5iZu0v/view)
- 本地交付包文件名：`卡拉迪亚地理地图_海陆边界恢复_v1.8.zip`


## 后续事故校正｜CGEO-MAP-AUD-004（2026-10-23）

此前 v1.6–v1.8 对海陆填色的相关宣称需要纠正：高程图 RGB 蓝色色相不是海洋掩膜，曾掩盖大面积低高程陆地。v1.8 仅恢复旧图颜色，并未验证水陆边界，不能作为最终海陆图。请以 [AUD-004 全域高程工作图审计](CGEO-MAP-AUD-004.md) 和 [Google Drive v1.9 独立工作图](https://drive.google.com/drive/folders/1eJjV3BJr2AOS3N3_d-6lY8sQHOGSqPVT)为准。暂不将任何版本的猜测海陆填色引入正式论文。
