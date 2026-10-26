# 自然地理空间核验备忘录08｜达玛尔河跨版本锚点间距与高程证据的可识别性审查

- 日期：2026-10-26
- 版本：v0.1
- 性质：基于已归档空间结果的派生复核；不宣称本轮重新解析原始地图二进制。
- Google Docs 原件：[打开](https://docs.google.com/document/d/1YWjvam_muUlfAM8J_K3zgqoAnHKu-2MJ_cgfH3n3TmU/edit)
- GitHub Markdown：[研究仓库版本](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-08-damar-cross-version-anchor-spacing-2026-10-26.md)
- 复算脚本：[Python](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-08-damar-cross-version-check-2026-10-26.py)
- 派生表：[锚点间距](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-08-damar-cross-version-segment-results-2026-10-26.csv) · [全地点高程表](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-08-damar-elevation-results-2026-10-26.csv) · [分组描述统计](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-08-damar-settlement-elevation-group-summary-2026-10-26.csv)

## 一、研究问题

备忘录06确认 Native 的 nile 路径与五个达玛尔河稳定文本锚点高度吻合；备忘录07确认 War Sails 的五个锚点都邻近 River(11) 导航面。但这两项结果并不自动证明两个版本具有相同的河道形状，也不证明 War Sails 的导航面构成连续天然水道。

本轮专门检验三个更窄的问题：

1. 官方地志所支持的锚点序列，在两版地图中的相邻距离是否只是统一比例缩放？
2. War Sails 的聚落高程与最近 River(11) 面高程，能否形成可用于判断下游方向的连续纵剖面？
3. River(11) 分成两个最近邻组件，究竟能支持到什么程度的空间结论？

## 二、资料与方法

输入仅使用已经归档并经前序核验的两份 CSV：

- Native：natural-geography-spatial-audit-06-damar-native-anchor-results-2026-10-26.csv，记录五个稳定锚点、原始 nile 路径距离及 PHYM river 栅格距离。
- War Sails：natural-geography-spatial-audit-07-damar-warsails-anchor-results-2026-10-26.csv，记录同版聚落坐标、高程、最近 River(11) 面、导航面组件及其包围盒。

按工作顺序 Zalm → Mabwaz → Nahlan → Hamoshawat → Mijayit，计算每对相邻锚点的二维欧氏距离。再以场景范围名义比值 1040/848 ≈ 1.226 作描述性参照，检查相邻距离差异是否可由统一比例变化解释。该比值不是已校准的坐标变换，因此只用来排除“看起来像统一缩放”的简单解释，不用于将坐标换算到共同地理空间。

高程部分分别列出聚落位置的 HGHT Z、最近 River(11) 面的导航 Z，以及该导航面最近点处的 HGHT Z。三者含义不同，不将导航面 Z 当作水面高程或河床高程。

## 三、锚点间距：War Sails 不是 Native 的统一比例缩放

| 相邻锚点 | Native 距离 | War Sails 距离 | WS/Native 比值 | 除以名义范围比值 1.226 后 |
|---|---:|---:|---:|---:|
| Zalm—Mabwaz | 35.935 | 44.272 | 1.232 | 1.005 |
| Mabwaz—Nahlan | 36.402 | 90.074 | 2.474 | 2.018 |
| Nahlan—Hamoshawat | 19.467 | 15.502 | 0.796 | 0.649 |
| Hamoshawat—Mijayit | 15.246 | 26.942 | 1.767 | 1.441 |

全图场景范围名义比值 1040/848 ≈ 1.226，仅作为描述性参照，并非已校准的坐标变换。结果显示，Zalm—Mabwaz 的间距比值约 1.232，接近名义范围比值；但 Mabwaz—Nahlan 的间距从 Native 的约 36.402 扩大到 War Sails 的约 90.074，约为 2.474 倍。Nahlan—Hamoshawat 的比值仅约 0.796，Hamoshawat—Mijayit 则约 1.767。统一缩放不能同时解释这些变化。

**解释边界：** 这说明两个版本的地图坐标布局／局部空间配置并非简单的全图等比例变换，尤其 Mabwaz 与 Nahlan 的相对间距在 War Sails 中显著增大。它不证明卡拉迪亚世界内部发生了聚落迁移、河道改道或地貌演变；两个版本的场景坐标必须各自在版本内解释。它也意味着，不能把 Native 的精确路径形状直接按比例投射到 War Sails。

## 四、War Sails 高程：现有数值不能当作河流纵剖面

| 锚点 | 聚落 HGHT Z | 最近 River(11) 面 ID | 到该面的距离 | 导航面 Z | 导航面最近点 HGHT Z | 导航面 Z − 同点 HGHT Z | 最近组件面数 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Zalm | 5.491 | 8185 | 2.646 | 5.070 | 4.927 | 0.144 | 42 |
| Mabwaz | 5.740 | 8201 | 3.214 | 5.738 | 5.217 | 0.520 | 32 |
| Nahlan | 4.280 | 510 | 2.858 | 4.028 | 3.711 | 0.317 | 42 |
| Hamoshawat | 5.821 | 518 | 4.044 | 4.737 | 4.292 | 0.445 | 42 |
| Mijayit | 5.018 | 392 | 3.496 | 3.999 | 3.552 | 0.447 | 42 |

两组 Z 值都不构成按上述锚点顺序单调下降的序列：聚落 Z 在 Mabwaz 与 Hamoshawat 处回升；最近导航面 Z 也在 Mabwaz 与 Hamoshawat 处回升。导航面 Z 与其最近点 HGHT Z 的差为 0.144—0.520 个场景单位，但这只说明该类导航面在这些采样位置相对于地形栅格的高度关系，不能把它解释为真实水深、自由水面高度或河床坡度。

因此，当前高程资料不能确认河流的连续纵坡、局部流向、全年常流性或河床剖面。该结果不是对达玛尔河主干模型的反证；它界定的是现有采样方式无法回答的问题。

### 4.1 聚落点位高程的描述性对照

在同一 War Sails HGHT 采样中，五个达玛尔河锚点的聚落 Z 值为 4.280—5.821，均值 5.270、中位数 5.491；四个对照地点 Qidnar、Bait Hatif、Abba、Asmait 的聚落 Z 值为 4.734—8.548，均值 6.949、中位数 7.2565。四个对照点中有三个高于五个达玛尔河锚点的最高值 5.821；Abba 的 Z 值为 4.734，低于锚点组均值。

| 点位组 | n | 最低 Z | 中位数 | 均值 | 最高 Z | 高于达玛尔锚点组最高值的点数 |
|---|---:|---:|---:|---:|---:|---:|
| 达玛尔河锚点 | 5 | 4.280 | 5.491 | 5.270 | 5.821 | — |
| 局地机制对照点 | 4 | 4.734 | 7.2565 | 6.949 | 8.548 | 3/4 |

这一描述性差异与 Qidnar（陆侧岩丘）、Bait Hatif（旱谷与高地春草）及 Asmait（山地凹处）的英文地志定位相容；Abba 是重要例外，说明局地地下蓄水绿洲不能简单归为高海拔点位。样本是按研究问题选择的非随机地点，且 Z 是聚落点位而非邻域坡度、河床或洪泛地平均高程，因此不能据此划定河漫滩、分水岭或汇水边界。四个对照点到最近 River(11) 面的距离为 26.315—90.119 场景单位，该“最近面”不应视为它们的局地水源。

## 五、River(11) 两个组件：走廊邻近成立，拓扑连续性未证

备忘录07记录，Zalm、Nahlan、Hamoshawat、Mijayit 最近邻属于同一 42 面组件，Mabwaz 最近邻属于另一个 32 面组件。两组件包围盒分别为：

- 42 面组件：X=468.837—504.959，Y=107.532—183.041。
- 32 面组件：X=433.951—466.036，Y=65.515—115.871。

包围盒的 X 间隔为约 2.801 个场景单位，Y 范围重叠约 8.339 个单位。包围盒接近只能说明两组面在粗略空间范围上相邻；包围盒不等于真实多边形边界，不能据此计算水道间隙，也不能证明两组件通过天然河道或不可航水面连接。

备忘录07沿官方地点顺序连接五个锚点的直线采样中，78.33% 的采样点距 River(11) 面不超过 5 个单位，92.22% 不超过 10 个单位。这支持“游戏导航水域大体邻近达玛尔河地点链”的走廊级判断，但采样线是测试线，不是河道中心线。结合两组件分离及 Mabwaz—Nahlan 间距异常扩大，War Sails 的证据强度应限定为**走廊级空间对应，中等置信度；连续天然河道几何未恢复**。

## 六、当前模型的置信度修订

- **高置信度：** Native 的 nile 原始路径与五个稳定达玛尔河锚点的空间顺序及 PHYM river 栅格高度吻合；官方英文地志支持峭壁入口、洪泛农业、下游与河口的功能序列。
- **中等置信度：** War Sails 的 River(11) 导航面与五个锚点及其连接测试线大体邻近，表示同一宽泛河流走廊的解释合理。
- **低置信度／未知：** War Sails 中的精确河道弯曲、Mabwaz 附近两组件间的真实水面形态、河床纵坡、自然水文连通、流向和流量。
- **不成立的推论：** 不能用聚落 Z 值或最近 River(11) 面 Z 值代替连续河床剖面；不能把两个版本的锚点距离差写成游戏世界内部的地理变化；不能由导航网格组件分离直接推断天然河流断流。

## 七、下一步

1. 继续把官方英文地志与 Native 的原始路径作为河流地貌序列的主证据；War Sails 作为独立的走廊级对应证据，而不是 Native 河线的直接复刻。
2. 若后续要回答纵坡、流向或河道弯曲问题，必须取得沿实际水面／河床几何的连续采样，或先恢复 river_triangles.bin 的源网格与坐标绑定；当前锚点高程不够。
3. 在没有新几何之前，优先研究河流走廊与洪泛农业、山地—旱谷集水系统的空间分工，不将技术资源缺口当作停研理由。

## 八、复算与来源

- [备忘录06｜Native 原始路径识别](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-06-damar-native-path-identification-2026-10-26.md)
- [备忘录07｜War Sails River(11) 近邻检验](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-07-damar-warsails-navmesh-anchor-registration-2026-10-26.md)
- [锚点间距派生表](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-08-damar-cross-version-segment-results-2026-10-26.csv)
- [高程可识别性派生表](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-08-damar-elevation-results-2026-10-26.csv)
- [复算脚本](https://github.com/Nobody-zz/awake-calradia-research-atlas/blob/main/research/geo/00/natural-geography-spatial-audit-08-damar-cross-version-check-2026-10-26.py)

核验声明：本备忘录重新计算的是两份已归档 CSV 中的锚点间距与局部高程关系，不宣称重新下载或解析本轮原始二进制。所有距离、高程均为游戏场景单位，不换算为现实米制参数。
