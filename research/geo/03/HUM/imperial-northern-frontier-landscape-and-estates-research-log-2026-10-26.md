# 卡拉德北方边疆土地改造论文｜研究过程与版本校勘日志

本文件收录论文形成过程中的原始ZIP校勘、项目中文导出来源说明和台账同步记录。它们用于材料追溯，不属于论文正文；论文论证与参考资料以同目录的主论文为准。

## 第二轮原始ZIP版本校勘补充（2026-10-24）

本节优先限定本文中所有未明确标注版本的聚落地志判断。逐键对照SandBox v1.4.8与NavalDLC v1.2.8后，本文的斯塔堤摩斯肥土—麦作结论仅适用于SandBox基础版；NavalDLC同ID描述已改为Miron河支流、含硫温泉与屠龙传说，不再提肥土或麦作，简中却仍保留基础版农业文本。故不能把该农业地貌作为DLC当前地志的事实。

威亚罗斯（village_EN5_1）基础版记山毛榉/橡树林坡地与传统帝国骑兵育马场；DLC改写为东部Myzead密林谷地，并明确由退役帝国军官创办育马场。俄耳特拉（village_EN5_2）在DLC中仅改为向南眺望Myzead，steppe stock育种和向帝国骑兵供马仍保留，但简中仍误译为“牧草”。阿瓦辛顿（village_EN6_1）仍记清灌丛、桑树与养蚕，DLC只重写其在Myzead的区位描述，简中未同步。

因此本文的“边疆土地改造与军马供应”模型仍可作为基础版文本的解释；涉及DLC现行地志时，必须分别登记版本，不将Stathymos的基础版粮食叙述或Vealos的“传统马场”说法无条件移植到DLC层。完整键级对照见[聚落文本版本与官方简中同步审计](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/03/HUM/settlement-text-version-and-localization-audit-2026-10-24.md)。

### 项目中文导出来源补充（2026-10-24）

本稿引用的萨涅俄帕（town_EN3）、阿耳戈隆（town_EN4）、居摩斯（village_EN1_3）和阿拉堤斯（village_EN4_2）属于项目导出中文存在、但其settlements.xml文本键在SandBox与NavalDLC英文/简中聚落语言表中均缺失的记录（来源审计LOC-03、LOC-04、LOC-27、LOC-28）。其英文fallback仍可直接从原始settlements.xml核对；对应中文段落的导出来源/版本未决，本文不将其当作已核验的官方同键译文。


## 第三轮证据台账同步（2026-10-24）

**涅俄科律斯（Neocorys，`village_EW2_2`）**的基础版与NavalDLC英文均记当地林地近期被清除，并写道：“The local landowners have established stud farms, supplying horses to the imperial cavalry.” 现补录为IMP-07、绑定C-40，版本审计为V-39。该条直接支持一个地方性的“清林地景—地主育马场—帝国骑兵供马”联系；它不能证明具体劳动者、土地权属、价格、数量、税役或全帝国统一军马制度。中文显示名“涅俄科律斯”见于项目百科导出，独立名称键未由当前归档复现；描述文本键本身有官方英汉同键。

**福林（Forin，`castle_village_S2_2`）**的两版英文均写道：“Landowners here have turned forest-land into pasture for horses.” 现补录为斯特吉亚比较证据STU-01、绑定C-41、版本审计为V-38。NavalDLC改写其河流、草坡和森林边缘的地点描述，但保留地主把林地转为马匹牧场的关系。它没有明确马匹买方或军队供应对象，只能作为土地利用的跨区域对照。该实体实际使用文本键`Settlements.Settlement.text.village_S1_2`，与`castle_village_S2_2`实体ID不一致；“福林”见于官方简中描述正文，独立名称键未由当前归档复现。
