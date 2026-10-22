# CGEO-MAP-RES-002｜双版本导航网格完整校验与《战帆》Flowmap 解码

- 日期：2026-10-22
- 版本：v0.2
- Google Drive 原件：[打开技术报告](https://docs.google.com/document/d/1GwLgawZTVD4NXSXYopn-OsKymVYNfcI3c3Mdg5fWezo/edit)
- 关联档案：[CGEO-MAP-RES-001](CGEO-MAP-RES-001.md)

## 本轮实质进展

1. 用同一解析器完整读取原版与《战帆》两个 Navmesh，逐面检查顶点/边引用，并验证每条面边与边表端点一致。
2. 《战帆》`flowmap.dds` 的 `dwFourCC=112 (0x70)` 已识别为 Direct3D 9 `D3DFMT_G16R16F`，即每像素两个16-bit浮点分量。512×512像素已解码为262,144个双分量 half-float 像素。
3. 两版 `terrain.bin` 的 `HGHT` 索引表均提取出256个单调递增偏移，并计算tile存储片段长度。高程像素仍未解码。
4. 明确记录 `river_triangles.bin` 的引用空间与 Navmesh 直接索引不匹配，暂不能用它们恢复河面XYZ。

## 一、Navmesh 同解析器校验

| 指标 | 原版《霸主》 | 《战帆》 |
|---|---:|---:|
| 文件大小 | 839,040 B | 926,074 B |
| 解压后 NMG9 | 1,962,213 B | 2,220,198 B |
| 顶点 | 16,436 | 17,424 |
| 边 | 33,584 | 37,747 |
| 面 | 17,153 | 20,258 |
| 四边形 | 14,774 | 14,033 |
| 三角形 | 2,379 | 6,225 |
| 单面引用边界候选 | 935 | 687 |
| 无效面顶点引用 | 0 | 0 |
| 无效面边引用 | 0 | 0 |
| 面边循环/边表端点不一致 | 0 / 66,233 | 0 / 74,807 |
| 被超过2个面引用的边 | 0 | 0 |
| 未解释尾部 | 260 B | 260 B |

两版均完整解析至260字节尾部，顶点和边引用有效，面边循环与边表端点全部匹配。该结果证明的是导航网格结构完整性，不是自然海岸线完整性。

坐标范围：
- 原版：X 59.570–825.273，Y 0.301–657.841，Z 0.868–22.390。
- 战帆：X 88.242–1005.006，Y 28.729–920.493，Z 2.519–29.689。

原版和DLC的 terrain.node_size 分别为53与65；Navmesh只覆盖导航区域。因此XY投影面积和不能直接当作大陆面积，也不能据此推导卡拉迪亚世界内部的地貌变化。

## 二、《战帆》Flowmap 格式确认

文件：`flowmap.dds`，1,048,704字节，SHA-256 `22d11e2e488535c95f1ab80abefe9da1fd85b186a80d5f4346b13212ec31deea`。

- 512×512，pitch 2,048字节，像素载荷1,048,576字节。
- pixel format flags=4，FourCC=112 (0x70)。
- 格式：`D3DFMT_G16R16F` / `DXGI_FORMAT_R16G16_FLOAT`，每像素两个IEEE-754 binary16分量。
- R：最小 -11.890625，最大 10.164063，均值 -0.675176，中位数 -0.199707。
- G：最小 -11.320313，最大 12.000000，均值 -0.018490，中位数 0.000028。
- √(R²+G²) 数值代理：最小0，最大12.004948，均值2.313683，95百分位8.645787。
- 无NaN/Inf。

格式依据：
- [Microsoft Learn: D3DFORMAT](https://learn.microsoft.com/en-us/windows/win32/direct3d9/d3dformat)
- [Microsoft Learn: Programming Guide for DDS](https://learn.microsoft.com/en-us/windows/win32/direct3ddds/dx-graphics-dds-pguide)

图中矢量只按存储R/G分量绘制。贴图Y轴是否反向、shader是否重映射分量，以及此文件是否绑定到具体水面/河流资源，尚未校准。不能在此阶段直接把箭头标注为自然径流方向。

## 三、terrain.bin 的 tile 分段边界

两版 `HGHT` 索引表均有256项单调递增偏移，片段长度按相邻偏移差及payload末端计算：

| 指标 | 原版 | 战帆 |
|---|---:|---:|
| tile数 | 256 | 256 |
| 片段长度最小值 | 724 B | 723 B |
| 片段长度中位数 | 87,842.5 B | 76,505.5 B |
| 片段长度均值 | 69,872.4 B | 57,328.5 B |
| 片段长度最大值 | 97,184 B | 96,687 B |
| 片段长度 ≤2,000 B | 29 | 47 |

这给出了稳定的tile分段边界，便于继续研究编码，但尚未恢复高程像素。terrain.bin 中出现的PNG签名字节序列不能直接视为有效PNG：标准IHDR/后续chunk CRC验证不通过。

## 四、river_triangles 的索引空间

《战帆》`river_triangles.bin`完整解析为2,210组、49,758条映射记录。`triangle_ref`范围191–933，`vertex_ref`范围0–860；它们不是Navmesh直接索引空间。源三角网格的XYZ顶点表尚未定位，因此不能把这些引用强行套到Navmesh上生成河面坐标。

## 研究边界与后续任务

本轮完成Navmesh结构校验、DLC Flowmap像素格式解码、HGHT 256项tile偏移/分段统计。尚未完成terrain高程解码、river_triangles源网格识别、Flowmap到世界XY的绑定校准。Navmesh边界不自动等于海岸线，资源版本差异不自动等于卡拉迪亚内部地理变迁。

后续优先级：
1. 研究HGHT各tile片段头部及编码模式；
2. 识别river_triangles引用的源三角网格；
3. 从scene.xscene及相关资源追踪Flowmap/河流掩码绑定；
4. 坐标校准完成后，再叠加Flowmap、河流几何、Navmesh和水面实体。

## 本地分析交付物

- 双版本Navmesh验证表：`cgeo_navmesh_dual_version_validation.csv`
- Navmesh指标差异表：`cgeo_navmesh_dual_version_delta.csv`
- 双版本Navmesh对照图：`cgeo_navmesh_dual_version.png`
- Flowmap解码图：`cgeo_warsails_flowmap_decoded.png`
- Flowmap统计：`cgeo_warsails_flowmap_stats.json`
- HGHT tile片段长度CSV/图：`cgeo_terrain_tile_segment_sizes.csv` / `cgeo_terrain_tile_segment_sizes.png`

本仓库仅同步研究报告与必要派生摘要，不提交原始游戏二进制资产。

## 修订：HGHT tile 偏移表与完整解码

后续技术档案 [CGEO-MAP-RES-003](CGEO-MAP-RES-003.md) 已完成 terrain 高程解码。HGHT偏移表指向LZ4解压后的raw输出，不是压缩文件字节偏移；本报告原先的tile长度统计以stored size作为最后一块终点，现由RES-003按raw size修订。正确中位数：原版87,689.5字节，《战帆》78,176.5字节。

两版HGHT均解码为256张257×257、16-bit灰度PNG，并拼接为4097×4097栅格。DLC的480条接缝全部精确匹配；原版477/480接缝精确匹配。MIDX每版另有4张4096×4096、8-bit灰度PNG。详见[RES-003报告](https://docs.google.com/document/d/1pTiVx_yOJpP6IVFzUcwr2Yeni3m2xb1Y-rbdcNj9HsM/edit)。

## Flowmap与导航类型语义边界

TaleWorlds官方文档说明Flowmap编辑器箭头表示方向、颜色表示强度，且影响水面shader和风暴移动；但没有公布DDS浮点分量的确切重映射或物理单位，因此原始R/G统计不能直接解释为流速。官方文档亦区分CoastalSea、OpenSea、River、NonNavigableRiver、UnderBridge和Lake等导航类型；这些是游戏导航分类，不独立证明自然水文连通。详见 [CGEO-MAP-RES-004](CGEO-MAP-RES-004.md) 与 [官方文档](https://moddocs.bannerlord.com/war-sails/wsworldmap/)。
