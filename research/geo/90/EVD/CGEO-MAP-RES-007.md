# CGEO-MAP-RES-007｜《战帆》港口与登陆点的世界坐标及水域导航归属
日期：2026-10-22；研究系列：CGEO 地理研究／地图数据与导航拓扑；版本：v1.0
关联：CGEO-MAP-RES-001—006

## 一、研究材料与目的
本轮对既有原始文件直接执行只读解码，而非仅转述已有报告。War Sails scene.xscene SHA-256：1fb8bb08210a377fb727dc9e69454f0368254f28f317cb81c5db2569e3862ebc；navmesh.bin SHA-256：f8b4b846eb930fbfb64da64bf9c9c191a5aee2f825bfce7d1a59deaa21b0175f。解析scene.xscene内的town_port、drop_point及其父级聚落实体的transform，转换成世界XYZ，并用已解压的NMG9网格查验落点的导航面类型与共享边连通分量。对原版scene.xscene额外检索相同名字的实体。

## 二、实体记录数与版本关系
原版scene.xscene中town_port=0、drop_point=0。
《战帆》：城镇town_port共29条记录，对应29个不同聚落；村庄drop_point共144条记录，对应72个不同村庄。村庄通常有civilian/looted两个场景状态版本，不能把144条记录算作144座村庄。港口/登陆标记涉及101个不同聚落，但不应据此推断游戏世界内部实际只有101个沿海定居点。
《战帆》部分村庄两场景状态位置存在差异；castle_village_EW7_2的两条世界XY记录彼此相距约0.637场景单位，故仍保留逐条记录。

## 三、坐标变换方法与核验
港口与登陆点在scene.xscene中是聚落实体的子项，child transform记录的是局部坐标，不能直接作为世界XY。按父子齐次TRS变换复合平移、旋转与缩放；Euler旋转暂按弧度、Rz×Ry×Rx顺序。父级不一定水平：存在非零俯仰/侧倾，若仅用平面Z轴旋转，173个点中有46个XY位置偏差超过0.1场景单位，最大偏差约0.986单位。本轮采用完整3D变换。
在此变换候选下，173个点的世界XY全部位于导航网格CoastalSea(18)或River(11)多边形内。把Euler值误读为度数时，候选水上导航网格的平均最近距离约为2.507场景单位；以弧度变换时为0。此几何一致性强力支持采用的变换解释，但并非对引擎全部旋转约定的独立反汇编证明。

## 四、港口与登陆点的导航类型归属
29个城镇港口：23个位于CoastalSea(18)；6个位于River(11)；没有港口点直接落于OpenSea(19)或UnderBridge(25)。
144条村庄登陆点记录：82条位于CoastalSea(18)；62条位于River(11)。
按照CGEO-MAP-RES-006中River(11)、CoastalSea(18)、OpenSea(19)、UnderBridge(25)的共享网格边图，173条记录全部归属最大组件1（3512个面）。没有一条标记落于东南组件2（309个面）或孤立组件3（1个面）。这是几何覆盖/边连通的证据，而非游戏运行时船只可以实际到达的测试。
在聚落去重尺度下：29个港口城镇中23个贴CoastalSea、6个贴River；72个村庄中41个贴CoastalSea、31个贴River。港口和村庄标记均属于最大候选水上导航网络。

## 五、来源与推论限制
直接文件观察：XML实体、tags、levels、父子层级、29/144条记录、原版同名实体不存在；NMG9导航面分类及共享边关系。
经空间交叉验证的解释：Euler弧度与3D父子TRS形成的世界坐标；与173/173标记点落入海域/河流导航面吻合。
不得作出的历史推论：原版没有这些专用实体，不证明原版世界没有港口；独立河流导航网络不等于独立天然流域；Navmesh面归属不证明真实水流方向、自然河岸线、历史航路或游戏内实际通航行为。
内部聚落ID尚未与官方settlements.xml地名表完成校对，故不擅自将town_V5等翻译成定名地点。

## 六、交付文件及复核
本地生成：warsails_ports_dropoff_world_navmesh.csv（173条标记点，世界XYZ与导航归属）、warsails_port_dropoff_unique_settlements.csv（101个去重聚落）、warsails_ports_dropoff_naval_components.png、results_summary.json、cgeo_map_007_analyze.py，连同CGEO-006只读Navmesh解析器打包为CGEO-MAP-RES-007_analysis_bundle.zip，共7个文件且ZIP CRC校验通过。
该研究仅解析当前项目中已上传的文件，不修改用户安装目录中的资源，不启动游戏。GitHub仅发布研究文本或派生统计，不上传游戏原始二进制。

## 七、下一步
（1）联通官方settlements.xml和官方中英地名索引，逐项核实29个港口与72个登陆村庄的名称及其世界坐标；
（2）检查独立东南河流组件为什么无本轮港口/登陆点标记，不能擅自断言其不可航；
（3）继续恢复river_triangles.bin索引的源三角网格，采用独立高程与Flowmap资料分析真实河流水面。

参考：TaleWorlds War Sails World Map：https://moddocs.bannerlord.com/war-sails/wsworldmap/
GitHub研究档案：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/90/EVD/CGEO-MAP-RES-007.md
