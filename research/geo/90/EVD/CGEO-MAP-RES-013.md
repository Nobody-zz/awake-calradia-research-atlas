# CGEO-MAP-RES-013｜《战帆》村庄登陆点港口匹配差异组的稳健性审计与距离指标勘误

- 日期：2026-10-23
- 版本：v1.0
- 关联档案：RES-008、RES-009、RES-010、RES-011、RES-012
- Google Drive 原件：[打开文档](https://docs.google.com/document/d/1W9t-MWsR8mvuq5DoUZtPy_vTZ-IAQrqaB_hhWrgIJeo/edit)

## 一、研究问题与档案定位

本报告复核 RES-012 中“直线最近港口”与“Navmesh 共享边加权图路径代理最近港口”不一致的 16 组村庄登陆点父级。目标是判断差异是否由 civilian/looted 双状态标记的选取造成，并厘清这些差异能支持何种地理解释。本文是 RES-012 的补充审计，不重复声称 RES-009 至 RES-011 已完成的状态配对、聚落 ID 映射及坐标配准工作。

## 二、数据来源与方法边界

主要输入为 Google Drive 中的 [72 组登陆点 CSV](https://drive.google.com/file/d/1dvLWiuSc1KWbsNDxeZiOPq7Q6LDG878j/view)、[29 个港口网络 CSV](https://drive.google.com/file/d/15qo8NOGuFCYs33GESLihVcGhIjTnXtm8/view) 和[完整复核分析包](https://drive.google.com/file/d/1GMG8gXe70m376txGvIcZH0lQrSz5552G/view)。源资源为《战帆》 `scene.xscene`、`navmesh.bin`；世界坐标沿用 RES-008 的 radians/XYZ 候选模型，候选欧拉轴序尚未由引擎源码终极确认。

比较两个指标：

- **A：直线最近港口**。每个父级聚落的登陆点到 29 个 `town_port` 的平面 XY 直线距离最小者。
- **B：导航图代理最近港口**。把 River(11)、CoastalSea(18)、OpenSea(19)、UnderBridge(25) 面按共享 edge ID 连接，以相邻面重心 XY 距离为边权，运行 Dijkstra 并加上端点至面重心距离。

B 不是游戏运行时航行路线，也不直接等于天然水系、实际航行里程或政治行政联系。

## 三、总体结果

72 组登陆点父级中，56 组（77.78%）在两种指标下选择同一港口，16 组（22.22%）选择不同港口。

| 聚落资源类别 | 总数 | 不一致组数 | 描述性比例 |
|---|---:|---:|---:|
| `castle_village` | 31 | 8 | 25.81% |
| `village` | 41 | 8 | 19.51% |
| 合计 | 72 | 16 | 22.22% |

两类在本样本中均有差异；这些描述性比例不足以证明聚落类别影响港口可达性，也不能排除空间分布和网格几何造成的影响。

RES-012 第九节已逐一比较每个父级的两个 `drop_point` 状态：72/72 组的直线最近港口 ID 相同，72/72 组的导航图最近港口 ID 相同，且 72/72 组“两个指标是否一致”的判定相同。因此，16 组差异不是因只选取父级的第一个状态标记造成。该稳定性结论复用 RES-012 已完成的复核，不作为本报告的新发现。

## 四、16 组差异清单

距离单位均为游戏场景 XY 单位，不换算为现实里程。表中箭头左侧是直线最近港口，右侧是导航图代理最近港口；两个距离分别属于各自所选的港口。

| 登陆点父级 | 直线最近港口 | 直线距离 | 导航图代理最近港口 | 路径长度代理 |
|---|---|---:|---|---:|
| `castle_village_B1_2` | `town_V7` | 75.93 | `town_V3` | 175.35 |
| `castle_village_ES8_1` | `town_ES2` | 94.00 | `town_ES3` | 140.32 |
| `castle_village_N1_2` | `town_N4` | 73.32 | `town_S2` | 117.46 |
| `castle_village_N5_1` | `town_N2` | 106.69 | `town_N3` | 140.21 |
| `castle_village_N8_1` | `town_N4` | 73.83 | `town_S2` | 131.26 |
| `castle_village_S7_1` | `town_K3` | 88.01 | `town_S4` | 131.51 |
| `castle_village_V2_1` | `town_V5` | 53.94 | `town_V3` | 98.08 |
| `castle_village_V3_1` | `town_V3` | 31.68 | `town_V8` | 57.17 |
| `village_ES2_2` | `town_ES2` | 36.66 | `town_ES3` | 63.81 |
| `village_ES4_1` | `town_ES2` | 87.70 | `town_ES3` | 136.76 |
| `village_ES4_3` | `town_ES2` | 37.04 | `town_ES3` | 70.43 |
| `village_ES6_2` | `town_ES2` | 87.02 | `town_ES3` | 132.89 |
| `village_EW4_1` | `town_EW4` | 39.45 | `town_EW1` | 71.10 |
| `village_S6_1` | `town_S4` | 69.16 | `town_N2` | 146.21 |
| `village_S6_2` | `town_S4` | 77.48 | `town_N2` | 141.94 |
| `village_V3_2` | `town_V3` | 28.25 | `town_V8` | 65.80 |

机器可读子集见 [RES-013 mismatch CSV](CGEO-MAP-RES-013_mismatch_cases.csv)。

## 五、重复模式与解释限度

- `town_ES2 → town_ES3`：5 组（`castle_village_ES8_1`、`village_ES2_2`、`village_ES4_1`、`village_ES4_3`、`village_ES6_2`）。
- `town_N4 → town_S2`：2 组（`castle_village_N1_2`、`castle_village_N8_1`）。
- `town_S4 → town_N2`：2 组（`village_S6_1`、`village_S6_2`）。
- `town_V3 → town_V8`：2 组（`castle_village_V3_1`、`village_V3_2`）。
- 其余 5 组为单例差异：`town_V7 → town_V3`、`town_N2 → town_N3`、`town_K3 → town_S4`、`town_V5 → town_V3`、`town_EW4 → town_EW1`。

重复模式表明差异并非随机散布于 16 个完全不同的配对；但场景实体 ID 中的字母数字前缀尚未被证明是地理分区代码，不能仅凭 ES、N、S、V 等前缀把记录划为地理集群。必须结合实际地图坐标和水域网络图件验证。

## 六、距离指标术语勘误

RES-012 派生 CSV 中字段 `navmesh_detour_ratio` 不宜在所有记录中解释为“绕行率”。该字段是导航图路径长度代理除以直线最近港口距离。对于上述 16 组差异，分子和分母对应的港口 ID 不同，因此两者比值并非同一目的地的绕行倍率，不能用来衡量同一条路线相对直线的绕行程度。

后续引用时应将其视为“跨指标距离比（旧字段名 `navmesh_detour_ratio`）”，不用于推断真实绕行率。若要测算真正的同目的地路径膨胀，必须补算每个登陆点到“导航图代理所选港口”的直线距离，再与该港口的路径代理距离相除；该值仍是面重心图的几何近似，而非引擎实测航程。

## 七、结论

在现有候选坐标与 Navmesh 图模型下，22.22% 的登陆点父级在“直线最近”与“网络路径代理最近”之间发生港口选择变化；这一差异对 civilian/looted 两个状态标记的选择稳定。它说明直线邻近关系不能自动替代网络可达性指标。

本轮不能确认村庄在游戏运行时实际使用哪一港口、是否存在行政从属、是否形成真实贸易联系，或这些差异是否代表卡拉迪亚的历史地理关系。坐标变换、面重心边权与实际引擎寻路之间仍存在方法边界。

## 八、下一步

建议将下一项工作设为 RES-014“最近港口匹配的网络权重敏感性分析”，而不是重复聚落 ID 映射。至少比较面重心距离与共享边中点/通道门点距离等替代权重；同时计算每个登陆点到同一“网络选定港口”的直线距离，重新定义同目的地路径膨胀指标；将 16 组映射回地图后再判断是否存在可解释的水域通道或局部空间集群。在完成敏感性分析前，不把本报告结果直接提升为历史人文地理结论。

## 九、双端归档

- [Google Drive 原件](https://docs.google.com/document/d/1W9t-MWsR8mvuq5DoUZtPy_vTZ-IAQrqaB_hhWrgIJeo/edit)
- [RES-012 72 组父级最近港口 CSV](https://drive.google.com/file/d/1dvLWiuSc1KWbsNDxeZiOPq7Q6LDG878j/view)
- [RES-012 29 个港口网络 CSV](https://drive.google.com/file/d/15qo8NOGuFCYs33GESLihVcGhIjTnXtm8/view)
- [RES-012 完整复核分析包](https://drive.google.com/file/d/1GMG8gXe70m376txGvIcZH0lQrSz5552G/view)

研究文件不包含游戏原始二进制资源；所有地理解释均保留坐标模型、导航网格与推论层级的限制。
