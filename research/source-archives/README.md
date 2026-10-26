# 官方原始资料归档：Bannerlord / War Sails

本目录登记研究所用官方模块原始文本资料包。为避免在研究仓库重复托管游戏资源压缩包，原始 ZIP 文件保存在 Google Drive 原始资料文件夹和 ChatGPT Library 的持久资料夹中；本仓库保留校验和、文件清单说明、稳定链接和版本边界。ZIP 文件没有被解压、改写或重新压缩。

## 原始文件

| 文件 | 大小 | SHA-256 | Google Drive |
|---|---:|---|---|
| Native.zip | 256 KB | `ae546052bc2184bb6d4a2cbc9f74a15f5d009285c48026a55775233a4dc4058c` | [打开](https://drive.google.com/file/d/1mjwjlNjZQGEBbD75GAISs0zNy2ZKfmDp/view) |
| NavalDLC.zip | 229 KB | `e41ad1c75665e736cad7d02319193a2cc6e0ed68e8bf2e44e1f151b62020b468` | [打开](https://drive.google.com/file/d/1K1rOhnZ8gV_jH2IP0LvaxXYlmpdgPjTI/view) |
| SandBox.zip | 508 KB | `54c358e5b318ffeda8a69ce41a7e665f3b9bef06a6e49b142a972c80ea9c1d55` | [打开](https://drive.google.com/file/d/1UoUoe0FMn4Di3eoN0NMexcgzCZOE8CJb/view) |
| SandBoxCore.zip | 61 KB | `a98810bfd5ddaa6d7b8b8927754a0159fed751eff672aef57613417c7284e642` | [打开](https://drive.google.com/file/d/1JWU9JaX65syZGjJvqVJvtuYfnoDUVSlq/view) |
| StoryMode.zip | 32 KB | `ad91692d499e505ad1ec9955d444d3cacdbe3cd058c72b6cfa0d33190335fa6f` | [打开](https://drive.google.com/file/d/1W7WdMJ8U-eTSixyGdv9bxqupUdXHy80E/view) |
| README.md | 3 KB | `42f8f2b43f4451b4f58abbb4c1dfc3858c04c94190d208f0496a46f8056e7d95` | [打开](https://drive.google.com/file/d/10AOwENJyiakm9d6Bp9QkxvUebdF7uN4k/view) |
| file_manifest.csv | 42 KB | `3d3097b755aef682302e0d717ac74d3ba739e48a1dac486794de1af47f8da40b` | [打开](https://drive.google.com/file/d/1664-BMbqMAmS3_DQzYyGCaiLX8kpVrLe/view) |

## 内容与版本边界

- 资料包记录了 67 个候选官方 XML：23 个英文原始 XML、22 个官方英文语言表、22 个官方简体中文语言表。
- 模块包含 Native、SandBox、SandBoxCore、StoryMode 与 NavalDLC（War Sails）。
- README 记录的安装版本字段存在差异：Steam buildid 24573425、package_info PC@v1.3.4、基础官方模块 v1.4.8、NavalDLC v1.2.8（要求基础版 v1.4.8）。这些字段分别保存，不互相覆盖。
- `file_manifest.csv` 保留源路径、相对路径、文件大小、SHA-256、模块版本、语言、ID 节点数、专题及重复判断。
- 资料是从用户提供的本机官方模块副本提取的研究候选文本，不是全部游戏资源镜像；第三方模组不在其中。
- GitHub 本目录保存归档目录和校验信息，原始压缩包本体放在 Drive/ChatGPT Library，以避免误把游戏原始资源作为研究文本提交进版本库。

## 持久存放位置

- Google Drive 文件夹：[卡拉迪亚地理研究｜官方原始资料库](https://drive.google.com/drive/folders/17y4EwetqNlFBW1Zf_d_CP4yrdyjmr8Rm)
- ChatGPT Library：`/Calradia Geography Research Source Files/`
## Native：Main_map 原始二进制（独立归档）

- Google Drive：[原始资料库](https://drive.google.com/drive/folders/17y4EwetqNlFBW1Zf_d_CP4yrdyjmr8Rm)
- GitHub 说明：[native-main-map/README.md](native-main-map/README.md) · [清单](native-main-map/manifest.csv) · [实际二进制目录](native-main-map/files/)

2026-10-26 实际下载并复算 5/5 个 Native 原件的字节数与 SHA-256，均与清单一致。GitHub main 已保存并核对其中 2/5 个二进制：`atmosphere.xml`、`navmesh.bin`。其余 `flora.bin`、`scene.xscene`、`terrain.bin` 保留在 Drive，当前 GitHub 连接器未能可靠提交这些较大二进制。

## War Sails DLC：Main_map 原始二进制（独立归档）

- Google Drive：[War Sails 专用文件夹](https://drive.google.com/drive/folders/1NONLB02YC62RM5D_-JUcFV0QbnkgeIIW)
- GitHub 说明：[war-sails-dlc/README.md](war-sails-dlc/README.md) · [清单](war-sails-dlc/manifest.csv) · [实际二进制目录](war-sails-dlc/files/)

2026-10-26 实际下载并复算 7/7 个 War Sails 原件的字节数与 SHA-256，均与清单一致。GitHub main 已保存并核对其中 4/7 个二进制：`atmosphere.xml`、`flowmap.dds`、`navmesh.bin`、`river_triangles.bin`。其余 `flora.bin`、`scene.xscene`、`terrain.bin` 保留在 Drive。

## 统一归档状态与技术限制

- Drive 原件：12/12 可下载，大小及 SHA-256 均已复核。
- GitHub main 的实际二进制：6/12；每个已提交文件都通过 Git blob SHA-1 与下载字节的精确比对。Native 与 War Sails 路径分开，未覆盖原始文件。
- 本轮尝试通过 GitHub Git Data API 提交 7,253,409 字节的 War Sails `flora.bin` 时，Base64 请求触发 `h2 protocol error: error reading a body from connection`，未能确认进入有效分支历史。不能把可能的孤立 blob 视为已归档。当前连接器未提供 Release 附件上传或 Git LFS 对象上传操作；其余较大文件继续由 Drive 保存。
- GitHub 官方常规 Git 单文件限制为超过 50 MiB 警告、超过 100 MiB 阻止；这些原件均低于 100 MiB，但“理论上可存储”不代表当前连接器能可靠传输。若之后要完成余下 6 个二进制的 GitHub 镜像，需要使用可靠的本地 Git 推送或受支持的 Release/LFS 上传通道，不应继续反复发送超大 Base64 请求。
- Native 与 War Sails 的资源差异只作为版本与资源差异记录；不得直接等同于世界内部历史地理变化。
