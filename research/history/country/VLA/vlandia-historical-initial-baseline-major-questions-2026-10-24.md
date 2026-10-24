# 瓦兰迪亚历史初步摸底与重大研究问题
**CHC-VLA-GEN｜首轮国别调查稿 v0.7（原始模块源级复核）｜2026-10-24｜未分配 H 编号｜状态：文化／王国／德泰尔传记及氏族中英键源级已核，其他场景持续待核**

## 摘要
瓦兰迪亚政治共同体的起点不是1084年的现成王国，也不是单一民族举国迁徙。官方文化史述追忆跨海而来、操多种语言的军事雇佣者与冒险家；帝国财政官员以土地、头衔代替现金报酬，军人定居、通婚、耕作，并据有附近帝国堡垒。地方志又记录若干并不从军饷制度产生的过程：奥斯蒂港的航海者与早期瓦兰迪亚定居，罗瓦尔地区瓦兰迪亚入侵前已占人口优势的诺德移民，萨哥特一带参加瓦兰迪亚征服的马萨（Massa；官中地志 town_V1 有“马萨语／马萨人”）盟部。王国沿革则将奥斯里克夺取帝国西部海岸、帝国为求和平承认王位、国王封认部属的男爵与伯爵及其战时效忠联系在一起。由此本稿暂择“帝国—边疆互动中的自主国家形成”为首选解释：帝国提供军事收入、土地权利和可侵占的城堡，跨海移民、地方生产和军事组织则赋予新共同体独立发展的能力；帝国继承及外交危机改变其合法性处境，但不自动制造这一社会基础。各环节未获独立编年记录，不得压成单一战争年份或从1084年边界倒推早期版图。

**中心历史问题：**原本凭借帝国薪银服务的海外武装，何以能够支配土地与农民、组织地方武力、谈判帝国承认并建立存在君臣契约和地区冲突的王权？

## 一、史料性质、边界与已有研究
本调查继承 I-0001 v1.4、I-0004 v2.2、I-0003 v3.13、I-0002 v3.42、Q-0013 v0.4 和《全大陆史料覆盖摸底与历史问题图谱》v0.1；分类为 CHC-VLA-GEN，成熟政治史专题可另归 CHC-VLA-POL，但不预占 H 号，不修改公共 S/E/P/D 登记。

**本轮实见：**（新增 e）用户在2026-10-24提供《游戏百科中文文本（简体中文）》encyclopedia-zh-cn.md：声明游戏版本 v1.4.8.119303，中文聚落名以 Native/CNs/std_common_strings_xml、王国及地志中文以 SandBox/CNs std_spkingdoms_xml/std_settlements_xml 由解析器逐键得出；覆盖53座城镇、141个村庄、8个王国，但不含城堡及 castle_village 型村落。该文件是本轮直接阅读的**有来源和版本声明的整理汇编**，不能混同于本轮直接取得原始 XML 字节。（a）TaleWorlds 2017-11-30 官方英文《Vlandia》原文；（b）标为游戏 vanilla 1.4.8 的 BannerlordDB 对 SandBoxCore 文化简介及 SandBox 聚落文本的公开数据呈现；（c）网络展示的一段 SandBox/spkingdoms.xml 英文文本，含王国 vlandia 键 IudGLWQZ；（d）项目 GitHub 的方法、登记和既有研究，以及 Google Drive 的全大陆摸底、Q-0012、CHC 法和《潘德拉克》工作稿。**历次版本史料获取记录：**v0.1—v0.5 时本对话未获得原始 ZIP，只能使用整理汇编和镜像；至 v0.6 已从用户 Library 的《Calradia Geography Research Source Files》取得 Native、SandBox、SandBoxCore、StoryMode、NavalDLC 五个原始 ZIP，并已逐键核验本篇核心文化、王国、德泰尔人物、贵族氏族及部分DLC对白；尚未完成全部 XML 系统审计。

证据标识：**A-直陈**＝所核文本明确这样记述（不保证传说/政治主张客观真实）；**A-镜像待核**＝出现于公开游戏数据转录，尚待原始XML同键核对；**B**＝受直接表述支持的相对次序；**C**＝比较后暂采的历史解释；**未知**＝尚不能断定。2017年开发者介绍和游戏文化文本具有共同叙事来源，不能统计为两个独立证人；游戏英文与中文译文亦非独立证人。开发者文中“built fortresses”，游戏文化文中“seized nearby imperial fortresses as their own”表明军事行动的不同表述，须作异文记录，不得默默拼合。2017年写“Osrac Iron-arm”，游戏王国沿革转录写“Osric Iron-Arm”，暂作同一人物异写的较强推定，而非建立两任开国国王。

已有 H-0001 研究沙拉斯、巴拉维诺斯等**卡拉德早期殖民史**，不可改称瓦兰迪亚上古史；H-0005 使用 S-0020 仅为后期军费与地方化案例，不证明共和国初期制度；I-0003 已登记 S-0020、E-0014、P-0031，不应为此复建全局编码；潘德拉克跨国战役由 CHC-CAL-MIL 独立稿统摄。

## 二、可以成立的相对年代
1. **瓦兰迪亚王国成立之前的西方多重人口史。**罗瓦尔（Rovalt/Rovalatys）地志称瓦兰迪亚入侵以前，因银矿传闻和皮毛资源而来之诺德移民已超过当地卡拉德人口；此地并未充分成为帝国城市。奥斯蒂港（Ostican）本为小帝国港，北方海员、曾受帝国不同派系雇用的海盗型船员活动于此，一些最早抵达海岸的瓦兰迪亚人在港区定居。上述前入侵移居并非都能排进同一顺序。[V5][V6]
2. **海外军事输入及名称形成。**文化简介称最初的瓦兰迪亚人来自海外，操多地语言，以护卫帝国边疆换取银币；共同名号追溯至 “无畏的”维伦德（Wilund the Bold；卡拉德语瓦兰狄翁，Valandion）。不可据此断言所有来者原属一个部族或仅沿同一登陆口岸迁徙。[V1][V2]
3. **军饷向土地/头衔补偿转变。**官方叙述以帝国财政不足解释支付替代。此时瓦兰迪亚军人的活动并不局限于今日西部疆界；早期军事服务的地理范围甚至指向阿塞莱沙漠至草原。财政原因是史述给出的解释，而非存在可审计的国库账本。[V1][V2]
4. **定居、通婚、生产与军事据点取得。**文化简介直陈婚姻、耕作及帝国堡垒占取；萨哥特城志又叙述马萨（Massa）部落作为瓦兰迪亚同盟参加入侵、瓦兰迪亚人在帝国旧城废墟上重建聚落；说明发展中存在多部落联盟、武力占取和对先住社群记忆的取代，不限于和平授地。[V2][V7]
5. **奥斯里克建国及对外承认。**2017年官方文章把他在一次未定年的“recent interregnum”中称王、夺取旧帝国西部都邑 Baravenos 和海岸地带相连；游戏王国沿革 IudGLWQZ 英文转录称他夺取西岸后获诸皇帝“as the price of peace”承认为王；同版中文汇编直接作“作为议和的代价，帝国被迫承认他为国王”。以文本当前最优解释，**实际夺地/称王先于帝国承认**；是否一次承认、由哪位皇帝、条约形式不明。对外承认不是对其既有军事征服的否认，也不是中央依旧能实际统辖新王国的证据。[V1][V3]
6. **王权与封臣契约演变。**王国沿革把奥斯里克对追随者土地宗主权的认可、封为 barons/counts，同其战时向王旗下集结的义务相联系；又追述后来君王与贵族在中央权力扩大和地方私斗容忍之间摇摆。德泰尔传记呈现晚期国王频繁调停封臣土地纠纷、平乱与应付觊觎王位者。以上显示从领军首领到受约束国王的政治演化，但完整领地法和领主继承制度不可据此补造。[V3][V4]
7. **潘德拉克及1084年前后的王国政治。**既有 CHC-CAL-MIL 工作稿现以 v1.4.5 反编译代码恢复的德泰尔、因加泰尔、恩泰里答话为 A2 文本；项目 v1.4.8.119303 的逐字核验仍待完成。不得把人物对白中的日期、战役细节与条约主张直接提升为 A1 级客观事实。德泰尔调解男爵、强王期待与军事扩张诉求的冲突可作为较稳固的后期王国结构线索。[V4][V9]

不能推出的年代：维伦德与奥斯里克之间的代数、定居究竟始于哪位帝王、北方商业迁徙与南方授地在何年并行、Baravenos夺取的绝对年份、王位承认和封臣称号颁授的具体日期；1084年领地图和现有氏族头衔不能填补这些空白。

## 三、国家形成的六项机制

### 3.1 军事雇佣：帝国边防需求与海外集团能力
雇佣使流动武装获得工资、战斗声誉、帝国内部行动通道；“speaking the tongues of many lands”及 维伦德（Wilund）／瓦兰狄翁（Valandion）双名暗示共同身份更可能在军事领导与对外交往中形成，而非事先统一。帝国主动创造机会，不等于单方面发明这个军事社会。军队规模、战术编组、各雇佣领袖彼此关系均未知。【A-直陈、C】

### 3.2 土地化：一次酬佣还是治理权转移？
“land grants and titles instead of silver”是关键机制：固定土地收益可能替代不稳定军饷，使军人供养家庭和长期驻军；头衔又可能赋予地位和争取服从的语言。可是受封的对象、土地处分权、赋税、司法、农民人身义务尚无记载；更不能把“授地”自动译成一套完备的世袭封建法。游戏文化介绍的“seized ... fortresses”反而提出**合法受封与后续武装侵占的边界**。应进一步查城堡历史辨别究竟哪些堡垒曾被授予，哪些是私占。【A-直陈、C】

### 3.3 征服联盟与人群整合
萨哥特地方志明确称马萨部落为参加瓦兰迪亚入侵的盟部。奥斯蒂港海员、罗瓦尔既有诺德居民与卡琉斯（Caleus，castle_village_V6_1；城堡中文通称“卡琉斯堡”，独立名称键待核）瓦兰迪亚/斯特吉亚/巴旦尼亚混合语言村民，表明王国居民绝不宜想象成一支最初的单族雇佣军后裔。瓦兰迪亚认同可能是随统治、婚姻、军功及土地实践扩大的政治文化共同体，具体同化途径仍待人物谱系和非贵族叙事检验。【A-镜像待核、C】

### 3.4 君臣秩序：两层承认与武力提供
王国沿革揭示两种性质不同的承认：帝国皇帝为了和平认可奥斯里克王位；奥斯里克认可追随者对土地的宗主权，以换取其战时集合。国王不能仅靠单一征服者私人强力长期统治；必须将军人首领变成各自有地盘、能够集结军力的领主。这样的安排既建立王权动员机制，也可能使地方男爵保留相当的谈判能力。【A-镜像待核、C】
德泰尔传记所述裁断领地之争，是王权依赖调停而非自动支配所有贵族的证据；1084年王国并非完成中央化的单一行政机器。【A-镜像待核、C】

### 3.5 土地、常民与区域经济
罗瓦尔早于瓦兰迪亚入侵的诺德探银与皮毛生计、奥斯蒂港海港及私掠活动，表明贸易与海洋生计并非授地制度附属品。阿利斯维斯特（Halisvust；village_V9_2）记瓦兰迪亚移民排干沼泽、播种小麦黑麦，表明移民可通过水土工程扩张可耕地。Ormanfard（中文名称未被本次汇编覆盖）的葡萄梯田及富人与常民饮酒差异揭示商品农业和消费等级；卡琉斯村（Caleus；村庄名称键待核）种亚麻，勒芒塔尔（Remental；village_V8_3）猎取皮毛并吸引希望远离南方男爵重压的迁入者。这里呈现北部山林相对宽松与南部领主支配较强的**地方记述中的差异**，但不能直接推出“瓦兰迪亚全国农民都是农奴”或制成完整的贵族—骑士—农奴固定金字塔。【A-镜像待核、C】

### 3.6 战争外交：对帝国、巴旦尼亚、斯特吉亚的不同关系
对帝国至少存在由受雇协力、赋地受封、私占/夺取到条约式承认、后来复杂同盟的多阶段关系，并非从首次入境起始终为敌。巴旦尼亚官方文化介绍把新兴瓦兰迪亚与斯特吉亚王国并列为更近时的征服/抵抗者；但“原住民”或“unsubdued tribes”均带有叙述立场。萨哥特马萨盟部及先住帝国废城把战争呈现为多方争夺，而非只是帝国—瓦兰迪亚两国战争。斯特吉亚方面可由北部混合语言、诺德移民与潘德拉克多方联盟观察联系；尚不能从文化混居直接推导某年签约或宣战。潘德拉克外交尤其需与共享战役档案分工处理。【A-镜像待核、C；部分潘德拉克待源级验证】

## 四、证据覆盖：已知／推论／未知

| 历史领域 | 已见直接叙述 | 当前较强推论 | 尚待证明 |
| --- | --- | --- | --- |
| 跨海来源与认同 | 多语佣兵、维伦德（Wilund）名号、港区早期移居 | 军事共同行动先于完整“民族”认同 | 迁出地、人口规模、统一语言出现年代 |
| 军役与财政 | 帝国付银；以土地与头衔替代 | 付酬形式变化提高部分军人的地方独立能力 | 国库数据、契约、授地地点及日期 |
| 领土取得 | 堡垒占据；萨哥特重建、海岸夺取 | 授予、侵占、征服是不同路径 | 逐堡垒地权链、原居民命运 |
| 王权与领主 | 和平承认王位；国王认领主土地并要求战时集结 | 双层承认构建协商性王权 | 条约、法定继承、税权及司法 |
| 生产与常民 | 排水耕田、葡萄农业、皮毛、矿业、地方语混合 | 区域经济在王国形成中拥有独立机制 | 赋税、劳役、人口结构、地租 |
| 城市和海洋 | 帝国旧港、航海者、先瓦兰迪亚城市生活 | 海港和北方资源吸引的移民流可能早于征服 | 航线、关税、船队、港务控制 |
| 对外战争与外交 | 帝国关系转变，巴旦尼亚/斯特吉亚抵抗，后期联军叙述 | 对外战事强化但未必创造既有贵族政治 | 战役和外交确年、誓约有效条款 |
| 地区家族与王权 | 德泰尔调停诸男爵、王位竞争及叛乱 | 地方势力与王权长期互相约束 | 家族地域集团边界及连续谱系 |

## 五、三种竞争解释及其权重
**甲：帝国财政衰弱决定论。**优点是文本确实将欠缺银币、以土地和头衔代薪列为转变前提，并以帝国政治空档解释君位宣布。弱点是无法独立说明为何这些佣兵能组织入侵、取得军政协调，也解释不了罗瓦尔瓦兰迪亚入侵前的诺德移民和奥斯蒂港海洋经济；把受封地视作完整建国充分条件，则缺必要中介。

**乙：海外军事文化自主国家形成论。**优点是解释跨海组织、战时联盟、马萨盟部、港市移居和军事首领权威。弱点是忽视帝国给出的现金、土地与头衔以及帝国后来以和平交换承认王位；它不能把帝国的制度和资源仅当“背景”。

**丙：帝国—边疆互动及地方资源转换论（本轮首选，C）。**帝国边防市场先使武装集团获得物资和合法活动空间；现金改授地扩大定居可能，入侵和城市夺取又把非正式军事权力转化为地方控制；奥斯里克的建国还需帝国外交承认与封臣领地承认，才能维持更长时段王权。罗瓦尔、奥斯蒂港和马萨史例说明另一批并非由帝国授地生成的自主动力。其弱点在于阶段中介主要来自同一官方叙事传统与散在地方志，缺完整同年、同一批行动者的证据链。

**可能推翻首选模型的观测至少两类：**
1. 若更多有效英文原文显示首批瓦兰迪亚的城堡、农庄、地方头衔和私军几乎全在帝国授地以前形成，并能独立维持，其国家形成应更多归因自主移民政治；帝国财政转型不是关键中介。
2. 若土地契约、人物传记或地方志反而显示奥斯里克政权主要依靠帝国派驻军政体系、授任官职和受认可的地方元老，而瓦兰迪亚军事集团尚不具独立地区征募与财力，则自主形成的权重应明显下降。
3. 若“recognised ... as the price of peace”经官方原始XML核查为旧版废弃、评论/模组替换或不同指代，王权双层认可模型须相应撤回或降级。不能用单份网络镜像强行解决国家主权合法性争议。

## 六、十个重大研究问题（按解释价值排列）
**VLA-RQ01／最高优先｜身份形成：**海外操多语的集团是在受雇前已经认同“瓦兰迪亚”，还是在 维伦德（Wilund）的军事首领名号、雇佣关系、共同定居后才获得外界与内部一致名称？有何非贵族语言或通婚证据？

**VLA-RQ02／最高优先｜土地与军权：**现金报酬改为土地与头衔后，获得的是耕地收益、军事屯田、封臣法权还是私人领地？如何区分帝国合法授予与后续占取堡垒？

**VLA-RQ03／最高优先｜双重承认：**奥斯里克成为“国王”与帝国将他承认为王是否属于两个时点？“price of peace”是对已有独立事实的承认，还是一次维系形式宗主关系的外交安排？如何核对 Osrac/Osric 与 Baravenos/Paravenos 异写？

**VLA-RQ04／较高｜军事社会转型：**农业定居如何养活武装，领地收益如何改写追随者的动员义务？王国初期军人首领是否先享有独立征募权，再被奥斯里克确认？

**VLA-RQ05／较高｜移民多源：**马萨盟部、北方诺德移民、奥斯蒂港海员与早期瓦兰迪亚军人，是互相重合的人群还是不同历史波次？哪种通婚、贸易和政治认同促成联合？

**VLA-RQ06／较高｜城市先于国家：**奥斯蒂港帝国海港和罗瓦尔非充分帝国化城市为何能成为后来的王国地区节点？城镇既有税市和贸易网络能否比帝国授地更好解释长期国力？

**VLA-RQ07／较高｜国王与男爵：**王国“granting ... suzerainty ... in exchange for ... war”实际规定哪些权利？王权是否主要依赖战时动员、仲裁、领地分配，而缺乏直接日常行政？

**VLA-RQ08／较高｜地区与常民：**瑞门托尔“男爵控制较轻”的北方与南部领主支配之差，是否源于地形、移民流、市场、传统法还是行政覆盖不足？对佃农和自由人的身份能有何直接证明？

**VLA-RQ09／较高｜外交与战役：**瓦兰迪亚与帝国关系从受雇到承认、再到潘德拉克战前誓约及逆盟，究竟发生了哪些法律和联盟变化？德泰尔与诸男爵的不同意见对王权征兵意味着什么？须等待 StoryMode 有效对白。

**VLA-RQ10／较高｜跨国关系与时序：**瓦兰迪亚同巴旦尼亚、斯特吉亚交战是否为持续边境活动、周期性同盟或不同区域的两套政治过程？是否能由混合语村庄、城镇易手记录与跨国婚姻找出独立纪年锚？

## 七、对协调对话的跨国接口（建议登记、不代替统一裁定）
1. **VLA–EMP：王权外交承认与帝国继承空档。**需对齐 SandBox/spkingdoms.xml vlandia/IudGLWQZ、SandBoxCore/spcultures.xml vlandia/1Ww5lg6I 和2017官方《Vlandia》的版本。先保留奥斯里克主动称王、帝国以和平为代价承认的并存模型；其时段不与1084年帝国内战、1077年潘德拉克自动同年。H-0005已收录 S-0020，请协调线视复核情况考虑 I-0003 的新争议登记，不自行占号。
2. **VLA–BAT：马萨、巴旦尼亚古老居民与瓦兰迪亚入侵。**Sargot 地志对“盟部留下创伤并取代旧城记忆”的叙述，须与 Battania 自述“original inhabitants”和后起王国侵袭比较；不可因现属于Vlandia便视为古瓦兰迪亚原生领土。
3. **VLA–STU/NOR：北方海员、诺德移民与混合语村庄。**Rovalt、Ostican、Caleus 和 Deriat 作为贸易、迁入及语言接触样本，不将诺德／斯特吉亚社群吸收入瓦兰迪亚单一源流。
4. **VLA–CHC-CAL-MIL：潘德拉克。**本线研究德泰尔与男爵的条约解释/战后内政；对战术、地点、先后顺序及1077纪年，引用共用战役工作稿并注明 StoryMode 缺件，不重写战役史或占有他线档案。

## 八、下一轮源级核查的三项关键任务
1. 取得实际官方 SandBoxCore/spcultures.xml（vlandia 键1Ww5lg6I）、SandBox/spkingdoms.xml（vlandia 键 IudGLWQZ）和版本对应英文/简中表，逐字校核 land grants / seized fortresses / recognised / suzerainty / barons / counts 的原始语义；补查 NavalDLC 有效同类文本及替换顺序。
2. 【第一轮已完成，见独立异文审计】逐 ID 比较 SandBox 与 NavalDLC 的瓦兰迪亚聚落坐标、英文描述和简中键；52个共同ID坐标均变化，35条英文描述不同，且存在简中译文滞后。仍待用完整运行时资料确认模块加载/覆盖顺序及当前版本显示结果。
3. 直接核对 SandBox/heroes.xml 的 Derthert（lord_4_1）、spclans.xml 的 dey Meroc（clan_vlandia_1）及其他具有背景正文的瓦兰迪亚氏族，并取得 StoryMode 潘德拉克有效人物对白；区分国王政治经历的传记叙述与受访者的自利辩护。

## 附录A：可追溯材料与史料限制
[V1] TaleWorlds，《Vlandia》，2017-11-30，https://www.taleworlds.com/en/News/199；官方发布但属早期回顾，提到 Wilund/Valandion、Osrac、Baravenos、帝国支付军饷与土地、授封、定居、建堡、独立。
[V2] SandBoxCore/ModuleData/spcultures.xml，Culture vlandia，项目旧调查键 **1Ww5lg6I**；本轮网页镜像 https://bannerlorddb.com/encyclopedia/culture/vlandia（声称 vanilla 1.4.8，未直接核对本机 XML）。关键异文：“seized nearby imperial fortresses as their own”；未在此条独立证实 Osric 与帝国和平承认。
[V3] SandBox/ModuleData/spkingdoms.xml，Kingdom vlandia，网页可见 XML 文本键 **IudGLWQZ**，https://pastecode.io/s/u1p27b7k（第三方转录，模块/版本与有效性待官方原件核验）。王权源于 Osric Iron-Arm，帝国诸皇帝为求和平认可王位；男爵/伯爵对地权认可及战时集结，继承君主强权与容忍地方纷争间摇摆。此条为本轮新增加的关键待核镜像线索，不冒称直接读取原始ZIP。
[V4] SandBox/heroes.xml lord_4_1、SandBox/spclans.xml clan_vlandia_1，德泰尔维系男爵与候位者、倾向仲裁的背景叙述；本轮见于公开文本转录 https://huggingface.co/datasets/TSEOsiris/bannerlord-lore-dataset/viewer/default/train?p=22 ，及 https://mountandblade.fandom.com/wiki/Derthert （后者混有玩家编纂内容，仅将与来源键相符的传记用作待核，非独立官方证据）。
[V5] SandBox/settlements.xml，Rovalt/Rovalatys，第三方呈现 https://bannerlorddb.com/encyclopedia/settlement/rovalt；早于瓦兰迪亚入侵的诺德移民、探银与皮毛生计、后续谷地农耕及人口流入。
[V6] 同模块，Ostican，https://bannerlorddb.com/encyclopedia/settlement/ostican；帝国港、北海航海人、参与帝国内战的私掠人员与早期瓦兰迪亚港区定居。
[V7] 同模块，Sargot，https://bannerlorddb.com/encyclopedia/settlement/sargot；Massa 盟部、入侵、帝国旧城废墟及瓦兰迪亚重建。
[V8] 同模块，Caleus https://bannerlorddb.com/encyclopedia/settlement/caleus；Remental https://bannerlorddb.com/encyclopedia/settlement/remental；Halisvust https://bannerlorddb.com/encyclopedia/settlement/halisvust；Ormanfard https://bannerlorddb.com/encyclopedia/settlement/ormanfard；皆为原文镜像，尚待本项目版本XML逐键验证。
[V9] 项目 CHC-CAL-MIL 独立潘德拉克战役工作稿，GitHub https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/03/Pendraic-Battle-Research-Working-Draft.md；Google Docs https://docs.google.com/document/d/1hc4HEGsIcvZ-y3sAwSlxAg-08yFbcUk4xA0hujGnDoM/edit；德泰尔、因加泰尔、恩泰里证词现有 A2 级反编译文本可查；它不是本项目 v1.4.8 生效 XML，版本匹配仍待核。
[V10] 项目《全大陆史料覆盖摸底与历史问题图谱》v0.1，GitHub https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/00/continental-historical-baseline-question-atlas-2026-10-23.md；此报告支撑资料库覆盖及缺件陈述，不作为瓦兰迪亚事件的独立证人。
[V11] I-0003 S-0020/E-0014/P-0031，与本报告相同的官方叙事传统： https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/00/1v52GmJ6BmyRUwUJjpLG3PalEKC9aBLaKYTqUHn3ZopI.md ；不重复立编号。
[V12] Battania 文化简介英文镜像，https://bannerlorddb.com/encyclopedia/culture/battania；关于帝国及后来的斯特吉亚、瓦兰迪亚战争叙述，属同一世界观文本系统的不同族群叙事。

**二创排除：**不得把《Bannerlord Immersion Project》改写的 Angevin/Valeric/Baldric 三国、毒杀及追加王位年表，或玩家“Filling in the Gaps”的确切年号纳入官方史实。Fandom 页面上混入的战术、亲缘与头衔推断只作为源文回查线索。

**版本与归档说明：**本文件为专属国别首轮研究；不更动其他国家研究稿、中央方法、I-0002／I-0003 或共同潘德拉克档案，不宣称完整国别通史、不声称三模块原始包本轮已逐键实读。

## 附录B：官方简体中文汇编的聚落与王国专名校勘（v0.4，2026-10-24）
**新材料性质：**用户提供 `encyclopedia-zh-cn.md`（题为《游戏百科中文文本（简体中文）》），其卷首明确声称按 Bannerlord v1.4.8.119303 的 `SandBox/ModuleData/settlements.xml` 和 `SandBox/ModuleData/spkingdoms.xml` 抽取背景，使用 `SandBox/CNs/std_settlements_xml`、`std_spkingdoms_xml` 解码中文正文，再由 `Native/CNs/std_common_strings_xml` 解码聚落**名称**。本轮确实读取了这份汇编，而非通过外部中文百科猜译。它所声明的来源可用于已覆盖条目的版本化名称核对，但本轮**未取得其声称的原始 XML 字节**，不能声称已独立重跑解析。

### B1. 聚落名：按汇编原样采用
| 对象及 ID | 中文名（汇编原文） | 来源覆盖/备注 |
| --- | --- | --- |
| Sargot，town_V1 | 萨哥特 | 官中名称；地志亦明确“马萨语”“马萨人” |
| Ocs Hall，town_V2 | 奥克斯·霍尔 | 官中名称 |
| Pravend，town_V3 | 帕拉汶德 | 官中名称；历史地志称古城“巴拉维诺斯” |
| Galend，town_V5 | 加伦 | 官中名称 |
| Jaculan，town_V6 | **杰屈朗** | 官中名称；纠正先前未经核实的“贾库兰” |
| Charas，town_V7 | 沙拉斯 | 官中名称 |
| Ostican，town_V8 | **奥斯蒂港** | 官中名称；不是“奥斯蒂坎” |
| Rovalt，town_V9 | **罗瓦尔** | 官中名称；不是“罗瓦尔特” |
| Remental，village_V8_3 | **勒芒塔尔** | 山地皮毛、较轻男爵统治等地志描述逐一吻合；纠正“雷门塔尔”“瑞门托尔” |
| Halisvust，village_V9_2 | **阿利斯维斯特** | 沼泽排水、小麦和黑麦等地志描述逐一吻合；纠正“哈利斯伏斯特”“哈利斯武斯特” |
| Calioc，village_V1_1 | **卡利奥克** | 平原、埃皮尔丘陵和比斯坎山间、低湿地种亚麻；**绝非 Caleus** |

### B2. Caleus 和 Ormanfard 的特殊排除
这份汇编的明示范围是53城、141村、8王国，**不含城堡**；聚落列表只有 `town_*` 与 `village_*`，没有 `castle_village_*` 条目。卡琉斯（Caleus）的英文地志对应 `castle_village_V6_1`，村民混用瓦兰迪亚、斯特吉亚、巴旦尼亚语言；其英文地志在独立网络镜像可见，但本中文汇编**没有 Caleus 条目**。因此不能从“卡利奥克（Calioc）”推成 Caleus 的译名，更不能将“卡留斯”或“卡莱乌斯”宣称官译；正文保留 `卡琉斯（Caleus；独立中文名称键待核）`。Ormanfard 的葡萄农业材料同样来自城堡辖属村庄的英文镜像，本汇编无法裁决其中文名；暂用英文名。

### B3. 人物称号、语义与异译不得自行抹平
同一中文汇编 `vlandia` 王国沿革写**“铁臂”奥斯里克**，`town_V3`、`town_V5` 城市沿革则写**“铁壁”奥斯里克**。这是**同版官中材料内部的译名差异**，不应以个人惯用译法修改原引文。该王国沿革中文还直接记：“作为议和的代价，帝国被迫承认他为国王”，以及“分封自己的副官们为男爵和伯爵”，因此本报告关于王权的论述现在有同版中文汇编的对应记载可查，但英文措辞的独立源校仍须继续。

**此前 v0.2/v0.3 专名勘误结果：**“卡留斯”为未经核实的误认，“卡莱乌斯”为研究音译；对 Caleus 都没有获得该版官中名称证据。“马萨”一词已在萨哥特中文地志明确出现，不应再写成研究暂译。此前“瑞门托尔”“哈利斯武斯特”与“贾库兰”的官译身份一并撤回，改依上表名称。其他没有出现在该卷的城堡、城堡村庄、人物及氏族名不因本次校勘获得官译确认。

### B4. 文件保管和外部校验链
本材料原件由用户在本轮会话上传，文件名 `encyclopedia-zh-cn.md`。报告只引用已提取的相应名称、对象 ID、史料语义和版本声明；**不将上传的整份整理文本擅自复制到公共 GitHub**。现存公开英文复核点：Caleus <https://bannerlorddb.com/encyclopedia/settlement/caleus>；Remental <https://bannerlorddb.com/encyclopedia/settlement/remental>；Halisvust <https://bannerlorddb.com/encyclopedia/settlement/halisvust>。相同对象可互校内容，但语言文件和英文描述仍属同一官方游戏语料谱系，不是独立历史证人。


### B5. 卡琉斯（Caleus）的中文名称：二手中文证据互校（v0.5）
**采用主名：卡琉斯（Caleus），城堡称卡琉斯堡（Caleus Castle）。**现可检出多个2022—2024年的简体中文《骑马与砍杀Ⅱ：霸主》独立使用实例：2022-08-28 B站“骑马与塔防：卡琉斯堡” <https://www.bilibili.com/video/BV1Qd4y1A7ZV/>；2022-10-27 3DM《后期什么城镇繁荣度高》列表“卡琉斯堡” <https://www.3dmgame.com/gl/3862646.html>；2024-03-26 B站游玩系列目录“卡琉斯堡” <https://www.bilibili.com/video/BV1bC411t7SU/>。因此此前称“卡琉斯无依据”已经不成立，且卡琉斯确比误写“卡留斯”具有明显的外部使用证据。
**对象的英中配准：**BannerlordDB <https://bannerlorddb.com/encyclopedia/settlement/caleus> 与 Mount & Blade Wiki <https://mountandblade.fandom.com/wiki/Caleus_Castle> 同指 Caleus Castle 下有 Caleus 与 Deriat 两座村庄；村庄 Caleus 的英文地志述海湾南侧、混合语言和亚麻；不要与城镇萨哥特属村 Calioc（本次已核为**卡利奥克**）混同。
**异译：**另有2022年中文游戏专栏“卡勒乌斯堡” <https://www.bilibili.com/read/cv16486742/>，是确实存在的传播异写；保留但不作为本文主名。
**证据等级与未完事项：**以上是跨年份中文游戏使用记录及英文对象归属的吻合，支持“卡琉斯”作为**有据中文通称/研究主名**；并不等同于直接读取官方游戏 `Native/CNs/std_common_strings_xml` 中 **Caleus Castle** 和 **Caleus** 名称 token 的原始字串。所附 `encyclopedia-zh-cn.md` 不含城堡及 `castle_village` 型条目，因此也不能凭它认证“卡琉斯”在 v1.4.8.119303 的独立官方名称键。进一步核证目标是该版本城堡与城堡辖村 name key、中文语言串，并记录其他游戏版本是否有变化。


## 后续研究专题索引（2026-10-24）
首轮总摸底继续作为 VLA 线的背景与问题索引，不再把全部城市和社会史研究内容堆入本文件。另立独立专题《西部征服、城市接收与地方权力形成：瓦兰迪亚的非均质建国过程》v0.1，对已取得的 v1.4.8.119303 中文百科八座瓦兰迪亚城市及相关村庄地志进行逐项分析，形成地方政体接收类型、地区经济、领主分歧、相对年代约束和十个 VLA-UR 问题；未申请 H 编号，也未改动全局登记。GitHub：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/country/VLA/vlandia-conquest-urban-transfer-regional-power-study-2026-10-24.md；Google Docs：https://docs.google.com/document/d/1SSX-QiNwj8IMVc4vq54KISKGZB4FRazVzuC5aP4rIrg/edit。


## 源级复核与现行校勘裁定（v0.6，2026-10-24）
用户在本对话中指出 `Native.zip` 等资料包含官方中文译名。经检索 Library 的 `/Calradia Geography Research Source Files/` 文件夹，现已实际取得 `Native.zip`、`SandBox.zip`、`SandBoxCore.zip`、`StoryMode.zip`、`NavalDLC.zip`，并按官方原始 XML 内 `{=key}` 与UTF-16 BE 编码的 `Languages/CNs/` 字符串表逐一配对。旧稿中声称“原始ZIP未取得”的说法**仅为 v0.1—v0.5 的历史过程记录，不再是当前资料状态**。

本轮已直接确认：瓦兰迪亚文化简介在 `SandBoxCore/spcultures.xml` 的真实键为 `1Ww5lg6I`（末尾是大写字母 I），其官方中文明确是**“无畏的”维伦德／瓦兰狄翁**；先前“英勇的威隆德／瓦兰迪恩”来自早期译稿或误认，**不能代表该版官中**。王国 `IudGLWQZ` 和德泰尔传记 `EHiQI7ps` 已经在 SandBox 生效英文及CNs中复核。氏族 `dey Tihr` 同键 `qFntgcGy` 的官中是**戴·提哈**，但帕拉汶德城市地志 `Nx0qK2g6` 作“戴·提尔”，两种官方译名应按原文保留，实体研究主名使用氏族键译名。

同一来源的 `SandBox/world_lore_strings.xml` 和官中分别核出 `rKKAYQkJ`（德泰尔自称奥斯里克为曾祖父，并讲皇帝赠金冠）、`yJQLtlXj`、`5mvtRbb8`（对王位及子孙争权的悲观陈述）。这些是**角色有据可查的官方话语**，却非独立编年／无缺环谱系。NavalDLC 新增沙拉斯港粮商、绿林兄弟会与戴·科尔坦男爵围城后追究海上供粮者的连续回忆文本，英中同键分别为 `TMdL4gJH`、`cc9JuNoL`、`9wYQGoha`。见新的独立政治史专题：
GitHub：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/country/VLA/vlandia-royal-vassal-power-primary-source-reappraisal-2026-10-24.md
Google Docs：https://docs.google.com/document/d/1CzUP3AsVe9zvgSkWG1HfAt-STWS83lJGXcyWUOibjB8/edit

保留边界：本次 `Native.zip` **没有** `std_common_strings_xml-zho-CN.xml`，因此仍**不能从当前这些文件验证 Caleus/卡琉斯独立名称键**；现用“卡琉斯”系有中文游戏使用记录的主名，并记录待核。当前 StoryMode.zip 不包括潘德拉克人物访谈的专门对白 XML；公开 v1.4.5 反编译代码已恢复对应英文文本，但不能把它冒称为 v1.4.8 原始 XML，项目版本逐字核验仍待完成。此前 `Ingalther`—`Calatild` 继承争议在所获有效贵族 `heroes.xml` 中**没有相关 `Hero.text`**，故不升为A级。


## 同线新专题索引（2026-10-24）
《瓦兰迪亚王权、封臣仲裁与继承权政治：从奥斯里克至德泰尔的制度张力》v0.1 已独立立稿；官方原始 XML 检验国王传记、王权言论及氏族名称，因加泰尔（Ingalther）统一为有据中文用名。卡拉蒂尔德—因加泰尔领地继承权冲突目前只有 SandBox/spclans.xml 开发注释支撑，不应作为1084年已发生史实。GitHub：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/country/VLA/vlandian-monarchy-vassals-dynastic-disputes-2026-10-24.md；Google Docs：https://docs.google.com/document/d/1GWvLahR_TYx5-f4eBVEdjTShTHXkCEdooJa7y7zI0Cc/edit。


## 瓦兰迪亚社会史新专题索引（2026-10-24）
新增《瓦兰迪亚乡村地权、绿林兄弟会与沙拉斯叛乱：王国政治整合的社会成本》v0.1：依据已核官方英文 XML 与同键简中，比较佃农地权、绿林兄弟会转型、杰屈朗异见、沙拉斯行会反王室围城、海运粮商营利与贵族海岸搜捕、码头帮派及流民。特别注明 DLC 只记“戴·科尔坦男爵”而不记具体姓名，不能直接认定为因加泰尔；现有 StoryMode XML 包未收录潘德拉克十九人访谈；公开 v1.4.5 反编译代码已恢复十九人答话，项目 v1.4.8 版本匹配仍待核。GitHub：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/country/VLA/vlandian-peasant-tenure-brotherhood-charas-rebellion-2026-10-24.md；Google Docs：https://docs.google.com/document/d/1A0DVKq8f9fULHQhtsnr9v6N3lE9dQy3L2ZMORGLcHKI/edit。不分配 H 编号，不修改中央 S/E/P/D 登记。


## 新增完成：SandBox／NavalDLC聚落地志异文审计（2026-10-24）
原待办“逐 ID 校验 SandBox 与 NavalDLC 的聚落描述”已完成第一轮。共同的52个瓦兰迪亚聚落ID中，52/52的posX、posY不同；35条英文地志正文不同，12条换键、23条沿用旧键；18条实质性英文改写未获相应简中内容更新。此为模块文本与地图配置差异，不得当作故事世界内部的历史事件。详见《战帆》聚落地志异文审计：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/country/VLA/vlandia-warsails-settlement-variants-localization-audit-2026-10-24.md；Google Docs：https://docs.google.com/document/d/1x-rgVuMsHbRkDUXvs8j194srP-DKgGzcQV98MYl7-SE/edit。


## 补记｜潘德拉克采访 A2 源级恢复（2026-10-24）

公开的 Bannerlord v1.4.5 反编译文件已恢复德泰尔（lord_4_1）、因加泰尔（lord_4_16）、恩泰里（lord_4_5）的十二段采访答话。它们可用于研究援帝誓约、男爵拒援、国王对战后扩张的判断及骑兵—弩兵协同，但属于人物立场性回忆。项目所存 v1.4.8.119303 程序集尚未逐字核对；不可把 A2 恢复文本与 A1 有效 XML 混同。全体证词索引：https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/history/03/Pendraic-Interview-Source-Inventory-v0.1.md。
