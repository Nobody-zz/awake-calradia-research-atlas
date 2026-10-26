# CHC-EMP-GEN｜《帝国官方叙事中的地方权威关系》源级与本地化审计 v0.3

**日期**：2026-10-26  
**审计对象**：帝国论文候选稿 v0.9 的13个核心英文 source key。  
**本版用途**：专门核验 v0.9 当前主语料；旧版《帝国地方秩序的多重来源：源级与本地化审计 v0.2》仍保留为早期论文候选稿的历史审计，不用其15键统计替代本版结果。  
**方法**：直接读取项目 SandBox v1.4.8.119303 归档中的英文 XML、对应官方简体中文语言表，并以项目上传的 `encyclopedia-zh-cn.md` 核定城镇中文主名。此审计核对的是项目归档字节，不代表对2026年最新游戏客户端的重新提取。

## 一、核心 source key 逐键核验

|源键|英文原始文件／记录|类型|英文 XML 命中|对应简中 key 命中|审计说明|
|---|---|---|---|---|---|
|nQOf27Rx|spclans.xml / hidden_hand|派系简介|是|是|秘密之手通过对当局有用而壮大；不等于正式授权。|
|9qAWNBvA|spclans.xml / eleftheroi|派系简介|是|是|自由民的边疆知识、领袖头衔、随从关系与对帝国实际权威的敌意。|
|bhxVA9w7|spclans.xml / legion_of_the_betrayed|派系简介|是|是|常备军废除、执政官私人随从队伍、军团对定期支付与合同的依赖。|
|0FHF0OXK|wanderer_strings.xml / backstory_a.spc_wanderer_empire_10|角色自述|是|是|医生故事开场；须与后续两个 key 作为同一叙事链处理。|
|pzK7TN05|wanderer_strings.xml / backstory_b.spc_wanderer_empire_10|角色自述|是|是|医生关于蛮族事务局扩权与索取病人信息的自述。|
|sfFLudTM|wanderer_strings.xml / backstory_c.spc_wanderer_empire_10|角色自述|是|是|同一医生故事的连续片段，不构成独立互证。|
|LjkQ4fYp|wanderer_strings.xml / backstory_a.spc_wanderer_aserai_4|角色自述|是|是|阿塞莱巷区守护者故事开场；只作跨文化边界案例。|
|Z8TfQDSV|wanderer_strings.xml / backstory_b.spc_wanderer_aserai_4|角色自述|是|是|同一守护者故事的连续片段。|
|PWpTT0NM|wanderer_strings.xml / backstory_c.spc_wanderer_aserai_4|角色自述|是|是|同一守护者故事的连续片段，不构成独立互证。|
|rGXdJybe|settlements.xml / town_ES3（Poros）|聚落地志|是|否|英文原文存在；当前随附的 std_settlements_xml-zho-CN.xml 未找到该 key。项目百科有《波罗斯》中文条目，作为辅助中文文本，不称为语言表逐键命中。|
|YYYxOiCq|settlements.xml / town_EN6（Amprela）|聚落地志|是|是|安普雷拉地志；原文并列边境预警、自由民马弓手与运输线贸易竞争，不足以证明统一指挥链。|
|LqPJY4s9|settlements.xml / town_EN4（Argoron）|聚落地志|是|否|英文原文存在；当前随附的 std_settlements_xml-zho-CN.xml 未找到该 key。项目百科有《阿耳戈隆》中文条目，作为辅助中文文本，不称为语言表逐键命中。|
|8UJ3cPrZ|settlements.xml / town_EN5（Myzea）|聚落地志|是|是|密泽亚地志；不能因其当前家园归属而把李图与多伦托斯家族绑定。|

**核验结果：13/13 个 source key 在对应英文 XML 中命中；11/13 个 key 在本轮可用的对应简中语言表中直接命中。** 缺失的是波罗斯 `rGXdJybe` 与阿耳戈隆 `LqPJY4s9`。两条英文文本均保留为主要史料；项目百科中文仅作辅助本地化文本。

## 二、城镇官方中文名称核定

以下中文主名以项目上传的 `encyclopedia-zh-cn.md` 中相应 `town_*` 条目标题为准。论文正文先用官方中文名，英文名只在首次出现时括注；不得以英文转写或临时译名替代中文主名。

|英文地名|官方中文主名|settlements.xml 记录／source key|中文文本来源状态|
|---|---|---|---|
|Poros|波罗斯|town_ES3 / rGXdJybe|百科有中文条目；对应简中语言表 key 未命中|
|Amprela|安普雷拉|town_EN6 / YYYxOiCq|简中语言表 key 命中|
|Argoron|阿耳戈隆|town_EN4 / LqPJY4s9|百科有中文条目；对应简中语言表 key 未命中|
|Myzea|密泽亚|town_EN5 / 8UJ3cPrZ|简中语言表 key 命中|
|Balgard|巴尔加德|town_S2 / Xom9DeXZ|用于斯特吉亚反例报告；中文名见百科|
|Revyl|雷维尔|town_S7 / T2E4xKVn|用于斯特吉亚反例报告；中文名见百科|
|Sibir|西比尔|town_S6 / PPadNxa6|用于斯特吉亚反例报告；中文名见百科|
|Varcheg|瓦尔切格|town_S1 / i2VkRLBg|用于斯特吉亚反例报告；中文名见百科|
|Varnovapol|瓦尔诺瓦波尔|town_S4 / aTMypBiY|用于斯特吉亚反例报告；中文名见百科|

城镇中文名称的核定与描述文本的逐键本地化命中是两个不同问题。即使某个描述 key 在当前简中语言表中缺失，也不因此否定百科条目中的官方中文城镇名称；反之，不能把百科中文段落误报为该 source key 在语言表中直接命中。

## 三、术语与证据层级

- `retinues`：官方简中将其译为“私兵”，但英文词义更宽。论文采用“随从队伍”，不据此提前认定法定军事身份。
- 波罗斯地志中的 “it is said” 必须保留传闻语气；没有具体判决记录，不能据此复原常设司法机关。
- `rGXdJybe` 与 `LqPJY4s9` 的中文百科文本仅作辅助阅读。解释以英文原文为主，并将本地化来源链的缺口明确列为限制。
- 角色背景中的连续 source key 仍各自属于一个叙事单元，不重复计算为独立互证。

## 四、文件校验

|文件|SHA-256|
|---|---|
|SandBox.zip|54c358e5b318ffeda8a69ce41a7e665f3b9bef06a6e49b142a972c80ea9c1d55|
|encyclopedia-zh-cn.md|33a6470bb184f16adca9f7078a1e841daac50d7f51bc9b9877f13d97973ddb6c|
|SandBox/ModuleData/spclans.xml|318afe49eb3a7e4b7b92877da58c69af5571925b31e13c0a3851ba995e47b070|
|SandBox/ModuleData/wanderer_strings.xml|5ba4524baef253eec8b57f2024e57f4f62b62d1c2266e178e183fc6ff8dd2c0d|
|SandBox/ModuleData/settlements.xml|e92bb2079526dcc4a125b6a7ae21b76240e5176d143aca98d083be9ce8c32524|
|std_spclans_xml-zho-CN.xml|ac150f1a3fdb7e7b3490ae311979be72ae57e37091092031c94e3ab2138781aa|
|std_wanderer_strings_xml-zho-CN.xml|97fa0e6b04e5591ec3466722fadb49d289b9b09839e7bb2d947f3eb45f9c70dd|
|std_settlements_xml-zho-CN.xml|46df7c77c4fa184d1c67c3dc5881f1098c3b6842ae051a188debd41af9d95aeb|

## 五、审计裁决

v0.9 的13个核心英文 source key 与附录一致，均可在对应英文 XML 中定位；11个 key 有对应简中语言表命中，波罗斯和阿耳戈隆两个 key 缺失的状态已明确标注。本文所用城镇中文主名均与项目百科条目标题一致。早期审计 v0.2 的15键统计属于旧版语料，不应被误读为当前13键语料的审计结果。