# 自然地理空间核验备忘录07｜《战帆》版达玛尔河走廊的聚落锚点与 River 导航面邻近检验

- 日期：2026-10-26
- 版本：v0.1
- 研究线：卡拉迪亚大陆自然地理
- Google Docs 原件：[打开备忘录](https://docs.google.com/document/d/1tz8Yx-LAb5VgmRS8udpxztet8u0vorIzEYQVgZrhvmA/edit)
- 锚点近邻结果：[CSV](natural-geography-spatial-audit-07-damar-warsails-anchor-results-2026-10-26.csv)
- 前序 Native 识别：[空间核验备忘录06](natural-geography-spatial-audit-06-damar-native-path-identification-2026-10-26.md)

## 一、研究问题与结论

Native 版本已通过原始 `scene.xscene` 路径几何，将内部路径名 `nile` 识别为达玛尔河走廊的强对应。War Sails 的 `Paths` 容器为空，terrain layer / PHYM 中也没有直接命名为 `river` 的层，因此不能沿用 Native 路径 ID 或坐标。本轮改用 NavalDLC 同版 `settlements.xml` 中的官方英文地志与聚落坐标，独立检查 War Sails Navmesh 的 River(11) 面。

扎勒姆、马卜瓦兹、纳赫兰、哈莫沙瓦特、米贾伊特五个达玛尔河锚点到最近 River(11) 导航面距离为 **2.646—4.044 场景单位**；对照地点吉德纳尔、拜特·哈提夫、阿卜巴、阿斯麦特的距离为 **26.315—90.119**。按英文地志的源头至河口顺序连接五个锚点，360 个间距不超过 0.5 场景单位的直线段采样点中，78.33% 距任一 River(11) 面不超过 5 单位，92.22% 不超过 10 单位。

这为“War Sails 的游戏导航水域表示大体沿着达玛尔河地点链分布”提供了独立空间支持；但 River(11) 是游戏导航分类，锚点之间的直线是测试线而非真实河道。当前结论是**游戏地图空间表示与官方达玛尔河锚点高度邻近**，不是已恢复天然河道中心线、河岸或洪泛边界。

## 二、同版官方英文地志与坐标锚点

坐标来自官方 `NavalDLC.zip` 的 `Modules/NavalDLC/ModuleData/settlements.xml`，使用各实体自身的 `posX/posY`。英文原文是地点识别依据，不以简体中文译文替代。

| 地点 | 实体 ID | X | Y | 英文地志定位 |
|---|---|---:|---:|---|
| Zalm / 扎勒姆 | `village_A7_4` | 491.851 | 115.267 | 达玛尔河从纳哈撒沙漠下降、开始穿越杰尔贾赖峭壁的入口 |
| Mabwaz / 马卜瓦兹 | `village_A7_3` | 458.555 | 86.089 | 俯瞰河流穿行台地；农田利用河流洪泛地淤泥 |
| Nahlan / 纳赫兰 | `village_A6_4` | 484.596 | 172.317 | 河流穿越峭壁时的洪泛平原，年度淤泥更新农田 |
| Hamoshawat / 哈莫沙瓦特 | `village_A6_2` | 488.553 | 157.329 | 达玛尔河下游、抵达耶什姆海之前 |
| Mijayit / 米贾伊特 | `village_A6_1` | 476.688 | 181.518 | 达玛尔河进入耶什姆海的河口附近 |

## 三、River(11) 导航面近邻

Navmesh 原始二进制经 RNM1/NMG9 解析：17,424 个顶点、37,747 条边、20,258 个面，其中 River(11) 898 面、NonNavigableRiver(22) 322 面。距离为聚落 `posX/posY` 到同版 River(11) 面多边形的二维最短距离，单位为场景单位。

| 达玛尔河锚点 | 最近 River(11) 面 ID | 最短距离 | 最近点 X,Y | 最近 River 组件面数 |
|---|---:|---:|---|---:|
| Zalm | 8185 | 2.646 | 489.906, 113.473 | 42 |
| Mabwaz | 8201 | 3.214 | 457.876, 89.230 | 32 |
| Nahlan | 510 | 2.858 | 481.774, 172.766 | 42 |
| Hamoshawat | 518 | 4.044 | 484.914, 159.093 | 42 |
| Mijayit | 392 | 3.496 | 479.952, 180.267 | 42 |

四个锚点（Zalm、Nahlan、Hamoshawat、Mijayit）最近的是同一个由 42 个 River(11) 面组成的连通组件；Mabwaz 最近的是另一个 32 面组件。两组件在 River(11) 类型内部不共享边。不能把这种游戏导航面分区直接解释成天然河流断流或水文不连通。

## 四、对照地点与高程

| 对照地点 | 官方文本中的局地机制 | 到最近 River(11) 面距离 |
|---|---|---:|
| Qidnar / 吉德纳尔 | 偶发强降雨导流、岩丘裂隙与椰枣园 | 36.808 |
| Bait Hatif / 拜特·哈提夫 | 旱谷、井水与春季高地草场 | 26.315 |
| Abba / 阿卜巴 | 山地宽谷、地下蓄水与绿洲 | 47.628 |
| Asmait / 阿斯麦特 | 红砂岩山地凹处、暴雨坡面径流拦蓄 | 90.119 |

这些地点并非随机抽样，差异只作描述性比较。它们与河流走廊和局地旱谷／井泉环境分开研究的模型相容，但不是统计显著性检验。

War Sails 的 HGHT 高程栅格由 256 个 257×257 的 16-bit 图块重建为 4097×4097；高度转换使用同版 `scene.xscene` 的 `min_height=-0.900`、`max_height=29.109`。五个锚点处采样 Z 约为 4.280—5.821 场景单位。最近 River(11) 面边界插值 Z 比相邻 HGHT 地形 Z 高约 0.144—0.520 场景单位。这只是游戏导航面与地形高程的相对位置，不能称为真实水面高程或水深。

## 五、资源结构与证据边界

1. War Sails `scene.xscene` 的 `Paths` 控制几何为 0 条，但仍保留 `river_script / river_generator`，引用 `worldmap_river_mask`、`worldmap_river_normal`、`world_map_heightmap` 与 `naval_worldmap_river` 材质。准确说法是“没有 Native 式显式 Paths 控制几何”，不是“没有河流相关实体”。
2. War Sails terrain layer 顺序为 `default, default_1, rock, grass, dirt, dirt2, forest`；PHYM 夏季栅格只出现值 1、2、3、5、6，没有 0、4、7。因此没有可直接命名为 river 的 PHYM layer。该差异不证明世界内部河流消失。
3. `river_triangles.bin` 已解析为 2,210 组、49,758 条映射记录，`triangle_ref` 范围 191—933、`vertex_ref` 范围 0—860；其源三角网格／顶点表尚未定位，不能直接恢复河面 XYZ，也不能把这些引用强行套到 Navmesh 索引上。
4. `flowmap.dds` 为 512×512 的 G16R16F 双分量纹理，原始格式与字节已验证，但贴图 UV 到场景 XY 的变换、分量重映射和物理单位尚未校准。本轮不从原始向量值推断河流流向或流速；它也不等同于 `river_generator` 引用的 `worldmap_river_mask`。

证据标签：A＝同版官方英文地志与坐标；B＝直接解析的同版场景、地形栅格和 Navmesh 多边形；M＝River(11)/NonNavigableRiver(22) 是游戏导航类别；C＝五个锚点与 River(11) 面的集中邻近关系支持游戏地图走廊对应的综合判断。Navmesh 近邻不能单独证明天然河道连通、流量、流向、洪泛范围或地下水联系。

## 六、下一项可证伪检验

优先定位 `river_triangles.bin` 中 `triangle_ref / vertex_ref` 所指向的源三角网格与顶点表。若恢复后的河面 XYZ 在 War Sails 自身坐标中沿五个官方锚点形成连贯走廊，才可把当前“River(11) 导航面近邻”推进为直接河流水面几何证据；若源网格无法定位或几何与锚点不符，则保留当前结论，不以 Navmesh 补画河道。

第二条可选检验是追踪 `worldmap_river_mask` 的资源来源及 shader UV 变换，并将其与同版锚点和 River(11) 面配准。未经坐标校准前，`flowmap.dds` 只作为未解释的游戏流向纹理保存。

## 七、来源与复算

- 官方英文地点文本包 NavalDLC.zip：[Google Drive 原件](https://drive.google.com/file/d/1K1rOhnZ8gV_jH2IP0LvaxXYlmpdgPjTI/view)；234,456 bytes；SHA-256 `e41ad1c75665e736cad7d02319193a2cc6e0ed68e8bf2e44e1f151b62020b468`。
- War Sails scene.xscene：[Google Drive 原件](https://drive.google.com/file/d/1iM3fBTTuoS9l0xj_-k3jqtrPmB_me1oR/view)；21,127,988 bytes；SHA-256 `1fb8bb08210a377fb727dc9e69454f0368254f28f317cb81c5db2569e3862ebc`。
- War Sails terrain.bin：[Google Drive 原件](https://drive.google.com/file/d/1JVKDyLKOfWuphEdy4gdchScbFdu4ftPw/view)；28,336,976 bytes；SHA-256 `56c3a0663fb2bf8404210772e187dcd707eb64d8b7e9b5496dfb509bdc3ea9fd`。
- War Sails navmesh.bin：[Google Drive 原件](https://drive.google.com/file/d/1L3zJ41J1w6pSbu5p06FlzZDAUiNXV6EF/view)；926,074 bytes；SHA-256 `f8b4b846eb930fbfb64da64bf9c9c191a5aee2f825bfce7d1a59deaa21b0175f`。
- War Sails river_triangles.bin：[Google Drive 原件](https://drive.google.com/file/d/17A4leaS8ba8yX5T-yJQLlvWamOCOd2Gj/view)；1,057,044 bytes；SHA-256 `24fefdbe74302bb2f678db7b4533f00524c9f153613114d88db9187a3252ab24`。
- War Sails flowmap.dds：[Google Drive 原件](https://drive.google.com/file/d/1oKvUIWLHkU7ZU0-5lBUAWqhWXfqpLFkH/view)；1,048,704 bytes；SHA-256 `22d11e2e488535c95f1ab80abefe9da1fd85b186a80d5f4346b13212ec31deea`。
- 双版本资源结构与 PHYM 复核：[CGEO-MAP-RES-019](../90/EVD/CGEO-MAP-RES-019.md)；导航网格分类边界：[CGEO-MAP-RES-006](../90/EVD/CGEO-MAP-RES-006.md)。

核验声明：本轮实际下载并复核上述 War Sails 原始文件的大小与 SHA-256；直接解析 scene.xscene、terrain.bin 的 HGHT/PHYM、navmesh.bin 与 NavalDLC settlements.xml。river_triangles.bin 与 flowmap.dds 的源网格／UV 绑定仍未解决。所有 Z 值与距离均为游戏场景单位，不换算为现实米制水文参数。
