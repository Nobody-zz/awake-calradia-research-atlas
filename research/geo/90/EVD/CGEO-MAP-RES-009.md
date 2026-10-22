# CGEO-MAP-RES-009｜《战帆》村庄登陆点 civilian/looted 变体的空间稳定性审计

技术报告 v1.0｜2026-10-22
关联档案：CGEO-MAP-RES-006、007、008。


## 一、研究问题
RES-007将144条村庄drop_point实体转换为世界坐标，识别出72个不同村庄，每个村庄各有level_1|level_2|level_3|civilian与level_1|level_2|level_3|looted两条状态变体。RES-008测量这些点到水上导航面与陆地导航面之间最近共享边的距离。本报告检验两种状态的登陆点在几何上是否稳定，以及状态切换是否改变所对应的导航面、导航类型或候选连通组件。


## 二、方法与证据范围
从RES-008派生表warsails_ports_dropoff_shore_distance.csv中提取144条drop_point记录，按settlement字段匹配72对civilian/looted记录。对每对计算世界XY欧氏位移、导航面ID/类型是否变化、候选连通组件是否变化，以及到最近可航水域—陆地导航边界的距离差。坐标单位为游戏场景XY单位，未换算为米。
本检验以已解码的scene.xscene层级变换与Navmesh分类为基础；未启动游戏，也未直接测量实际登岸动画、船只控制或运行时寻路。civilian与looted只是场景资源状态标签，不应理解为两种自然地理环境。


## 三、主要结果
- 配对样本：72个村庄、144条登陆点记录。
- 50/72对（69.44%）世界XY位移不超过0.01场景单位。
- 69/72对（95.83%）位移不超过0.1；71/72对（98.61%）不超过0.5；72/72对均不超过1场景单位。
- 位移中位数0.00384场景单位，平均值0.02041，P90为0.02488，P95为0.05756，最大值0.63712。
- 72对中，导航类型变化0对、最近导航面ID变化0对、候选连通组件变化0对。
- 到水陆导航边界距离差绝对值中位数0.00172场景单位，最大0.10204。

因此，这72对点位在当前场景坐标与Navmesh分类下高度稳定。最大偏移来自castle_village_EW7_2，约0.637场景单位；但该对仍位于同一导航面、同一类型和同一候选连通组件，最近水陆边界距离变化仅约0.00183。应将其记录为资源级局部偏移，而非直接认定为导航异常。


## 四、解释与边界
1. 数据支持“civilian/looted状态变体通常复用同一登陆点空间位置”；更精确地说，绝大多数坐标完全相同或只有极小偏移。
2. 所有配对的最近导航面ID与导航类型均相同，说明状态标签没有在本次提取中导致登陆点切换到另一个导航面或水上网络组件。
3. 这不能证明两种游戏状态下船只的实际可用性、交互脚本或AI寻路行为完全一致；需要运行时或脚本层验证。
4. 距离使用导航网格水陆共享边作为代理，不是渲染水岸或自然岸线；场景单位也未校准到现实长度。
5. 这不是地理环境变化证据，而是同一DLC地图内不同场景状态资源的几何比较。


## 五、派生数据
配对逐村数据CSV：CGEO-MAP-RES-009_drop_point_variant_audit.csv
位移直方图和水陆边界距离对照图保存在分析成果目录。
GitHub报告：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/90/EVD/CGEO-MAP-RES-009.md
GitHub配套CSV：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/90/EVD/CGEO-MAP-RES-009_drop_point_variant_audit.csv


## 六、下一步
优先核对NavalDLC当前版本的settlements.xml与简体中文语言表，确认RES-008中四个新增Nord城镇的当前官方中文译名，并将29个显式港口标记关联到完整聚落条目。之后统计全部城镇、城堡、村庄中哪些有港口或登陆点标记；未出现标记只能表述为“本场景未找到对应显式实体”，不能推出聚落没有航海活动。


## 七、来源与复核
- 派生表warsails_ports_dropoff_shore_distance.csv（173条港口/登陆点记录，包含世界坐标、导航类型、最近水陆边界距离和settlement ID）。
- 上游档案CGEO-MAP-RES-007（坐标变换与Navmesh匹配）、CGEO-MAP-RES-008（港口地名与水陆边界距离审计）。
- TaleWorlds官方War Sails World Map文档：https://moddocs.bannerlord.com/war-sails/wsworldmap/
