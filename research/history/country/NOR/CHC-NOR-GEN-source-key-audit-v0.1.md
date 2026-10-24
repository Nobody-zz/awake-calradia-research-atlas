# CHC-NOR-GEN｜第一批关系卡与时空骨架源键审计

版本：v0.1｜2026-10-24  
范围：CHC-NOR-GEN 第一批21张关系卡 v0.1 与时间—空间骨架 v0.1 所用源键。  
资料底本：项目中上传的 Native、SandBoxCore、SandBox、StoryMode、NavalDLC 官方模块 ZIP；现行对照版本依既有档案记录为 Bannerlord v1.4.8 / War Sails v1.2.8。官方简体中文地名另以已上传的 encyclopedia-zh-cn.md 复核。

## 一、审计结论

- 在第一批关系卡与时间—空间骨架的合并范围内，识别出 **65 个唯一源键**。65 个键均在对应官方英文与官方简体中文语言表中找到精确 ID。
- 其中 **64 个键**可在随附原始 XML 的属性中直接追溯到 {=key} 引用；**bLTkig9T** 的英文/中文字符串存在于 NavalDLC 的 XSLT 命名文化语言表，但在本次包含的原始 XML 中未找到直接 {=bLTkig9T} 引用。暂记为“译文可核、直接源链待追”，不等于断言它没有来源。
- v0.1 中 **aTMypBi** 是笔误；实际源键为 **aTMypBiY**，对应瓦尔诺瓦波尔。随附语言表没有精确的七字符键 aTMypBi。
- **6 个键**同时出现在 SandBox 与 NavalDLC 的聚落源文件和两套语言表中：aTMypBiY、PPadNxa6、i2VkRLBg、1SnAH5K8、QD3oaaNK、Xom9DeXZ。它们是跨模块复用的键和版本差异，不是六组额外独立证据。
- 最重要的实质性校勘不是拼写，而是当前 NavalDLC 英文对 **西比尔、卡·班塞斯、巴尔加德**的地形或历史措辞有修订，而官方简中仍保留 SandBox 旧版文字。相关历史解释以当前 NavalDLC 英文为语义基准，中文差异必须明确登记。

## 二、源文件路径与语言表规则

| 来源类型 | 英文原始文件 | 官方英文语言表 | 官方简中语言表 |
| --- | --- | --- | --- |
| 王国沿革 | NavalDLC/kingdoms.xml | NavalDLC/Languages/std_kingdoms_xml.xml | NavalDLC/Languages/CNs/std_kingdoms_xml-zho-CN.xml |
| 人物传记 | NavalDLC/heroes.xml | NavalDLC/Languages/std_heroes_xml.xml | NavalDLC/Languages/CNs/std_heroes_xml-zho-CN.xml |
| 聚落地志 | NavalDLC/settlements.xml | NavalDLC/Languages/std_settlements_xml.xml | NavalDLC/Languages/CNs/std_settlements_xml-zho-CN.xml |
| 海上劳动者/流浪者背景 | NavalDLC/naval_dialog_strings.xml | NavalDLC/Languages/std_naval_dialog_strings_xml.xml | NavalDLC/Languages/CNs/std_naval_dialog_strings_xml-zho-CN.xml |
| 诺德文化描述 | 直接源 XML 引用未在随附包中闭合 | NavalDLC/Languages/std_NavalDLC_SandBoxCore_SPCultures_xslt.xml | NavalDLC/Languages/CNs/std_NavalDLC_SandBoxCore_SPCultures_xslt-zho-CN.xml |
| 六个跨模块聚落键 | SandBox/settlements.xml 与 NavalDLC/settlements.xml 均有同键 | 两模块各自的 Languages/std_settlements_xml.xml | 两模块各自的 Languages/CNs/std_settlements_xml-zho-CN.xml |

## 三、关系卡逐卡源键登记

| 关系卡 | 主要源键 | 源文件定位 |
| --- | --- | --- |
| 01 北方海岸与多种生计网络 | bLTkig9T、danasORQ、m6ZgnpN9；资源例证 azr733J3、EaH59vf8、h5tD3Cjj、LkKDVSJa、TKeLjx14、ozyk0Toa | 文化 XSLT 语言表；NavalDLC naval_dialog_strings.xml、kingdoms.xml、settlements.xml |
| 02 格雷蒂斯湾季节市场与地方雅尔权力 | nxmX99pO | NavalDLC settlements.xml |
| 03 特龙德拉格集会与王廷咨询圈 | Lg5rbZse | NavalDLC settlements.xml |
| 04 阿格尔特公共会集与聚落形成 | j84R3OFX | NavalDLC settlements.xml |
| 05 哈加德东向扩展与朱姆内多族群边疆 | zh2tG1MX、PG95aHx1、gGLcvhD9、DN6XgaS3 | NavalDLC settlements.xml、naval_dialog_strings.xml |
| 06 瓦尔维克人口增长、气候与移居 | Zn9NwSTf；内陆定居参照 yowxgqGD、INqm4EHB、hBOy8ZUM | NavalDLC settlements.xml |
| 07 帝国服役财富与沃尔比约恩的统一 | m6ZgnpN9、wKMRsw16 | NavalDLC kingdoms.xml、heroes.xml |
| 08 圭卡的雅尔资格与精英重组 | GPf0avBi | NavalDLC heroes.xml |
| 09 瓦格纳菲特排水、授地与粮食 | fVkcvgSc | NavalDLC settlements.xml |
| 10 贝恩兰战败、婚盟与地方不满 | 82aSnTOv | NavalDLC heroes.xml |
| 11 Thing 裁决、执行与财富门槛 | FVwyrKBh、ijmUcJWt、KfUc1Hhl、97mvKD9y | NavalDLC naval_dialog_strings.xml |
| 12 村庄派役与雅尔家内劳动 | bYjzSZeE、vPNcuore、hs9ntbwB | NavalDLC naval_dialog_strings.xml |
| 13 合作捕鲸与捕获物争议 | R2LtaPrL、GgUnrDeT、HZKEfJ3q | NavalDLC naval_dialog_strings.xml |
| 14 家户财产、私人船只与海上武装 | ZlbiEKZL、d5lpGY8m、Gtdo9T3r、aEEnTzJY、l0jyALdX | NavalDLC naval_dialog_strings.xml |
| 15 瓦尔诺瓦波尔与西比尔的毛皮网络 | aTMypBiY、PPadNxa6 | SandBox 与 NavalDLC settlements.xml；使用当前 DLC 英文时优先 NavalDLC 版本 |
| 16 瓦尔切格的独立臣属关系 | i2VkRLBg | SandBox 与 NavalDLC settlements.xml |
| 17 罗瓦拉堤斯与卡·班塞斯的诺德活动 | 1SnAH5K8、QD3oaaNK | SandBox 与 NavalDLC settlements.xml；卡·班塞斯英文在 NavalDLC 中有实质性改写 |
| 18 朱姆内水手在库赛特可汗麾下受雇 | DtEBwPpJ、HTe5X0E5、p4OvT9BS | NavalDLC naval_dialog_strings.xml |
| 19 诺德水手的帝国海军经历与潘德拉克记忆 | iyfKyaRB、W01GTKJa、Y1fwBgHt、g0mUObp7 | NavalDLC naval_dialog_strings.xml |
| 20 地方圣地、资源利用与王朝政治 | mSaQ0Cof、Y5YbDNKp、KtN9VSiR、OAvlqAql | NavalDLC settlements.xml、heroes.xml |
| 21 王国纽带脆弱与征服策略 | m6ZgnpN9、Bule74H4 | NavalDLC kingdoms.xml、heroes.xml |

## 四、时间—空间骨架的补充锚点

以下键用于扩展区域覆盖，不替代逐卡论证：0kDUOy2G（于利克舍恩）、rKW7FqWa（米兹卡格）、2pt8EBsS（哈卡许斯）、4fLQlZya（盖于斯达尔）、DJCei132、PKlv8jCB、Xom9DeXZ（巴尔加德）、yOezgAaK（拉萨霍夫）、dVSR4l4D（夏尔韦德），以及前表列出的贝恩兰和朱姆内河谷聚落。以上均有相应 NavalDLC 英文与官方简中语言表条目；Xom9DeXZ 同时存在于 SandBox。

## 五、版本与翻译差异：逐条保留

### 1. aTMypBiY｜瓦尔诺瓦波尔

- SandBox 与 NavalDLC 都有该键，主要叙事一致：诺德人夺取该城，作为扩大对斯特吉亚毛皮贸易影响力的基地。
- 英文只有大小写等编辑差异，简中描述相同。
- 不是独立互证；v0.1 的 aTMypBi 为笔误。

### 2. PPadNxa6｜西比尔

- SandBox 英文：Sibir was founded in a dark valley amid the Chertyg mountains...
- NavalDLC 英文：Sibir was founded on the seaward slopes of the Chertyg Mountains...
- SandBox 与 NavalDLC 的官方简中都仍写“在车尔特格山脉的一处幽谷中建立了西比尔”，没有反映当前 DLC 英文的“临海坡地”。
- 因此，关于西比尔的精确地形位置不能只照抄官方简中；应按当前 NavalDLC 英文记录，并把翻译滞后列为已核问题。

### 3. i2VkRLBg｜瓦尔切格

- 两模块版本的核心叙事一致：诺德创立者为与巴旦尼亚内陆贸易而臣属于至高王，卷入当地政治后被斯特吉亚军队击败，城镇被对方索取。
- NavalDLC 英文做了轻微编辑，不构成独立证据，也没有改变主要因果关系。

### 4. 1SnAH5K8｜罗瓦拉堤斯

- 两模块版本的主要叙事一致：诺德移民因银矿与毛皮财富传闻涌入；在瓦兰迪亚入侵前，诺德人口已多于卡拉德人。
- 英文编辑差异主要是地名大小写，不改变当前可支持的结论。

### 5. QD3oaaNK｜卡·班塞斯

- SandBox 英文旧版开头将卡·班塞斯写成位于高崖上，可望见曾属巴旦尼亚、现由斯特吉亚人与瓦兰迪亚人控制的土地；并称高王蒙的船队传说仍在当地流传。
- NavalDLC 英文将其改写为：沿海氏族声称巴旦尼亚祖先曾跨水迁居；该海域旧称 Muir Mon，如今称 Muir Gal（“外国人的海”）；现今更可能看到诺德冒险者与雇佣兵加入斯特吉亚人、瓦兰迪亚人及其他势力向巴旦尼亚腹地推进。
- 两模块简中仍保留 SandBox 旧版的开头。因此，中文表中的“曾属巴旦尼亚、现由瓦兰迪亚人与斯特吉亚人占领”不是当前 NavalDLC 英文的对应句。
- 此修订同时涉及空间记忆、沿海族群迁徙传说和现时雇佣活动，须作为版本变化登记，不应把旧中文和当前英文拼成一段单一叙事。

### 6. Xom9DeXZ｜巴尔加德

- SandBox 英文称巴尔加德位于 Mazopor Bay，创立者来自 Nordlands。
- NavalDLC 英文改为 Byalic Sea，创立者来自 Nordvyg。
- 官方简中仍为“马佐波尔湾”和“诺德的移民们”，没有反映英文更新。
- 此差异直接影响北方沿海与诺德—斯特吉亚接触地带的空间定位。现阶段以 NavalDLC 英文为当前文本基线，不能把两个水域名称当作已被证实的历史变迁；应先查明这是有意修订还是资料不一致。

## 六、语义审计中的其他高优先级修正

1. **沃尔比约恩的服役身份**：m6ZgnpN9 称其在帝国 Vaegar Guard 服役十年；wKMRsw16 称其作为 mercenary 为帝国效力。两种说法可兼容，但现有文本不足以确定该卫队的组织属性，更没有说明其巨额财富来自何种具体收入。
2. **圭卡案的代词指向**：GPf0avBi 及其官方简中都更倾向于怀疑圭卡参与叔父遇害并被诺德维格统一派收买。不能把这条文本改写为沃尔比约恩收买杀手或策划谋杀。
3. **特龙德拉格的统治者单复数**：Lg5rbZse 英文为 “the Nord king”，官方简中为“诺德的国王们”。解释政治参与和王权结构时以英文单数为基准，不以中文复数推断集体王权。
4. **阿格尔特的争议性质**：j84R3OFX 英文为 “claims and feuds”，官方简中为“纠纷和争执”。没有充分依据把 claims 限定为土地请求。
5. **伊丽卡的政治行为语气**：OAvlqAql 的 “machinations” 带有权谋、暗中筹划的负面意味，简中“运筹帷幄”语气较中性。可以记录叙述者的怀疑性框架，但不能由一个词推出具体谋杀或仪式细节。

## 七、流浪者背景字符串的证据单位

naval_dialog_strings.xml 中的多条 key 不是多份独立证词，而是同一 backstory 的连续段落：

- spc_wanderer_nord_2n：PG95aHx1 → gGLcvhD9 → DN6XgaS3（朱姆内迁居、瓦尼人土地使用协议、狩猎冲突及婚姻暴力）。
- spc_wanderer_nord_3n：FVwyrKBh → ijmUcJWt → KfUc1Hhl → 97mvKD9y（贝恩兰定居、Thing 裁决、执行成本与债务）。
- spc_wanderer_nord_4n：bYjzSZeE → vPNcuore → hs9ntbwB（村庄派役、雅尔家内铁匠劳动、欠薪与逃离）。
- spc_wanderer_nord_1n：R2LtaPrL → GgUnrDeT → HZKEfJ3q（女性捕鲸者的家族合作、鲸尸争议与离村）。
- spc_wanderer_nord_0n：ZlbiEKZL → d5lpGY8m → Gtdo9T3r（家户继承争端、私人船只、劫掠与跨国雇佣）。
- spc_wanderer_nord_7n：aEEnTzJY → l0jyALdX（雅尔之子与伙伴的海上掠劫、以付款避免冲突）。
- spc_wanderer_nord_5n：DtEBwPpJ → HTe5X0E5 → p4OvT9BS（朱姆内舵手为可汗效力、河湖作战与战利品损失）。
- spc_wanderer_nord_6n：前置 g0mUObp7 与 iyfKyaRB → W01GTKJa → Y1fwBgHt（帝国海军职业经历、晋升、潘德拉克后的军饷与纪律问题）。

这些叙述对社会史有价值，但均为游戏人物背景文本；其价值在于提供官方设定中的社会机制与个人记忆，不等于多份独立档案互相印证。

## 八、后续动作

1. 将本审计的键与版本差异回写关系卡 v0.2 和时间—空间骨架 v0.2。
2. 与 STU 线核对巴尔加德与瓦尔切格的地名、空间与王朝起源叙事；与 BAT 线核对卡·班塞斯及巴旦尼亚沿海记忆；与 VLA 线核对罗瓦拉堤斯和雇佣活动。
3. 对 bLTkig9T 的 XSLT 源链保留待查项，不阻塞其他已闭合键的研究。
4. 不把模块重复文本当作独立互证，不修改公共 I/Q，不预占 H 编号。