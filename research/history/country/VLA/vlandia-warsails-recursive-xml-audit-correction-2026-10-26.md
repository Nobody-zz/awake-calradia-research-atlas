# 瓦兰迪亚《战帆》聚落 XML 递归差异复核：原版与 DLC 配置层补记

**CHC-VLA-GEN｜源级审计补记 v0.1｜2026-10-26｜不分配 H 编号**

## 摘要

本补记纠正《战帆》聚落地志异文审计 v0.1 中一项过宽的结论。先前审计准确识别了共同聚落的坐标、地志文本、港口字段与名称值差异，但将“未发现其他 XML 属性值差异”写得过于笼统。重新读取相同归档，并递归比较 `Settlement` 下的 `Components`、`Buildings` 与 `Locations` 后，发现此前未列出的游戏配置差异：6 个聚落的 `Village.village_type` 不同、14 处建筑等级不同、8 处场景名不同，另有 4 处新增 `Location` 子节点及 3 处新增 `Building` 子节点。

这不是对瓦兰迪亚历史年表的新增事件证据，而是原版 SandBox 与 NavalDLC 源文件之间的配置差异。它对研究方法有直接影响：不能只比较地志文字而忽略生产类型、建筑配置与场景注册；同样也不能把模块差异写成卡拉迪亚世界内部发生过的历史变迁。

## 一、来源与复验方法

直接读取用户 Library 中既有的官方模块归档，未重新上传、替换或改写原始资料：

| 归档 | SHA-256 | 项目归档标签 |
|---|---|---|
| `SandBox.zip` | `54c358e5b318ffeda8a69ce41a7e665f3b9bef06a6e49b142a972c80ea9c1d55` | v1.4.8 系列 |
| `NavalDLC.zip` | `e41ad1c75665e736cad7d02319193a2cc6e0ed68e8bf2e44e1f151b62020b468` | v1.2.8 系列 |

本轮实际比较的内层文件及 SHA-256：

- SandBox `Modules/SandBox/ModuleData/settlements.xml`：`e92bb2079526dcc4a125b6a7ae21b76240e5176d143aca98d083be9ce8c32524`
- NavalDLC `Modules/NavalDLC/ModuleData/settlements.xml`：`4f2924a0b236062d1720e0ad48131d23fa4863e5c0aa7fe475f36b0056b9e436`

以上 ZIP 校验值与既有异文审计一致。以两个 `settlements.xml` 中相同的52个瓦兰迪亚聚落 ID 为比较范围，逐项检查顶层 `Settlement` 属性及其嵌套子节点；对 `Village`、`Building`、`Location` 分别核对属性与子节点数量。本文报告的是归档源文件差异，不是游戏运行时最终合并结果。

**版本限制：**归档中没有完整 `SubModule.xml`、模块启用顺序或运行时合并结果，故不能仅凭这两个 XML 判定当前构建实际采用的最终属性。TaleWorlds 的 XML 合并文档说明了托管 XML 可以按唯一属性合并，但通用规则不能代替本次构建的模块注册与运行时证据：https://moddocs.bannerlord.com/bestpractices/merging_module_xml_files_with_native/

## 二、递归复核结果

### 2.1 顶层差异仍成立

此前登记的文件事实保留：

- 52 个共同聚落 ID 的 `posX` 与 `posY` 全部不同；
- 16 个聚落的 `gate_posX` 与 `gate_posY` 不同；
- 12 个聚落在 NavalDLC 中新增 `port_posX`、`port_posY`；
- 35 个聚落的英文地志正文不同；
- 只有 `village_V1_2` 的英文名称值从 `Etirfurd` 改为 `Echarfurd`；
- `owner` 与 `culture` 在52个共同 ID 中未变。

### 2.2 此前遗漏的嵌套差异

| 差异类型 | 数量 | 具体范围 |
|---|---:|---|
| `Village.village_type` | 6 个聚落 | 3 个城堡辖村、3 个普通村庄 |
| `Town/Buildings/Building.level` | 14 处 | `castle_V1`、`castle_V2`、`castle_V6`、`town_V8` |
| `Locations/Location.scene_name` | 8 个聚落 | 主要为村庄场景切换至 NavalDLC 的海上袭击场景变体 |
| `Locations` 子节点数量 | 4 个聚落 | `town_V3`、`town_V5`、`town_V7`、`town_V8` 新增港口位置 |
| `Buildings` 子节点数量 | 3 个聚落 | `town_V3`、`town_V5`、`town_V8` 新增造船厂建筑 |

对14个瓦兰迪亚城堡辖村另行核验，`bound`（所属城堡）、`hearth`（游戏配置中的村庄数值）、`culture` 与所属城堡的 `owner` 均未见差异。这里的 hearth 是游戏数据字段，不能直接换算成历史人口。

### 2.3 生产类型变化清单

| 聚落 ID | SandBox 类型 | NavalDLC 类型 | 对应英文地志变化 |
|---|---|---|---|
| `castle_village_V3_1`（Drapand） | `fisherman` | `whaler` | 从鳕鱼渔场叙述扩展为远洋捕鲸；使用新文本键并有对应新简中译文 |
| `castle_village_V4_1`（Ormanfard） | `vineyard` | `wheat_farm` | 从葡萄梯田与葡萄酒改为小麦、大麦与巴旦尼亚山口警戒；使用新文本键并有对应新简中译文 |
| `castle_village_V6_2`（Deriat） | `trapper` | `swine_farm` | 英文从捕河狸、水貂与海豹改为养猪，但沿用旧文本键，DLC 简中仍是旧捕猎描述 |
| `village_V5_2`（Meroc） | `fisherman` | `whaler` | 英文改为日常捕鱼与高收益远海捕鲸；使用新文本键并有对应新简中译文 |
| `village_V5_3`（Nogrent） | `sheep_farm` | `vineyard` | 英文从放羊改为葡萄酒及渔夫浓汤；使用新文本键并有对应新简中译文 |
| `village_V8_3`（Remental） | `trapper` | `salt_mine` | 英文从毛皮捕猎与森林相对自由改为银矿枯竭后转产盐业，但沿用旧文本键，DLC 简中仍是旧捕猎描述 |

以上六项说明，DLC 不只改写地方史叙述，还修改了游戏为聚落配置的生产类型。四项使用新文本键的类型变化获得了相应新简中译文；Deriat 与 Remental 则出现源文件配置／英文地志已经变化、同键简中仍保留旧描述的情况。**这属于可直接核对的文本与配置不一致，不等于可以断定玩家运行时必然看到哪一版中文。**

### 2.4 建筑等级差异明细

| 聚落 ID | 建筑 ID | SandBox → NavalDLC |
|---|---|---|
| `castle_V1` | `building_castle_guard_house` | 1 → 2 |
| `castle_V2` | `building_castle_fortifications` | 1 → 3 |
| `castle_V2` | `building_castle_barracks` | 0 → 2 |
| `castle_V2` | `building_castle_training_fields` | 0 → 2 |
| `castle_V2` | `building_castle_guard_house` | 0 → 2 |
| `castle_V2` | `building_castle_siege_workshop` | 0 → 1 |
| `castle_V2` | `building_castle_castallans_office` | 0 → 2 |
| `castle_V2` | `building_castle_granary` | 1 → 2 |
| `castle_V2` | `building_castle_craftmans_quarters` | 2 → 0 |
| `castle_V2` | `building_castle_farmlands` | 3 → 0 |
| `castle_V2` | `building_castle_mason` | 1 → 2 |
| `castle_V2` | `building_castle_roads_and_paths` | 2 → 0 |
| `castle_V6` | `building_castle_guard_house` | 1 → 3 |
| `town_V8` | `building_settlement_guard_house` | 1 → 2 |

这是初始建筑配置的差异，不是城堡在故事内实际经历扩建、衰败或战损的证据。尤其不能把 `castle_V2` 多项等级变化写成某场战争后的历史重建。

### 2.5 场景与港口节点差异

8 个 `Location.scene_name` 变化如下：

- `castle_village_V2_1`：`vlandia_village_f` → `vlandia_village_b_navalraid`
- `castle_village_V3_1`：`vlandia_village_i` → `vlandia_village_m_navalraid`
- `castle_village_V7_1`：`vlandia_village_n` → `vlandia_village_b_navalraid`
- `castle_village_V3_2`：`vlandia_village_m` → `vlandia_village_b_navalraid`
- `village_V3_2`：`vlandia_village_m` → `vlandia_village_m_navalraid`
- `village_V3_3`：`vlandia_village_m` → `vlandia_village_b_navalraid`
- `village_V3_4`：`vlandia_village_h` → `vlandia_village_b_navalraid`
- `village_V5_2`：`vlandia_village_m` → `vlandia_village_m_navalraid`

此外，`town_V3`、`town_V5`、`town_V8` 各新增 `building_shipyard`，等级分别为 1、3、1；`town_V3`、`town_V5`、`town_V7`、`town_V8` 各新增 `Location id="port"`，场景为 `vlandia_shipyard`。这些差异与 DLC 的港口、造船及海上袭击玩法配置相符，但没有完整模块注册与运行时验证前，不能据此确认每个点在目标运行模式中均已启用。

## 三、对瓦兰迪亚历史研究的影响

1. **生产经济不能只读地志。** Drapand、Ormanfard、Deriat 的生产类型发生变化；若分析捕鲸、葡萄酒、粮食或养猪的经济意义，必须标明 SandBox 与 NavalDLC 版本，不能把两套配置合并成一份恒定的历史地理。
2. **中文地志不是总能反映英文与配置变化。** Deriat 与 Remental 的同键简中仍保留旧经济叙述。分析时应把英文原文、中文译文与 `village_type` 三列分开记录。
3. **不能将模块差异历史化。** 城堡建筑等级、造船厂与场景节点的变化属于源文件配置事实；它们不能证明世界观中发生过一次扩建、港口启用或海战。
4. **此前的审计结论应作范围限定。** 原附录 E 关于“未发现其他 XML 属性值差异”的说法应修订为：第一轮审计已确认顶层聚落属性的主要差异，但未完整递归覆盖嵌套配置；本补记补齐了可直接复验的嵌套差异。

## 四、后续任务

- 若要确认游戏实际运行时采用的最终属性，需要取得目标构建完整的 `SubModule.xml`、模块启用与加载顺序，以及合并后的对象或实测结果。
- 对瓦兰迪亚经济史，优先在 SandBox 与 NavalDLC 两种配置下分别分析生产类型，不把模拟配置直接等同于历史产量或人口。
- 名称校勘继续维持现有边界：城堡辖村的英文地志中出现的中文译名，不自动等于已验证的独立官方名称键；Caleus 等名称仍需完整 Native 名称语言表才能最终裁定。

**结论：**递归复核没有推翻原审计的顶层坐标、地志和港口差异结果，但补出了对生产类型、城堡建筑、港口与场景有解释价值的嵌套配置差异。后续研究应将“地志叙述”“官方简中翻译”“模拟配置”和“运行时最终状态”作为四个不同层次处理。
