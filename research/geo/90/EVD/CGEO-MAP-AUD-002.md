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
