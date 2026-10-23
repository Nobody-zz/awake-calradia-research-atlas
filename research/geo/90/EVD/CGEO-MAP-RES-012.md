# CGEO-MAP-RES-012｜《战帆》港口—村庄登陆点导航路径与直线距离比较

**日期**：2026-10-23  
**[Google Drive正式报告](https://docs.google.com/document/d/1jDRZrvSPNy4vJyGZoEKRUsgalbchCR0d1D0-POnJtj4/edit)** · [复核ZIP（脚本+CSV+图）](https://drive.google.com/file/d/1GMG8gXe70m376txGvIcZH0lQrSz5552G/view) · [分布图](https://drive.google.com/file/d/1XZi6UKqfx-_KTuYdQMAndpz3-l_Hk-eG/view)

## 档案定位与来源

- [RES-009](CGEO-MAP-RES-009.md) **已经**证明144个 `drop_point` 是72个父级的civilian/looted配对；本报告的对应计数只是复核，不宣称首次发现。
- [RES-010](CGEO-MAP-RES-010.md) **已经**把29个城镇港口与72个登陆点聚落关联至当前官方 `NavalDLC/settlements.xml`，核定了相应英文回退名和有证据的中文译名。
- [RES-011](CGEO-MAP-RES-011.md) **已经**配准101个聚落XML坐标和水路接入锚点。
- **本报告新增**：29个港口与72组登陆点之间的导航面共享边加权路径代理、六个River港口到CoastalSea的路径代理、以及直线最近港口与路径最近港口的差异审计。

使用原始 `warsails/scene.xscene`、`warsails/navmesh.bin` 和[RES-008](CGEO-MAP-RES-008.md)已纠正的radians/XYZ**候选**世界坐标。只读处理，不修改或再分发游戏原始资源。

## 样本

29个 `town_port`，对应29个不同父级 `town_*`。144个 `drop_point`，对应72个不同父级，每个父级恰好2个（41个 `village_*`、31个 `castle_village_*`）。72对中28对的XY相同（1e−8容差），44对有小偏移，最大0.637120场景单位（`castle_village_EW7_2`）；**全部72对在同一Navmesh面**。状态配对的直接XML证明参见RES-009。

## 六个River(11)类型港口

按RES-010已核验的官方聚落XML英文回退名列出；中文名只有当前DLC语言表直接核定的才标注。

| 场景ID | 官方英文回退名 | 当前DLC官方中文证据 | 所在River面到最近CoastalSea面的图距离代理（场景单位） |
|---|---|---|---:|
| `town_A7` | Askar | 当前DLC中文表未直接匹配 | 151.483 |
| `town_ES3` | Poros | 当前DLC中文表未直接匹配 | 26.976 |
| `town_EW1` | Lageta | 当前DLC中文表未直接匹配 | 79.418 |
| `town_EW6` | Rhotae | 当前DLC中文表未直接匹配 | 102.820 |
| `town_N4` | Hargard | **哈加德（当前DLC官方简体中文）** | 256.504 |
| `town_V3` | Pravend | 当前DLC中文表未直接匹配 | 44.485 |

这是**Navmesh面重心加权图**上的距离代理，不是港口到海岸线的最短距离，更不是实际游戏航行里程。

## 直线最近港口与导航图最近港口

- 方法A：每个村庄父级取第一个 `drop_point`，选择XY直线距离最小的港口。
- 方法B：把River(11)、CoastalSea(18)、OpenSea(19)、UnderBridge(25)的Navmesh面作为节点，按共享同一edge ID建立双向边，边权为面重心间XY欧氏距离；对29个港口运行Dijkstra，加上起终点标记到所属面重心的距离后选择最短代理。
- **56/72组（77.78%）** 的两个最近港口相同；**16/72组（22.22%）不同**。
- 72组最短港口路径代理：中位数65.016、90百分位142.971、最大258.830场景单位。
- 29个港口两两406个无序组合的路径代理距离中位数809.467场景单位。

这里的16组差异表明，**不能把平面直线最近港口自动当作水路网络最近港口**。但Navmesh面重心连线未必完全处于实际可航走廊，亦未验证船舶尺寸、桥下净空、水面Z、速度或引擎寻路；因此方法B仍只是研究性代理，**不能直接解释为游戏内行政从属或真实航线**。本轮用每个父级的第一个状态点代表村庄，下一步应检查两个状态点分别计算时结果是否变化。

## 数据与复核

- [72组父级最近港口CSV](https://drive.google.com/file/d/1dvLWiuSc1KWbsNDxeZiOPq7Q6LDG878j/view)
- [29个港口网络CSV](https://drive.google.com/file/d/15qo8NOGuFCYs33GESLihVcGhIjTnXtm8/view)
- [完整8文件ZIP（含144标记、406港口对、源脚本、JSON、PNG）](https://drive.google.com/file/d/1GMG8gXe70m376txGvIcZH0lQrSz5552G/view)

**证据边界**：标记数量、父级名、Navmesh面类型、共享边来自原始游戏资源；世界坐标使用尚未由引擎源码终极验证的radians/XYZ模型；最短路径是自定义加权图算法。严禁将版本机制差异直接解释为卡拉迪亚自然地理变化。

## 两个状态点的稳定性复核

在144条原始drop_point候选坐标中，按72个父级逐对比较两个状态点：**72/72组直线最近港口ID相同，72/72组导航图最近港口ID相同，72/72组直线/导航图一致性判定相同**。标记级112/144一致、32/144不一致；父级级仍为56/72一致、16/72不一致。因此16组差异不是选择第一个状态点所造成，但依然只是离线Navmesh面重心加权图的结果，不是运行时实际航路验证。


## 补充勘误：`navmesh_detour_ratio` 字段（2026-10-23）

该字段是导航图路径长度代理除以直线最近港口距离。对于 `nearest_port_agrees=false` 的记录，分子与分母对应不同的港口 ID，因此它不是同一目的地的绕行倍率，不能解释为真实或代理路线的“绕行率”。请参见 [RES-013](CGEO-MAP-RES-013.md) 及 [Google Drive 原件](https://docs.google.com/document/d/1W9t-MWsR8mvuq5DoUZtPy_vTZ-IAQrqaB_hhWrgIJeo/edit)。RES-012 第九节所载双状态稳定性结果仍有效；本补充仅澄清比值字段的解释边界。
