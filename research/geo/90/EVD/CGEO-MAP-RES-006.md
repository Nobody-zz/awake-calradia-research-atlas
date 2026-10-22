# CGEO-MAP-RES-006｜原版与《战帆》水域导航网格类型及连通性审计

技术报告 v1.0｜2026-10-22
关联：CGEO-MAP-RES-001至005；原版及NavalDLC Main_map原始navmesh.bin


## 一、研究方法
重新读取原版与《战帆》navmesh.bin，解压RNM1外层LZ4数据，按NMG9结构逐面读取顶点引用、边引用和五项meta元数据。面类型取meta[2]，按公共边索引建立无向面邻接图；计算同类型连通区域、不同类型之间的共同边数与XY长度、网格面XY投影面积。《战帆》候选水上网络仅暂选River(11)、CoastalSea(18)、OpenSea(19)、UnderBridge(25)，排除NonNavigableRiver(22)。本分析是直接二进制几何/图论统计，不是游戏内实际航行测试，也不是天然水系连通证据。地形类型名称与数值采用同版本独立Navmesh逆向资料交叉核验；可航类型的玩法说明依据TaleWorlds官方War Sails地图文档。


## 二、两版水域类型与面数
原版Navmesh：Lake(8)180面、Water(10)898面、River(11)1376面，原版Water/Lake等类型不可直接与DLC的CoastalSea/OpenSea作为相同水文分类比较。
《战帆》Navmesh：River(11)898面、CoastalSea(18)1969面、OpenSea(19)880面、NonNavigableRiver(22)322面、UnderBridge(25)75面。
《战帆》同类型面经共享边连通的区域数量：River 29块、CoastalSea 3块、OpenSea 5块、NonNavigableRiver 17块、UnderBridge 22块。注意同一种类型的多个区域可能通过另一种类型的面间接连接，不能简单相加。


## 三、不同水域面类型的几何邻接
两面共享同一navmesh边索引时才视为相邻；仅共用一个顶点不算边连通。依此直接读得：
CoastalSea 18 ↔ OpenSea 19：570条公共边，XY总长5297.03场景单位；
River 11 ↔ CoastalSea 18：6条公共边，XY总长49.57；
River 11 ↔ UnderBridge 25：44条公共边，XY总长171.57；
River 11 ↔ NonNavigableRiver 22：3条公共边，XY总长10.23；
CoastalSea 18 ↔ NonNavigableRiver 22：1条公共边，XY总长4.26。
这仅是导航网格拓扑，而不是两类自然水体的真实相交长度。


## 四、候选水上导航网络的三个连通区域
取Navmesh面类型11/18/19/25作为候选集合，对共享同一边的面构建无向图并求连通分量，共3822个候选导航面，分为三个区域。
主水域（组件1）：3512个面，包括River 594、CoastalSea 1969、OpenSea 880、UnderBridge 69。面重心覆盖场景XY范围约X90.98—939.03、Y67.50—915.33；面积投影和约257207.34场景单位平方。
东南河流组（组件2）：309个面，包括River 303、UnderBridge 6。面重心范围约X822.73—938.61、Y141.45—435.06；面积投影和约2796.80场景单位平方。它在此面邻接定义下没有连接主水域。
孤立单面（组件3）：1张River面，面心约(678.36,315.995)，XY投影面积2.375场景单位平方。
主水域约占候选面数的91.89%。此结果是Navmesh共享边网络的离线图结构；并不能排除引擎存在特殊转场、桥区移动条件、运行时寻路限制或其他动态行为。也不能将“东南河流组”的独立性直接写成封闭天然流域。


## 五、原版与《战帆》的解释边界
原版与DLC场景网格大小、导航类型、面大小和可通行定义均不同。不能依据面数量、类型缺失、区域数量或XY投影面积差值，断言游戏世界内部发生海侵、造岛、河流自然改道或水域消失。Navmesh边界不是海岸线，UnderBridge是航行行为控制类别。自然地理研究仍须另行叠合已解码的HGHT高程、PHYM terrain layer、河流水面几何与Flowmap，但它们本身不能自动证明水动力学方向。


## 六、可复核交付与图件
本轮本地分析脚本：cgeo_map_006/navmesh_water_audit.py；输出navmesh_terrain_type_stats.csv、navmesh_group_adjacency.csv、navmesh_connected_components.csv、warsails_navigable_components.csv、warsails_waterland_boundary_edges.csv以及四幅地理图。ZIP成果包：CGEO-MAP-RES-006_analysis_bundle.zip（12个文件，已完成CRC校验）。
《战帆》水域类型图：https://drive.google.com/file/d/1dpw5TdI7BX5Z4kA989_pqKbDvUEah_Cf/view
《战帆》候选连通网络：https://drive.google.com/file/d/1UIlPp1cnLeOneyQwFeLBzh9P3jFo2EWv/view
《战帆》类型邻接矩阵：https://drive.google.com/file/d/1DA3yH2ijnrnbsPWp4b1HpYXtZWG8lyci/view
原版水域类型图：https://drive.google.com/file/d/1vmEQChpeHq2cHxvgatuClTgn3qoHvDTN/view


## 七、史料与下一步
TaleWorlds官方指南：https://moddocs.bannerlord.com/war-sails/wsworldmap/
类型编号交叉核验：https://github.com/davgor/MNBL-modding-repo/blob/23ba089566884dabe61164f47ae3d9e4f145da86/docs/formats/navmesh-bin.md
研究继续方向：恢复《战帆》场景中town_port、drop_point的父级变换，获得实际世界XY，检查其所在/邻近的Navmesh类型及所属水域连通区域；定位river_triangles.bin引用的源网格。港口和村庄的局部坐标不能不经父级转换就直接放到世界地图上。


Google Drive原件：https://docs.google.com/document/d/1LKqRVItDPxfNsasdYQ3MldJkwSASXj5GT5QOCEaz-KE/edit

注：GitHub仅存储研究文本与派生指标，不上传游戏原始二进制资源。
