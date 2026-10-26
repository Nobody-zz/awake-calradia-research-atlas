# 自然地理空间核验备忘录06｜达玛尔河在 Native Main_map 中的场景路径直接识别

- 日期：2026-10-26
- 版本：v0.1
- 研究对象：基础版 Native `Main_map` 的原始 `scene.xscene`
- Google Docs 原件：[打开](https://docs.google.com/document/d/1GpMJkQxRe9tnEJWvFLkREYSU4Zs5ij-on-7gEguz3L4/edit)
- 原始文件：[Native Main_map 资源与校验清单](../../source-archives/native-main-map/README.md)
- 前序：[备忘录05｜候选路径范围排除与原始资源恢复](natural-geography-spatial-audit-05-damar-path-candidate-2026-10-25.md)

## 一、结论

本轮已从 Google Drive 重新取回 Native 原版 `scene.xscene`，核对文件大小为 19,877,756 字节，SHA-256 为 `919796b65e497260a8eebab5442ac79af6992957de9e8a17fbb2aaf6fd1b5019`，与前序记录一致。直接解析原始 XML 后，达玛尔河文本锚点与场景路径 `nile` 呈现独特且高度集中的几何对应。

**当前最强识别为：Native `Main_map` 中的 `nile` 路径就是达玛尔河走廊的场景路径实现。** 这一判断来自路径几何、五个稳定聚落坐标的近邻距离、沿控制点序列的空间顺序和与其他河流路径的距离差，不是依据 `nile` 这个名称的字面含义。正式地理名称仍使用“达玛尔河”；`nile` 仅作为原始资源中的内部路径名。

## 二、直接读取的原始结构

- `scene.xscene` 的 `<Paths>` 容器有 20 条路径、共 686 个控制点。
- 其中 15 条为河流样式路径，5 条为海域／湖泊边界样式路径。
- `nile` 路径有 31 个控制点，`interpolation_type="linear"`。
- `nile` 路径控制点包围盒：X=353.242—420.130，Y=-9.997—190.892。
- 五个稳定锚点的坐标来自同版官方 `SandBox/ModuleData/settlements.xml`，并非从图像反推。

## 三、点—线距离

对每个聚落点，按 `nile` 路径相邻控制点构成的线段计算二维欧氏最短距离。线性插值属性使该算法与原始路径的平面几何表达相符。

| 稳定锚点 | 聚落实体 ID | X | Y | 到 `nile` 的最短距离 | 最近线段序号（从0起） |
|---|---|---:|---:|---:|---:|
| Zalm | `village_A7_4` | 390.254 | 97.643 | 6.994 | 12 |
| Mabwaz | `village_A7_3` | 413.587 | 124.973 | 5.556 | 7 |
| Nahlan | `village_A6_4` | 404.877 | 160.318 | 3.078 | 5 |
| Hamoshawat | `village_A6_2` | 394.921 | 177.046 | 3.879 | 3 |
| Mijayit | `village_A6_1` | 410.054 | 178.898 | 5.703 | 1 |

五个距离均小于 7 场景单位；均值为 5.041，最大值为 6.994。最近线段序号从 Mijayit 附近的 1、Hamoshawat 的 3、Nahlan 的 5、Mabwaz 的 7 到 Zalm 的 12，沿 `nile` 控制点顺序形成连续的空间序列。

## 四、与其他河流路径的区分

在其余河流样式路径中，每个锚点的次近路径均为 `river_emp_south`，但其距离分别为：Zalm 205.862、Mabwaz 169.930、Nahlan 151.126、Hamoshawat 149.513、Mijayit 135.827 场景单位。与 `nile` 相比，次近路径距离约为 23.8—49.1 倍。其余候选路径与五个锚点的几何距离显著更大。

这不仅排除了此前已绘制的十条 `river_*` 路径，也将识别推进到原始 XML 中具体的路径实体。之前的范围排除备忘录05应保留为研究过程记录，但当前识别状态以本备忘录06为准。

## 五、证据边界与下一步

### 已直接确认

- Native 原版 `scene.xscene` 文件可访问且哈希与前序记录一致。
- 原始 XML 中存在名为 `nile` 的 31 控制点线性路径。
- 五个达玛尔河稳定文本锚点到该路径的距离全部小于 7 场景单位，且沿控制点顺序一致。
- 其他河流路径与锚点的距离远大于 `nile`。

### 尚待完成

- 本轮尚未重新解码 `terrain.bin` 的原始 PHYM index 7，因此未声称已完成路径与 PHYM7 原始栅格的逐像素／逐格配准。
- 近邻关系可支持将 `nile` 识别为达玛尔河的场景路径实现，但不能单独确定流向、流量、季节性洪泛范围或地下水连通性。
- 下一步从 Native `terrain.bin` 提取 PHYM 四季记录中的 index 7，与 `nile` 折线及五个锚点进行原始栅格配准；随后在 War Sails 版本独立重复相同流程，不假设路径名称、坐标或拓扑保持不变。

## 六、复算

本仓库附有 [点—线距离复算脚本](natural-geography-spatial-audit-06-damar-native-path-identification-2026-10-26.py)。脚本读取 Native `scene.xscene` 与官方锚点坐标，逐条解析全部 20 条路径，输出每个锚点的最近路径、距离与线段序号。它不读取 `terrain.bin`，因此不替代下一阶段的 PHYM 栅格核验。