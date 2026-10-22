# CGEO-MAP-RES-008｜《战帆》港口与登陆点旋转单位勘误及可航网格复核

- 日期：2026-10-23
- [Google Drive 原件](https://docs.google.com/document/d/1aL-g-FRDguFHEAFbMZ2ypz5uWMIEcHXnd3HS5mmMYVw/edit)
- 前序报告：[RES-007](CGEO-MAP-RES-007.md)（旧结论被本报告修订）
- 原始数据：本项目 `warsails/scene.xscene`、`warsails/navmesh.bin`（只读）

## 勘误：旧坐标旋转单位错误

RES-007 将 `rotation_euler` 的数值当作 **角度（degrees）**，只用父级Z旋转计算局部坐标。新一轮分别按角度、弧度及多种欧拉轴序重新计算，并以Navmesh面内含测试核验。这不是微小数值误差，而是会使大量港口标记落到错误导航面上的模型缺陷。

| 指标 | 旧模型：degrees、Z-only | 新候选：radians、Euler XYZ |
|---|---:|---:|
| town_port | 29 | 29 |
| town_port位于CoastalSea或River | **8** | **29**（CoastalSea 23、River 6） |
| drop_point | 144 | 144 |
| drop_point位于CoastalSea或River | **77** | **144**（CoastalSea 82、River 62） |
| 均位于候选水上组件#1 | 待复核 | **173** |
| 全部实例可落到Navmesh多边形内 | 173 | 173 |

**明确撤回**：“21个港口标记落在陆地面”和“67个登陆点标记落在陆地面”这两条旧模型结论。它们不是已核实的游戏港口现状。

## 实际校验

采用同一份NMG9网格解码，使用KD树检索候选网格面、XY多边形内含判断，使用Shapely STRtree计算到可航水域导航面多边形的距离。水上候选类型：River(11)、CoastalSea(18)、OpenSea(19)、UnderBridge(25)，不包含NonNavigableRiver(22)。

| 对照指标（173个实例） | 结果（场景XY单位） |
|---|---:|
| 旧degrees/Z-only → radians/XYZ坐标差，中位数 | 4.534 |
| 同上，90百分位数 | 10.103 |
| 同上，最大值 | 15.436 |
| 发生导航面类别改变的标记数 | 88（港口21、登陆点67） |
| radians/Z-only → radians/XYZ坐标差，中位数 | 0.0378 |
| 同上，最大值 | 0.986 |
| radians/Z-only与radians/XYZ的导航面类别差异 | **0个** |

仅用弧度制Z旋转与用弧度制完整XYZ旋转，恰好都能把173个标记放入可航候选面。这降低了“父级倾斜角导致面类别不稳定”的担忧。反之，弧度制 `zyx` 轴序有明显不同结果：仅8个港口属于CoastalSea、且一些港口落在陆地面，说明仍须核验引擎的准确欧拉约定。

## 证据界限

- 官方 [War Sails World Map](https://moddocs.bannerlord.com/war-sails/wsworldmap/) 要求 `town_port` 与 `drop_point` 标记位于可航导航面，如CoastalSea或River。弧度XYZ模型的173/173符合程度构成**独立功能约束的强支持**。
- 但我们尚未从引擎源码直接验证其精确欧拉轴序、旋转矩阵手性与父子缩放应用顺序，因此称其为**最符合官方约束的候选坐标模型**，不能提前宣称完全掌握引擎变换。
- 144个drop_point实例有72个不同父级，不能写成144座村庄；29个town_port实例对应29个不同父级。实际航线可达性仍须游戏内寻路与水陆接驳机制核对。
- 本轮不将可航Navmesh连通性解释为自然河网或地貌演化证据。

## 交付

本次保留以下可复核数据文件：`marker_rotation_audit.py`、`navmesh_reference.py`、`rotation_audit_summary.json`、`marker_rotation_sensitivity.csv`、`town_port_corrected_world_coordinates.csv`、`drop_point_corrected_world_coordinates.csv`、`marker_positions_radian_xyz_overlay.png`。七项成果组成完整ZIP（不含任何原始游戏二进制资源）。

下一项研究是核验引擎确切矩阵约定、把港口与村庄ID可靠关联，并检查各港口对应的实际可航路径。
