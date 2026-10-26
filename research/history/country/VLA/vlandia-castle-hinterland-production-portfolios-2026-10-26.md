# 瓦兰迪亚城堡辖村的生产组合与领地结构：从聚落配置到历史推论边界

**CHC-VLA-GEN｜独立经济史／配置审计工作稿 v0.2｜2026-10-26｜不分配 H 编号｜修订奥斯里克宗主权句法表述**

## 摘要

本稿接续瓦兰迪亚研究的第三优先任务：把地志中的经济叙述与游戏实际聚落配置分开核验。直接读取既有 SandBox.zip、NavalDLC.zip 中的 `settlements.xml`，并用 SandBox 的 `spclans.xml` 及同键官方简中氏族表核对初始配置。SandBox 源文件中可识别出 **8座瓦兰迪亚城堡与14个绑定于这些城堡的辖村**。每个辖村的 `Village.bound` 指向相应城堡，城堡 `owner` 指向具体氏族；这些是初始游戏配置事实，不是奥斯里克时代的封地授予记录。

辖村的生产类型构成多种组合：粮食与橄榄、海产与马匹、亚麻与黏土、橄榄与铁矿、粮食与葡萄等。它们支持一个可检验的工作假说：瓦兰迪亚领主的领地基础可以从“单一庄园”以外的资源组合来研究。但由于现有源文件没有给出产量、租税、劳动义务或收入分配，不能据此证明各城堡实际掌握了多少经济收益，也不能把 `hearth` 直接解释为人口。

《战帆》源文件还改变了3个瓦兰迪亚城堡辖村的 `village_type`：Drapand 从渔村转为捕鲸村、Ormanfard 从葡萄园转为麦田、Deriat 从捕猎村转为养猪村。它们与英文地志改写大体呼应，但 Deriat 沿用旧文本键，官方简中仍显示旧捕猎描述。此项差异应视为版本配置／本地化问题，而不是故事世界内发生过经济转型的历史证据。

## 一、材料与方法

直接读取项目 Library 中已有的官方模块归档，不重新上传或公开原始 ZIP。

| 文件 | SHA-256 |
|---|---|
| SandBox.zip | `54c358e5b318ffeda8a69ce41a7e665f3b9bef06a6e49b142a972c80ea9c1d55` |
| NavalDLC.zip | `e41ad1c75665e736cad7d02319193a2cc6e0ed68e8bf2e44e1f151b62020b468` |
| SandBox `settlements.xml` | `e92bb2079526dcc4a125b6a7ae21b76240e5176d143aca98d083be9ce8c32524` |
| NavalDLC `settlements.xml` | `4f2924a0b236062d1720e0ad48131d23fa4863e5c0aa7fe475f36b0056b9e436` |
| SandBox `spclans.xml` | `318afe49eb3a7e4b7b92877da58c69af5571925b31e13c0a3851ba995e47b070` |

比较对象为 SandBox 中的 `castle_V1`—`castle_V8` 及其 `castle_village_V*` 辖村，并与 NavalDLC 中同 ID 对照。氏族中文名按 SandBox `std_spclans_xml-zho-CN.xml` 同键核对。表内城堡和辖村名保留英文源名，避免把地志正文中的中文译名误当作已经独立核验的名称键。

**证据等级：**
- **A-配置事实**：XML 明确记录的聚落 ID、`bound`、`owner`、`village_type`、`hearth` 和文本键。
- **A-地志直陈**：官方英文地志明确讲述的资源、生计或地方记忆；它确认文本说了什么，不保证叙述为中立编年。
- **C-历史解释**：对资源组合、地方权力与国家形成的机制假说。
- **U-未知**：没有来源可确认的实际产量、租税、产权法律、劳役、收入归属或历史授地日期。

## 二、8座城堡与14个辖村：初始配置清单

下表的 `hearth` 是游戏 XML 中的村庄数值字段，不是人口统计。类型名称按 XML 原值保留。

| 城堡 ID | 城堡所属氏族（同键官方简中） | 辖村 ID | SandBox 生产类型 | NavalDLC 生产类型 | hearth |
|---|---|---|---|---|---:|
| `castle_V1` | `clan_vlandia_11` — dey Rothad（戴·洛塔德） | `castle_village_V1_1` Usanc | `olive_trees` | `olive_trees` | 498 |
| `castle_V2` | `clan_vlandia_9` — dey Jelind（戴·热兰） | `castle_village_V2_1` Hongard | `wheat_farm` | `wheat_farm` | 400 |
| `castle_V2` | 同上 | `castle_village_V2_2` Ferton | `olive_trees` | `olive_trees` | 400 |
| `castle_V3` | `clan_vlandia_2` — dey Tihr（戴·提哈） | `castle_village_V3_1` Drapand | `fisherman` | `whaler` | 285 |
| `castle_V3` | 同上 | `castle_village_V3_2` Valanby | `vlandian_horse_ranch` | `vlandian_horse_ranch` | 280 |
| `castle_V4` | `clan_vlandia_10` — dey Folcun（戴·佛尔坎） | `castle_village_V4_1` Ormanfard | `vineyard` | `wheat_farm` | 170 |
| `castle_V5` | `clan_vlandia_5` — dey Gunric（戴·贡里克） | `castle_village_V5_1` Tirby | `flax_plant` | `flax_plant` | 640 |
| `castle_V5` | 同上 | `castle_village_V5_2` Sirindac | `clay_mine` | `clay_mine` | 640 |
| `castle_V6` | `clan_vlandia_6` — dey Valant（戴·瓦朗） | `castle_village_V6_1` Caleus | `flax_plant` | `flax_plant` | 429 |
| `castle_V6` | 同上 | `castle_village_V6_2` Deriat | `trapper` | `swine_farm` | 429 |
| `castle_V7` | `clan_vlandia_1` — dey Meroc（戴·梅罗克） | `castle_village_V7_1` Talivel | `olive_trees` | `olive_trees` | 667 |
| `castle_V7` | 同上 | `castle_village_V7_2` Rodetan | `iron_mine` | `iron_mine` | 264 |
| `castle_V8` | `clan_vlandia_7` — dey Fortes（戴·佛特斯） | `castle_village_V8_1` Verecsand | `wheat_farm` | `wheat_farm` | 230 |
| `castle_V8` | 同上 | `castle_village_V8_2` Marin | `vineyard` | `vineyard` | 341 |

**源级限定：**城堡 `owner` 与辖村的 `bound` 是游戏配置中“谁持有城堡／辖村绑定到哪座城堡”的记录。它们不能证明这些氏族在奥斯里克时代就拥有同样的地产，更不能将当代 `owner` 字段倒推为历史上的原始受封者。城堡 ID 的编号也不表示建造顺序。

## 三、从生产组合到领地经济：可以提出什么问题？

### 3.1 组合而非单一产物

SandBox 的14个辖村中，粮食、橄榄、葡萄、亚麻、黏土、铁矿、渔业／捕鲸、马匹和捕猎／养猪等生计并存。若以城堡为单位观察，出现以下配置组合：

- **Hongard Castle**：小麦与橄榄。
- **Drapand Castle**：海产与马匹养殖；辖村地志分别涉及北方寒流鳕鱼渔场、特朗河口沼泽围场养马。
- **Tirby Castle**：亚麻与黏土。
- **Caleus Castle**：亚麻与捕猎；DLC 配置改为亚麻与养猪。
- **Talivel Castle**：橄榄与铁矿。
- **Verecsand Castle**：小麦与葡萄。
- **Usanc Castle** 与 **Ormanfard Castle** 在 SandBox 中各有一个辖村，前者以橄榄为主，后者以葡萄园为主。

**C级工作假说：**领地的经济基础可以由多种生产活动构成，不能只以单一庄园作物或“骑士土地”概括。粮食、马匹、铁矿与海产也可能与驻军供给、装备维护和港口贸易相联系。

**尚未证明：**每座城堡是否实际从这些生产中征税、各村是否向所属城堡供货、收入是否归城主个人、村庄之间是否存在互补贸易，以及这些配置是否由开发者有意设计为经济组合。XML 中存在绑定关系，不等于存在可见的历史财务账本。

### 3.2 生产类型与地志正文并非同一层证据

- **Drapand**：SandBox 类型为 `fisherman`，NavalDLC 改为 `whaler`；DLC 英文也将鳕鱼渔场扩展为捕猎露脊鲸、黑鲸等远洋活动。新文本键有相应简中译文。这是生产类型与地志叙述同向变化的案例。
- **Ormanfard**：类型由 `vineyard` 改为 `wheat_farm`；DLC 英文改为小麦、大麦与守卫巴旦尼亚山口的村民，新文本键有相应简中译文。
- **Deriat**：类型由 `trapper` 改为 `swine_farm`；英文地志也改为养猪、到高地觅食坚果和根茎，但仍使用旧文本键，DLC 简中继续显示旧的捕河狸、水貂与海豹描述。
- **Sirindac**：类型仍为 `clay_mine`，DLC 地志补入早期淘银、矿脉枯竭及后来主要出口黏土的序列。这里是地志补充资源史，而不是当前生产类型改变。
- **Caleus**：类型仍为 `flax_plant`；地志称当地居民使用瓦兰迪亚、斯特吉亚与巴旦尼亚多种语言。初始配置把它归入瓦兰迪亚文化，但不能因此断言当地语言同质。政治／文化标签与地方人口的语言记忆必须分开。
- **Rodetan**：类型仍为 `iron_mine`，地志称当地铁矿为瓦兰迪亚多处锻炉供应矿石。此句可支持“文本把地方矿业与王国锻造联系起来”的结论，但不能计算矿石量、税收或军事装备份额。

这些例子说明，经济史研究至少要同时保留三个字段：`village_type`（模拟配置）、英文地志（叙述性经济）和官方简中（译文状态）。任何一个字段都不能替代另外两个。

### 3.3 Hearth 不等于人口或产量

初始 XML 中各辖村的 `hearth` 数值介于170与667之间，但这只是游戏配置字段。现有来源没有提供从 hearth 到人口、耕地面积、粮食产量或税收的可靠换算关系。因此本稿不按 hearth 对领地经济实力作数值排名，也不将高值解释为某村历史人口更多。

## 四、与国家形成研究的连接

国家形成总论提出：帝国以土地与头衔替代银币，军事人员定居、耕作并占据部分堡垒；奥斯里克又承认追随者为男爵、伯爵并授予其土地宗主权，以换取战时集结。当前城堡辖村数据能提供的连接有限：

1. **可以连接到“生产性领地”的研究问题。**初始配置显示，城堡及辖村关系与多种资源生产类型并存，支持继续调查领地如何与军役、城市供应和地方生产发生联系。
2. **不能证明“这些城堡就是奥斯里克授地”。**没有有效文本把表中的八座城堡逐一列为奥斯里克授予的土地，也没有早期封地清册或对应日期。
3. **不能证明领主拥有全部生产收益。**`bound` 表示游戏中的辖属关系，未说明租税、地租、市场交易或农民使用权。
4. **不能把 DLC 类型变化写成历史转产。**Drapand、Ormanfard、Deriat 的差异首先是两个模块源文件的模拟配置差异。只有出现独立的故事内时间线证据时，才可进一步讨论其是否代表某种叙事版本重写。

## 五、后续研究问题

- **VLA-ECO01：**能否在其他官方 XML 中找到村庄生产类型对应的实际商品、贸易路线、市场供给或城堡军队消费字段？
- **VLA-ECO02：**地志中“供应王国锻炉”“为城镇提供粮食”等语句，能否与游戏系统的商品配置相互核验？
- **VLA-ECO03：**国王授予领地与城堡辖村的绑定关系之间，是否存在明确的故事内连接？没有连接文本前，不将初始配置视作历史封地清册。
- **VLA-ECO04：**Deriat、Remental 等沿用旧文本键的生产类型／地志冲突，在目标运行时会显示旧简中、英文回退还是其他资源层？需取得完整模块注册与加载证据。
- **VLA-ECO05：**Caleus 的混合语言叙述与其 `Culture.vlandia` 配置如何并存？这可作为政治归属不等于语言同质的案例，但不能据此计算族群比例。

## 六、结论

瓦兰迪亚初始游戏配置中，8座城堡与14个城堡辖村构成了一个可追踪的领地结构；辖村生产类型呈现粮食、橄榄、葡萄、亚麻、黏土、铁矿、马匹与海产等多样组合。它为研究“领主权力如何依托地方生产”提供了结构性线索，却没有提供足以还原税权、租佃制度、人口规模或历史授地时间的资料。

本稿因此将“生产组合”作为下一阶段可证伪的研究假说，而不把它提升为既成历史结论。后续应优先查找商品流通、生产机制与军队供给的可验证字段，并将源文件配置、英文叙述、官方简中与运行时最终状态分别登记。

**归档状态：**本稿归入 CHC-VLA-GEN，不分配 H 编号，不修改中央 S/E/P/D 登记；仅引用原始文件的必要键、字段和校验值，不将用户私人原始 ZIP 复制到公共仓库。
