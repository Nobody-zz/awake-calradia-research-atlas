# Native Main_map 原始资源

版本：Bannerlord 基础版 Native。此目录只对应基础版原始地图资源，不与 War Sails DLC 混放。

- Google Drive 原始资料库：[打开文件夹](https://drive.google.com/drive/folders/17y4EwetqNlFBW1Zf_d_CP4yrdyjmr8Rm)
- GitHub 原始文件目录：[files/](https://github.com/Nobody-zz/awake-calradia-research-atlas/tree/main/research/source-archives/native-main-map/files)
- 清单：[manifest.csv](manifest.csv)

## 文件级校验（2026-10-26）

五个 Drive 原件均已实际下载。文件字节数与 SHA-256 已重新计算，并与本目录 manifest 一致。

| 原始文件 | 字节数 | SHA-256 | GitHub 二进制状态 |
|---|---:|---|---|
| `atmosphere.xml` | 4,962 | `7848867d9e0e72a5fbec4db20c9f022a7b3d77410da52eab7435f2a0d90d623d` | [已提交并逐字节核对](files/Native_Main_map_atmosphere.xml) |
| `flora.bin` | 7,849,897 | `78fe9777af8cc7161796a72e325803be83bbd5bf73c4e8c9b72cbb4375f4815d` | Drive 原件已验证；GitHub 尚未保存 |
| `navmesh.bin` | 839,040 | `e01ad7ff2aa870a8933ece39df35be4370b7e4d29683b6df8e680a81880eb7f7` | [已提交并逐字节核对](files/Native_Main_map_navmesh.bin) |
| `scene.xscene` | 19,877,756 | `919796b65e497260a8eebab5442ac79af6992957de9e8a17fbb2aaf6fd1b5019` | Drive 原件已验证；GitHub 尚未保存 |
| `terrain.bin` | 27,646,798 | `3b583d9ff5504a6c871caa466a14654593bee42c27df3e3316eda6cb4d85ab49` | Drive 原件已验证；GitHub 尚未保存 |

GitHub 上两个已提交文件的 Git blob SHA-1 均与当前下载字节计算出的 Git blob 身份一致。其余三个文件的 `github_url` 留空，不能将清单或 Drive 链接视为 GitHub 二进制备份。

## 归档边界

- 原始字节不做改写；分析输出另存到研究证据目录。
- 本轮通过 Google Drive 下载并重新计算全部五个 SHA-256。Native `scene.xscene` 与 `terrain.bin` 与此前已记录的 SHA-256 一致。
- 当前 GitHub 连接器对 7,253,409 字节的 Base64 二进制上传请求返回 H2 body 错误；当前可用操作中没有 Release 附件或 Git LFS 对象上传入口。本轮不重复提交大型请求。GitHub 已保存的小文件均以实际 Git blob 身份验证；未保存的原件继续以 Drive 为准。
- 与 War Sails 对照时，必须先按版本分别解析和记录，不把资源差异直接解释为世界内部的历史地貌变化。
