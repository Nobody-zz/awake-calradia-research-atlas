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


## 八、原始场景 XML 层级独立复核与父级去重（2026-10-23）

此次再从原始 `NavalDLC/SceneObj/Main_map/scene.xscene` 逐个读取 **173个实例**（29个 `town_port`、144个 `drop_point`），不只是从 RES-008 的坐标派生表筛选。

- 29个 `town_port` 对应29个不同父级；144个 `drop_point` 对应**72个村庄父级**，每个父级恰有一个 `civilian` 和一个 `looted` 状态标记。两个状态具有相同 `main_map_village_dropoff` 标签、`level_1/2/3` 层级标记。59个父级先列civilian，另13个先列looted，因此不能以XML出现顺序识别状态。
- 72对状态标记中，**28对三维坐标在1e-8容差内完全一致**；72/72对在 RES-008 候选坐标模型下落于相同Navmesh面、具有相同导航类型与主候选航路组件。XY相距中位数0.0038396、均值0.0204078、90百分位0.0248790、最大0.6371200场景单位，最大差位于 `castle_village_EW7_2`。
- 34个 `drop_point` 实例（17个村庄父级各2个状态）的**标记自身**transform包含 `non_orthogonal_rotation_mat`；向上追溯的父级变换链未发现此字段。标记自身旋转不改变标记原点坐标，但可能影响登船/登陆的方向与局部坐标轴，不能用单纯Euler字段解释其朝向。
- 按父级合并后共有**101组场景水路接入锚点**（29个城镇父级+72个村庄父级），而不是173个独立地点。基于RES-008候选radians/Euler xyz坐标模型，101组均处于水上主候选连通组件：64组在CoastalSea(18)，37组在River(11)。这不等于独立核验了101个官方settlements.xml聚落记录。此项对应关系另见[CGEO-MAP-RES-011](CGEO-MAP-RES-011.md)的双源联结审计。

### 证据等级与新交付物

直接XML文件证据：173个实例数量、72个 `civilian/looted` 配对与层级标签、29+72父级去重、17个含非正交矩阵的村庄父级。

条件性几何判断：坐标微小位移、Navmesh相同面/类型、水域组件归属；仍依赖RES-008的弧度Euler xyz**候选**父级变换，尚不能称为完全经引擎验证的世界坐标。

- [Google Drive 正式报告](https://docs.google.com/document/d/1o3j6Upzmh7KbbxggqJHKj_mH310tDaKhvCe5pqCSaos/edit)
- [72组村庄双状态坐标与面分类CSV](https://drive.google.com/file/d/1rxdH4pfEuhU9UagAu3U1TPT3Ue0jB_-h/view)
- [101组去重的父级水路接入锚点CSV](https://drive.google.com/file/d/1hLTPLE5cZwGG1jDWmawtKWlAHKU1nNYV/view)
- [101组锚点地图](https://drive.google.com/file/d/1DCzFcxsfM8vvPlusvKvgSF9mv_bp1CNi/view)
- [双状态间距分布图](https://drive.google.com/file/d/13OvKbnqmG-5qRu_Jt1TB0TrJIbZG7Bpj/view)
- [审计JSON](https://drive.google.com/file/d/1Q4fTnxH_xdZJj7R4o9BzJRLevqLIsUTd/view)

复核脚本 `village_state_pair_audit.py` 及数据、地图收录于本地10文件分析包 `CGEO-MAP-RES-009_village_state_pair_bundle.zip`（CRC验证通过，不含原始游戏二进制）。
