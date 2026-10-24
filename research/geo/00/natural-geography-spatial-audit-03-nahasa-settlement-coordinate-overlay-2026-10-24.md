# 自然地理空间核验备忘录03｜纳哈撒聚落实体坐标与双版本高程图的初步配准

日期：2026-10-24  
版本：v0.1  
性质：空间核验工作备忘录，不是正式论文，不分配CGEO永久论文编号。

Google Drive备忘录：[打开文档](https://docs.google.com/document/d/1bILR1-Lrt7Ai9nrwfECG_ln7jF07KfCj9QMWP9VL0BU/edit)  
Google Drive图件：[纳哈撒聚落实体坐标与双版本高程图对照](https://drive.google.com/file/d/1tZiucv0sSqJ_ED1CNLFfW5DLzgxmTrHO/view)

## 一、核验目的与底本

本轮将官方模块的聚落实体坐标与已归档的双版本高程图面板进行第一次同坐标系叠加，检查纳哈撒地志中最常用的达玛尔河文本锚点是否已经具备足够空间证据。

直接读取并核对的官方文本包：
- SandBox.zip，SHA-256：`54c358e5b318ffeda8a69ce41a7e665f3b9bef06a6e49b142a972c80ea9c1d55`
- NavalDLC.zip，SHA-256：`e41ad1c75665e736cad7d02319193a2cc6e0ed68e8bf2e44e1f151b62020b468`

两个校验值与研究仓库的官方原始资料归档清单一致。本轮直接读取各自的 `ModuleData/settlements.xml`，提取实体ID、英文名称、posX/posY与inline英文fallback文本；图件使用CGEO-MAP-RES-005已经归档的同尺度场景Z高程面板。基础版场景范围为848单位见方，《战帆》为1040单位见方，故两版坐标各自在其版本内解释，不跨版直接相减或视为同址。

## 二、核心地点的官方坐标

| 实体ID | 地点 | SandBox X,Y | NavalDLC X,Y | 官方地志支持的最窄命题 |
| --- | --- | ---: | ---: | --- |
| village_A7_4 | Zalm（扎勒姆） | 390.254, 97.643 | 491.851, 115.267 | 两版均称达玛尔河从纳哈撒进入杰尔贾赖峭壁通道；河流淤泥支持作物生长。 |
| village_A7_3 | Mabwaz（马卜瓦兹） | 413.587, 124.973 | 458.555, 86.089 | 两版settlements.xml内嵌英文均记载达玛尔河穿行峭壁台地及洪泛平原淤泥耕作；其文本键不在两版聚落语言表中。 |
| village_A6_4 | Nahlan（纳赫兰） | 404.877, 160.318 | 484.596, 172.317 | 两版均称位于达玛尔河洪泛平原，洪水反复带来淤泥。 |
| village_A6_1 | Mijayit（米贾伊特） | 410.054, 178.898 | 476.688, 181.518 | 两版均将其置于达玛尔河入耶什姆海的河口／河口附近，强调淤泥沉积。 |
| castle_village_A4_2 | Qidnar（吉德纳尔） | 423.748, 135.275 | 540.980, 110.400 | SandBox称其在达玛尔河洪泛平原；NavalDLC改称位于峭壁陆侧、面向内陆沙漠的岩丘，靠偶发暴雨导水。 |
| village_A7_2 | Bait Hatif（拜特·哈提夫） | 421.323, 106.433 | 448.186, 137.415 | SandBox称其在达玛尔河洪泛平原；NavalDLC改称位于偶发暴雨切割的旱谷，靠井水耕作。 |
| village_A3_1 | Abba（阿卜巴） | 474.865, 101.265 | 551.665, 129.904 | 两版均记载山地径流在地下蓄积并维持绿洲；新版更明确置于峭壁旱谷。 |
| castle_village_A2_2 | Asmait（阿斯麦特） | 622.677, 107.025 | 767.715, 134.089 | 两版均记载拦蓄罕见暴雨产生的山地径流；新版注明红砂岩山地。 |
| village_A8_1 | Ezbet Nahul（艾兹贝特·纳胡勒） | 509.571, 147.601 | 642.167, 146.521 | SandBox强调海上岩石台地与岩隙地下水；NavalDLC将其置于基斯巴滨海小平原，利用蓄水池、井与坡面集雨。 |

## 三、叠加结果与解释边界

1. 现有图件支持完成的是“实体坐标—已归档高程图面板”的版本内可视配准。核心地点在基础版面板上落入纳哈撒南部低起伏至丘陵相接的地形色带；这只提供地形背景，不证明某点位于实际河道、洪泛边缘或海岸线上。
2. 扎勒姆、马卜瓦兹、纳赫兰和米贾伊特在两版文本中保持较稳定的达玛尔河关系描述，但地点的坐标分布不应独立替代河道几何。尤其是马卜瓦兹：官方inline fallback文本是直接证据，却不能据此假定其地理位置已经跨版本同址配准。
3. 吉德纳尔和拜特·哈提夫是最重要的冲突锚点。两者的地志在英文版本之间改变了水文地貌解释；坐标也属于各自版本独立的场景坐标系统。现有材料无法判断这些变化是地图布局调整、聚落实体迁移、叙述重写，还是多因素共同作用，不能写成卡拉迪亚世界内部河道改道或聚落搬迁的历史事件。
4. 图件采用高程可视化面板，而非原始4097×4097栅格直接绘图；其颜色表达相对场景Z值，不是海陆掩膜。不能把低值蓝色当作海洋，也不能把蓝色线条直接当作河流。图件未叠加原始河流Paths、河面网格或经过验证的海岸线。
5. 本轮没有重新解析 `terrain.bin`、`river_triangles.bin`、Flowmap或Navmesh，没有新产出可独立复核的河岸线／洪泛区面积／高程统计。因此本备忘录不宣称完成B类自然水文测绘，只报告坐标字段与现有图件的初步对照。

## 四、研究结论

纳哈撒地志的水文分类已经具备足够官方文字证据，可区分达玛尔河洪泛—淤泥农业、峭壁旱谷的偶发暴雨径流、地下水维持的绿洲以及滨海小平原的多源集水。当前最缺的不是再增加地点描述，而是把这些文字锚点与同版本实际河道、水面和高程几何逐一配准。

下一步优先级：
1. 获取或恢复版本明确的原始河流Paths／水面几何，确认达玛尔河主干与四个稳定文本锚点的相对位置。
2. 单独核验Qidnar与Bait Hatif，不将旧版洪泛平原描述直接移植到NavalDLC。
3. 用同一套方法核验拉科尼斯湖—涅维斯河的实体坐标、河道路径和湖缘；在此之前不发布完整流域拓扑结论。
4. 若原始几何资源不可恢复，保留“官方文本支持、空间配准待核”的状态，不用渲染图补足不存在的精度。

## 五、关联资料

- [自然地理研究问题图谱与证据矩阵](https://docs.google.com/document/d/1IzIEm-CgErZ_REROhHnuXstqvK2vKjPoSXoeyanNFUg/edit)
- [自然地理源级复核备忘录01](https://docs.google.com/document/d/1dlRqWn1R8VzeddpHjIaHdeBz-wk-fuTQLTRxSwg8dNI/edit)
- [自然地理源级复核备忘录02](https://docs.google.com/document/d/12tBeuWmMPpEmnM3rYZCBDj4g638RxY-4AKM0jq_jNas/edit)
- [CGEO-MAP-RES-003高程图块解码与拼接](https://docs.google.com/document/d/1pTiVx_yOJpP6IVFzUcwr2Yeni3m2xb1Y-rbdcNj9HsM/edit)
- [CGEO-MAP-RES-005共同高程尺度与原版河流路径校验](https://docs.google.com/document/d/1nj_dvB-V34xGh5ckDmEohtnzKOlYwu4FcOUErCOs2T8/edit)
- [官方原始资料归档清单与SHA-256](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/source-archives/README.md)
