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

基础版 Native 的五个 `Main_map` 文件保存在 Google Drive 原始资料库根目录；与 War Sails 子文件夹分开，不覆盖、不混放。

- Google Drive 原始资料库：[打开](https://drive.google.com/drive/folders/17y4EwetqNlFBW1Zf_d_CP4yrdyjmr8Rm)
- GitHub 归档说明：[native-main-map/README.md](native-main-map/README.md)
- GitHub 校验清单：[native-main-map/manifest.csv](native-main-map/manifest.csv)

已从当前可读取的 Drive 原件重新计算五个文件的 SHA-256；`scene.xscene` 与 `terrain.bin` 的值与前序记录一致。GitHub 当前保留清单和 Drive 索引，不声称已将大体积二进制原件提交到仓库。

## War Sails DLC：Main_map 原始二进制（独立归档）

用户于 2026-10-25 另行提供了 War Sails `Main_map` 的七个原始资源。它们已放入与 Native 原版分开的 Google Drive 子文件夹；不覆盖 Native 文件。

- Google Drive 独立文件夹：[War Sails DLC — Main_map 原始资源（2026-10-25）](https://drive.google.com/drive/folders/1NONLB02YC62RM5D_-JUcFV0QbnkgeIIW)
- GitHub 归档说明：[war-sails-dlc/README.md](war-sails-dlc/README.md)
- GitHub 校验清单：[war-sails-dlc/manifest.csv](war-sails-dlc/manifest.csv)

GitHub 当前保存该批资源的来源说明、校验清单和稳定 Drive 链接；本轮连接器未能可靠提交大体积原始二进制本体，因此不将 GitHub 清单误称为二进制备份。七个原件均已由 Google Drive 文件夹清单确认存在。
