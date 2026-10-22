# 卡拉迪亚大陆历史研究：官方原始文本资料库

游戏目录：D:\\SteamLibrary\\steamapps\\common\\Mount & Blade II Bannerlord
Steam App ID 261550；本地 Steam buildid 24573425。安装包 package_info.txt 显示 PC@v1.3.4；基础官方模块 SubModule.xml 显示 v1.4.8；NavalDLC 显示 v1.2.8 并要求基础版 v1.4.8。不同版本字段分别记录。
官方模块依 SubModule.xml 的 Official / OfficialOptional 判定；NavalDLC 是 War Sails 模块目录名。第三方模块排除。
资料包含 67 个候选 XML：23 个英文原始 XML、22 个官方英文语言表和 22 个官方简体中文语言表。Languages 根目录是英文覆盖，Languages/CNs 对应 zho-CN。原 XML 路径结构与字符串 ID 保留。目录中另有 CNt、BR、DE、FR、IT、JP、KO、PL、RU、SP、TR 等其他语言译文；本包未复制这些版本。
file_manifest.csv 按文件记录完整源路径、模块相对路径、大小、SHA-256、模块版本、语言、ID 节点数、专题和重复判断。sources/ 为空，故无法与既有研究文件核对重复。

## 英文原始文件及专题

Native：global_strings.xml、module_strings.xml、native_strings.xml（跨模块叙事/百科及通用文字）。
SandBox：world_lore_strings.xml（历史与政治论述）；settlements.xml（聚落背景）；spkingdoms.xml（王国及政治主张）；spclans.xml（家族）；heroes.xml（人物）；concept_strings.xml（百科概念）；comment_strings.xml（人物评论）；companion_strings.xml、wanderer_strings.xml（人物背景）；module_strings.xml（任务/模块文字）。
SandBoxCore：spcultures.xml（文化沿革与社会政治描述）。
StoryMode：module_strings.xml、story_mode_settlements.xml（剧情文本与聚落覆盖）。
NavalDLC / War Sails：settlements.xml、clans.xml、heroes.xml、kingdoms.xml、naval_cultures.xml、naval_dialog_strings.xml、module_strings.xml（海岸聚落、人物/家族/政治实体、文化与海上对话）。

## 初读的本地文本线索（未作外部史实验证）

world_lore_strings.xml 有关于卡拉德人早期政治传统和共和国/帝制的对话；spkingdoms.xml 有关于北方边疆土地、地产阶层和元老院主张，以及西部帝国征服帕拉诸部、通婚与旧语言习俗淡化的叙述；spcultures.xml 有卡拉德人早期居地与无王传统的长描述。War Sails 文件含聚落介绍、人物/家族/王国定义及海上对话，可能形成新增专题材料。需按完整条目和 ID 逐一核对后再引用。

## 搜索边界

已找到优先目标 world_lore_strings.xml、settlements.xml、spkingdoms.xml、spclans.xml、heroes.xml、spcultures.xml；通用 strings 以多个 *_strings.xml 命名存在。War Sails 使用 clans.xml、kingdoms.xml、naval_cultures.xml。只复制史料候选 XML；没有复制游戏原文件以外的改动到安装目录。本包不是所有官方 XML 的完整镜像；语音资产索引与大量非叙事界面 XML 未逐项收录。

原件 SHA-256：42f8f2b43f4451b4f58abbb4c1dfc3858c04c94190d208f0496a46f8056e7d95
原件 Google Drive：https://drive.google.com/file/d/10AOwENJyiakm9d6Bp9QkxvUebdF7uN4k/view
