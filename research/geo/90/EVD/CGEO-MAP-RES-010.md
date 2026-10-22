# CGEO-MAP-RES-010｜《战帆》港口与登陆点聚落 ID 及官方地名核对
技术报告 v1.0｜2026-10-22  
关联档案：CGEO-MAP-RES-007、008、009  
数据来源：用户已归档的 NavalDLC.zip、SandBox.zip、cgeo_map_007 / cgeo_map_008 派生数据。
## 一、研究目的
将场景资源中识别的 29 个 `town_port` 与 72 个不同的 `drop_point` 所属聚落 ID，和官方 `NavalDLC/ModuleData/settlements.xml`、DLC 官方简体中文名称表进行直接匹配。目标是把上一轮依赖旧版名称索引或社区交叉表的地名结论，区分为当前官方文件已确认、旧索引参考、当前文件未提供译名三种状态。
## 二、方法
1. 读取 `Modules/NavalDLC/ModuleData/settlements.xml`，逐项解析 `Settlement id`、`name` 的英文回退名称、名称 localization key、culture、owner 与原始 posX/posY。
2. 读取 `Modules/NavalDLC/ModuleData/Languages/CNs/std_settlements_xml-zho-CN.xml`，按 `Settlements.Settlement.name.<settlement_id>` 直接键匹配官方简体中文名称；同时对照英文语言表确认英文名。
3. 将官方聚落条目与 RES-007 的 101 个去重标记聚落和 RES-008 的 29 条港口名录连接。旧版中文名称仅单列为此前研究参考，不冒充当前 DLC 官方译名。
4. 原始 ZIP 未修改。坐标来自既有场景层级变换结果；聚落 XML 的 posX/posY 是聚落场景位置，不与港口实体的 world_x/world_y 混为一列。
## 三、总体匹配结果
- 场景标记关联的去重聚落：101 个，其中 29 个城镇港口、72 个村庄登陆点。
- 101/101 个聚落 ID 均在当前 NavalDLC settlements.xml 找到对应的官方 Settlement 条目。
- 101 个目标 ID 中，有 22 个名称在当前 DLC 官方简体中文表里存在直接匹配：4 个港口城镇和 18 个村庄/城堡村庄，全部属于新增 Nord 名称组。
- 其余 79 个目标 ID，在当前 NavalDLC 官方简体中文名称表中未找到对应的名称 key。对此报告保留官方 XML 中的英文回退名；对 25 个非 Nord 港口，另列 RES-008 使用的旧版中文名称索引作为参考，不据此声称其为当前 DLC 文件中直接确认的译名。
- 当前 DLC 官方中文表已直接确认新增 Nord 四城：Hvalvik＝瓦尔维克；Gretysfjord＝格雷蒂斯湾；Thronderlag＝特龙德拉格；Hargard＝哈加德。前 3 个城镇港口位于 CoastalSea 导航面，Hargard 港口位于 River 导航面。
## 四、29 个港口城镇名录
| Settlement ID | 当前官方英文名 | 当前 NavalDLC 官方简体中文名 | 导航类型 | 中文名证据状态 |
|---|---|---|---|---|
| town_A1 | Quyaz | — | CoastalSea | 旧版索引：古亚兹 |
| town_A4 | Razih | — | CoastalSea | 旧版索引：拉齐赫 |
| town_A6 | Sanala | — | CoastalSea | 旧版索引：撒纳拉 |
| town_A7 | Askar | — | River | 旧版索引：阿斯凯尔 |
| town_A8 | Qasira | — | CoastalSea | 旧版索引：加西拉 |
| town_B3 | Car Banseth | — | CoastalSea | 旧版索引：卡·班塞斯 |
| town_EN2 | Diathma | — | CoastalSea | 旧版索引：狄亚特马 |
| town_EN4 | Argoron | — | CoastalSea | 旧版索引：阿耳戈隆 |
| town_ES1 | Danustica | — | CoastalSea | 旧版索引：达努斯提卡 |
| town_ES2 | Vostrum | — | CoastalSea | 旧版索引：沃斯特鲁姆 |
| town_ES3 | Poros | — | River | 旧版索引：波罗斯 |
| town_ES7 | Syronea | — | CoastalSea | 旧版索引：席隆尼亚 |
| town_EW1 | Lageta | — | River | 旧版索引：拉革塔 |
| town_EW2 | Zeonica | — | CoastalSea | 旧版索引：泽翁尼卡 |
| town_EW4 | Ortysia | — | CoastalSea | 旧版索引：俄耳堤西亚 |
| town_EW6 | Rhotae | — | River | 旧版索引：洛泰 |
| town_K3 | Makeb | — | CoastalSea | 旧版索引：马凯布 |
| town_K5 | Chaikand | — | CoastalSea | 旧版索引：柴坎 |
| town_N1 | Hvalvik | 瓦尔维克 | CoastalSea | 当前 DLC 官方中文 key 匹配 |
| town_N2 | Gretysfjord | 格雷蒂斯湾 | CoastalSea | 当前 DLC 官方中文 key 匹配 |
| town_N3 | Thronderlag | 特龙德拉格 | CoastalSea | 当前 DLC 官方中文 key 匹配 |
| town_N4 | Hargard | 哈加德 | River | 当前 DLC 官方中文 key 匹配 |
| town_S2 | Balgard | — | CoastalSea | 旧版索引：巴尔加德 |
| town_S3 | Omor | — | CoastalSea | 旧版索引：奥莫尔 |
| town_S4 | Varnovapol | — | CoastalSea | 旧版索引：瓦尔诺瓦波尔 |
| town_V3 | Pravend | — | River | 旧版索引：帕拉汶德 |
| town_V5 | Galend | — | CoastalSea | 旧版索引：加伦 |
| town_V7 | Charas | — | CoastalSea | 旧版索引：沙拉斯；当前 DLC 中文 key 未匹配 |
| town_V8 | Ostican | — | CoastalSea | 旧版索引：奥斯蒂港 |
“—”表示当前 NavalDLC 的官方简体中文名称表中没有该目标 ID 的直接名称 key，并不等于游戏运行时一定显示英文，也不代表该名称不存在其他本地化来源。
## 五、18 个由当前 DLC 官方中文名称表直接确认的登陆点聚落
| Settlement ID | 英文名 | 当前官方简体中文名 |
|---|---|---|
| castle_village_N1_1 | Laxahof | 拉萨霍夫 |
| castle_village_N1_2 | Agilting | 阿格尔特 |
| castle_village_N2_2 | Tharklif | 塔克利夫 |
| castle_village_N5_1 | Fimbulgard | 菲姆比加德 |
| castle_village_N6_1 | Haugr | 豪格 |
| castle_village_N6_2 | Nifdal | 尼芙达尔 |
| castle_village_N7_1 | Hakarshus | 哈卡许斯 |
| castle_village_N8_1 | Skarthness | 斯卡特奈斯 |
| castle_village_N9_1 | Ulikshorn | 于利克舍恩 |
| castle_village_N9_2 | Thralathorp | 特拉阿托普 |
| village_N1_1 | Aalgrun | 阿尔格伦 |
| village_N1_2 | Lagshofn | 拉葛斯霍芬 |
| village_N1_4 | Gripsby | 格里普斯比 |
| village_N2_2 | Midskag | 米德斯卡格 |
| village_N2_3 | Dorstrand | 多斯特兰 |
| village_N3_3 | Holarsver | 霍拉斯韦尔 |
| village_N4_3 | Faergap | 法尔加普 |
| village_N4_4 | Gauksdal | 盖于斯达尔 |
这 18 个名称直接来自当前 NavalDLC 官方简体中文表。其余 54 个登陆点聚落的 ID 与英文名仍已成功匹配，但本次所读 DLC 中文表未提供相应名称 key；没有用猜测译名填空。
## 六、证据分级与限制
- **A级｜官方文件直接确认：** 101 个 ID 对应的 Settlement 记录、英文回退名、culture/owner、聚落 XML 坐标；22 个官方简体中文名称 key。
- **B级｜已有派生数据：** 港口实体世界坐标、所属导航面类型、到水陆导航共享边的距离。它们来自 RES-007/008 的场景/网格分析，不是自然海岸线测量。
- **C级｜旧版名称参考：** 25 个既有港口的中文名来自 RES-008 引用的旧版 Bannerlord 1.3.15 名称索引；与当前 DLC 官方中文 key 分栏保存。
- **未确认：** 当前 DLC 名称表未直接匹配的 79 个目标 ID 在其他运行时本地化覆盖层中是否存在别的中文名称；以及未出现港口/登陆标记的聚落是否具有其他航海机制。
不得把当前中文名称表的缺项解释为地名未翻译、游戏显示英文或聚落没有航海活动。不得把版本资源差异解释成世界内部地理变化。
## 七、来源与复核路径
- 原始 DLC ZIP：Google Drive https://drive.google.com/file/d/1K1rOhnZ8gV_jH2IP0LvaxXYlmpdgPjTI/view
- 原始 SandBox ZIP：https://drive.google.com/file/d/1UoUoe0FMn4Di3eoN0NMexcgzCZOE8CJb/view
- 上游 RES-007：Google Drive https://docs.google.com/document/d/1rHualy_SArSYNJog4KPxt7qqL_-LtCgzD2GI0WDZNcE/edit
- 上游 RES-008：Google Drive https://docs.google.com/document/d/1v52GmJ6BmyRUwUJjpLG3PalEKC9aBLaKYTqUHn3ZopI/edit
- 上游 RES-009：Google Drive https://docs.google.com/document/d/1o3j6Upzmh7KbbxggqJHKj_mH310tDaKhvCe5pqCSaos/edit
- 官方 War Sails 世界地图文档：https://moddocs.bannerlord.com/war-sails/wsworldmap/
派生 CSV：CGEO-MAP-RES-010_settlement_name_mapping.csv（101 行，含 ID、英文名、中文译名状态、文化、聚落坐标及对应点位信息）；CGEO-MAP-RES-010_port_town_name_mapping.csv（29 条港口城镇）。

Google Drive原件：https://docs.google.com/document/d/1JmXqLuMxxWbxvd7HMZ49RExaLj9ff5Mf74MLWulFAm8/edit
