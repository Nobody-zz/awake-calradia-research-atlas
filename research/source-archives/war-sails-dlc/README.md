# War Sails DLC — Main_map 原始资源

版本：War Sails DLC。此目录只对应 DLC 原始地图资源；基础版 Native 原件保存在另一 Google Drive 位置，不覆盖、不混放。

- Google Drive 专用文件夹：[War Sails DLC — Main_map 原始资源（2026-10-25）](https://drive.google.com/drive/folders/1NONLB02YC62RM5D_-JUcFV0QbnkgeIIW)
- Native 原始资料库：[打开文件夹](https://drive.google.com/drive/folders/17y4EwetqNlFBW1Zf_d_CP4yrdyjmr8Rm)
- GitHub 二进制目录：[files/](https://github.com/Nobody-zz/awake-calradia-research-atlas/tree/main/research/source-archives/war-sails-dlc/files)
- 清单：[manifest.csv](manifest.csv)

## 文件级校验（2026-10-26）

七个 Drive 原件均已实际下载。文件字节数与 SHA-256 已重新计算，并与原始归档记录一致。

| 原始文件 | 字节数 | SHA-256 | GitHub 二进制状态 |
|---|---:|---|---|
| `atmosphere.xml` | 4,941 | `8375ecccc7a721b5d32e8e4fbc59e00b3a2182202d334a79cd01972668533f6d` | [已提交并逐字节核对](files/WarSails_Main_map_atmosphere.xml) |
| `flora.bin` | 7,253,409 | `7996acbbcbfc09ed9cc8e3fc88fe74de2008cbc736c42e584a2efc3742a2d884` | Drive 原件已验证；GitHub 尚未保存 |
| `flowmap.dds` | 1,048,704 | `22d11e2e488535c95f1ab80abefe9da1fd85b186a80d5f4346b13212ec31deea` | [已提交并逐字节核对](files/WarSails_Main_map_flowmap.dds) |
| `navmesh.bin` | 926,074 | `f8b4b846eb930fbfb64da64bf9c9c191a5aee2f825bfce7d1a59deaa21b0175f` | [已提交并逐字节核对](files/WarSails_Main_map_navmesh.bin) |
| `river_triangles.bin` | 1,057,044 | `24fefdbe74302bb2f678db7b4533f00524c9f153613114d88db9187a3252ab24` | [已提交并逐字节核对](files/WarSails_Main_map_river_triangles.bin) |
| `scene.xscene` | 21,127,988 | `1fb8bb08210a377fb727dc9e69454f0368254f28f317cb81c5db2569e3862ebc` | Drive 原件已验证；GitHub 尚未保存 |
| `terrain.bin` | 28,336,976 | `56c3a0663fb2bf8404210772e187dcd707eb64d8b7e9b5496dfb509bdc3ea9fd` | Drive 原件已验证；GitHub 尚未保存 |

四个已提交文件的 Git blob SHA-1 均与当前 Drive 下载字节计算出的 Git blob 身份一致。三个未提交文件的 GitHub 链接留空；清单不代表二进制备份。

## 归档边界

- 七个文件均仍保存在 War Sails 专用 Drive 文件夹，原始字节不做改写。
- 对 `flora.bin` 的一次 GitHub Base64 blob 提交请求返回 H2 body 错误；当前可用 GitHub 连接器没有 Release 附件或 Git LFS 对象上传入口。本轮不重复提交大型请求。
- 后续结构分析必须使用 War Sails 自身的场景、地形、导航网格与流向纹理；不能拿 Native 的坐标或路径 ID 直接解释 DLC。
