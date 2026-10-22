# CGEO-MAP-RES-011｜《战帆》聚落坐标与水路接入锚点的双源配准审计

技术报告 v1.0｜2026-10-23｜研究档案CGEO

## 摘要

首次把RES-010中来自官方NavalDLC settlements.xml的101条聚落坐标，与RES-009从scene.xscene派生的101处去重水路锚点，按聚落ID严格一对一联结。29个town_port、72组村庄drop_point全部匹配成功，聚落位置与对应锚点的世界XY在所有101处均存在正的坐标偏移。

这一偏移是聚落XML坐标与游戏场景中港口/登陆点标记位置之间的平面直线距离，不是现实公里、离海距离、沿路距离，也不是对聚落位置错误的判定。

## 一、样本与计算方法

来源A：用户研究资料库的CGEO-MAP-RES-010_settlement_name_mapping.csv（101条）；SHA-256=c778566ab7c01a2df754582a5884234511592a646b316c1e0bdbc59d860ed0ab。它记录官方DLC settlement ID、英文回退名称、官方名称本地化状态、XML坐标与此前已校准的港口/村庄标记XY。

来源B：RES-009直接由scene.xscene的29个town_port和72组civilian/looted村庄drop_point去重形成的distinct_water_access_sites.csv（101条）；SHA-256=e921b2ea777b0e16e087168fdc2bf33ccd148984c8cfd2f4f31fc3593021b0be。

本轮以来源A的settlement_id与来源B的site_name做one-to-one连接，结果101/101条完整匹配。两份派生表所给水路锚点XY相差均小于0.000001场景单位；属于派生数据间的一致性验证，不等于引擎旋转矩阵约定的独立确认。

定义ΔX=港口/登陆点worldX−聚落XML posX；ΔY=worldY−XML posY；D=sqrt(ΔX²+ΔY²)。72个村庄采用civilian与looted两标记中点作为一处父级锚点的统计代表；研究特定游戏状态时不能以中点替代实际生效标记。

## 二、101处距离统计

全部101处：D最小2.1066、中位数4.6726、平均5.0208、90百分位7.0948、最大13.0966场景单位；36处超过5单位，4处超过10单位。

29个town_port：D最小3.0351、中位数4.8982、平均5.0606、90百分位6.4546、最大6.9575；没有一处超过10单位。

72组drop_point：D最小2.1066、中位数4.3296、平均5.0048、90百分位7.7071、最大13.0966；4处超过10单位。两组的中位数相近，村庄组却有更长的高值尾部。样本为固定世界地图中有显式水路标记的目的性选取，不宜从中推断所有卡拉迪亚聚落的统计分布。

## 三、四处长偏移的精确聚落ID

castle_village_S8_2，英文回退名Glavstrom：D=13.0966，ΔX=+4.2771，ΔY=+12.3785；marker在CoastalSea(18)面。

village_EN2_1，英文回退名Alosea：D=12.1077，ΔX=+5.4290，ΔY=+10.8223；marker在CoastalSea(18)面。

village_EN1_3，英文回退名Gymos：D=12.0943，ΔX=+1.7070，ΔY=+11.9732；marker在CoastalSea(18)面。

castle_village_ES4_1，英文回退名Lavenia：D=11.3246，ΔX=+6.3320，ΔY=−9.3890；marker在CoastalSea(18)面。

四处均为村庄登陆点。英文名来自官方XML的英文回退字段；未把来源未确认的中文译名冒充官方名称。D值较大只说明水路锚点与聚落位置分离明显，不证明标记错误放置、港口道路中断或自然地理异常。

## 四、研究边界与历史地理解释

官方聚落位置反映聚落资源锚点，town_port/drop_point的功能是连接水上导航网格。两者用途不同；直接用settlements.xml坐标表示港口位置会造成系统性偏移。这里的straight-line D不是沿地表可通行路径，地图场景单位也尚未转换成世界书中的现实地理尺度。

聚落culture_id是游戏资源归属，不可据此直接推论地理区域的历史族群或生态。港口与登岸点的Navmesh分类、路径连通性亦不等于天然水系与实际运行时船只航行验证。本轮未修改游戏文件，所有图像和CSV是原始文件与已有已验证派生表的研究性衍生输出。

世界坐标沿用RES-008的radians/Euler xyz候选矩阵。该模型与173/173可航标记一致，但尚未由底层引擎的变换约定独立证明；因此所有空间距离仍带有明确的条件性。

## 五、下一阶段

必须从官方NavalDLC settlements.xml生成全体聚落（包括没有显式水路标记者）的类型和ID清单；才能回答哪些聚落拥有可航接入标记、哪些在本次scene.xscene中没有。不能以101当作地图全部聚落数。

对四处长偏移村庄，分别核验scene.xscene祖先变换、陆地导航面边界、实际海岸线以及道路/登陆机制。再用引擎真实可达路径长度对比直线D；不以直线偏移推断道路交通条件。

## 六、交付物与图件

Google Drive：聚落→水路锚点空间矢量图 https://drive.google.com/file/d/1C8upn3Yw3x3V09toLov9geBvBSp7Crpk/view

Google Drive：29城镇港口对72村庄登陆点偏移分布 https://drive.google.com/file/d/1Vl6g1rbmS6mUYs-ZsCoqGk1kuOI4Eu1-/view

完整101项派生表：CGEO-MAP-RES-011_settlement_to_access_offsets.csv；汇总JSON：CGEO-MAP-RES-011_offset_summary.json；离线复算脚本：settlement_access_offset_analysis.py；ZIP分析包不包含原始游戏二进制。

上游官方聚落ID核对档案：https://docs.google.com/document/d/1JmXqLuMxxWbxvd7HMZ49RExaLj9ff5Mf74MLWulFAm8/edit；原版/战帆研究仓库：https://github.com/Nobody-zz/awake-calradia-research-atlas

Google Drive原件：https://docs.google.com/document/d/1dB3p_ie6D_LW97Hs0cpt7oziMVgCSiSpfS1kCNCTHSc/edit

本报告仅提交派生证据和统计，不分发游戏原始资产。
