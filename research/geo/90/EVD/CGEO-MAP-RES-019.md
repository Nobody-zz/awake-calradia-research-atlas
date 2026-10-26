# CGEO-MAP-RES-019｜双版本 Main_map 原始资源校验与河流表示结构对照

- 日期：2026-10-26
- 版本：v0.1
- 范围：Bannerlord 基础版 Native 与 War Sails DLC 的 Main_map 原始资源归档核验、scene.xscene 与 terrain.bin 源级结构复核
- 统一清单：[main-map-manifest.csv](../../source-archives/main-map-manifest.csv)
- Native 原件：[Google Drive](https://drive.google.com/drive/folders/17y4EwetqNlFBW1Zf_d_CP4yrdyjmr8Rm) · [GitHub 清单](../../source-archives/native-main-map/manifest.csv)
- War Sails 原件：[Google Drive](https://drive.google.com/drive/folders/1NONLB02YC62RM5D_-JUcFV0QbnkgeIIW) · [GitHub 清单](../../source-archives/war-sails-dlc/manifest.csv)
- 复算脚本：[CGEO-MAP-RES-019_verify_source_archives.py](CGEO-MAP-RES-019_verify_source_archives.py)

## 一、归档核验结论

**Drive 原件 12/12 可实际下载；12/12 的文件大小和 SHA-256 均与清单一致。** 本轮没有重复上传原始文件，而是重新下载已归档的 Drive 原件后逐字节复核。

GitHub main 当前实际保存并核对的二进制为 6/12：

- Native：atmosphere.xml、navmesh.bin（2/5）。
- War Sails：atmosphere.xml、flowmap.dds、navmesh.bin、river_triangles.bin（4/7）。

六个已提交文件的 Git blob SHA-1 均与当前下载字节按 Git blob 规则计算的身份一致。Native flora.bin、scene.xscene、terrain.bin，以及 War Sails flora.bin、scene.xscene、terrain.bin 目前没有可核实的 GitHub 分支文件路径；这些原件继续以 Drive 为准。完整逐文件状态见统一清单，GitHub URL 仅对确实已提交的文件填写。

### 上传通道限制

本轮尝试用 GitHub Git Data API 提交 7,253,409 字节的 War Sails flora.bin 时，Base64 请求返回错误：h2 protocol error: error reading a body from connection。该请求未完成可验证的分支提交；不能将可能存在的孤立 Git blob 视为归档成功。当前可用的 GitHub 连接器提供 create_blob、create_tree、create_commit 和 update_ref，但没有 Release 附件上传或 Git LFS 对象上传操作。本轮不再重复提交大型 Base64 请求。

GitHub 官方文档说明，普通 Git 文件超过 50 MiB 会产生警告，超过 100 MiB 会被阻止；Release 与 Git LFS 是可选的分发路径。这里的限制不是说这些原件超过 GitHub 的通用文件上限，而是当前连接器无法可靠传输较大的二进制请求。参见 [GitHub 关于大型文件的说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)。

## 二、scene.xscene 结构对照

| 指标 | Native | War Sails |
|---|---:|---:|
| scene 名称 / 版本 | Main_map / 2 | Main_map / 2 |
| game_entity 数量 | 37,918 | 41,834 |
| terrain 节点配置 | 16 × 16 | 16 × 16 |
| node_size | 53.000 | 65.000 |
| 配置边长（16 × node_size） | 848 场景单位 | 1,040 场景单位 |
| min_height / max_height 参数 | -0.723 / 23.052 | -0.900 / 29.109 |
| terrain layer 数量 | 8 | 7 |
| Paths 控制几何 | 20 条路径 / 686 个控制点 | 0 条路径 / 0 个控制点 |
| water_plane 实体 | 8 | 5 |
| ocean 材质属性 | wat_main_map_ocean_g | wat_open_ocean_g |

Native 的 terrain layers 依序为 default、flora_forest、rock、grass、dirt、dirt2、forest2、river；第 7 号索引（从 0 起）明确标记为 river。War Sails 的 layers 为 default、default_1、rock、grass、dirt、dirt2、forest，没有 river 标签。

Native 的 Paths 容器包含 20 条线性路径，其中 15 条为河流样式路径、5 条为海域或湖泊边界样式路径。War Sails 的 Paths 容器没有路径控制几何。注意：War Sails 场景中仍有 river_script / river_generator，也保留若干带 Path Name 变量的实体；因此准确说法是“没有 Native 那种 Paths 控制几何”，而不是“场景中不存在任何河流相关实体”。

两版 river_generator 都引用 worldmap_river_mask、worldmap_river_normal 与 world_map_heightmap，且 Show River Area=false、Snap To Water Planes=true；但 Native 使用 worldmap_river_mat、Extra Pixel Count=1、Terrain Height Offset=0.320，War Sails 使用 naval_worldmap_river、Extra Pixel Count=0、Terrain Height Offset=0.000。water_plane 材质也不同：Native 8 个均为 worldmap_lake_clear；War Sails 为 3 个 worldmap_water 与 2 个 naval_worldmap_water。

## 三、terrain.bin 与 PHYM 夏季层

两版 terrain.bin 均以 ZGR6RTRN、版本 2 开头，并包含 MIDX、HGHT、NRML、WGHT、PHYM 五个 section。PHYM 直接解压与结构校验结果如下：

| 指标 | Native | War Sails |
|---|---:|---:|
| PHYM section version | 1 | 1 |
| PHYM section / offset-table 偏移 | 22,078,014 | 21,618,044 |
| PHYM 压缩 payload 偏移（section 偏移 + 1,064） | 22,079,078 | 21,619,108 |
| PHYM 压缩 payload 大小 | 5,567,760 B | 6,717,908 B |
| PHYM 解压大小 | 67,642,368 B | 67,642,368 B |
| PHYM 解压后 SHA-256 | 51b156e34c2bd34aa76d50a3b1d22339373e9d51e93d36905cd086cd27841c36 | 15175c3291c115f70f868a532c946c09117bce473d4df37696d8405c39485a79 |
| tile 数量 | 256 | 256 |
| 单 tile 记录大小 | 264,228 B | 264,228 B |
| 夏季重建栅格 | 4097 × 4097 | 4097 × 4097 |

每个 tile 都包含 season 0–3 的四条记录，每条记录 66,049 个样本。使用原始 16 × 16 tile 目录、每 tile 257 × 257 样本及共享边缘拼接后，Native 夏季栅格的值计数为：

| PHYM 值 | 栅格单元数 |
|---:|---:|
| 0 | 7,919,735 |
| 1 | 97 |
| 2 | 1,829,780 |
| 3 | 3,141,557 |
| 4 | 1,696,554 |
| 5 | 1,265,618 |
| 6 | 626,533 |
| 7 | 305,535 |

War Sails 夏季栅格只出现值 1、2、3、5、6：

| PHYM 值 | 栅格单元数 |
|---:|---:|
| 1 | 6,266,126 |
| 2 | 1,691,103 |
| 3 | 2,804,065 |
| 5 | 5,929,373 |
| 6 | 94,742 |

War Sails 重建栅格没有值 0、4、7；与其 scene.xscene 的 terrain layer 表相互印证，当前版本没有可直接命名为 river 的 PHYM layer。Native 的 PHYM 值 7 对应明确标记为 river 的 layer，共 305,535 个栅格单元，约占栅格 1.8202%。

这并不证明 War Sails 中没有河流。DLC 场景仍有 river_generator，并使用河流 mask / normal 与新的 naval_worldmap_river 材质；War Sails 资源组还单独包含 river_triangles.bin。此前 CGEO-MAP-RES-002 已将 river_triangles.bin 解析为 2,210 组、49,758 条映射记录，但其源三角网格索引空间尚未定位，因此仍不能直接恢复河面 XYZ。

## 四、达玛尔河识别状态与解释边界

Native 原始 scene.xscene 的 nile 路径仍是达玛尔河走廊的最强识别。既有 [自然地理空间核验备忘录06](../00/natural-geography-spatial-audit-06-damar-native-path-identification-2026-10-26.md) 记录了 31 个控制点、五个稳定聚落锚点到路径的 3.078–6.994 场景单位距离，以及路径采样与原始 PHYM river layer 的高度对应。本轮重新下载的 Native scene.xscene 与 terrain.bin SHA-256 均与该备忘录的输入指纹完全一致；本轮结构复核确认其 20 条路径、686 个控制点及 PHYM 值 7 的计数仍一致。

**不能把 Native 的 nile 路径名、路径 ID 或坐标直接带入 War Sails。** DLC 的 Paths 控制几何为空，terrain layers 与 PHYM 值也发生变化。下一步应先确定 War Sails river_triangles.bin 的 triangle_ref / vertex_ref 所指向的源网格和顶点表，再使用 War Sails 自身版本的聚落坐标或实体变换建立锚点，寻找达玛尔河的 DLC 几何对应。当前尚不能断言 river_triangles.bin 已经包含达玛尔河本身，也不能从二进制差异推导河流在卡拉迪亚世界内部发生了自然改道。

## 五、复算方法

复算脚本会校验 12 个原始文件的大小和 SHA-256，解析两版 scene.xscene 的地形层、Paths 与 river_generator 字段，并解压 terrain.bin 的 PHYM 夏季层。脚本仅读取源文件，不写回或修改原件。输入目录可以使用原始文件名，也可以使用 Drive 下载桥接器生成的 Native_Main_map_ / WarSails_Main_map_ 前缀文件名。

建议在安装 numpy 与 lz4 的 Python 环境运行：

```bash
python CGEO-MAP-RES-019_verify_source_archives.py --native-dir ./native --war-sails-dir ./war-sails
```

资源差异仅说明游戏地图资源与渲染实现的版本差异，不等于卡拉迪亚世界内部的历史地貌变化。
