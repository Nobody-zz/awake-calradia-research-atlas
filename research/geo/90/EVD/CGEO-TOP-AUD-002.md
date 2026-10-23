# CGEO-TOP-AUD-002｜卡拉迪亚大陆地理专名扩展校勘与分版地志异文审查

地名学、地理文献校勘与版本史料批判附录｜2026年10月23日｜研究底本：SandBox、NavalDLC 英文及简体中文语言表

## 摘要

本报告不从地图画面、拉丁字母的直观发音或社群常用语推定中文专名，而是以项目存档的两套英文—简体中文同键地志核实山地、半岛、海湾、河流、湖泊及区域名；进而检查英文地志内容与未同步修订的中文译文之间的文献学冲突。两版聚落英文本地化语言表分别有274、358条字符串，存在238个共同ID；这238个ID对应的英文字符串全部有文字差异，中文字符串却全部相同。这里的“有文字差异”包括大小写、措辞和地理叙述重大变化，**不能因此认为238处地貌均发生了变化**。特别是重新编写的英文说明，只能说明版本文本变更，不能直接解释为世界内部自然地理发生过变迁。

## 一、底本、核验方法和分级

- 基础版：`SandBox.zip`，`Modules/SandBox/ModuleData/Languages/std_settlements_xml.xml` 与 `CNs/std_settlements_xml-zho-CN.xml`；
- 航海扩展版：`NavalDLC.zip`，同结构的 `std_settlements_xml.xml`、`CNs/std_settlements_xml-zho-CN.xml`；必要时参照`std_NavalDLC_SandBoxCore_SPCultures_xslt.xml`和`std_naval_dialog_strings_xml.xml`；
- 两版各自以`<string id>`进行精确匹配，不以地名拼写的局部字母相同视为同一实体；原始聚落实体`settlements.xml`和现存城镇名称对照另设字段。
- A：对应英文原文与简体中文译文可在同一字符串ID直接核对到名称形式。A级并不必然意味着另有专门的“中文实体名称”键。
- B：中文社区、既有索引或研究负责人明确校正但当前存档无直接名称键的项目首选名。须注明依据，不能冒称A级。
- C：仅英文版本存在、汉译未同步或已移除的地貌对象。保留英文名和译名待考标记；只作当版文献所述事实，不借旧简中译文复原。

## 二、经过同键核实的自然地理专名

| 地理要素 | 稳定英文名称 | 采用简体中文名称 | 举证文本字符串ID及说明 |
| --- | --- | --- | --- |
| 内海 | Perassic Sea | 珀拉斯海 | `JhBSnWAe`；俄耳堤西亚 |
| 海湾 | Gulf / Bay of Charas | 沙拉斯湾 | `Settlements.Settlement.text.castle_village_EW1_1`、`JhBSnWAe`；英文湾/海湾措辞可分版，不应推测海湾重构 |
| 北方海域 | Byalic Sea | 比亚里海 | `Settlements.Settlement.text.castle_village_S1_1` |
| 海湾 | Bay of Varcheg | 瓦尔切格湾 | `Settlements.Settlement.text.castle_village_B4_1` |
| 海湾／峡湾称谓 | Mazopor Bay | 马佐波尔湾 | `Settlements.Settlement.text.village_S2_2` |
| 半岛 | Ebor Peninsula | 埃博半岛 | `1SnAH5K8`；罗瓦拉堤斯地志 |
| 半岛 | Kachyar Peninsula | 卡恰尔半岛 | `i2VkRLBg`、`Settlements.Settlement.text.castle_village_S1_1` |
| 河谷 | Morcomb | 摩康谷 | `Settlements.Settlement.text.castle_village_B3_1` |
| 地貌高地 | Uchalion | 乌卡利翁（地貌类别按版本单列） | `4OAz8urz`等；部分旧文“高原”，新版有“山体”等写法，不预设同形态 |
| 东部丘陵 | Akkan Hills | 阿克坎丘陵 | `Settlements.Settlement.text.castle_village_K1_1`、`castle_village_ES2_1` |
| 草原高原 | Devseg Plateau | 德夫赛格高原 | `Dxnj5JQE`、`Settlements.Settlement.text.castle_village_K1_2` |
| 帝国东部高地 | Myzead | 密泽亚德 | `Settlements.Settlement.text.castle_village_ES3_1`；英文“高原/高地”异文 |
| 滨海丘陵 | Iltaric Hills | 伊勒塔尔丘陵 | `kghCLS9q`、`Settlements.Settlement.text.village_ES3_3` |
| 谷地／平原名称 | Lycarea | 吕卡里亚 | `Settlements.Settlement.text.castle_village_ES5_1`、`village_ES3_3`；按文献所述具体地貌用“谷”“平原” |
| 东北山名 | Mount Iltan | 伊勒坦山 | `F5HlQdgf`；蒂亚尔地志 |
| 湖间转运地 | Iltan portages | 伊勒坦运输线 | `Settlements.Settlement.text.castle_village_EN7_1`，基础版专指湖间运输条件，不与伊勒坦山自动合并 |
| 南方崖地 | Jarjara Escarpment | 杰尔贾赖峭壁 | `Settlements.Settlement.text.castle_village_A4_2`、`village_A7_4` |
| 南方关口 | Scorched Gates | 枯焦之门 | `Settlements.Settlement.text.village_A7_4` |
| 北方大湖 | Lake Laconis | 拉科尼斯湖 | `aTMypBiY`等 |
| 中部大湖 | Lake Tanaesis | 塔奈西斯湖 | `bPDqyqkb`、`Settlements.Settlement.text.castle_village_K1_1` |
| 草原语言湖名 | Tanaz Sea / Lake Tanaz | 达那孜海 | `bPDqyqkb`、`Settlements.Settlement.text.castle_village_K4_1`；与塔奈西斯湖同一水体的异语名称 |
| 东南湖沼 | Calsea | 卡勒萨 | `Settlements.Settlement.text.castle_village_ES4_1`、`village_ES1_1` |
| 东南河流 | Calsa River | 卡勒萨河 | `Settlements.Settlement.text.village_ES1_1` |
| 东南河流 | Tiagys River | 蒂亚具斯河 | `Settlements.Settlement.text.castle_village_ES2_2`；不同版与Teyagh指涉关系不可直接合并 |
| 东南河流 | Sethys River | 塞堤斯河 | `Settlements.Settlement.text.village_ES2_1` |
| 河口分汊谷地 | Tripotamia | 三河河谷 | `Settlements.Settlement.text.village_ES2_1`、`village_ES2_2`，**纠正论文旧音译“特里波塔米亚”** |
| 北方河流 | Jumne River | 朱姆内河 | `bLTkig9T`、`DtEBwPpJ`等 |
| 南部河流 | Damar River | 达玛尔河 | `Settlements.Settlement.text.village_A7_4` |
| 北方地理地域 | Nordvyg | 诺德维格 | `bLTkig9T`、`danasORQ` |
| 北方岛屿 | Beinland | 贝恩兰；岛屿语境可称贝恩兰岛 | `bLTkig9T`，同句明确 `island of Beinland` |
| 北方城镇 | Gretysfjord | 格雷蒂斯湾（城镇名称） | `nxmX99pO`、`Settlements.Settlement.name.town_N2`；名称不直接证实地貌成因 |
| 北方河港城镇 | Hargard | 哈加德 | `Settlements.Settlement.name.town_N4`；**不按英文重新音译** |
| 西南海域 | Bahr al-Yeshm / Jade Sea | 拜赫尔·耶什姆／翡翠之海 | `Settlements.Settlement.text.castle_village_A5_1`、`village_A5_3` |

地名类别不能直接由译名中的“湾”“山”“高原”推出成因。尤其西部的摩康谷在基础版被叙述为裂谷，航海扩展版同地名附近的山系措辞则有所改动；构造地貌的正式判定还需独立地质或形态资料。

## 三、版本地志冲突的关键个案

| 锚点与地点 | SandBox英语地志所述 | NavalDLC英语地志所述 | 简中状态与学术处置 |
| --- | --- | --- | --- |
| `F5HlQdgf` 蒂亚尔 Tyal | 伊勒坦山西部山麓 | 通向伊勒坦山的高谷、岩质山峰 | 中文仍“西麓”；不将两版视为同一相对高程定位 |
| `Settlements.Settlement.text.castle_village_EN7_1` 厄毗诺萨 Epinosa | 冰川湖—伊勒坦运输线，拉科尼斯—塔奈西斯湖间拖船 | 河流环抱的舌形地，喀拉卡索斯、朱姆内与达武纳名称并列 | 中文仍旧运输线；需分版记录河道节点 |
| `Settlements.Settlement.text.castle_village_K4_1` 泰佩斯 Tepes | 喀拉卡孜河支流附近，木材浮运入湖 | 德夫赛格高原与达那孜海之间森林低地，木材由牛拖至水边再转运 | 中文仍旧支流和木材浮运版本 |
| `Settlements.Settlement.text.castle_village_A4_2` 吉德纳尔 Qidnar | 达玛尔河漫滩、年际洪泛、椰枣园 | 杰尔贾赖峭壁内侧岩质丘陵，数年一遇暴雨及导水渠 | 中文未同步；禁止合并成同处实测水文制度 |
| `Settlements.Settlement.text.village_ES1_1` 恺拉 Caira | 卡勒萨水网与卡勒萨—蒂亚具斯平行洪泛平原 | 达努斯提卡以东湿润平原与卡勒萨丘陵阻风 | 中文仍旧河湖洪泛叙述 |
| `Settlements.Settlement.text.village_ES2_1` 阿特费尼亚 Atphynia | 塞堤斯河入海，三河河谷与盐田 | 蒂米安丘陵、含贝壳岩层和古海湾隆起的地方传说 | 中文仍旧河口；新版传说不等于确证地质史 |
| `Settlements.Settlement.text.castle_village_ES2_1` 科雷尼亚 Corenia | 塔奈西斯湖东南、阿克坎丘陵附近 | 塔奈西斯湖滨的 Tanaetic Plain 北部 | 中文仍旧地理区位；新版英文区域名暂无本轮可核中文译名 |
| `Settlements.Settlement.text.castle_village_B3_1` 德鲁伊莫尔 Druimmor | 摩康谷裂谷，隔开乌卡利翁高原与埃博半岛山脉 | 乌卡利翁山体高地的最高地段之一 | 中文仍旧“摩康谷”；不足以推断真实造山演变 |
| `Settlements.Settlement.text.castle_village_EN7_2` 庞斯 Pons | 伊勒坦湖间运输线交叉处 | 喀拉卡索斯河上的旧桥毁于洪水后，渡口发生替代 | 中文仍旧湖间运输线；不能混成单一时空关系 |
| `Settlements.Settlement.text.village_K3_1` 沙佩什特 Shapeshte | 札罕河和喀拉卡孜河汇流处 | 塔奈西斯湖湾渔村 | 中文仍旧两河汇流；既有CGEO-TOP-AUD-001已标疑 |

这里不能使用“较新版本一定更加接近同一真实地理的最终定论”的方法预设。版本文本的差异首先是史料层次差异，若要选择一个作为特定研究时期的优先依据，须说明采纳理由，并依同版地图地物另作验证。

## 四、对既有论文的具体订正

1. `CGEO-S-HYD-001` 统一 Tripotamia 正文为“三河河谷”；明确伊勒坦运输线与伊勒坦山不同。有关厄毗诺萨、吉德纳尔、恺拉及阿斯凯尔等地理表述按不同版本拆分，未再将旧汉译作为新版英文的旁证。
2. `CGEO-S-TRN-001` 统一英文河港 Hargard、河流 Jumne 首见处为“哈加德（Hargard）”“朱姆内河（Jumne River）”，将湖间转运线路名称统一为“伊勒坦运输线”，而非单一确定码头。
3. `CGEO-S-GEO-001` 对海湾城镇 Gretysfjord 明确规范中文为“格雷蒂斯湾”；新增有关埃博半岛、卡恰尔半岛、比亚里海、伊勒塔尔丘陵等的经校勘名称，用于后续地貌区域验证。
4. `CGEO-O-REG-001` 与 `CGEO-N-N001-001` 则需把阿克坎丘陵—德夫赛格高原—密泽亚德的地理关系单独考察，不以“帝国东界”“库赛特草原”的政治词替代具体自然地域。

## 五、进一步的历史地理认识

本轮校勘不仅影响中文标签，也改变了可提出的问题。例如东部的阿克坎丘陵与德夫赛格高原分别在乌赛克、埃斯梅地志中出现，支持“湖岸—山麓—高原牧地”的地域分异研究；帝国东部密泽亚德的狭谷与桑树种植地志支持高地生业结构的局部分析。西部埃博半岛的矿业、森林毛皮和谷地农业，显示“冬季严寒”与“人口较密集”可以并存；卡恰尔半岛与瓦尔切格湾则提示海崖—半岛—湾岸交通间的相互制约。这些都是地志中的局部条件，而不是已实测的大陆自然地理边界。

## 六、资料限制和后续问题

本轮核对涵盖项目保存的语言表而不是全部运行时本地化资源。对某个英文名没有独立的简中实体名称键时，不应推断其无中文译名。新版只在英文出现的山名，如 Tanaetic Plain、Thymian Hills、Calsean Hills、Caracasos、Davuna 等，今后首次出现应保留英文，并标记中文暂译待核，不能借旧版中文地志为其“证明译名”。

扩展地名学专题须遵守“英文本键确定对象—同键汉译确定用字—文本版本限定地理陈述—独立史料检验年代”的四步程序。完整论文优先描述卡拉迪亚的自然与历史地理，只在引注、资料方法与该类校勘附录明列档案来源。

资料链接：
- 已存原始资料归档：https://drive.google.com/drive/folders/17y4EwetqNlFBW1Zf_d_CP4yrdyjmr8Rm
- 前一轮校勘：https://docs.google.com/document/d/1TBFat1RzfI8-sPRDEntJ_bmoZ1xx2kxC4bSo7djV1qc/edit
- 地理研究总索引：https://docs.google.com/document/d/1KlBS4Lv27FR13ycc7hPqAWPhPinDcmzKVmLc1q8efeE/edit

## 七、同键译文错置与校勘等级修正

对238个两版共同字符串ID进一步按英文大小写、空白和标点标准化比较，24处英文差异在这种标准化后消失；其余214处存在字词层面的差异，但不能将其全部认定为地理学说或地貌事实发生实质变化。作为初步风险筛查，英文字符串相似度小于0.75的共有138处（采用直接字符序列相似度），这只用于设定人工复核优先级，不代替逐条阅读及版本判定。238条同键简中译文全部未变化。

此外，发现**中文与英文同字符串ID但译文完全错置**的独立案例：
- 位置：`Settlements.Settlement.text.castle_village_A7_1`，Uqba。基础版英文记为珀拉斯海沿岸村庄收集雨水和山麓径流灌溉农田及椰枣园；《战帆》英文改称珀拉斯海滨海平原，亦写出集雨和径流利用。
- 两版简体中文同键内容却以“但再次假设你是执政官加里俄斯，正谋划称帝”开篇，随后写执政官与苏丹缔约和流放名单，**不对应Uqba的水源、耕作或聚落地貌**。
- 因而不能用该简中条目确认Uqba的当地地貌，亦不能假设其在英文中没有提到集雨农业；正文引用此地时须回到分版英文原文。

**修订证据等级：** 同一字符串ID只提供文件级配对，属于“形式同键”；A级中文译名确认还必须有人工作业核对中英文是否指向同一命名实体、相同叙述语境，而不能只依据两个文本都带有该ID就自动升级。对于像Uqba这样明显错置的翻译，应登记“同键不对应／译文不可用（X）”。同一条目的其他地名若偶然出现，不可因文本错置而沿用为该地理实体的中文名称证据。英文原文应首先决定地理意义，中文译名需按对应的有效文本核对。

检索范围限定为项目已存两套聚落英汉语言表，不以一次不匹配推断全游戏所有文字版本均有相同错误。 


## 2026-10-24｜植被和景观的同键分版审查补录

本轮以归档 `SandBox.zip` 与 `NavalDLC.zip` 的 `Languages/std_settlements_xml.xml` 和 `Languages/CNs/std_settlements_xml-zho-CN.xml` 核查森林、草场、灌丛及湿地，已对应新稿 CGEO-S-BIO-001。以下变化会改变生态地理解释，不能把两版景观拼成同一时期空间图，也不能根据版本发布先后自动推出世界内部历史演替：

| 地点／英文地志字符串ID | SandBox 英文描述 | NavalDLC 英文描述 | 核查结论 |
| --- | --- | --- | --- |
| 卡南克／`village_V8_2` | 海雾丘陵中高大的雪松 `cedars` | 海雾丘陵中的紫杉 `yew`，新增高大冷杉及云杉 `fir and spruce` | 树种替换及新增不能当作同版共存或有年代的演替；简体中文未补充新版树种 |
| 鲁兰德／`village_V3_2` | 特朗河中游森林谷地，猪采食橡实 | 特朗河北侧多风、少林海岸，猪吃黑麦和小麦 | 原地植被和饲养模式改写；中文沿用旧版橡树林表述 |
| 色雷刻托／`castle_village_EW4_1` | 南方热风、山泉、试验栽培椰枣 | 入海溪流周围橡树林、林中养猪 | 人工试种作物与自然林地类型不能跨版合并 |
| 特美摩斯／`castle_village_EN8_2` | 塔奈西斯湖北端橡树、山毛榉、松树林业 | 伊察拉平原—密泽亚德高地接触带的夏季山坡牧草、冬雨后谷底草生 | 森林生产区与季节草场是两版不同地域描述 |
| 弗雷吉昂／`village_V2_3` | 帕拉汶德北部沼泽及亚麻草场 | 奥克斯大厅附近浅谷，原沼泽湖经贵族排水后种亚麻 | 新版同一条内含明确历史排水过程；中文旧稿不作新版排水记载 |
| 伊尔卡里亚乔诺巴斯／`village_S3_1` | 弥戎河入湖瀑布附近的清林耕作 | 新近清林，黑麦大麦供应俄墨尔；东北方向仍大量林地，居民正在继续砍林开田 | 只有新版条目内部的“recently cleared”与正在清林，才可用作有过程的景观改造证据 |
| 斯科林／`village_S3_2` | 拉科尼斯湖岸与湾内捕鱼 | 伊尔卡里亚草地丘陵与森林镶嵌，残林有毛皮动物 | 不能据两版差异推论湖泊变为草地与森林 |

另外：两版都直接记载乌瑟莱姆（`castle_village_B8_1`）的橡、紫杉、松林及福林（`village_S1_2`）的林地转马场；加隆托（`castle_village_EW1_1`）的海岸耐盐草甸；阿利斯维斯特（`village_V9_2`）的沼泽排水种谷。它们可作为跨版本较稳定的局地描述，但版本文本同源，不能计作彼此完全独立的自然调查。

**解释规则**：相同聚落键不等于相同景观文本；同一中文键沿用旧叙述也不代表新版英文可由之补证。森林树种、天然植被、农业经营、季节牧草及变更后的土地覆盖应分别立项，而不以经济活动标签直接绘制天然植被带。


## 2026-10-24｜基础版北帝国聚落英文—简中语义偏差补录（CGEO-S-HUM 第三轮）

本轮核查发现**同键对应、中文地名可用、但地理经济语义被误译**的两条风险。它与前文的“同键译文完全错置”不同：中文句子仍描述同一地点，只是关键动作或对象发生了偏移。校勘材料范围为用户文库 v1.4.8.119303 官方简中聚落条目与可检索同版本官方英语转录；本轮尚未重新完整解包 SandBox ZIP 逐字符串比对，暂作为**高可信待原包回读**的语义审校记录，不称已完成全部官方源档核验。

| 聚落与字符串键 | 官方简中关键语义 | 对应基础版英文语义 | 对历史地理的影响 | 核查等级 |
| --- | --- | --- | --- | --- |
| 斯塔堤摩斯 Stathymos／`Settlements.Settlement.text.village_EN1_2` | “高地的溪流灌溉着山坡上的沃土” | “The highland streams wash fertile soil down the hillsides”：山溪向坡下冲运肥沃土壤 | 不应因中文“灌溉”就创设人工灌渠、地主灌溉工程史；当地谷地麦作仍有直接文字支持 | 英汉语义复核确认；原包本轮未复解 |
| 俄耳特拉 Orthra／`Settlements.Settlement.text.village_EN5_2` | “从东方草原运来牧草，为帝国骑兵部队提供马匹” | “It was founded as a stud farm to breed imperial horses with steppe stock from the east”：较新军用育马场使用来自东部草原的育种牲畜／马种 | 被误译的贸易对象从活畜／马种变为草料；禁止据此建立东方向西长途干草路线；可以提出跨地域种畜育种联系但规模与路线仍未证 | 英汉语义复核确认；原包本轮未复解 |

比较示范：CGEO-S-HUM北方新稿已依据这两处英文语义重写了麦田水土机制和军马供应机制；阿瓦辛顿村的英文“cleared away the thickets and thornbrush”是清除灌木与荆棘，不能无来源改写为伐尽成熟森林。以上风险无须否认官方译名的有效性，错误集中在动词和贸易对象，正是本项目“英语决定内涵、中文决定专名”的适用案例。

英文对照页面：https://mountandblade.fandom.com/wiki/Stathymos ；https://huggingface.co/datasets/TSEOsiris/bannerlord-lore-dataset/viewer/default/train?p=24 。后者与前者均为文本再现或资料转录，不能视为来源相互独立的第二/第三官方证词。
完整专题论文：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/03/HUM/imperial-northern-frontier-landscape-and-estates-2026-10-24.md ；https://docs.google.com/document/d/1yH8EtspASm4a9LYwph4AwUIZki7x_212KZALNC4FIK4/edit
