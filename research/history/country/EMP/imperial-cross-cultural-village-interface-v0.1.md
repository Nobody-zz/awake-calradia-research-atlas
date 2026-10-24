# CHC-EMP-GEN｜跨文化聚落中的帝国接口：村庄与城堡附属村庄回检 v0.1

**工作包 A 子任务｜2026-10-24**  
**基线**：SandBox v1.4.8 官方英文 `settlements.xml`；简中描述对照 SandBox 官方语言表与 `encyclopedia-zh-cn.md`；NavalDLC v1.2.8 单独对读。
**范围**：对既有18个非帝国文化候选城镇，按 `Village.bound` 读取51条直接附属于这些城镇的普通村庄描述；另全表扫描非帝国文化普通村庄与城堡附属村庄，寻找直接提及 Empire/imperial/Emperor/Calradic/Republic/Senate 等的文本。
**名称规则**：普通村庄中文名只采用上传百科核定的官方名称；城堡附属村庄没有独立官方中文名称键的，保留英文名，不创造译名。

## 一、先报负面结果：城镇关联村庄不自动保留帝国史

- 18个候选城镇共检出 51 条当前绑定的普通村庄记录。
- 这 51 条普通村庄描述中，0 条直接出现帝国、帝国的、皇帝、卡拉德语/文化、军团、共和国或元老院等明确帝国词项。
- 这不表示它们与帝国历史毫无关系；而是说明现存村庄地志大多描述当前生产、地貌与地方生计，帝国历史更常集中在城镇地志或少数直接涉及帝国边疆/市场的村庄文本中。当前 `bound` 只表示现存数据里的聚落关联，不能反推历史时期稳定不变的领属。
- 对这51条的官方中文名与描述已在机器可读表中逐条保留，供后续按城市和主题检索。

## 二、全表中直接提及帝国关系的非帝国文化村庄记录

|源ID|官方中文名（如有）／英文名|文化标签|当前绑定地点|文本键|直接接口|版本差异|
|---|---|---|---|---|---|---|
| castle_village_B1_1 | Ab Comer（未见独立官方中文名称键） | Culture.battania | castle_B1（castle_B1） | Settlements.Settlement.text.castle_village_B1_1 | 贸易/商品 | DLC有文本差异 |
| castle_village_B2_1 | Llanoc Hen（未见独立官方中文名称键） | Culture.battania | castle_B2（castle_B2） | Settlements.Settlement.text.castle_village_B2_1 | 区位/通道 | DLC有文本差异 |
| castle_village_B2_2 | Cantrec（未见独立官方中文名称键） | Culture.battania | castle_B2（castle_B2） | Settlements.Settlement.text.castle_village_B2_2 | 旧帝国土地/边界 | DLC有文本差异 |
| castle_village_K4_1 | Tepes（未见独立官方中文名称键） | Culture.khuzait | castle_K4（castle_K4） | Settlements.Settlement.text.castle_village_K4_1 | 贸易/商品；多语言地名 | DLC有文本差异 |
| castle_village_S4_2 | Ismilkorg（未见独立官方中文名称键） | Culture.sturgia | castle_S4（castle_S4） | Settlements.Settlement.text.castle_village_S4_2 | 旧帝国土地/边界；贸易/商品；边境暴力 | DLC有文本差异 |
| castle_village_S6_1 | Takor（未见独立官方中文名称键） | Culture.sturgia | castle_S6（castle_S6） | Settlements.Settlement.text.castle_village_S6_1 | 旧帝国土地/边界；边境暴力 | DLC有文本差异 |
| castle_village_V2_1 | Hongard（未见独立官方中文名称键） | Culture.vlandia | castle_V2（castle_V2） | Settlements.Settlement.text.castle_village_V2_1 | 旧帝国土地/边界 | DLC有文本差异 |
| village_B1_4 | 阿斯·卡瓦尔 | Culture.battania | town_B1（Marunath） | Settlements.Settlement.text.village_B1_4 | 旧帝国土地/边界 | DLC有文本差异 |
| village_B4_1 | 布林·格拉斯 | Culture.battania | town_B4（Seonon） | Settlements.Settlement.text.village_B4_1 | 区位/通道 | DLC有文本差异 |
| village_S5_1 | 维西布罗特 | Culture.sturgia | town_S5（Tyal） | Settlements.Settlement.text.village_S5_1 | 贸易/商品 | DLC有文本差异 |

### 源级摘要与证据边界

#### castle_village_B1_1｜Ab Comer（未见独立官方中文名称键）

- **文本键**：`Settlements.Settlement.text.castle_village_B1_1`；**文化标签**：`Culture.battania`；**当前绑定**：`castle_B1`（castle_B1）。
- **SandBox英文原文**：Ab Comer sits on the steep pass cut by the upper Trand river that climbs the Uchalion plateau. The tribes of this region grow grapes on the hillsides, used to make a white wine popular with the imperial and Vlandian aristocracies.
- **官方简中描述**：阿布·科梅尔坐落于穿过乌卡利翁高原的特朗河上游的陡峭处。当地各部落会在山坡上种植葡萄，用以酿造一种深受帝国与瓦兰迪亚贵族欢迎的白葡萄酒。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Ab Comer sits on the Etircomb, the steep valley which climbs from the Vlandian coastal plain to the Uchalion plateau, cut by the small creeks feeding the Trand River. The tribes of this region grow grapes on the hillsides, used to make a white wine popular with the imperial and Vlandian aristocracies.

#### castle_village_B2_1｜Llanoc Hen（未见独立官方中文名称键）

- **文本键**：`Settlements.Settlement.text.castle_village_B2_1`；**文化标签**：`Culture.battania`；**当前绑定**：`castle_B2`（castle_B2）。
- **SandBox英文原文**：Llanoc Hen sits in a ridge in the heights of the Uchalion massif. The villagers, known as skilled pig-farmers, look down two passes, the western one leading up from Vlandian lands and the eastern one leading up from the Empire.
- **官方简中描述**：拉诺克·亨位于乌卡利翁地块的高山山脊处。村民们都是熟练的养猪户，他们下山后有两条路，一条向西通往瓦兰迪亚，另一条向东通往帝国。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Llanoc Hen sits at the foot of the Cafalcombe that climbs from the western imperial lands to the Uchalion massif. Oak and other trees grow thick in the valley, providing nuts and thick roots to feed the local hogs.

#### castle_village_B2_2｜Cantrec（未见独立官方中文名称键）

- **文本键**：`Settlements.Settlement.text.castle_village_B2_2`；**文化标签**：`Culture.battania`；**当前绑定**：`castle_B2`（castle_B2）。
- **SandBox英文原文**：Cantrec sits in the rocky Glen of Balasog that climbs up from the imperial lands into the plateau of the Uchafion. The lands is not especially fertile here, but pigs thrive in the bush and shrubland of the heights.
- **官方简中描述**：坎特雷克坐落于帝国领土通往乌喀利昂高原处多岩的巴拉索格峡谷之中。当地土壤并不十分肥沃，但高处的灌木林地很适合养猪。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Cantrec sits in the rocky Cafalcombe that climbs up from the imperial lands into the plateau of the Uchalion. The lands is not especially fertile here, but pigs thrive in the bush and shrubland of the heights.

#### castle_village_K4_1｜Tepes（未见独立官方中文名称键）

- **文本键**：`Settlements.Settlement.text.castle_village_K4_1`；**文化标签**：`Culture.khuzait`；**当前绑定**：`castle_K4`（castle_K4）。
- **SandBox英文原文**：Tepes sits overlooking a tributary of the Karakaz, a river that flows from the north into Lake Tanaz, which the Empire calls Tanaesis. This district specializes in the harvest of timber which is floated down the river and sold to the lake towns.
- **官方简中描述**：泰佩斯村俯瞰着喀拉卡孜河的一条支流，喀拉卡孜河自北方流入帝国人称作塔奈西斯的达那孜海。该地区盛产木材，人们顺流而下，将木材销往湖边的城镇。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Tepes sits in forested lowlands between the Devseg plateau and the lake that the Khuzaits call the Tanaz Sea. This district specializes in the harvest of timber, which is dragged by oxen to the water and then floated to the lake towns.

#### castle_village_S4_2｜Ismilkorg（未见独立官方中文名称键）

- **文本键**：`Settlements.Settlement.text.castle_village_S4_2`；**文化标签**：`Culture.sturgia`；**当前绑定**：`castle_S4`（castle_S4）。
- **SandBox英文原文**：Ismilkorg sits on grassy downs between the Galcha and Vastra rivers, two small tributaries of the Miron. The people here are mostly cattle-herders as well as cattle-rustlers, and have long traded raids with the imperial frontier villages to the east and Battanians to the west.
- **官方简中描述**：伊斯米尔科格坐落于弥戎河的两条小支流——加尔察河与瓦斯特拉河间长满草的低地上。当地人大多既养牛又偷牛，并长期劫掠东边的帝国边境村庄和西边的巴旦尼亚人。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Ismilkorg sits in the Irkaria hill country between Lake Laconis and the gulf that the Sturgians call the Battanian Sea. The people here are mostly cattle-herders as well as cattle-rustlers, and have long traded raids with the imperial frontier villages to the south and Battanians to the west.

#### castle_village_S6_1｜Takor（未见独立官方中文名称键）

- **文本键**：`Settlements.Settlement.text.castle_village_S6_1`；**文化标签**：`Culture.sturgia`；**当前绑定**：`castle_S6`（castle_S6）。
- **SandBox英文原文**：Takor is a cattle raising village at the pass that the Battanians call Mynad Rhyfel, the mountain of war, and their imperial and Sturgian neighbors call Minador. It is one of the main trading and raiding routes between the wild north and the more settled imperial lands.
- **官方简中描述**：塔科尔是一座养牛村，位于巴旦尼亚人称作“米纳德·里韦尔”，即“战争之山”的山口处。他们的帝国与斯特吉亚邻居们则称之为“弥那多耳”。这是连通荒凉北方与相对稳定的帝国疆土的主要通道之一，无论对商贸还是对劫掠来讲。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Takor is a cattle-raising village in the heart of the Chertyg Mountains. The term 'Takorski' is used by other Sturgians to refer to someone whose speech is unintelligible. Above the village, small wisps of smoke show where wandering Vakken forest dwellers make their temporary fields, sowing them for one or two seasons before moving elsewhere.

#### castle_village_V2_1｜Hongard（未见独立官方中文名称键）

- **文本键**：`Settlements.Settlement.text.castle_village_V2_1`；**文化标签**：`Culture.vlandia`；**当前绑定**：`castle_V2`（castle_V2）。
- **SandBox英文原文**：Hongard sits in the warm wooded lands near the meandering Trand river. This land, rich in wheat and once the heartland of the Empire, is now the center of the Vlandian kingdom.
- **官方简中描述**：翁加尔坐落于蜿蜒的特朗河附近的温暖林地。这片盛产小麦的土地曾是帝国的腹地，如今却成了瓦兰迪亚王国的中心。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Hongard sits in the warm wooded lands near the meandering Trand River. This region, rich in wheat and once the heartland of the Empire, is now the center of the Vlandian kingdom.

#### village_B1_4｜阿斯·卡瓦尔

- **文本键**：`Settlements.Settlement.text.village_B1_4`；**文化标签**：`Culture.battania`；**当前绑定**：`town_B1`（Marunath）。
- **SandBox英文原文**：Ath Cafal sits near the head of the Cafalcombe, a steep valley that descends to the imperial lands. Decent clay can be found in the small streams that rush down from the hills on all sides.
- **官方简中描述**：阿斯·卡瓦尔靠近卡瓦尔谷——通往帝国领土的陡峭山谷之起始端。山上奔流而下的小溪中可以收集到优质的黏土。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Ath Cafal sits near the head of the Cafalcombe, a steep valley that descends to the imperial lands. The villagers gather fine clay from local streambeds to trade to the potters of nearby towns.

#### village_B4_1｜布林·格拉斯

- **文本键**：`Settlements.Settlement.text.village_B4_1`；**文化标签**：`Culture.battania`；**当前绑定**：`town_B4`（Seonon）。
- **SandBox英文原文**：Bryn Glas sits in a ridge in the eastern escarpment of the Uchalion massif. Villagers raise grapes on the slopes, making a strong, dark red wine highly valued by the Vlandians and the Empire.
- **官方简中描述**：布林·格拉斯坐落于乌卡利翁地块东边的悬崖上。村民们在山坡上种植葡萄，酿造出浓郁的深红色葡萄酒，深受瓦兰迪亚人和帝国人的喜爱。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Bryn Glas sits on the eastern shores of the Llyn Tywal. Villagers raise grapes on the slopes, making a strong, dark red wine highly valued by the Vlandians and the Empire.

#### village_S5_1｜维西布罗特

- **文本键**：`Settlements.Settlement.text.village_S5_1`；**文化标签**：`Culture.sturgia`；**当前绑定**：`town_S5`（Tyal）。
- **SandBox英文原文**：Visibrot is a sheep-rearing village on the lower slopes of Mount Iltan, just below the network of glacial lakes known as the Iltan portages. Though this region is cold and remote, its importance as a trade juncture between Lakes Laconis and Tanaesis, between the Empire and the steppe, mean that it is relatively densely populated.
- **官方简中描述**：维西布罗特是伊勒坦山缓坡上的一座养羊村，正好位于人称伊勒坦运输线的冰湖网络下。尽管该地区寒冷偏僻，但它作为拉科尼斯湖与塔奈西斯湖之间，帝国和草原之间贸易节点的重要性，仍使其拥有了相对稠密的人口。
- **NavalDLC对读**：DLC有文本差异。 DLC英文：Visibrot is a sheep-rearing village on the lower slopes of Mount Iltan. Though this region is cold and remote, its importance as a trade juncture between Lakes Laconis and Tanaesis, between the Empire and the steppe, mean that it is relatively densely populated.

## 三、历史解释：四种不同的帝国接口

### 1. 旧帝国腹地被后来的国家重新占据：Hongard

城堡附属村庄 `castle_village_V2_1` 的英文直接说该地“once the heartland of the Empire”，如今则是瓦兰迪亚王国的中心。这是“帝国旧地—新政治中心”的直接证据；但它不能说明全区在任何一个时期都由同一套行政机构控制，也不应把后来的瓦兰迪亚社会降格为帝国的残余。

### 2. 边境不是单向防线，而是贸易、掠袭与牧业交错地带

斯特吉亚文化的 `castle_village_S4_2`（Ismilkorg）把当地畜牧与偷牛并置，并说居民长期与东面的帝国边境村庄、西面的巴旦尼亚人互相袭掠；`castle_village_S6_1`（Takor）则将山口描述为北方与较定居帝国土地之间的主要贸易和袭掠通道。`village_S5_1`（Visibrot）又把伊勒坦湖泊拖运线定位为帝国与草原之间的贸易交汇点。这里的边疆同时是资源生产区、市场接口和暴力通道。

### 3. 帝国商品市场延伸到境外，未必伴随直接统治

巴旦尼亚的 `castle_village_B1_1`（Ab Comer）称当地白葡萄酒受到帝国与瓦兰迪亚贵族欢迎；`village_B4_1`（Bryn Glas）称当地浓郁红酒同样受到两方贵族重视。它们支持跨境商品消费关系，却没有说明贵族采购是否来自税收、贡赋、商人合同或私人庄园。

### 4. 水系和地名本身可以保留多种政治语言

库赛特文化的 `castle_village_K4_1`（Tepes）把一条河描述为流入湖泊的支流，并明确说库赛特称湖为 Tanaz、帝国称其为 Tanaesis；当地木材沿河漂运到湖边城市出售。这一条把多语言地理知识与商品流向连接起来，但不能据此推定官方测绘、统一边界或帝国直接经营木材业。

## 四、审计与限制

- 关键词检索会产生假阳性：`castle_village_B4_1` 名为 Pendraic，但其描述正文只讲持续的低烈度战争和三方袭掠，没有直接提到帝国，因此不计入“直接帝国关联”样本。
- 51条候选城镇绑定村庄的零直接帝国词项，是文本覆盖结果，不是历史上没有帝国关系的证据。它说明城镇与乡村地志承担不同的叙述功能：城镇较常保留政治沿革，村庄较常保留现状生产与地貌。
- 本表的当前绑定和文化标签是数据结构，不可反推古代领属；文本中的“帝国市场”也不自动证明中央统一市场、国家征购或具体贸易量。
- NavalDLC文本差异须逐条对照；即使同一条记录保留了经济主题，也不能把版本异文拼成一段连续历史。

## 五、下一步

将这组10条直接接口材料与18个跨文化城镇的地志并读，重点检查：城镇的帝国政治记忆与村庄的现状生产是否相互支持；边境市场是否存在可复核的双向商品联系；以及哪些地点只有地理邻接而没有直接帝国联系。之后再把结果接入工作包 C 的地方自治、边疆服务和非正式强制模型。

**机器可读附表**：同目录 CSV 保留10条直接接口记录的完整英文、官方简中描述、绑定地点、源键及 NavalDLC 对读。
