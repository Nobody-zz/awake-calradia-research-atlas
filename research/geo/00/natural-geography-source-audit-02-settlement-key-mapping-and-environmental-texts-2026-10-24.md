# 自然地理源级复核备忘录 02｜聚落实体与文本键映射、气候植被同键异文审计

日期：2026-10-24  
Google Docs 原件：[自然地理源级复核备忘录02](https://docs.google.com/document/d/12tBeuWmMPpEmnM3rYZCBDj4g638RxY-4AKM0jq_jNas/edit)  
版本：v0.1  
性质：源级校勘与跨专题一致性审计，不是正式论文，不分配CGEO永久论文编号。

## 一、问题与底本

第一轮复核发现：只比较 `std_settlements_xml` 的共同字符串ID，会把“语言表中的文本改写”“文本键改派给另一个聚落实体”“聚落实体ID改派给另一个名称”混在一起。第二轮因此同时读取：

- `Modules/SandBox/ModuleData/settlements.xml`
- `Modules/NavalDLC/ModuleData/settlements.xml`
- 两版 `Languages/std_settlements_xml.xml`
- 两版 `Languages/CNs/std_settlements_xml-zho-CN.xml`

底本仍为项目归档的官方模块副本：SandBox.zip SHA-256 `54c358e5b318ffeda8a69ce41a7e665f3b9bef06a6e49b142a972c80ea9c1d55`；NavalDLC.zip SHA-256 `e41ad1c75665e736cad7d02319193a2cc6e0ed68e8bf2e44e1f151b62020b468`。两者与仓库 `research/source-archives/README.md` 的指纹一致。

## 二、全量实体与文本键映射统计

| 核验项目 | 结果 | 解释边界 |
| --- | --- | --- |
| SandBox／NavalDLC聚落实体总数 | 493／540 | 《战帆》增加47个实体；共有实体ID为493个。 |
| 两版共有实体中具有聚落地志text属性者 | 327个 | 另有166个共有实体在两版定义中都没有该类地志文本。 |
| 共有实体的text键保持不变 | 289个 | 这些实体仍引用同一文本键；须再比较该键的英汉值。 |
| 共有实体的text键发生变化 | 38个 | 36个实体名称不变但改用新文本键；另有2个实体ID对应的名称和文本键一起对调。 |
| 两版共有语言表ID | 238个 | 其中210个为 `Settlements.Settlement.text.*` 键、3个为 `Settlements.Settlement.name.*` 键、25个为其他／哈希式ID；不是238条独立的聚落地志。 |
| 238个共同语言表ID的英汉值 | 238个英文值均不同；238个简中值均相同 | 这是字符串表层面的事实，不等于238条实际生效的游戏内地志都没有更新中文。 |
| 38个改派text键的中文值 | 38个新键均有英文和简中值；其中32个新键的简中值与原键不同，6个相同 | 新键可能携带已经更新的译文；不能只看旧的共同键判断游戏实际使用的译文。 |
| 共有实体名称变化 | 3个ID的名称值变化 | 两个ID在Kohi Ajik／Tismil之间对调；另有Etirfurd改为Echarfurd。 |

### 语言表共同ID的引用映射

210个共同 `text` 键中，有208个在两版继续引用相同的实体集合；另有两个键 `Settlements.Settlement.text.village_K2_2` 与 `Settlements.Settlement.text.village_K6_4` 在两个实体ID之间交换引用。这个交换与聚落实体名称对调相对应，并非单纯的地志文本变化。

因此，上一份备忘录中的“238个共同ID英文全部变化、简中全部不变”应严格理解为**语言表ID层面的统计**。它不能直接换算为实际游戏内有多少条译文滞后，也不能单独证明相应自然地理事实发生变化。实际核验必须沿着“实体ID—实体名称—text键—英文表值—简中表值—fallback文本”逐层追踪。

## 三、两个最重要的身份映射案例

### 1. Kohi Ajik与Tismil：实体ID对调

| 模块 | 实体ID | 名称 | text键 | 当前英文地志要点 |
| --- | --- | --- | --- | --- |
| SandBox | `castle_village_K7_2` | Kohi Ajik | `Settlements.Settlement.text.village_K6_4` | 恋人山脚下的狭窄干谷；向东部游牧者购马并转售给库赛特贵族。 |
| NavalDLC | `village_K2_2` | Kohi Ajik | `Settlements.Settlement.text.village_K6_4` | 恋人山脚下的山谷；东侧为Ozu河源头之一。 |
| SandBox | `village_K2_2` | Tismil | `Settlements.Settlement.text.village_K2_2` | Ozu河排泄德夫赛格高原南部；居民放牧绵羊。 |
| NavalDLC | `castle_village_K7_2` | Tismil | `Settlements.Settlement.text.village_K2_2` | Ozu河排泄高原南部；新版突出当地马匹繁育。 |

同一实体ID在两版指向不同名称，反过来，同一名称在两版也使用不同实体ID。两条文本键仍分别跟随Kohi Ajik与Tismil的名称使用，但英文语义已重写，简中值仍保留旧版。对于Ozu河、德夫赛格高原南缘及Tiagys源流的研究，不能把 `castle_village_K7_2` 或 `village_K2_2` 单独当成跨版本稳定的地理实体ID。

### 2. Urunjan：旧键仍在表中，新版实体改用新键

- SandBox实体 `village_K4_4` 使用 `Settlements.Settlement.text.village_K4_4`，定位在德夫赛格高原西缘、阿克坎山脚。
- NavalDLC同名实体改用 `eutVVgbR`，定位在高原东缘、速兰答各山脚。
- 新键 `eutVVgbR` 在NavalDLC英文和简中语言表中均有对应值，中文已经更新为“乌伦占位于速兰答各山脚下，靠近德夫赛格高原的东端”。

这说明旧的共同键仍显示旧中文，不等于《战帆》实际引用的新键也没有更新中文。只比较共同键会漏掉这一类改派键的情况。

## 四、气候与植被专题的同键异文样本

| 实体／文本键 | SandBox英文文本支持 | NavalDLC英文文本支持 | 简中同键问题 | 研究意义 |
| --- | --- | --- | --- | --- |
| Cananc `village_V8_2` | 莱恩诺北部潮湿林丘、海雾中的雪松；林地养猪。 | 地点改为埃博半岛；树种改为紫杉，并补充冷杉、云杉和移民／领主统治叙述。 | 简中仍为莱恩诺北部与旧树种描述。 | 地理定位与树种文本均改写；不能解释成同一地点的生态演替年代。 |
| Rulund `village_V3_2` | 特朗中部林谷、橡树林与养猪。 | 改为特朗河以北的多风海岸，森林稀少，依靠海岸坡地种植黑麦与小麦。 | 简中仍为林谷与橡树描述。 | 旧版森林景观和新版海岸景观不能拼成同一套自然分区证据。 |
| Tememos `castle_village_EN8_2` | 塔奈西斯湖北端树木繁茂的丘陵；林农采伐橡、山毛榉和松树。 | 改为伊察拉平原与迈泽阿德高地交界的季节性马匹放牧地。 | 简中仍为森林采伐描述。 | 是植被／土地利用文本的版本重写，不代表林地在世界内部突然变为牧场。 |
| Chornobas `village_S3_1` | 林地开垦区，俯瞰弥戎河注入拉科尼斯湖的瀑布；瀑布水雾润田。 | 改为伊卡拉丘陵的近期清林地，生产粮食供给奥莫尔；未再提及瀑布或河口。 | 简中仍保留瀑布、弥戎河和拉科尼斯湖叙述。 | 水文论文不能把旧版瀑布关系直接移植到新版文本。 |
| Lochana `castle_village_EN2_1` | 拉科尼斯湖东岸；湖泊缓和北方冬寒，支持桑树种植。 | 城堡守卫Caracasos河，与对岸厄毗诺萨构成北部边防；附近海洋缓和冬寒。 | 简中仍写东岸与湖泊调温。 | “湖泊调温”与“海洋调温”是不同文本证据，须分版本记录。 |
| Mazen `village_K3_3` | 塔奈西斯湖北端渔村，在Karakaz河捕鱼。 | 同一湖区地点改为湖泊缓和冬寒、种桑养蚕。 | 简中仍写捕鱼与Karakaz河。 | 湖泊对局地冬季气候的作用是新版文本新增解释，不能从旧中文直接得到。 |
| Canterion `village_ES4_3` | 吕卡里亚平原东部，地势缓升、降雨多于平原其他部分。 | 改为塞堤斯河、奥尼安岩丘和提米安丘陵之间的养马区。 | 简中仍写“降雨较多”。 | 新版没有保留旧版的比较降雨断言，不能把它当作新版气候证据。 |
| Caira `castle_village_ES1_2` | 卡勒萨水系网络内，卡勒萨河与蒂亚具斯河洪泛平原适合种小麦。 | 丹努斯提卡以东湿润平原；佩拉西克海的海气被卡勒萨丘陵滞留，形成当地气候。 | 简中仍写旧版河湖网络和洪泛平原。 | 同一键从水文—冲积叙述改为海气—地形—湿润环境解释。 |
| Fregian `village_V2_3` | 帕拉汶德以北平原，暖南方过渡到寒冷北方；沼泽与牧场间种亚麻。 | 改为奥克斯霍尔附近浅谷，原沼泽湖由瓦兰迪亚领主排水后种亚麻。 | 简中仍为旧版平原和沼泽／牧场。 | 新版明确记载湿地排水改造，但地点背景也已改变。 |
| Elipa `village_EW5_1` | 阿里斯河谷上游，光照充足、水源丰沛的帝国粮仓高地。 | 改为俯瞰伊察拉平原的高地；平原是干燥、盐渍化的古湖床，主要为草地与灌丛，高地仍肥沃多雨。 | 简中仍为旧版阿里斯河谷粮仓。 | 新版明确区分古湖床平原与周边高地，不能将旧版地理位置和新版景观拼接。 |

## 五、证据判断与后续修订规则

1. 对每个聚落，先读取两版 `settlements.xml`，确认实体ID、名称、`text`键、inline fallback文本和坐标；再解析该键在英文、简中语言表中的实际值。
2. 若实体ID改派给另一名称，应以名称与版本对应关系重新识别实体，不沿用旧实体ID的地理含义。
3. 若text键改变，必须核对新键的英汉值；旧共同键的简中值不代表新版实体当前使用的翻译。
4. 若text键不变而英文变化、中文不变，则该实体的简中同键确实保留旧文本，需在自然地理论文中标记为“英文改写、简中未同步”。
5. 只有在原文明确记载清林、排水、垦殖等人为行为时，才把该版本文本支持的景观改造与纯粹的地志重写区分开来；文本改写本身不是世界内部变迁。
6. 本轮是官方文本和键映射核验，没有重新解析高程、河道几何、Navmesh或土地覆盖数据，故不产生新的B类地图测绘结论。

## 六、关联资料

- [自然地理研究问题图谱与证据矩阵 v0.2](https://docs.google.com/document/d/1IzIEm-CgErZ_REROhHnuXstqvK2vKjPoSXoeyanNFUg/edit)
- [自然地理源级复核备忘录01 v0.2](https://docs.google.com/document/d/1dlRqWn1R8VzeddpHjIaHdeBz-wk-fuTQLTRxSwg8dNI/edit)
- [CGEO-S-HYD-001《卡拉迪亚大陆河流水系与湖泊研究》v0.3](https://docs.google.com/document/d/1qoWxPgRqqHxPSjv9NqeVfy2oj3fkqlEq_xF5CxPrpTc/edit)
- [官方源档归档清单与SHA-256](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/source-archives/README.md)
