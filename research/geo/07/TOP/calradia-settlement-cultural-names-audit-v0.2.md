# 卡拉迪亚地名证据底表：现有清单质量审查与 v0.2 登记说明

工作底表 v0.2｜核验日期：2026-10-26｜状态：基础数据审计，未授 H 号

本文件是地名证据底表的质量审查与维护规范，不是独立历史论文。当前正典中文译名不因本轮发现而自动修改。

## 一、质量结论

原 v0.1 的方向正确：不凭想象为每种文化补造一整套城名，并优先记录原文直接出现的名称关系。但它目前只能作为“线索清单”，还不能直接当作可复核的证据底表。主要原因是缺少逐条的稳定 ID、名称键、版本、语言表命中状态和明确的同一地点判定字段；同时把几种证据性质不同的材料放在了同一栏。

本轮保留三组有直接历史名称证据的核心条目：

- Rhotae — Rotash：原文明确把 Rotash 作为该地点先前使用的名称。
- Iyakis — Yachios：原文明确记载该地曾是名为 Yachios 的帝国自治前哨。
- Pravend — Paravenos：原文称 Paravenos 后来成为卡拉德人的首都，并明确说它“如今称为 Pravend”。

需要修正或降级的旧条目：

1. **Charas — Charasea 不得再作为同一地点的异名候选。** Pravend 的描述说 Paravenos 取代 Charasea 成为首都；Charas 则有独立的城镇 ID。现有原文没有把 Charasea 等同于 Charas。两者名称相近不构成同地证据。
2. **Rovalt — Rovalatys 是未解决的文本字段冲突，不是已证实的异名。** 两个版本的聚落主名字段都写 Rovalt，但描述正文开头写 Rovalatys；简中条目名与描述正文也存在相应差异。暂不改动正典中文名。
3. **Sargot 的“设防营地”是词义／地名类型解释，不是另一正式城名。** 原文没有给出该城此前使用的帝国专名。
4. **Akkalat 的 “the White Fortress” 是名称释义，不应另建成一个已证实的平行专名。** 原文把 Akkalat 说成库赛特人使用的称名，但没有给出一个可确认的达西旧名。
5. **Varcheg 的诺德语词源是命名解释，不是保存下来的诺德旧城名。**
6. **Husn Fulq 中的 Fulq／Phalcos 是人物别名。** 该人物别名不能计入城镇异名；它是检索 “also known as” 时需要排除的反例。

## 二、版本与原始资料覆盖

### 2.1 聚落记录数量

直接解析归档的官方 XML：

| 项目 | SandBox v1.4.8.119303 | NavalDLC v1.2.8 |
|---|---:|---:|
| Settlement 记录总数 | 493 | 540 |
| 城镇 | 53 | 57 |
| 城堡 | 67 | 76 |
| 城堡村庄 | 132 | 150 |
| 村庄 | 141 | 157 |
| 藏身处等其他记录 | 100 | 100 |

493 个基础版聚落 ID 全部出现在 DLC 文件中；DLC 新增 47 条记录，其中包括 4 座诺德城镇。53 个共同城镇的英文回退主名在两个版本中完全一致，DLC 新增的城镇是 town_N1—town_N4。

对 493 个共同聚落 ID 的字段比较结果：

- 英文回退主名有 3 条记录发生变化：village_V1_2、village_K2_2、castle_village_K7_2。
- 38 条记录的 text key 发生变化。
- 271 条描述文本存在逐字差异。此计数包含文字改写、大小写、标点或其他编辑差异，不等于 271 条世界内部历史事件。
- 493 组 posX/posY 坐标全部不同。
- 共同 ID 的 culture 与 owner 字段未发现变化。

**解释边界：** 地图版本的坐标变化不能直接证明聚落在世界内部迁移；XML 主名或描述改写也不能自动解释为历史上的正式更名。聚落身份、地图位置、控制权和政治共同体变化必须分开登记。

### 2.2 原始文件与可复核路径

当前对照使用的原始路径：

- SandBox 原始聚落：Modules/SandBox/ModuleData/settlements.xml
- SandBox 英文描述表：Modules/SandBox/ModuleData/Languages/std_settlements_xml.xml
- SandBox 简中描述表：Modules/SandBox/ModuleData/Languages/CNs/std_settlements_xml-zho-CN.xml
- NavalDLC 原始聚落：Modules/NavalDLC/ModuleData/settlements.xml
- NavalDLC 英文描述表：Modules/NavalDLC/ModuleData/Languages/std_settlements_xml.xml
- NavalDLC 简中描述表：Modules/NavalDLC/ModuleData/Languages/CNs/std_settlements_xml-zho-CN.xml

归档文件 manifest 中的源文件 SHA-256：

| 文件 | 版本 | SHA-256 |
|---|---|---|
| SandBox settlements.xml | v1.4.8 | E92BB2079526DCC4A125B6A7AE21B76240E5176D143ACA98D083BE9CE8C32524 |
| SandBox std_settlements_xml.xml | v1.4.8 | C3C852527616255B3CD4C10F82A79A7DB231D57D32015615DB8A250D9927CCE4 |
| SandBox std_settlements_xml-zho-CN.xml | v1.4.8 | 46DF7C77C4FA184D1C67C3DC5881F1098C3B6842AE051A188DEBD41AF9D95AEB |
| NavalDLC settlements.xml | v1.2.8 | 4F2924A0B236062D1720E0AD48131D23FA4863E5C0AA7FE475F36B0056B9E436 |
| NavalDLC std_settlements_xml.xml | v1.2.8 | 4F6414EE9C319FFB21E65AABED6DEEB9A21BF8421F10EE167F74755AA54192AD |
| NavalDLC std_settlements_xml-zho-CN.xml | v1.2.8 | 9FFBB92133CF79F8EB13849D27C5A4CFDF24D4F1B958C09519011D07137249BF |

### 2.3 中文名称来源的缺口

项目百科 encyclopedia-zh-cn.md 将基础版聚落中文名称的来源记为 Native 简中 std_common_strings_xml。但这份原始名称表**不在当前 67 文件 manifest，也不在本轮可用的 Native.zip、SandBox.zip、SandBoxCore.zip 或 NavalDLC.zip 中**。现有归档无法直接按原始名称 key 重新核验 53 座基础版城镇的中文主名。

因此：

- 53 座基础版城镇的中文名保留为“项目百科当前名称参考”，不在本轮擅自更改，也不把它们误标为已从原始名称表逐键复核。
- NavalDLC 简中表对 town_N1—town_N4 的名称键有直接匹配：Hvalvik＝瓦尔维克、Gretysfjord＝格雷蒂斯湾、Thronderlag＝特龙德拉格、Hargard＝哈加德。
- SandBox 的 std_settlements_xml 简中表有 3 个聚落名称键，但没有 53 座基础版城镇的名称键；DLC 简中表包含更多新增聚落名称键。
- 53 座基础版城镇中，27 个描述 text key 可在当前 SandBox 英文和简中描述表中直接匹配，另外 26 个没有在所提供语言表中找到对应 key。项目百科中仍存在这些条目的中文描述，但其官方本地化来源需要补齐原始表后才能确认。

以上均为来源状态说明，不是对既有正典中文译名的否定。

## 三、当前优先冲突

### P0：先解决身份与来源问题

| 条目 | 发现 | 当前处理 |
|---|---|---|
| village_V1_2 | 英文回退名从 Etirfurd 变为 Echarfurd；描述被重写；中英文名键仍保留旧简中“埃蒂尔菲德”及旧描述 | 版本级名称／文本重写冲突。保留正典译名，暂不解释为世界内部更名 |
| village_K2_2 与 castle_village_K7_2 | 两条记录的英文名称和描述在两个版本之间互换；中文名称键仍分别保留“帖斯密勒”和“柯希·阿吉克” | 成对审计。先核对 ID 与聚落类型映射，不从坐标差异推断迁移 |
| town_V9 | 主名 Rovalt，描述正文开头 Rovalatys；两个版本均如此 | 未解决的字段拼写冲突，不认定为异名 |
| town_V7 / town_V3 | Charas 与 Charasea 曾被旧清单列为候选关系，但原文只明确说 Paravenos 取代 Charasea 成为首都 | 撤销同地候选关系；保持实体分离 |
| castle_village_ES4_2 | DLC 英文描述已换成另一段内容，简中表仍保留基础版的 Nahr al-Kals／Calsa 河流记述 | 这些异名只可作为基础版来源证据，不能不加版本说明地引用为当前 DLC 英文叙述 |

### P1：名称和本地化差异

| 条目 | 发现 | 当前处理 |
|---|---|---|
| town_N4 Hargard | 名称键给出“哈加德”，同条中文描述却写“阿加尔要塞” | 保留名称键的现行译名；把正文形式记录为本地化不一致 |
| town_N2 Gretysfjord | 官方简中名称键为“格雷蒂斯湾” | 不擅改正典译名；保留英文拼写并标注 fjord／湾的词义差异 |
| town_K3 Makeb | DLC 英文描述删去喀拉卡孜河瀑布／急流句，简中描述仍保留该句 | 当前 DLC 叙述引用必须回到英文版本逐条核对 |
| town_V5 Galend | DLC 英文描述增加 whalers，简中描述仍只提渔民 | 记录为描述本地化漂移，不视为城镇名称变化 |
| town_EW4 Ortysia | Bay of Charas 在 DLC 英文中变为 Gulf of Charas，简中仍作“沙拉斯湾” | 记录文本版本差异，不推断海岸地貌变化 |
| castle_village_A1_2 Fanab | Gulf of Shariz 在 DLC 英文中变为 Bay of Shariz，简中仍作“沙瑞兹海湾” | 保留两个版本的原词，不推断实体变化 |
| castle_village_S6_1 Takor | DLC 英文描述改写，简中仍保留基础版 Mynad Rhyfel／Minador 山口描述 | 这组跨文化地名暂列基础版来源证据 |

完整冲突记录见 settlement-version-conflicts-v0.1.csv。

## 四、区域名称：必须按实体类型分开

区域名称不应简单并入城镇异名。当前区域关系底表至少需要区分以下几组：

- Lake Tanaesis — Tanaz／Tanaz Sea：同一湖泊的草原／库赛特文化称名；“海”是名称形式，不是水体类别变化。
- Bay of Charas — Gulf of Charas：Ortysia 描述中的版本措辞差异。
- Bay of Charas — Shariz／Gulf of Shariz／Bay of Shariz：原文明确将 Shariz 与阿塞莱人对海湾的称呼联系起来；不能把海湾名称与城镇 Charas 合并成一个实体。
- River Miron — Myr：巴旦尼亚人的河流称名。
- Mynad Rhyfel — Minador：基础版描述中同一山口的跨文化称名；DLC 已改写对应英文描述。
- Nahr al-Kals — Calsa：基础版描述中同一河流的阿塞莱语称名与帝国称名；DLC 英文描述已更换。
- Bahr al-Yeshm — Jade Sea：同一内海的阿塞莱语名称及英文释义。
- Calsea — Calsa：不能合并。Calsea 指河流、湖泊与潟湖组成的区域水网；Calsa 是基础版描述中的河流名称。现有简中都译作“卡勒萨”，构成中文字符串碰撞。
- Beinland：诺德人对岛屿的称名，释义为“骸骨之地”；Hvalvik 是岛上的城镇。
- Jumne：诺德人对河流的称名。原文只推测其词源与斯特吉亚语有关，并没有给出另一个可登记的斯特吉亚河名。
- Iltan portages／portages of Iltan：同一冰川湖运输网络的词序变体，不是拉科尼斯湖或塔奈西斯湖本身的异名。
- Transtanaesia：帝国在大湖之外的属地／保护领的历史政治区域名，不是塔奈西斯湖的异名。
- Caldea：连接帝国与阿塞莱土地的河流及咸水潟湖网络，是区域名称，不是城镇异名。
- Tripotamia：塞堤斯河分流形成的河谷名称，不是河流或海域的别名。

详见 regional-name-relations-v0.1.csv。中文词形如果来自项目百科而不是当前原始语言表，必须保留相应来源状态，不得静默升级为已核定官方名称。

## 五、建议统一记录格式

推荐以“一个名称关系一行”的方式建表，而不是把多个异名塞进一个文本单元格。最低字段如下：

| 字段 | 用途 |
|---|---|
| record_id | 关系记录唯一 ID，不代替游戏实体 ID |
| entity_id | 聚落或区域的稳定源 ID；区域尚无游戏 ID 时使用项目内部 ID |
| entity_type | 城镇、城堡、村庄、城堡村庄、岛屿、湖泊、河流、山口、区域水网等 |
| canonical_en | 当前英文原名／源字段回退名 |
| canonical_zh | 当前项目采用的中文显示名；未核验时明确标记状态 |
| variant_en / variant_zh | 旧称、文化称名、释义或文本变体 |
| relation_type | 历史旧称、文化称名、语言转写差异、官方本地化差异、词源释义、字段冲突、同名异地候选等 |
| same_referent_status | 明确同一实体／可能同一实体／未证实／明确不同实体 |
| culture_or_language | 哪一文化或语言使用该称名；没有明确证据则留空 |
| source_version | SandBox v1.4.8.119303、NavalDLC v1.2.8 等 |
| source_path | 原始 XML 或语言表的完整相对路径 |
| settlement_id | 若来自聚落，记录稳定 ID |
| name_key / text_key | 名称键与描述键分列；不得只保存描述键 |
| localization_status | 原始语言表直接匹配、XML fallback、项目百科参考、缺失待核等 |
| evidence_level | A1 明确历史旧称；A2 明确文化称名；B 词义／词源解释；C 未解决字段冲突；X 排除案例 |
| control_change_ref | 单独链接控制权变化记录；无证据则留空 |
| movement_ref | 单独链接聚落迁移记录；无证据则留空 |
| political_change_ref | 单独链接政治共同体变化记录；无证据则留空 |
| notes / reviewed_on | 证据边界、复核日期与后续任务 |

同一名称关系应分别保存英文原文、中文当前参考名、源文件版本和来源键。对“正式更名”的判定，至少需要明确的历史名称措辞或同等强度证据；不能仅凭两个名称拼写相似、中文译名相近或地图坐标变化认定。

## 六、当前交付文件

- calradia-town-name-source-table-v0.2.csv：基础版 53 座城镇与 DLC 4 座新增城镇，共 57 条；保留英文主名、名称键、描述键、语言表命中状态与版本文本差异标记。
- calradia-settlement-name-relations-v0.1.csv：聚落异名、文化称名、词义释义、人物别名排除项及未解决的同地关系候选。
- regional-name-relations-v0.1.csv：跨文化区域称名、版本措辞变体、词义释义及中文名称碰撞。
- settlement-version-conflicts-v0.1.csv：高影响聚落名称／描述键冲突、版本文本差异及处理边界。
- calradia-settlement-cultural-names-inventory-v0.1.md：原始首轮清单，保留作历史记录；其中 Charas—Charasea 候选关系应以本审查的“不合并”结论为准。

## 七、下一步最小闭环

1. 补入 Native 的原始聚落名称语言表（当前归档中缺失），对 53 个基础版城镇中文主名逐键复核；未找到源键的名称继续保留为项目参考，不改正典。
2. 对 village_V1_2、village_K2_2 与 castle_village_K7_2 进行源级身份映射复核，确认是版本数据重分配还是其他定义变化。
3. 对 26 个未在现有 SandBox 语言表中直接命中的城镇中文描述逐项标注来源；没有原始译文时，不声称是官方中文文本。
4. 将同一流程扩展到城堡、村庄、城堡村庄与区域实体；在完成覆盖之前，不把当前 57 城镇表描述为全大陆所有聚落的完整地名表。

本轮未更改任何已核定正典中文译名，未把版本文本差异解释成世界内部历史事件，也未分配 H 编号。