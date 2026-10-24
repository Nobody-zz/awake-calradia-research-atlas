# CHC-EMP-GEN｜《帝国地方秩序的多重来源》源级与本地化审计 v0.2

**日期**：2026-10-24  
**审计对象**：论文工作稿 v0.2；论文候选稿 v0.1 的证据基础。  
**审计方法**：直接读取本项目上传的 SandBox.zip 与对应官方简体中文语言表 XML；以项目上传的 encyclopedia-zh-cn.md 作为辅助中文百科文本。  
**结论**：15/15 个论文源键在英文 XML 中找到；14/15 个源键在本轮可用的对应简中语言表中找到匹配项。唯一未直接命中者为波罗斯地志 key rGXdJybe；英文原文存在，项目百科文件有对应中文条目，但当前 SandBox 简中聚落语言表中没有该 key，故须标注为辅助本地化记录，而非语言表直接命中。

## 一、逐键核查

|论文源键|英文原始文件与记录|证据类型|论文中的用途|简中校验状态与限制|
|---|---|---|---|---|
|nQOf27Rx|SandBox/ModuleData/spclans.xml；Faction hidden_hand|F：派系简介|秘密之手通过“对当局有用”而壮大，同时参与镇压、抢掠、打手与赃物交易|对应 key 存在于 std_spclans_xml-zho-CN.xml；派系显示名 Hidden Hand 的官方简中为“秘密之手”。|
|9qAWNBvA|spclans.xml；Faction eleftheroi|F|自由民的边疆知识、头衔、进入统治者随从队伍及对帝国实际权威的敌意|对应 key 存在于简中表；派系显示名为“自由民”。正文遵从英文 retinues 写“随从队伍”，不直接采用简中“私兵”，避免把叙述中的随从关系提前定性为特定法律／军事身份。|
|xahrUc5n|spclans.xml；Faction brotherhood_of_woods|F|绿林兄弟会从劫富济贫叙事转向勒索、恐怖和与地方当局交易|对应 key 存在于简中表；派系名为“绿林兄弟会”。这是派系简介对组织演变的概括，不是每个成员的独立行为记录。|
|B8c2mNKj|spclans.xml；Faction embers_of_flame|F|火焰余烬的起源叙事及其后来的敲诈行为|对应 key 存在于简中表；派系名为“火焰余烬”。不得与拉狄摩斯的真理之国合并。|
|bhxVA9w7|spclans.xml；Faction legion_of_the_betrayed|F|潘德拉克之后常备军被废、执政官私兵取代常备军及军团依赖合同|对应 key 存在于简中表；派系显示名为“被弃者军团”。其英文描述开头使用 “The Last Legion”，正文以官方派系显示名称呼该组织。|
|pzK7TN05|wanderer_strings.xml；backstory_b.spc_wanderer_empire_10|A：角色自述|蛮族事务局从外部部族事务扩展到帝国内部，并索取病人信息|对应 key 存在于简中表，文本使用“蛮族事务局”；这是医生的自述，不是行政档案。|
|sfFLudTM|wanderer_strings.xml；backstory_c.spc_wanderer_empire_10|A|蛮族事务局以揭露医患关系相威胁，迫使医生参与逼供|对应 key 存在于简中表；不能仅凭角色自述复原该局的全部权限与执行频率。|
|LjkQ4fYp|wanderer_strings.xml；backstory_a.spc_wanderer_aserai_4|A|巷区守护者的社区地位与保护职责|对应 key 存在于简中表，英文 protector 译为“守护者”；正文统一使用“阿塞莱巷区守护者”，不另造“保护者”作为官方术语。|
|Z8TfQDSV|wanderer_strings.xml；backstory_b.spc_wanderer_aserai_4|A|守护者拒绝卫队长要求掩盖暴力、提供居民情报|对应 key 存在于简中表，仍为跨文化比较材料，不能直接移植为帝国制度。|
|PWpTT0NM|wanderer_strings.xml；backstory_c.spc_wanderer_aserai_4|A|守护者在社区信任与官员威胁之间作出选择并离开|对应 key 存在于简中表；属于同一角色故事的连续片段，不是独立互证。|
|R9KivNZ6|wanderer_strings.xml；backstory_a.spc_wanderer_empire_6|A|拉狄摩斯的追随者来自信仰、债务与受压迫感|对应 key 存在于简中表；只能作为前追随者叙述的起始部分。|
|7JMaPpkN|wanderer_strings.xml；backstory_b.spc_wanderer_empire_6|A|真理之国开始向村庄收“税”、向商人和领主收保护费，并杀害抱怨者|对应 key 存在于简中表，文本译名为“真理之国”；不得与火焰余烬合并。|
|7caHipXX|wanderer_strings.xml；backstory_c.spc_wanderer_empire_6|A|帝国第三支部队摧毁该组织，旧成员进入领主随从或被监禁|对应 key 存在于简中表；与前两条属于同一角色故事，不构成独立互证。|
|QNVJgFbF|companion_strings.xml；str_npc_backstory_d.6|A|“holy poverty”与组织靠捐献维持生活的并置|对应 key 存在于简中表，但译文“以朝圣的名义诱骗佃农财物”有实质语义偏移；正文以英文解释。|
|rGXdJybe|settlements.xml；Settlement town_ES3|S：聚落地志|波罗斯的自治、牲畜盗窃、血仇及双方邀请后才介入的地方仲裁|英文 key 存在于 settlements.xml，但在本轮所附 std_settlements_xml-zho-CN.xml 中未找到对应 key。项目百科 encyclopedia-zh-cn.md 含《波罗斯》中文条目，故仅作为辅助中文文本；该条目将 “Livestock rustling and blood feuds are common here” 写成“嘶鸣的牲畜和流血的斗殴在此地成了一道靓丽的风景线”，未保留“牲畜盗窃／血仇常见”的具体含义。正文以英文为主证，并将该中文文本的来源链标为待进一步核对。|

**证据类型说明**：F = faction description（派系简介）；A = autobiographical/character narrative（角色自述或角色背景）；S = settlement description（聚落地志）。这些类别说明文本体裁，不代表其叙述已被独立档案证实。

## 二、四项关键本地化裁决

### 1. 官方名称与分析用语

- Hidden Hand → “秘密之手”。
- Eleftheroi → “自由民”；该派系简介正文另称“自由民，又名厄琉忒耳”，但派系显示名本身是“自由民”。
- Brotherhood of the Woods → “绿林兄弟会”。
- Embers of the Flame → “火焰余烬”。
- Legion of the Betrayed → “被弃者军团”。
- Bureau of Barbarian Affairs → 角色故事简中为“蛮族事务局”。
- Kingdom of Truth → 角色故事简中为“真理之国”。
- Aserai alley protector → “守护者”。

正文使用这些官方简中名称；涉及制度性质时优先保留英文原文的语义强度，不以中文译文额外添加法律或经济事实。

### 2. “retinues” 不宜直接定译为“私兵”

自由民英文原文称其年轻人被纳入 “the retinues of archons and emperors”；对应简中将其译作“执政官和皇帝们的私兵”。“私兵”比英文 retinues 的语义更具体，容易让读者预先认定其法律身份与军事组织形式。论文因此用“随从队伍”，并把其是否构成正式私兵留作未决问题。

### 3. “holy poverty” 的讽刺结构与译文偏移

QNVJgFbF 将“白天靠捐献生活、夜晚躲避地方贵族”与劝说地主佃户接受 “holy poverty” 并置，形成明显的讽刺性自我暴露：一个依赖他人供养的宗教团体，劝导地主的佃户走向被神圣化的贫困，暗示宗教动员可能改变佃户的财产、劳动与对地主的依附关系，并使组织自身从中获益。把它解释为对宗教名义下攫取佃户资产的讽刺有文本依据，但原文没有直接叙述某项具体盗窃、诈骗手段或实际财物流向，因此应写成讽刺性暗示，而不是已经证实的诈骗事实。

官方简中“以朝圣的名义诱骗佃农财物”加入英文没有的“朝圣”，并把复杂的阶级讽刺简化为直接骗财，反而弱化了原句中“靠捐献维持自身，却劝佃户接受神圣贫困”的矛盾结构。

### 4. 波罗斯的中文条目不能当作当前语言表的直接命中

英文 key rGXdJybe 在 settlements.xml 中存在；当前附件中的 std_settlements_xml-zho-CN.xml 没有该 key。encyclopedia-zh-cn.md 的头部说明其聚落描述由 SandBox 简中语言表解析而来，并标注 Bannerlord v1.4.8.119303，但这条特定描述的当前源键对应关系仍未在随附语言表中复现。因此：
- “波罗斯”作为中文地名，采用项目百科条目；
- 关于自治、牲畜盗窃、血仇和仲裁的历史解释，以英文 rGXdJybe 为主；
- 不声称该中文段落已在本轮对应语言表中逐键核实；
- 将该差异列为待追查的版本／提取链问题。

## 三、源文件版本与校验

项目百科头部标注：Bannerlord v1.4.8.119303。以下 SHA-256 均由本轮项目附件直接计算。它们证明当前工作所读字节的身份，不证明这些文件是 2026 年最新客户端版本。

### 1. 归档包

|附件|SHA-256|
|---|---|
|SandBox.zip|54c358e5b318ffeda8a69ce41a7e665f3b9bef06a6e49b142a972c80ea9c1d55|
|Native.zip|ae546052bc2184bb6d4a2cbc9f74a15f5d009285c48026a55775233a4dc4058c|
|SandBoxCore.zip|a98810bfd5ddaa6d7b8b8927754a0159fed751eff672aef57613417c7284e642|
|NavalDLC.zip|e41ad1c75665e736cad7d02319193a2cc6e0ed68e8bf2e44e1f151b62020b468|
|StoryMode.zip|ad91692d499e505ad1ec9955d444d3cacdbe3cd058c72b6cfa0d33190335fa6f|
|encyclopedia-zh-cn.md|33a6470bb184f16adca9f7078a1e841daac50d7f51bc9b9877f13d97973ddb6c|

### 2. 本文使用的英文源 XML

|文件|SHA-256|
|---|---|
|SandBox/ModuleData/spclans.xml|318afe49eb3a7e4b7b92877da58c69af5571925b31e13c0a3851ba995e47b070|
|SandBox/ModuleData/wanderer_strings.xml|5ba4524baef253eec8b57f2024e57f4f62b62d1c2266e178e183fc6ff8dd2c0d|
|SandBox/ModuleData/companion_strings.xml|9c4ca26f9b3776e0219cf52114f0641a5b335dd12620fac7e1ecca6b2580fafc|
|SandBox/ModuleData/settlements.xml|e92bb2079526dcc4a125b6a7ae21b76240e5176d143aca98d083be9ce8c32524|

### 3. 对应简中语言表

|文件|SHA-256|
|---|---|
|std_spclans_xml-zho-CN.xml|ac150f1a3fdb7e7b3490ae311979be72ae57e37091092031c94e3ab2138781aa|
|std_wanderer_strings_xml-zho-CN.xml|97fa0e6b04e5591ec3466722fadb49d289b9b09839e7bb2d947f3eb45f9c70dd|
|std_companion_strings_xml-zho-CN.xml|37ca9655847d931a8d2382f35e931384b00949ddc4dffc8994965a1972147952|
|std_settlements_xml-zho-CN.xml|46df7c77c4fa184d1c67c3dc5881f1098c3b6842ae051a188debd41af9d95aeb|

## 四、审计裁决

1. 本文主要英文 source key 均在随附 SandBox v1.4.8 英文 XML 中直接命中。
2. 官方简中名称按可直接命中的语言表核定；波罗斯描述文本的对应关系单独标注为未完成的本地化来源链核查。
3. 对 “holy poverty” 与 retinues 的解释以英文为准；简中用于校勘，不允许其新增语义反向改写英文证据。
4. 本文仍是机制解释型候选稿，不能据此量化地方治理模式的普遍程度，也不申请 H 编号。