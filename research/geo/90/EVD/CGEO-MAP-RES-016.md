# CGEO-MAP-RES-016｜《战帆》港口与导航网格空间配准复核（v2.2）

2026-10-23 · 卡拉迪亚大陆地理研究 · 地理测绘方法与港口区位专题

**状态：图像配准存在实证冲突；尚不能确认原始游戏网格或港口坐标错误，也未取得正式海岸线。**

## 研究问题
将既有 RES-012 的 29 个候选港口 XY 与 Navmesh 面类型声明，映射到独立 RES-006 的已渲染《战帆》水域类别图，检查两份研究成果是否构成同一可靠空间参照。

## 资料与方法
- CGEO-MAP-RES-006 战帆水域面类型 PNG（1340×1322），包含 OpenSea、CoastalSea、River 与导航陆面。
- RES-012 town_port_network_access.csv：29个候选港口 XY；6个面类型11（River），23个面类型18（CoastalSea）。
- RES-010 settlement name mapping CSV：港口实体与英文名称索引。
- 沿用 RES-015 近似图像回标：px=56.25+1.10375*xscene，py=1116.333−1.106667*yscene；采纳 RGB 欧氏距离小于12的来源本色像素。分别计算点到声明类别和任意可辨导航水域的最近距离。

## 结果
| 检查项 | 结果 |
|---|---:|
| 港口点数 | 29 |
| 声明类别与渲染图采样类别相符 | **1** |
| 落在可识别导航陆面颜色 | **18** |
| 落在 OpenSea / CoastalSea 颜色 | **7**（未必符合声明类别） |
| 未分类或抗锯齿色 | **4** |
| 到任一导航水域颜色距离 ≤5 场景单位 | **12** |
| 到任一导航水域颜色距离 >20 场景单位 | **11** |
| 到任一导航水域颜色距离中位数 | **11.45 场景单位（近似）** |
| 到声明类别颜色距离中位数 | **25.75 场景单位（近似）** |

距离较大的示例：Poros 78.91、Vostrum 69.90、Syronea 61.77、Askar 60.70、Hargard 55.13 场景单位（仅归档图像之间的近似测量，不是码头实际离水距离）。

## 学术判断
现有《战帆》候选港口 XY 与归档 Navmesh 渲染图 **未通过跨图空间一致性检验**。可能原因包括截图刻度回标、坐标转换、数据版本差异、港口点语义或 Navmesh 渲染误差。不能据此说游戏原始数据有误；更不能将候选港口吸附到最近蓝色像素后作为官方地图。

之前据错位地图推论的具体河口、临水类型、港口—海峡区位应降为待证假说。原版与《战帆》继续分别研究。

下一步须恢复各版本原始 Navmesh 顶点、面类型、港口及登陆点定位，直接实施点在多边形和面 ID 核验后再重画正式海岸线。

## 可核验附件
- [29港口逐点复核 CSV](https://drive.google.com/file/d/1e8z29r9rZ0kaSmrYcpGReVAEAY3UQYa_/view)
- [港口与导航类别交叉诊断图](https://drive.google.com/file/d/1a47JBgqUn6NoufCyL-7EOJdhY0X2U8rl/view)
- [29港口距同类导航水域统计图](https://drive.google.com/file/d/1sWPwUNSGtfZlfxYSVATk113dGxW2JAtc/view)
- [Google Drive 地图档案](https://drive.google.com/drive/folders/1eJjV3BJr2AOS3N3_d-6lY8sQHOGSqPVT)

本版使用已归档的二次渲染图，仅是一项交叉证据审计，不能替代原始导航网格。