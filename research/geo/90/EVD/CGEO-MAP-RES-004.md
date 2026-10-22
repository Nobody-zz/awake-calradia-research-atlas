# CGEO-MAP-RES-004｜高程物理标定、PHYM季节图层与Flowmap证据边界

- 日期：2026-10-22
- 版本：v1.0
- Google Drive 原件：[技术报告](https://docs.google.com/document/d/1fKzaKYxxic4x9G8YIqI7_6nlARjeGOVAR8FF0_KBF6s/edit)
- 关联档案：[RES-002](CGEO-MAP-RES-002.md)、[RES-003](CGEO-MAP-RES-003.md)

## 结论

本报告将已解码的原版与《战帆》Main_map数据与同版本独立格式逆向研究交叉核验。外部来源明确区分Verified、Inferred和Unknown；本报告只采用与本项目文件结构相符的交叉结论，不将外部推断自动升级为本项目直接观察。

### 1. HGHT高度编码公式

独立格式研究针对Bannerlord 1.4.8.119303 / War Sails 1.2.8.119303确认：

`Z = min_height + v × (max_height − min_height) / 65535`

其中 `v` 为16-bit无符号样本，`min_height` 和 `max_height` 取自同一版本 `scene.xscene` 的terrain属性；除数为65535而不是65536。量化误差上限为 `(max_height−min_height)/131070`。

| 版本 | min_height | max_height | 范围 | 每个码值的Z步长 |
|---|---:|---:|---:|---:|
| 原版 | -0.723 | 23.052 | 23.775 | 0.000362783 |
| 《战帆》 | -0.900 | 29.109 | 30.009 | 0.000457908 |

这些值先按游戏场景Z坐标处理；未校准场景单位与现实距离前，不直接称为米或现实海拔。

RES-003中基于Navmesh顶点的回归仍有诊断价值，但不得作为正式高度转换公式。Navmesh顶点可能有地表偏移或局部误差。正式转换应使用scene.xscene的min/max与上述编码公式。

### 2. XY映射与拼接

独立研究确认ZGR6RTRN节点序号为 `i = idy * node_dimension_x + idx`，即X变化最快；PNG行列中列对应+X、行对应+Y。单块样点位置：
`x = (idx*(R-1)+col)*node_size/(R-1)`
`y = (idy*(R-1)+row)*node_size/(R-1)`
相邻节点共享边界，16×16个257×257图块拼接为4097×4097栅格。这与本项目DLC 480/480接缝、原版477/480接缝完全匹配结果相互支持。+Y并不自动等于现实地图北方，北向仍需以确定地标校准。

### 3. PHYM结构：撤回“四通道RGBA”假说

本项目先前依据264,228字节的块长提出“32字节头+257×257四通道栅格”。该算术等式成立，但内部结构解释错误，现正式撤回。

同版本独立格式研究将每块解析为4条季节记录：
- u32 season：0夏、1秋、2冬、3春
- u32 count：R×R
- u8 layer[count]：单字节terrain layer index数组

R=257时，每条记录8+66,049=66,057字节；四季共264,228字节，恰好匹配本项目的每块长度。PHYM值是terrain layer index，不是physics-material ID；索引按X-major排列。具体物理材质须结合scene.xscene的layer配置映射，不能把数值直接命名为草地、岩石或沙地。

### 4. MIDX语义仍未知

本项目已恢复每版4张4096×4096、8-bit灰度PNG；独立研究也确认MIDX为全局四图，但其含义仍未知。其值不直接等于terrain layer index、physics-material ID或terrain_materials.xml索引。图像已解码不等于语义已确定，暂不将其命名为季节、植被、土壤或海拔图。

### 5. Flowmap官方语义及数值边界

TaleWorlds官方文档说明，War Sails Flowmap编辑器中的箭头方向代表风与水流方向，颜色代表强度；Flowmap影响水面shader与风暴移动。官方文档未公布本项目DDS浮点分量的精确重映射、坐标变换或物理单位。因此已解码的R/G值可用于原始数值分布分析，但不能直接换算为现实流速。

官方文档还区分CoastalSea、OpenSea、River、NonNavigableRiver、UnderBridge、Lake等Navmesh类型。这些是游戏导航/行为分类，不单独证明自然河网连通、流域边界或水体面积。

## 修订清单

1. RES-002的Flowmap统计保留，但补充官方语义与物理单位未知的限制。
2. RES-003的Navmesh—HGHT回归只保留为相关性诊断；正式Z转换采用terrain min/max公式。
3. RES-003的PHYM“四通道RGBA”解释撤回，改为四季terrain layer index数组。
4. MIDX继续标记为“已解码、语义未知”。
5. 禁止将原版与《战帆》资源差异直接解释为卡拉迪亚世界内部的海侵、造岛、河流改道或气候变化。

## 后续工作

1. 以两版各自的min/max生成可比色标高程图。
2. 从scene.xscene的layers、seasonal masks和材质配置建立PHYM索引对照表。
3. 追踪MIDX与terrain shader / Granite tileset的绑定关系。
4. 校准Flowmap原始浮点分量与编辑器箭头之间的转换。
5. 最后叠加高程、PHYM、Navmesh、河流几何与Flowmap，分别保留自然地理层和游戏机制层。

## 来源

- 独立terrain.bin格式逆向（目标版本与本项目一致）：[格式说明](https://github.com/davgor/MNBL-modding-repo/blob/23ba089566884dabe61164f47ae3d9e4f145da86/docs/formats/terrain-bin.md) · [参考实现](https://github.com/davgor/MNBL-modding-repo/blob/23ba089566884dabe61164f47ae3d9e8f4e145da86/tools/scenebin/terrain_bin.py)
- TaleWorlds官方：[War Sails World Map](https://moddocs.bannerlord.com/war-sails/wsworldmap/)
