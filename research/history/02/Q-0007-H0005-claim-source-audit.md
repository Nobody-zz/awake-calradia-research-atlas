# Q-0007｜H-0005 核心断言逐句引注与英汉本地化审计

版本：v0.1｜2026年10月22日  
审计对象：H-0005《从共和统帅到帝国皇权：卡拉德军事指挥权的长期化》v0.8（同步修订为v0.9）  
性质：核心引文与主要命题的第一轮定向审计；不是全文逐句核销，也不是外部专家审稿。

## 一、材料范围与方法

直接读取 GPT 项目附件中的 SandBox.zip、SandBoxCore.zip、NavalDLC.zip 及 file_manifest.csv。本审计核对了 SandBox 与 SandBoxCore 中被 H-0005 实际引用的英文 XML 条目，并逐键检查对应官方简体中文语言表是否存在。67/67 个 XML 的路径、字节数和 SHA-256 一致只证明资料包完整，不证明每个文件都已完成语义审查。

本轮同时复核 TaleWorlds《Empire – Part 1》（[官方页面](https://www.taleworlds.com/en/News/210)）和《Dev Blog 30/11/17》（[官方页面](https://www.taleworlds.com/en/Games/Bannerlord/Blog/37)）。前者是 H-0005 主线制度史的共同来源，后者描述较晚的瓦兰迪亚边疆军事财政案例。两者都是官方叙述，但不是相互独立的卡拉德内部编年史。

证据等级沿用项目规则：A＝官方文本直接记载；B＝由直接文本严格支持的有限观察；C＝基于材料提出的研究性解释；D＝证据不足的推测。A 级只表示“官方文本确实这样叙述”，不自动等于独立验证的历史事实。

## 二、核心断言—来源—译文审计矩阵

| H-0005论断 | 原始来源与键 | 官方简体中文情况 | 审计结论与边界 |
|---|---|---|---|
| 早期最高军事指挥权具有短期性质；共和国有不定期公民大会与常设元老院 | TaleWorlds《Empire – Part 1》；无 XML 文本键，官方开发者历史介绍 | 不适用 | A：官方回顾直接这样叙述。它是同一篇总体历史叙述，不能因论文分段而变成多份独立见证。 |
| 扩张战争持续时间增加，统帅渐不于战役后卸任 | 同上 | 不适用 | A：文本直接并列叙述军队常年在外与统帅留任；C：战争延长是否严格造成延任，尚无逐代时间表、法律条文或独立制度记录。 |
| 公民大会逐渐依皇帝意愿召集，常在军营举行，老兵影响上升 | 同上 | 不适用 | A：官方回顾明确如此描述；不能由此推出大会固定迁出某座首都、参与资格恒定或程序始终不变。 |
| 北方老家族获授边地并承担防务，皇帝后期以土地和金钱酬赏军人 | SandBox/ModuleData/spkingdoms.xml，Kingdom id=empire，键 aEfsyVH4 | SandBox/ModuleData/Languages/CNs/std_spkingdoms_xml-zho-CN.xml 中同键存在 | A：官方区域沿革直接记载；范围限于北方旧家族与该段所述后期政治，不证明所有省份普遍如此。 |
| 西部帕拉语言与习俗逐渐被遗忘，西部地主支持加里俄斯 | 同文件，Kingdom id=empire_w，键 mOZsbV8j | 对应简体中文键存在 | 英文核心词是“mostly forgotten”（大多被遗忘）；中文“已消亡殆尽”更强。正文以英文为准，不从中文译文推断语言、习俗完全灭绝。地主支持加里俄斯是地方性描述，不能推成地主阶层整体政治立场。 |
| 南方商业城邦被纳入帝国、财富增长，南方贵族支持拉盖娅 | 同文件，Kingdom id=empire_s，键 Xtyb9Dyr | 对应简体中文键存在 | 英文“would seem to confirm these fears”表示这一政治支持似乎印证其他元老家族的担忧；中文“也乐于将这种顾虑付诸现实”容易将主语转为拉盖娅本人。此处属于译文语义偏移，不能据中文强化人物意图。 |
| 潘德拉克战役后废除最后一支常备军、改用执政官私人扈从 | SandBox/ModuleData/spclans.xml，Faction id=legion_of_the_betrayed，键 bhxVA9w7 | SandBox/ModuleData/Languages/CNs/std_spclans_xml-zho-CN.xml 中同键存在 | A：官方组织背景直接这样叙述，但该组织有怀旧和反改革立场。英文写“in the wake of the battle of Pendraic”；中文增加“惨败”，不可把“惨败”作为英文原文的直接记载。 |
| 德洛修斯所率旧军团遭伏击；角色把纪律和帝国衰弱归咎于阿雷尼科斯改革 | SandBox/ModuleData/companion_strings.xml，键 mk0l1BfB、rNkwrwo4 | SandBox/ModuleData/Languages/CNs/std_companion_strings_xml-zho-CN.xml 中两键均存在 | 两段属于同伴角色背景/自述，且均呈反改革立场。应拆分为“旧军团遭伏击”“常备军制度改变”“角色将衰败归因于改革”三个叙述，不得拼接为已经证明的单一因果链。 |
| 皇子继位是惯例而非法律，元老院曾选阿雷尼科斯 | SandBox/ModuleData/heroes.xml，Hero id=lord_1_5，键 04xAg0yN | SandBox/ModuleData/Languages/CNs/std_heroes_xml-zho-CN.xml 中同键存在 | A：官方人物传记直接这样叙述；不能代替成文法、同时代法律记录或完整继承程序。 |
| 元老院选帝、家族继承、军人择主与民众大会是不同的合法性依据 | SandBox/ModuleData/world_lore_strings.xml，键 Cx2FCePF、uJeoa6u1、SCogGc7N、T1svPL9Z、uK4IX036、OFOXDkPv、Cgdg9Q8t、spQJxKtr | SandBox/ModuleData/Languages/CNs/std_world_lore_strings_xml-zho-CN.xml 中八键均存在 | 这些对白证明角色提出过这些政治主张，不证明其主张已成为统一宪法。Cx2FCePF/uJeoa6u1 是同一角色连续对白；OFOXDkPv/Cgdg9Q8t/spQJxKtr 是另一角色连续对白，不能按键数视为独立互证。 |
| 卡拉德人无王传统、丘陵部族到帝国形成 | SandBoxCore/ModuleData/spcultures.xml，Culture id=empire，键 X0kKBzsW | SandBoxCore/ModuleData/Languages/CNs/std_spcultures_xml-zho-CN.xml 中同键存在 | A：官方文化概述直接这样叙述；其内容与《Empire – Part 1》明显重叠，属于同一官方世界观的关联文本，不作独立外部互证。 |
| 瓦兰迪亚雇佣军从银币报酬转为授地与头衔、定居并取得独立权力 | TaleWorlds《Dev Blog 30/11/17》 | 不适用 | A：官方开发者文本直接叙述；这是较晚的边疆军事财政案例，只能作比较，不能直接证明早期皇权长期化的起因。 |

## 三、已落实的论文修订

1. H-0005 版本号更新为 v0.9；第六节军团改革段落拆分了常备军废除、旧军团遭伏击与反改革者对衰败的归因，避免把它们拼成单线因果链。
2. 注释〔2〕〔3〕〔5〕补入原始英文 XML 路径、文本键及对应简体中文语言表路径；注释〔6〕标出“惨败”属于中文本地化增译；注释〔8〕明确同一角色连续对白不能按键数计作独立证据。
3. 论文新增编者校勘附记，记录三处译文语义偏移：
   - mOZsbV8j：“mostly forgotten”／“已消亡殆尽”；
   - Xtyb9Dyr：“would seem to confirm these fears”／“也乐于将这种顾虑付诸现实”；
   - bhxVA9w7：“in the wake of the battle of Pendraic”／“在潘德拉克战役的惨败之后”。
4. Q-0006 附录B、I-0002 与 I-0003 已登记本轮审计范围及新增来源、命题和争议记录。

## 四、未解决问题与下一步

- Q5-09 仍开放：官方总体回顾能支持制度变化的叙述，但缺乏独立年代锚点、制度程序和相互独立的历史见证，不能验证“战争延长—统帅延任—大会控制—皇权世袭化”的单线因果链。
- 本轮只完成 H-0005 核心引文和主要命题的第一轮定向核验，尚未逐段核销全文所有历史断言、脚注及比较史学文献的具体页码。
- 下一轮按同样的“正文断言—原始路径/键—英文原文—官方中文键是否存在—证据等级—推论边界”标准审计 H-0001—H-0004；继续聚焦帝国与早期大陆社会，不启动诺德专题。
