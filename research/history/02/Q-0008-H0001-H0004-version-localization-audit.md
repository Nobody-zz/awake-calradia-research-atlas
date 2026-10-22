Q-0008｜H-0001—H-0004 逐句引注与英汉本地化复核（第一轮）

版本：v0.4｜2026年10月22日（执行更新）

审计性质：对四篇论文的核心命题、引注键、官方简体中文覆盖与原版／War Sails文本差异进行定向复核。不是四篇论文全文逐字校对，也不是外部同行评审。

## 一、审计范围与方法

审计对象为H-0001《卡拉德人的早期建城与殖民网络》、H-0002《征服、合邦与同化》、H-0003《从部族联盟到共和国》、H-0004《卡拉德人到来以前的帕拉诸部落》当前云盘稿。依据本项目上传的SandBox.zip、SandBoxCore.zip、NavalDLC.zip、file\_manifest.csv，直接检查SandBox与NavalDLC的settlements.xml及其简体中文语言表，并检查spkingdoms.xml、spcultures.xml的关键文本键。对于正文直接写在XML属性中的英文条目，即使它的键未出现在单独的英文语言表中，也仍然是可直接读取的官方英文来源；但若简体中文语言表没有对应键，论文中的中文释文必须标为工作译文／既有汇编译文，不得称为已核实的官方游戏译文。

本轮重新计算并与file\_manifest.csv逐项对照的文件包括：SandBox/ModuleData/settlements.xml（702,255 bytes；SHA-256 E92BB2079526DCC4A125B6A7AE21B76240E5176D143ACA98D083BE9CE8C32524）；SandBox官方简体中文settlements语言表（74,952 bytes；46DF7C77C4FA184D1C67C3DC5881F1098C3B6842AE051A188DEBD41AF9D95AEB）；SandBoxCore/ModuleData/spcultures.xml（152,632 bytes；D8A06B5FB28AE446AB3ADE8823A088744A3C4D5EB020FED1C044C2C923553F23）及其简体中文语言表（63,028 bytes；302DB2F0E1ACA11030C88C81643576062782E612CF44043A4734EE2F31EFC3BA）；NavalDLC/ModuleData/settlements.xml（789,997 bytes；4F2924A0B236062D1720E0AD48131D23FA4863E5C0AA7FE475F36B0056B9E436）及其简体中文语言表（89,694 bytes；9FFBB92133CF79F8EB13849D27C5A4CFDF24D4F1B958C09519011D07137249BF）。六个文件的字节数与SHA-256均与清单相符。这只证明本轮所用源文件与项目清单一致，不表示全部DLC聚落异文均已完成审查。

## 二、H-0001｜建城与殖民网络

1. 沙拉斯：SandBox/ModuleData/settlements.xml，Settlement id=town\_V7，正文键0cZmKO76。英文正文直接称其传统上被视为卡拉德人在新大陆的第一块殖民地，并记述帝国强盛时首都北迁至巴拉维诺斯、沙拉斯继续作为航海和贸易枢纽。该正文键存在于SandBox与NavalDLC的settlements.xml内，但不在所提供资料包的独立英文或简体中文settlements语言表中；当前中文释文应继续标为工作译文／既有汇编译文。此条与town\_V3“巴拉维诺斯不久取代沙拉斯成为首都”的说法存在相对年代张力。论文已正确保留此问题，不得将“迅速”换算为年数或补造第二次迁都。

2. 巴拉维诺斯：Settlement id=town\_V3，正文键Nx0qK2g6。独立英文与简体中文语言表均有对应键；SandBox与NavalDLC英文正文实质相同，只有Empire大小写等编辑性差异。英文称其为卡拉狄乌斯建立的第二座“重要殖民地”，并称其很快取代沙拉斯成为首都；这不等于全部聚落中严格按时间排序的第二座城市。现有正文对“第二座重要殖民地”的限定是适当的。

3. 俄耳堤西亚：Settlement id=town\_EW4，正文键JhBSnWAe。英文与简体中文语言表均有对应键。SandBox与NavalDLC正文主要叙述稳定，细微差别包括“Bay of Charas”改为“Gulf of Charas”及Empire大小写。文本支持“珀拉斯海第一块卡拉德殖民地”“早期数世纪受古亚兹统治”“后来帝国扩张将殖民地并入母共和国”的官方叙述，但不提供精确年代或统治制度细节。

4. 贾尔马律斯：Settlement id=town\_EW3，正文键TI3fS2xN。英文正文存在于SandBox与NavalDLC的settlements.xml，但正文键不在单独英文或简体中文语言表中。正文直接称其为珀拉斯海内陆最早的帝国殖民地之一、用作压制西部帕拉部落的基地，并叙述巴拉维诺斯接收其驻军送来的战利品和奴隶，以及将军卡尔索斯发动政变。中文释文必须标为工作译文／既有汇编译文；该条没有提供殖民活动的精确年代，不能证明这些安排在卡拉狄乌斯生前已经成熟。

5. 拉革塔与洛泰：town\_EW1正文键ZAGUIKOn、town\_EW6正文键5SpYVtie。英文正文均存在于settlements.xml，但两个键都不在所提供资料包的独立英文或简体中文settlements语言表中。H-0001原脚注〔8〕〔9〕此前没有像脚注〔1〕〔5〕那样明确标出中文释文性质；本轮已补明工作译文／既有汇编译文，避免读者误认为官方简体中文条目已核实。英文内容支持拉革塔的欺诈性献城记忆、洛塔什随后遭攻取和摧毁；它们是官方城市沿革，不是独立的同期战报。

6. 西帝国与南帝国区域沿革：SandBox/ModuleData/spkingdoms.xml，empire\_w键mOZsbV8j、empire\_s键Xtyb9Dyr。两键均有英文及官方简体中文条目。mOZsbV8j英文说旧语言与习俗“are mostly forgotten”，中文译为“已消亡殆尽”，语义强度更高；正文分析应以英文原文为准，不得把它扩展为语言完全灭绝。Xtyb9Dyr英文“would seem to confirm these fears”指南方贵族支持拉盖娅似乎印证其他元老家族的担忧；官方中文“也乐于将这种顾虑付诸现实”容易改变主语、强化拉盖娅本人的意图。该中文不应作为人物意图的独立证据。

7. 帝国文化概述：SandBoxCore/ModuleData/spcultures.xml，Culture id=empire，正文键X0kKBzsW。英文与官方简体中文语言表均有对应键。它概述卡拉德人早期处于南方海域与巴旦尼亚森林之间的丘陵地带、无王传统、邻邦结盟或被征服以及最终帝国化。该文本与TaleWorlds《Empire – Part 1》总体历史回顾内容重叠，应作为同一官方世界观中的不同文类处理，不能计作独立的古代史料互证。

H-0001本轮结论：核心英文来源键存在；两处此前未标清的中文释文（town\_EW1、town\_EW6）现已补充说明。迁都相对年代、海上流亡者与内陆部族之间的人口连接、俄耳堤西亚早期殖民与后期海巡之间的断代仍未解决。

## 三、H-0002｜征服、合邦与同化

1. 已确认的缺失独立语言表键：town\_EW1/ZAGUIKOn（拉革塔）、town\_EW6/5SpYVtie（洛泰／洛塔什）、town\_EW5/rX8oGVvV（阿弥塔堤斯）、town\_EN2/wKMo2CUP（狄亚特马）、town\_EN3/EJZLzhJk（萨涅俄帕）、town\_EN4/LqPJY4s9（阿耳戈隆）。这些条目的英文长篇正文直接嵌在SandBox/ModuleData/settlements.xml中，但没有对应的独立英文或官方简体中文settlements语言表键。H-0002脚注〔2〕—〔4〕〔7〕〔8〕〔11〕已将其中文释文标作工作译文／既有汇编译文，处理正确。

2. 已有英文与官方简体中文键：town\_ES6/RL2vacqv（费卡翁）、town\_ES4/WGtzBswe（吕卡隆）、town\_EN5/8UJ3cPrZ（密泽亚）。这些来源直接支持费卡翁特定战争中的部落联合与求和、吕卡隆征服末期的相对和平合邦、密泽亚在李图领导下寻求帝国保护等地方性叙述。它们不能单独证明长期存在的统一帕拉联盟、通用合邦条款或固定的地方治理制度。

3. 西帝国区域沿革empire\_w/mOZsbV8j的中文“已消亡殆尽”强于英文“mostly forgotten”；H-0002正文“旧语言和习俗逐渐消退”的表述相对谨慎，建议继续以英文为论证依据，并在脚注中明示本地化差异。

4. 本轮发现的、与H-0002直接引用聚落相关的原版／DLC差异不止赫塔尼亚和克里俄斯：

• village\_EN4\_4（赫塔尼亚）：SandBox英文称林农仍说Palaic languages；NavalDLC英文改为Dryatic languages。DLC简体中文仍译作帕拉语，未同步。

• village\_EN3\_3（克里俄斯）：SandBox英文称其位于石灰岩山脊且适宜牧马；NavalDLC英文改为阿里斯河流入俄佛堤斯湖的位置，并新增古帕拉人在湖岸建圣地的叙述。DLC简体中文仍是旧的地形／牧马文本。

• village\_EN3\_1（厄诺伊萨）：SandBox英文称其位于俄佛堤斯湖岸，并保存古帕拉圣地与彼世门户的传说；NavalDLC英文改为厄诺伊萨位于流向拉科尼斯湖的涅维斯河边。DLC简体中文仍保留基础版的俄佛堤斯湖与圣地叙述。因此“厄诺伊萨—俄佛堤斯湖圣地”应明确限定为SandBox基础版文本，不能声称跨版本稳定。

• village\_ES3\_1（卡诺洛斯）：SandBox英文称其位于吕卡里亚平原南部；NavalDLC英文改为珀拉斯海以北的平原。两版均保留帝国入侵前的养马与吕卡里亚骑手记忆，故“前帝国马业”主张仍有两版文本支持，但精确方位应标明版本。DLC简体中文仍保留基础版方位。

• village\_ES4\_3（坎忒里翁）：SandBox英文称其位于吕卡里亚平原东部、坡地降雨较多；NavalDLC英文改为塞堤斯河、奥尼石山与忒弥安丘陵之间，并新增村庄以优良战马闻名的叙述。DLC简体中文仍保留基础版方位和降雨描述。

• town\_EN5（密泽亚）：SandBox英文称Myzeiad是帝国中东部的富饶丘陵地；NavalDLC改写为Myzead、帝国东部的山地高地。两版均保留李图、保护性归附及后续政治冲突主线；官方简体中文仍保留基础版地貌措辞。

• town\_EW4（俄耳堤西亚）：Bay of Charas改为Gulf of Charas，属于轻微用词变化；相关历史主线不变。

上述清单仅覆盖H-0001—H-0004实际引用且本轮对读的ID，不代表已审查全部NavalDLC聚落文本。

H-0002本轮结论：关于地方征服结局的核心叙述与对应英文条目相符；“费卡翁联合”只能解释为具体战争中的协调；阿弥塔堤斯条目明确把“天谴”定位为帝国宣传；赫塔尼亚、克里俄斯、厄诺伊萨等语言／圣地命题必须注明版本，不能把本地化旧译误作DLC英文原文。

## 四、H-0003｜从部族联盟到共和国

1. Culture.empire/X0kKBzsW的英文与官方简体中文键均存在。其文本确实记述无王传统、邻邦结盟或被征服、最终形成帝国并“有实无名地演变为君主政体”，但没有具体建制年份、公民资格边界、城邦加入程序或宪制形成过程。它与《Empire – Part 1》是内容重叠的官方回顾，不是第二份独立的古代证词。

2. 本篇引用的部分聚落中文释文需要明确标注工作译文：town\_EN4/阿耳戈隆的LqPJY4s9、town\_EW3/贾尔马律斯的TI3fS2xN、town\_EW1/拉革塔的ZAGUIKOn，均有英文内嵌正文，但不在独立英文或官方简体中文settlements语言表中。H-0003原脚注〔6〕〔8〕〔10〕已补入键与翻译性质说明。town\_EN5/密泽亚的8UJ3cPrZ则有官方简体中文键，但Myzeiad/Myzead和区域地貌措辞在DLC版本中发生变化。

3. H-0003关于自由公民大会、常设元老院、短期最高军事统帅权、埃刻里翁与西佩戈斯等制度及英雄叙事，主要依赖TaleWorlds《Empire – Part 1》。该官方文章未包含在本轮上传的XML档案中；本轮尝试访问旧版Blog/45和News/210页面均遇到403，故本轮没有重新抓取全文。相关主张仍应按项目既有引用记录处理，不声称已在本轮重新完成外部网页逐段核验。即使文章内容可核对，也属于官方总体历史回顾，不提供完整年代和早期会议程序，不能据此填补所有制度形成过程。

H-0003本轮结论：现有正文对文化概述的回顾性性质、与《Empire – Part 1》的同源关系以及制度年代的不确定性处理适当；本轮主要补强缺失语言表键的标记和外部网页可访问性记录。共和国形成的精确年代、城邦联盟的制度过程、公民资格与因果链仍待证。

## 五、H-0004｜前征服帕拉社会

1. 本篇引用的缺失独立语言表键包括town\_EW1/ZAGUIKOn、town\_EW6/5SpYVtie、town\_EW5/rX8oGVvV、town\_EN2/wKMo2CUP、town\_EN3/EJZLzhJk、town\_EN4/LqPJY4s9。当前脚注〔86〕已将相应中文释文标为工作译文／既有汇编译文。费卡翁、吕卡隆、密泽亚以及若干村庄条目有官方简体中文键，但“有键”不等于DLC文本一定与旧译同步。

2. 赫塔尼亚village\_EN4\_4的Palaic/Dryatic差异与克里俄斯village\_EN3\_3的圣地新增叙述已被正确登记。本轮又确认：厄诺伊萨village\_EN3\_1在NavalDLC英文中不再叙述俄佛堤斯湖岸与古帕拉圣地，而改为涅维斯河通往拉科尼斯湖的河岸位置；DLC简体中文仍保留SandBox基础版的湖泊圣地文本。因此，H-0004中“萨涅俄帕与厄诺伊萨一致呈现俄佛堤斯湖圣地”的命题只在SandBox v1.4.8基础版的两条记述内成立，不应被理解为跨版本稳定的双条互证。克里俄斯DLC新增圣地则是另一条版本限定的官方叙述，不构成独立考古证明。

3. 卡诺洛斯village\_ES3\_1与坎忒里翁village\_ES4\_3的地理描述在DLC英文中也有改写，官方简体中文仍保留基础版方位。两版均保留前帝国养马记忆；因此可保留“吕卡里亚地区的前帝国马业”这一受限命题，但“位于吕卡里亚平原南部／东部”“坡地降雨更多”等具体地理断言须明确以SandBox v1.4.8文本为依据。骑手是否属于帕拉人仍无直接证据。

4. 密泽亚town\_EN5/8UJ3cPrZ在DLC中的Myzeiad/Myzead及地貌描述发生轻微改写，简体中文未同步；其李图与保护性归附的主线叙述仍在两版保留。俄耳堤西亚town\_EW4的Bay/Gulf用词差异不改变其核心叙述。

H-0004本轮结论：多中心、不均衡政治联系仍只能作为C级解释模型；费卡翁联合不等于常设联盟或统一帕拉王国，吕卡里亚骑手族属未明，语言与圣地证据必须按具体版本和条目分别登记。原版与DLC文本不能被拼接成一条内部历史时间线。

## 六、落实的修订与证据边界

执行更新（2026-10-22）：已将Q-0008的定向修改实际写回H-0001—H-0004四篇Google Docs原稿，而非仅保留在本审计备忘录中。H-0001补明拉革塔与洛泰缺少独立语言表键、中文释文为工作译文／既有汇编译文，并限定“mostly forgotten／已消亡殆尽”的语义差异；H-0002修订厄诺伊萨圣湖段落与脚注，新增卡诺洛斯、坎忒里翁、密泽亚的DLC版本差异；H-0003在阿耳戈隆、贾尔马律斯、拉革塔脚注中补明英文正文键及中文释文性质；H-0004更新为v0.6，修改正文、命题登记和脚注，限定厄诺伊萨圣湖记忆与吕卡里亚马业空间主张。I-0002已更新四篇状态；I-0003已新增S-0052—S-0056、P-0057、D-0043—D-0045，并更新相关既有源项、命题与争议记录。

本轮已完成：对项目附件中的SandBox与NavalDLC英文settlements.xml及对应官方简体中文语言表进行直接对读；实际修改H-0001—H-0004正文、脚注或复核记录；更新I-0002与I-0003。另已用出版方目录核验Hansen、Terrenato、Malkin、Mackil所引相关章节与页码，并把可核实的范围写回H-0001—H-0003；这只完成书目元数据和章节页码核验，不等于已逐页验证每一比较性论点。尚未完成：H-0001—H-0004每一正文断言与脚注的逐项核销；TaleWorlds《Empire – Part 1》全文的外部网页重新抓取；NavalDLC全部聚落条目的全面异文审计。后续继续按“正文断言—原始文件路径／Settlement或Kingdom ID—文本键—英文原文—官方中文键是否存在及是否过时—证据等级—推论边界”逐项核查，不启动新国家专题

## 七、追加核验：地图坐标与比较文献页码（2026-10-22）

1. 原始 settlement XML 的直接计数复验与 I-0003/S-0033、D-0021一致：SandBox有493个Settlement ID，NavalDLC有540个，其中493个为共有ID；这493个共有ID的posX/posY属性全部不同。共有条目的text属性有271处不同，DLC另有47个新增ID，其中38个新增ID带叙述文本。该结果描述的是模块数据差异，不证明卡拉迪亚内部发生过城市迁移、河道改道、海岸变化或行政中心转移。H-0001脚注〔15〕已改为列出三个可复核坐标例子。

2. 比较史学书目核验：Hansen《Polis》第16章正式题名为“The Greek Conception of Polis as a City with a Hinterland”，页码101–105（Oxford Academic：https://academic.oup.com/book/47289/chapter-abstract/422665211）；Terrenato《The Early Roman Expansion into Italy》第4章页码109–154、第5章155–193、第6章194–247（Cambridge University Press目录及章节页：https://www.cambridge.org/core/books/abs/early-roman-expansion-into-italy/heterogeneous-conquest-i-a-crosssection-of-polity-biographies-and-types-of-conflicts/A169F00268C4D070BAAFADF9F7FECB3E；https://www.cambridge.org/core/books/abs/early-roman-expansion-into-italy/heterogeneous-conquest-ii-family-biographies-and-agendas/C130088B695656188C64CC6D3061B02F）；Malkin《A Small Greek World》第1章“Introduction: Networks and History”，页码3–64（Oxford Academic：https://academic.oup.com/book/5459/chapter-abstract/148340557）；Mackil《Creating a Common Polity》导论页码1–18、第4章147–236、第5章237–325、第6章326–399（Oxford Academic：https://doi.org/10.1525/california/9780520272507.003.0007）。H-0001—H-0003已补入相关章节和页码。

3. 本轮核验仅确认出版方目录中的书目、章节名称与页码，并据此修订引用信息；没有取得全部专著全文逐页核对每项具体论点。正文仍须将现实历史研究作为比较框架，而非卡拉迪亚史实的替代证据。H-0001—H-0004逐句断言—脚注的全面核销仍在进行。

---

Source of truth: [Google Docs](https://docs.google.com/document/d/1wfwd2clfqR95v2xaWUZjo90-hPGNOOjMfD0fOCpeqnY/edit)
