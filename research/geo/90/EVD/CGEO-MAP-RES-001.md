# CGEO-MAP-RES-001｜原版与《战帆》Main_map 原始资源清单及结构差异

- 版本：v1.0
- 日期：2026-10-22
- 研究系列：CGEO 地理研究；地图版本与数据工程
- Google Drive 原件：[原始资源清单及结构差异](https://docs.google.com/document/d/1RchZ3Q87ii5CmrIkqJjl8IDFG-ZTe8jAsJOcpEnXB0s/edit)
- Google Drive 文件指纹表：[CSV 清单](https://drive.google.com/file/d/1d8xjzRKjtrtvaAGpD4ODaw76vo701pDU/view)

## 研究范围与来源界限

从项目文件库分别取回原版《霸主》与《战帆》Main_map 资源，在独立工作目录中只读解析并计算 SHA-256。未启动游戏、未修改原始文件。版本归属依据用户确认的 atmosphere.xml 及对应上传文件组；部分二进制文件不内嵌绝对安装路径，哈希是本轮附件副本的稳定指纹，不等于对用户本机安装目录的原位校验。

## 文件清单

| 版本 | 文件 | 字节数 | SHA-256 |
|---|---|---:|---|
| 原版 | scene.xscene | 19,877,756 | `919796b65e497260a8eebab5442ac79af6992957de9e8a17fbb2aaf6fd1b5019` |
| 原版 | terrain.bin | 27,646,798 | `3b583d9ff5504a6c871caa466a14654593bee42c27df3e3316eda6cb4d85ab49` |
| 原版 | navmesh.bin | 839,040 | `e01ad7ff2aa870a8933ece39df35be4370b7e4d29683b6df8e680a81880eb7f7` |
| 原版 | flora.bin | 7,849,897 | `78fe9777af8cc7161796a72e325803be83bbd5bf73c4e8c9b72cbb4375f4815d` |
| 原版 | atmosphere.xml | 4,962 | `7848867d9e0e72a5fbec4db20c9f022a7b3d77410da52eab7435f2a0d90d623d` |
| 战帆 | scene.xscene | 21,127,988 | `1fb8bb08210a377fb727dc9e69454f0368254f28f317cb81c5db2569e3862ebc` |
| 战帆 | terrain.bin | 28,336,976 | `56c3a0663fb2bf8404210772e187dcd707eb64d8b7e9b5496dfb509bdc3ea9fd` |
| 战帆 | navmesh.bin | 926,074 | `f8b4b846eb930fbfb64da64bf9c9c191a5aee2f825bfce7d1a59deaa21b0175f` |
| 战帆 | river_triangles.bin | 1,057,044 | `24fefdbe74302bb2f678db7b4533f00524c9f153613114d88db9187a3252ab24` |
| 战帆 | flowmap.dds | 1,048,704 | `22d11e2e488535c95f1ab80abefe9da1fd85b186a80d5f4346b13212ec31deea` |
| 战帆 | flora.bin | 7,253,409 | `7996acbbcbfc09ed9cc8e3fc88fe74de2008cbc736c42e584a2efc3742a2d884` |
| 战帆 | atmosphere.xml | 4,941 | `8375ecccc7a721b5d32e8e4fbc59e00b3a2182202d334a79cd01972668533f6d` |

## 场景 XML 的直接差异

- 两版场景均名为 `Main_map`，scene version 为 2。
- 原版有 37,918 个 `game_entity`；战帆有 41,834 个。
- 两版地形配置均为 16×16 节点；原版 `node_size=53.000`、配置边长 848 场景单位；战帆 `node_size=65.000`、配置边长 1,040 场景单位。原版高度范围参数为 -0.723 至 23.052；战帆为 -0.900 至 29.109。场景单位未校准为米/公里。
- 原版 `Paths` 有 20 条路径、686 个控制点（15 条河流样式路径，5 条水域/岸界样式路径）；战帆 `Paths` 容器为空。但两版均保留 `river_generator`，所以不能把 DLC 的空 `Paths` 解读为河流消失。
- 原版河流材质引用为 `worldmap_river_mat`、Extra Pixel Count=1、Terrain Height Offset=0.320；战帆为 `naval_worldmap_river`、0、0.000。两版都引用 `worldmap_river_mask`、`worldmap_river_normal` 和 `world_map_heightmap`。
- 原版有 8 个 `water_plane`，均用 `worldmap_lake_clear`；战帆有 5 个，其中 2 个用 `naval_worldmap_water`，3 个用 `worldmap_water`。海洋材质引用由 `wat_main_map_ocean_g` 变为 `wat_open_ocean_g`。

## 二进制资源解析状态

- 两版 `navmesh.bin` 均为 RNM1 外层容器，解压后含 NMG9 网格数据。原版结构计数：16,436 顶点、33,584 边、17,153 面；战帆计数：17,424 顶点、37,747 边、20,258 面。战帆的逐面拓扑/索引校验仍需使用同等完整的验证流程。
- 两版 `terrain.bin` 均以 ZGR6RTRN 版本 2 开头，含 MIDX、HGHT、NRML、WGHT、PHYM 分块。HGHT/PHYM 的完整图块编码尚未解出，不宣称已重建完整高程图。
- 战帆 `river_triangles.bin` 已完整解析为 2,210 组和 49,758 条映射记录；引用的源三角网格索引空间尚未确定，故还不能恢复河流水面 XYZ。
- 战帆 `flowmap.dds` 为 512×512，载荷 512×512×4 字节；FourCC 字段为 0x70，编码语义未确认。原始通道图不等于已解释的流向图。
- 两版 `atmosphere.xml` 的时间、雾效、太阳高度、曝光、色彩分级等参数不同；这些首先是场景表现配置，不是气候观测。

## 重要来源校正

此前生成的 `bannerlord_main_map_analysis_bundle.zip` 属于混合来源：场景路径与八个水面实体来自原版 `scene.xscene`；河流三角映射和 Flowmap 原始通道图来自《战帆》上传组。不得将该旧包整体称为单一版本的地图分析。后续图表必须写明版本、源文件和 SHA-256。

## 地理学解释边界

以上是地图资源/场景实现差异，不能直接解释为卡拉迪亚世界内部发生海侵、造岛、河流自然改道或城市迁移。下一阶段应解码 terrain 高程图块、确认 river_triangles 的源索引空间，并在各自版本内重建几何，再开展对照。不得把地图设计差异当作世界内部历史事件。


## 后续解码更新

原文中“HGHT/PHYM图块编码尚未解出”的状态已由后续文件分析更新。参见 [CGEO-MAP-RES-003](CGEO-MAP-RES-003.md)：原版与《战帆》HGHT均已解码为256张257×257、16-bit灰度PNG，并拼接成4097×4097高程栅格；MIDX每版恢复出4张4096×4096灰度PNG。高度样本到场景Z值的转换、XY方向与MIDX/PHYM图层语义仍待确认。
