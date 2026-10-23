# CGEO-MAP-RES-014｜聚落中文地名规范表

版本：v1.0｜2026-10-23

## 判定规则

1. `settlements.xml` 中的英文名称和实体 ID 是地理对象主键。
2. 当前随档官方简体中文文件 `SandBox/ModuleData/Languages/CNs/std_settlements_xml-zho-CN.xml` 主要包含聚落地理/百科描述；对 53 个城镇的 `Settlements.Settlement.name.*` 独立名称键未检出可匹配的中文译名。
3. 若地图采用的中文形式在该官方中文地理文本中有完全一致的字串，则记为“官中地理文本中检出同一中文形式”；这只是译名见证，不等同于证明它是独立官方名称键。
4. 未检出的标注加 †，作为研究暂译保留，不能称为已核实官方译名。表格保留具体文本片段供人工复核。

## 本版地图标注

| 英文原名 | 地图中文标注 | 状态 |
|---|---|---|
| Epicrotea | 埃皮克罗提亚† | 研究暂译，待核 |
| Diathma | 狄亚特马 | 官中地理文本有同形用例 |
| Argoron | 阿尔戈隆† | 研究暂译，待核 |
| Lageta | 拉盖塔† | 研究暂译，待核 |
| Zeonica | 泽翁尼卡 | 官中地理文本有同形用例 |
| Ortysia | 俄耳堤西亚 | 官中地理文本有同形用例 |
| Danustica | 达努斯提卡 | 官中地理文本有同形用例 |
| Vostrum | 沃斯特鲁姆 | 官中地理文本有同形用例 |
| Poros | 波罗斯† | 研究暂译，待核 |
| Varcheg | 瓦尔切格 | 官中地理文本有同形用例 |
| Omor | 奥莫尔 | 官中地理文本有同形用例 |
| Tyal | 蒂亚尔 | 官中地理文本有同形用例 |
| Sibir | 西比尔 | 官中地理文本有同形用例 |
| Quyaz | 古亚兹 | 官中地理文本有同形用例 |
| Sanala | 萨纳拉† | 研究暂译，待核 |
| Askar | 阿斯卡尔† | 研究暂译，待核 |
| Sargot | 萨哥特† | 研究暂译，待核 |
| Pravend | 帕拉汶德 | 官中地理文本有同形用例 |
| Ostican | 奥斯蒂坎† | 研究暂译，待核 |
| Marunath | 马鲁纳斯† | 研究暂译，待核 |
| Car Banseth | 卡·班塞斯 | 官中地理文本有同形用例 |
| Seonon | 塞奥农† | 研究暂译，待核 |
| Baltakhand | 巴尔塔坎德† | 研究暂译，待核 |
| Makeb | 马凯布 | 官中地理文本有同形用例 |
| Chaikand | 柴坎 | 官中地理文本有同形用例 |

## 解释与限制

本版不再把先前的所有音译统称为“官方译名”。官方文本中能找到的同形译名予以保留；未能在现有官方 CN 文本中核实的地名加 †。由于本次资料包没有可逐项映射的独立城镇名称中文键，† 只能通过补充取得当前版本完整地名语言表或由官方游戏界面逐项核验后移除。

官方文本证据文件：`cgeo_work/SandBox.zip` 内 `Modules/SandBox/ModuleData/Languages/CNs/std_settlements_xml-zho-CN.xml`；地理对象与英文原名来自同包 `Modules/SandBox/ModuleData/settlements.xml`。