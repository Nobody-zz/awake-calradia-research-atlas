# CHC-EMP-GEN｜城堡附属村庄史料覆盖：50条记录、区域生产与边疆社会

**工作包A第三批源级分析 v0.1｜2026-10-24**  
**研究范围**：SandBox/ModuleData/settlements.xml中culture=Culture.empire且有非空text的50条castle_village记录；与47条village记录、19条town记录、1条retirement_retreat特殊地点合计117条。这里的castle_village是城堡领地所关联的村庄记录，不是50座城堡的描述。  
**研究性质**：CHC-EMP-GEN工作札记，不申请H编号，不修改公共I/Q索引。

## 一、源级核对与翻译覆盖

- SandBox/ModuleData/settlements.xml：归档v1.4.8，文件SHA-256为E92BB2079526DCC4A125B6A7AE21B76240E5176D143ACA98D083BE9CE8C32524。
- NavalDLC/ModuleData/settlements.xml：归档v1.2.8，文件SHA-256为4F2924A0B236062D1720E0AD48131D23FA4863E5C0AA7FE475F36B0056B9E436。
- SandBox官方简中语言表为描述翻译的校验来源。与19座城市不同，这50条castle_village记录在本次归档中没有独立的简体中文name key，因此本表保留英文源名与稳定ID，不自行制造“官方中文村名”。部分中文描述正文中有音译形式，但不能把它们冒充为独立名称表记录。
- 50条描述中，33条使用castle_village自身的中文文本键，14条复用既有village文本键；另有3条在当前SandBox简中语言表中未找到对应描述翻译：Masangara（castle_village_EN5_2，复用village_EN2_3键）、Jogurys（castle_village_ES7_1，自身键缺失）、Eunalica（castle_village_ES7_2，复用village_ES7_3键）。这些记录的英文原文仍可直接研究，但引用中文时不得假装已有官方译文。
- 另有retirement_retreat，描述只是游戏地点功能提示，不构成帝国历史叙事，应从历史论证样本中排除。

## 二、50条记录清单与首轮主题分类

### A. 北部与东部高地（18条）

| settlement ID | 英文源名 | 描述文本键后缀 | 首轮主题 |
|---|---|---|---|
| castle_village_EN1_1 | Varagos | castle_village_EN1_1 | 山地牧羊；与俄佛堤斯湖的水系联系 |
| castle_village_EN1_2 | Aeoria | village_EN3_2 | 帝国腹地的方言保留帕拉语词汇 |
| castle_village_EN2_1 | Lochana | castle_village_EN2_1 | 拉科尼斯湖调节气候；桑树与丝业 |
| castle_village_EN2_2 | Nortanisa | village_EN4_3 | 湖岸渔业与浅水捕捞 |
| castle_village_EN3_1 | Rhesos | castle_village_EN3_1 | 高原牛与山地牧草 |
| castle_village_EN3_2 | Dyopalis | village_EN1_4 | 北部粮食产区 |
| castle_village_EN4_1 | Gaos | castle_village_EN4_1 | 旧游牧牧民与牛相关地名记忆 |
| castle_village_EN4_2 | Themys | village_EN5_3 | 高地绵羊饲养 |
| castle_village_EN5_1 | Atrion | castle_village_EN5_1 | 涅维斯河谷、桑树与丝业 |
| castle_village_EN5_2 | Masangara | village_EN2_3 | 排干湿地、草甸畜牧；缺少对应简中描述键 |
| castle_village_EN6_1 | Ataconia | castle_village_EN6_1 | 山麓盐矿开采 |
| castle_village_EN6_2 | Potamis | village_EN4_1 | 前卡拉德时期延续的牛业、奶与黄油贸易 |
| castle_village_EN7_1 | Epinosa | castle_village_EN7_1 | 伊勒坦运输线、稀疏人口与大群牛只 |
| castle_village_EN7_2 | Pons | castle_village_EN7_2 | 伊勒坦湖网交叉点、山地盐矿 |
| castle_village_EN8_1 | Syratos | castle_village_EN8_1 | 塔奈西斯湖北岸的亚麻 |
| castle_village_EN8_2 | Tememos | castle_village_EN8_2 | 林业、橡木／山毛榉／松木与湖边城市市场 |
| castle_village_EN9_1 | Mecalovea | castle_village_EN9_1 | 边疆崖地聚落、瀑布切割地层暴露矿石 |
| castle_village_EN9_2 | Agalmon | castle_village_EN9_2 | 森林村落、与斯特吉亚人通婚及战争导致的关系紧张 |

### B. 西部、沿海与内陆生产区（16条）

| settlement ID | 英文源名 | 描述文本键后缀 | 首轮主题 |
|---|---|---|---|
| castle_village_EW1_1 | Garontor | castle_village_EW1_1 | 沙拉斯海峡地理；沿海草甸育马 |
| castle_village_EW1_2 | Lysia | village_EW4_2 | 珀拉斯海与西大洋之间的海峡、盐田 |
| castle_village_EW2_1 | Thorios | castle_village_EW2_1 | 阿里斯河谷灌溉粮食，供养帝国中部 |
| castle_village_EW2_2 | Bergum | castle_village_EW2_2 | 与托里俄斯共同构成中部粮食腹地 |
| castle_village_EW3_1 | Onica | castle_village_EW3_1 | 梯田葡萄园与帝国范围内流通的干型葡萄酒 |
| castle_village_EW3_2 | Tarcutis | village_EW2_1 | 海岸葡萄园、砂质土壤与晨雾 |
| castle_village_EW4_1 | Thractorae | castle_village_EW4_1 | 帝国地主试验种植椰枣 |
| castle_village_EW4_2 | Gamardan | village_EW3_1 | 海湾渔业与金枪鱼捕捞 |
| castle_village_EW5_1 | Veron | castle_village_EW5_1 | 排水良好的砂质山地葡萄园 |
| castle_village_EW5_2 | Goleryn | castle_village_EW5_2 | 绵羊饲养与偷羊并存；靠近瓦兰迪亚和巴旦尼亚边境 |
| castle_village_EW6_1 | Hertogea | castle_village_EW6_1 | 橄榄种植与芳香型橄榄油 |
| castle_village_EW6_2 | Nideon | village_EW1_3 | 河谷葡萄种植 |
| castle_village_EW7_1 | Oristocorys | castle_village_EW7_1 | 俄耳堤西亚湾航路与酿酒葡萄 |
| castle_village_EW7_2 | Elvania | castle_village_EW7_2 | 海湾与向阳山坡的橄榄种植 |
| castle_village_EW8_1 | Gersegos | castle_village_EW8_1 | 银矿与其他贵金属开采 |
| castle_village_EW8_2 | Vathea | village_EW6_2 | 德律亚山脉深井铁矿 |

### C. 南部与东部边境（16条）

| settlement ID | 英文源名 | 描述文本键后缀 | 首轮主题 |
|---|---|---|---|
| castle_village_ES1_1 | Odrysa | castle_village_ES1_1 | 帝国东部边境、木材业与边境对手 |
| castle_village_ES1_2 | Caira | village_ES1_1 | 卡勒萨水网与卡勒萨河、蒂亚具斯河冲积平原的谷物 |
| castle_village_ES2_1 | Corenia | castle_village_ES2_1 | 卡拉德语使用范围边缘、粮食与边防观察 |
| castle_village_ES2_2 | Metachia | castle_village_ES2_2 | 边境帝国殖民地、桑树与丝业 |
| castle_village_ES3_1 | Melion | castle_village_ES3_1 | 桑蚕丝同时用于贵族服饰和游牧／边疆战士的箭矢防护 |
| castle_village_ES3_2 | Sagolina | castle_village_ES3_2 | 银矿与帝国长期征服、守卫东部高地的成本 |
| castle_village_ES4_1 | Lavenia | castle_village_ES4_1 | 渔业、城堡守卫卡勒萨通道、通往阿塞莱的交通 |
| castle_village_ES4_2 | Ethemisa | castle_village_ES4_2 | 卡勒萨河谷与谷物生产 |
| castle_village_ES5_1 | Morenia | castle_village_ES5_1 | 河岸黏土供应帝国南部陶窑 |
| castle_village_ES5_2 | Atphynia | village_ES2_1 | 塞堤斯河口盐田与三河谷地 |
| castle_village_ES6_1 | Sestadaim | castle_village_ES6_1 | 盐矿、矿工死亡记忆与秃鹫传说 |
| castle_village_ES6_2 | Amycon | village_ES6_3 | 牧羊、孜然调味的干咸奶酪 |
| castle_village_ES7_1 | Jogurys | castle_village_ES7_1 | 原游牧地近来转为耕种；帝国殖民者发展桑蚕业；缺少对应简中描述键 |
| castle_village_ES7_2 | Eunalica | village_ES7_3 | 塔奈西斯湖西岸低地亚麻；缺少对应简中描述键 |
| castle_village_ES8_1 | Chanopsis | castle_village_ES8_1 | 密泽亚德高原的谷物 |
| castle_village_ES8_2 | Popsia | village_ES4_2 | 松木采伐与销售；NavalDLC加入帕拉神话记忆 |

## 三、历史解释：村庄材料将帝国的资源网络具体化

### 1. 资源并不只是地志背景，有时直接连到国家需求

本组有若干明确连接：
- 托里俄斯与柏耳贡的谷物被写成供养帝国中部的大宗粮食来源，且SandBox文本强调河流灌溉和两地共同供给；NavalDLC改成两处各自位于特美亚谷地、依赖降雨与土壤肥力，删去了两村之间的共同供给关系。
- 伽伦托的沿海草甸被用于育马；奥尼卡生产在帝国范围内受欢迎的干型葡萄酒；伽伦戈利亚银矿在另一批城市关联村庄中被明确连接到铸造帝国第纳尔。结合本组格尔塞戈斯的贵金属、瓦西娅的铁矿和麦卡洛维亚的矿石，矿产、货币和军事资源的联系值得继续追踪。
- 墨利翁的桑蚕丝被描述为同时服务于宫廷服饰和边疆战士，后者将丝织品穿在铠甲下以增加对箭矢的防护。这是本组最清楚的跨社会层次物质文化线索：丝并非只有奢侈消费意义，也被赋予军事用途。
- 阿特里翁在NavalDLC中增加了由帝国贵族组成、资金充足的联合体修筑堤坝排干湿地并发展桑树的叙述。该版本把丝业生产与资本投入、土地改造和集体组织直接联系起来；SandBox没有这段内容，故不能无标注地把它当作稳定的跨版本史实。

### 2. 帝国边境是生产区、交通区和多语言接触区

伊勒坦运输线附近的埃皮诺萨与庞斯，在SandBox中主要呈现冰川湖之间的船只拖运、盐矿和畜牧；NavalDLC则将埃皮诺萨改写成多条河流汇合的贸易与冲突节点，并把庞斯的地名解释转为一座被洪水冲毁、后来由其他渡口替代的桥。两版共同指向北部水路的战略性，但对具体交通地理的描述并不一致。

东部的奥德律萨在SandBox中靠近蒂亚具斯河与库赛特领土，支撑小规模木材业；NavalDLC把它改写为靠近阿塞莱方向的卡勒萨关口，并增加多种语言的岩石涂写，包含征服者宣示和士兵乡愁。此变化把边境从单一邻国防线改写为多语言、反复接触和争夺的文化空间，不能当作一段真实历史中边境由库赛特方向“移动”到阿塞莱方向的证明。

科雷尼亚保存了卡拉德语使用范围的边缘：文本称越过阿克坎丘陵后主要使用达西语和草原语言，当地居民种粮并观察边境。阿厄里亚则在帝国腹地保留帕拉语词汇的方言记忆。二者一起说明，语言接触并不只存在于边疆，旧语言影响也可在腹地长期留下痕迹。

### 3. 地方社会的组织和政治记忆可以超出资源统计

阿加尔蒙的SandBox文本记载当地森林村民与斯特吉亚邻居长期通婚，战争爆发后关系紧张；NavalDLC将这段社会关系改为高地谷物生产。前者为跨境婚姻与战争影响提供了一个具体个案，但仅适用于SandBox版本。

戈勒林同时出现绵羊饲养与偷羊，说明生产与对资源的非正式攫取可以并存；拉文尼亚在NavalDLC中除捕鱼外，还记载居民可在商船、保护商船的帝国舰队和袭击商船的海盗之间从事海上工作。这表明边疆和海岸居民的经济角色可能跨越合法商业、国家军事服务和海盗活动，不能仅用“农民”或“渔民”一种身份概括。

赫托该亚在NavalDLC中增加温泉、地底蒸汽和帕拉先知预言帝国兴衰的传说。波普西亚也在NavalDLC中增加巨人兄弟与山岳起源神话。它们的历史价值主要是记录后来的地方记忆如何把自然地貌与帝国命运联系起来，而不是证明预言或神话事件真实发生。

## 四、SandBox与NavalDLC异文：不能作为历史阶段拼接

本组50条中，多项描述不仅改变地名或大小写，还改写生产活动、地方社会或文化记忆。最重要的异文如下：

| 对象 | SandBox v1.4.8 | NavalDLC v1.2.8 | 处理原则 |
|---|---|---|---|
| Varagos（castle_village_EN1_1） | 以绵羊饲养为主 | 改为桑树与蚕丝 | 经济活动替换，不写成产业转型 |
| Lochana（EN2_1） | 拉科尼斯湖岸的桑树与丝业 | 增加卡拉卡索斯河城堡、对岸埃皮诺萨及长期边防，保留丝业 | DLC增加防务结构，不反推SandBox缺乏边防史 |
| Atrion（EN5_1） | 涅维斯河谷种桑树 | 增加湿地排干、堤坝与帝国贵族联合体投资 | 新增土地改造和精英资本叙述，版本限定 |
| Ataconia（EN6_1） | 盐矿开采 | 改为橡树林和养猪 | 资源活动替换 |
| Epinosa（EN7_1）与Pons（EN7_2） | 伊勒坦湖网、船只拖运、牛群与盐矿 | 河流交汇、跨语言地名记忆、被洪水冲毁的桥与替代渡口 | 交通地理和命名记忆改写 |
| Tememos（EN8_2） | 林农采伐木材销往湖边城市 | 改为马匹季节性放牧 | 林业与马业叙述替换 |
| Agalmon（EN9_2） | 森林村庄、与斯特吉亚人通婚、战争令关系紧张 | 改为山地谷物生产 | 跨境社会关系被删除，不能把版本差异解释为关系恶化或消失 |
| Thractorae（EW4_1） | 帝国地主试验种植椰枣 | 改为橡树、猪群和橡实饲料 | 经济活动替换 |
| Gamardan（EW4_2） | 海湾金枪鱼捕捞 | 改为连接沙拉斯与阿米尼斯谷地城市的通道和葡萄酒贸易 | 渔业叙述被交通—贸易叙述替换 |
| Oristocorys（EW7_1） | 葡萄种植与航路气候 | 改为躲避蚊虫和南方海盗、出海捕捞大型鱼类 | 经济与安全叙述显著改写 |
| Elvania（EW7_2） | 橄榄种植 | 改为葡萄酒种植 | 产业替换 |
| Odrysa（ES1_1） | 帝国东部、库赛特方向与木材业 | 阿塞莱方向的卡勒萨关口、多语言岩刻与雪松木材业 | 地缘与文化接触叙述改变 |
| Caira（ES1_2） | 卡勒萨水网冲积平原种粮 | 强调达努斯提卡以东潮湿平原、居民守卫阿塞莱边境 | 增加居民的边防身份 |
| Metachia（ES2_2） | 和平时期建立的帝国边境殖民地、丝业桑树 | 保留殖民地和丝业，改写为湖岸平原向密泽亚德山脊过渡 | 经济与殖民记忆稳定，空间表述不同 |
| Sagolina（ES3_2） | 银矿解释帝国征服和守卫东部土地的成本 | 改为采盐 | 矿产种类与历史解释变化，不能合并 |
| Lavenia（ES4_1） | 渔村，邻近城堡守卫卡勒萨通往阿塞莱的通道 | 捕鱼、商船运输、帝国护航舰队与海盗袭击 | 海上职业和安全关系扩展 |
| Ethemisa（ES4_2） | 卡勒萨河的多语言命名与谷物生产 | 早期迁居者、井灌、隐士和山羊传说 | 生产地志被定居与宗教记忆叙述替换 |
| Atphynia（ES5_2） | 塞堤斯河口盐田 | 山谷盐沉积、贝壳与地质传说 | 盐业延续但地貌解释改变 |
| Popsia（ES8_2） | 松木采伐与出售 | 增加帕拉神话中的巨人兄弟和塔尔尼亚山起源 | 生产记述外加地方神话，不能把神话作为同期事件 |
| Hertogea（EW6_1） | 橄榄与芳香油 | 保留橄榄，增加温泉、地底蒸汽和预言帝国兴衰的帕拉先知 | 地方记忆扩展，版本限定 |

其余异文多涉及河流、山脉、方位、谷地名称或生产背景的重写；在实际写作中仍应保留版本标签。不同文本的差异是开发文本的异文，不是游戏世界内部历史阶段的证据。

## 五、可检验的历史问题与竞争解释

1. **帝国生产网络究竟多大程度被国家直接组织？**  
   支持国家联系的材料包括中央帝国粮食供给、军马、帝国殖民地丝业、贵族资金参与土地排水、银矿解释征服与防务成本。竞争解释是多数村庄只描述地方生产，国家联系只是少数被特别点出的例子。下一步应统计117条中的明确目的地、明确国家用途、明确投资主体和仅有资源描述四类，而不是把它们全部称为中央计划经济。

2. **边境居民如何在多种政治秩序之间生活？**  
   埃皮诺萨、庞斯、奥德律萨、科雷尼亚、拉文尼亚等文本将交通、守边、语言、贸易与海上军事服务结合起来。竞争解释是这些内容分散在不同版本和不同村庄中，尚不足以构造统一边境制度。下一步要与对应城镇地志、领主自述和其他文化一侧的边疆记录交叉验证。

3. **旧语言、族群通婚和地名记忆是否意味着整合不彻底？**  
   腹地阿厄里亚的帕拉语词汇、科雷尼亚的卡拉德语边界、SandBox阿加尔蒙的跨境通婚和高地Gaos的游牧词源，都显示帝国统治下仍可见多层文化记忆。竞争解释是地志刻意选取异质风俗来增加地方特色，不能据此估计语言人口比例。需要更多同地区文本和跨文化对照。

4. **资源能否解释帝国对特定地区的长期投入？**  
   Sagolina的银矿与征服、守卫成本之间有直接叙述联系；铁矿、银矿、马业和丝业在其他记录中也反复出现。竞争解释是这些是地志作者对地理价值的回顾性解释，缺乏财政账册、产量、军费和时间序列，尚不能量化资源对政治决策的因果权重。

## 六、阶段结论

本批50条castle_village记录把帝国史的观察范围从城市和城镇关联村庄延伸到城堡领地的生产与边疆社会。它们显示，帝国文化标签之下同时存在粮食、畜牧、马业、丝业、葡萄酒、橄榄、盐、铁、银、木材、渔业和陶业原料；还保存语言残留、通婚、殖民、土地改造、海上职业、边境守望和地方神话。它们既不是单纯的“资源清单”，也不是一套统一中央制度的直接证明。

本批最稳妥的判断是：**帝国的地方社会以多种生产方式、交通条件和身份关系支撑更大范围的政治秩序，但这种支撑在各地并不均质，且官方地志版本之间会重新分配经济活动和文化记忆。** 这是一项可被后续样本修正的C级工作模型。

工作包A的归档样本已完成第一轮读取：19条城市、47条普通村庄、50条城堡附属村庄及1条非历史性地点说明。下一步应将这116条历史叙述纳入统一的源级分类表，并对跨文化的旧帝国城镇和边疆地点作回检；随后再推进工作包B的跨区域经济网络专题。
