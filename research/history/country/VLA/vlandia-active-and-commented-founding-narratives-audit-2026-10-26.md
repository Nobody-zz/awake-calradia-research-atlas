# 瓦兰迪亚起源叙事的生效文本与旧稿分层：奥斯里克、乌索尔与“海上公爵”

**CHC-VLA-SRC｜源级辨析札记 v0.1｜2026-10-26｜未分配 H 编号｜不修改中央 I/S/E/P/D 登记**

## 一、研究问题

项目现存的 SandBox 官方资源中，至少能看到两种看似不同的瓦兰迪亚起源叙事：

1. 生效的 `spkingdoms.xml` 王国沿革将瓦兰迪亚王权追溯至奥斯里克（Osric Iron-Arm）：他夺取帝国西海岸，帝国诸皇帝为求和平承认他为王；奥斯里克再承认副官的男爵、伯爵地位和土地宗主权，以换取战时集结。
2. `world_lore_strings.xml` 中有一段被 XML 注释包住的旧王国背景文本，称帝国于882年授予 Waland 海民军阀乌索尔（Uthor）“海上公爵”（Dux of the Sea）头衔，之后他们宣布独立，控制原属帝国的河谷和牧场。

这两段材料不应被直接拼成一条连续年表，也不应把第二段当成当前生效的官方王国简介。**源级核验确认：奥斯里克文本是当前有效王国沿革；乌索尔—882年—Dux of the Sea 文本在本次所存 `world_lore_strings.xml` 中处于注释内，相关字符串键也没有出现在所存英文与官方简中世界地志语言表中。**它是可研究的旧稿／开发史材料，不是当前有效游戏文本所直接陈述的世界内事实。

## 二、直接核验结果

本次重新解析 SandBox.zip 中的以下文件，并核对其 SHA-256：

| 文件 | SHA-256 | 本次用途 |
|---|---|---|
| `Modules/SandBox/ModuleData/spkingdoms.xml` | `1d0664283c916dbbd11a02bcd55bbba75e1de10354b54bd35508f59720dde41a` | 生效王国沿革及 `Kingdom.id=vlandia` |
| `Modules/SandBox/ModuleData/Languages/std_spkingdoms_xml.xml` | `176b13dd1ff8f007ca591a74112c610382eeecb28d4ab5a56a09c76c9479908d` | 同键英文语言表 `IudGLWQZ` |
| `Modules/SandBox/ModuleData/Languages/CNs/std_spkingdoms_xml-zho-CN.xml` | `0ec14c3871dc92988413ff86e66583740780bdc1d84d486917e529bc78fbc5d8` | 同键官方简中译文 |
| `Modules/SandBox/ModuleData/world_lore_strings.xml` | `fa30ce156b89db56069e61fa88fce88cb9c83af55fcc7a27bfd0ac3c8a8472d1` | 检查旧背景块的 XML 注释状态 |
| `Modules/SandBox/ModuleData/Languages/std_world_lore_strings_xml.xml` | `6558fbf323c0d42c18516dace260e7d2d560515aae6756959a813d55d6a17fbc` | 检查旧背景文本键是否存在于英文表 |
| `Modules/SandBox/ModuleData/Languages/CNs/std_world_lore_strings_xml-zho-CN.xml` | `a571185ea4258f4427053893b688590c576824e9a2d203bd5a90a885577a5b36` | 检查旧背景文本键是否存在于官方简中表 |
| `Modules/SandBox/ModuleData/spclans.xml` | `318afe49eb3a7e4b7b92877da58c69af5571925b31e13c0a3851ba995e47b070` | 交叉核对瓦兰迪亚开发注释 |

### 2.1 生效文本：奥斯里克王权起源

`spkingdoms.xml` 中生效的 `Kingdom.id=vlandia` 使用键 `IudGLWQZ`；英文语言表的正文是：

> The Vlandian monarchy descends from Osric Iron-Arm, a warlord who seized the western coasts of the Empire and was recognized as king by the emperors as the price of peace.

同段继续说，奥斯里克承认自己的副官为男爵和伯爵，给予他们对其土地的宗主权，以换取他们战时向其旗帜集结；此后各代瓦兰迪亚国王对王权扩张与放任男爵内斗采取不同策略。

同键官方简中译文保留了奥斯里克夺取西岸、帝国为议和承认其王位、授予副官爵位与土地宗主权并要求战时效忠的核心内容。英文中的 `the emperors` 是复数；它没有给出具体皇帝、日期、条约名称或准确边界。因此，本段支持的是王权起源的官方叙述与最小制度关系，不支持一个精确的建国年份。

### 2.2 旧背景文本：乌索尔与882年

`world_lore_strings.xml` 第123行附近有注释标识 `intra-vlandian, someone who squired with furthard`，随后开始一个以 `<!--string id="rake_lore"` 开启、到第183行 `/-->` 才关闭的旧字符串块。该块中的瓦兰迪亚条目包括：

- `faction_bg1_vlandia`：`Founded in 882 when the Empire granted Uthor, a warlord of the Waland seafarers`
- `faction_bg2_vlandia`：`who had long ravaged the western coasts, the title 'Dux of the Sea.'`
- `faction_bg3_vlandia`：`They have since declared themselves an independent kingdom, controlling`
- `faction_bg4_vlandia`：`the river valleys and pastures that were once some of the Empire's wealthiest lands.`

这四段合读，叙事顺序是：帝国授予海民军阀乌索尔“海上公爵”头衔——海民后来宣布独立——控制原属帝国的河谷与牧场。它与生效文本的重点明显不同：旧稿从帝国授予头衔和指定年份开始；生效王国沿革从奥斯里克的征服及帝国为和平承认其王位开始，并把王权与副官的地权、军役交换相连。

### 2.3 语言表没有把旧稿键重新激活

在本次 SandBox.zip 的英文和官方简中 `std_world_lore_strings_xml` 语言表中，未检出 `IfWaPiaW`、`NHiel2zM`、`6hc8VPrF`、`NXD4kJqk` 这四个旧稿键。它们只出现在注释中的旧 `string` 元素及其内嵌英文回退文本；有效 XML 解析不会将这些注释子串读作当前 `world_lore_strings.xml` 的生效 `string` 元素。

相比之下，奥斯里克段落的 `IudGLWQZ` 确实存在于有效 `spkingdoms.xml` 的 `Kingdom.id=vlandia` 文本引用中，也有同键英文和简中语言表条目。德泰尔政治自述的 `rKKAYQkJ` 等键同样仍在有效政治自述字符串中；它们与旧 `faction_bg*` 片段属于不同状态，不应因同处一个文件而混为一谈。

## 三、开发注释提供的另一种瓦兰迪亚形成概述

`spclans.xml` 中还有一段未加载的 VLANDIA 设计注释，称瓦兰迪亚战船最初以商人身份来到卡拉迪亚西岸，见土地富庶后决定夺取；帝国先与其作战，随后授予贵族头衔和地产、将其纳为帝国客户；当其反叛后，帝国再次与之作战，最终形成独立王国。该段没有给出乌索尔姓名或882年，但与旧 `world_lore_strings.xml` 背景段共享若干构想：海上来者、帝国授予头衔／地产、后续独立。

两份开发材料可能反映相近的早期设定框架，但目前不能确认它们的先后版本、作者意图或相互继承关系。它们不是两份独立的历史见证，因为它们都是官方资源中的开发注释；更不能把它们与当前生效的奥斯里克沿革算作三个互相印证的来源。

## 四、可以得出的历史与开发史判断

### A. 当前游戏世界的生效叙述

当前生效王国沿革将奥斯里克定位为王朝起源人物，强调征服后帝国承认、对副官领地权利的认可，以及战时军事义务。德泰尔的有效人物传记和政治自述进一步将王权记忆与帝国金冠、叛乱、觊觎者和封臣争地联系起来。此线应继续作为瓦兰迪亚政治史主论证的基础。

### B. 旧稿所保存的开发史线索

被注释掉的旧背景以乌索尔、Waland 海民和882年作为创始节点，并以“海上公爵”头衔描述帝国—海民关系。它可能说明开发过程中曾考虑以帝国授予的边疆海权职位作为瓦兰迪亚起源框架，随后生效简介转而突出奥斯里克的军事征服和王权交易。但“随后”目前只是文件状态上的比较，不是已经重建的开发时间顺序：单凭同一 ZIP 中的注释状态，不能确定何时删除、为何删除或是否曾在公开版本中生效。

### C. 两种叙事是否可以在世界内兼容？

逻辑上可以提出一种兼容假说：乌索尔可能代表更早的海上军事首领传统，而奥斯里克则是后来建立王朝的征服者；帝国曾授予的头衔、客户关系、叛乱与后续议和也可能构成更长的政治过程。

但本次有效文本没有说乌索尔是奥斯里克的祖先、前任或同一人物，也没有把882年与奥斯里克的活动建立年代联系。因此，兼容模型只能作为 C 级待证假说，不能把它写进已证年表，更不能用它填补奥斯里克的绝对年代。

## 五、翻译与术语注意

- `Dux of the Sea` 是旧稿里的英文头衔，当前生效王国沿革没有这个词组。中文研究中可暂译“海上公爵”，但应标注为旧稿术语，而非当前有效游戏中的正式瓦兰迪亚爵位。
- `Waland seafarers` 在旧稿中是族群／海民称呼；不能无证据地与当前瓦兰迪亚人、某个现实历史民族或具体氏族完全等同。
- `Uthor` 只出现在旧稿背景段；当前生效王国沿革不提此人。不得把他直接列为奥斯里克的前任、祖先或副手。
- `Founded in 882` 只给旧稿所描述的另一套王国背景定年，不是奥斯里克王权的有效建国年。
- “帝国授予头衔／地产”与“帝国为和平承认已经夺取西岸的奥斯里克为王”是两种不同的政治动作。即使将来证明两者可以串联，也需说明主体、对象、时间与权利内容，而不能统一翻译成模糊的“帝国承认瓦兰迪亚”。

## 六、后续任务与停止条件

1. 将旧稿 `Uthor/882/Dux of the Sea` 标记为“注释中的开发史材料”，不写入当前世界内相对年代链，不作为奥斯里克生年或建国年依据。
2. 在可取得的其他官方版本中检查该四键是否曾作为生效 `string` 元素存在；只有找到带版本标识的有效 XML，才可讨论其公开生效历史。
3. 若没有历史版本可核，停止追溯“乌索尔是否真实存在于当前世界史”的推论，将其保留在开发史附录即可；研究资源优先用于已生效的奥斯里克—德泰尔—封臣关系证据。
4. 将本札记与王室谱系／政治地理审计、王权封臣工作稿交叉引用。它的作用是清理来源状态，不能独立承担一篇瓦兰迪亚建国史的因果论证。

## 关联研究

- [瓦兰迪亚历史初步摸底与重大研究问题](vlandia-historical-initial-baseline-major-questions-2026-10-24.md)
- [瓦兰迪亚王权、封臣与王朝争端研究](vlandian-monarchy-vassals-dynastic-disputes-2026-10-24.md)
- [瓦兰迪亚王室谱系与政治地理：奥斯里克、加伦与帕拉汶德三组记忆的证据审计](vlandia-royal-lineage-and-political-geography-audit-2026-10-26.md)
- [瓦兰迪亚有效人物—氏族关系字段审计](vlandia-effective-hero-clan-relationship-field-audit-2026-10-26.md)

**阶段结论：**奥斯里克起源是当前有效王国沿革；乌索尔、882年与“海上公爵”来自被注释的旧背景稿。二者应作为不同证据状态记录。旧稿可用于研究开发设定如何变化，却不能作为当前世界内事实的直接证据。
