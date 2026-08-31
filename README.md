# 魔兽世界 12.1 全量 33,069 原生高清 AI 超分重构图标包
### World of Warcraft 12.1 Full 33,069 HD Icons AI Remaster System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![World of Warcraft](https://img.shields.io/badge/WoW-12.1%20%7C%20Retail%20%7C%20Classic-blue.svg)](https://worldofwarcraft.blizzard.com/)
[![Resolution](https://img.shields.io/badge/Resolution-128x128%20Native%20BLP2-green.svg)]()
[![Performance](https://img.shields.io/badge/Performance-0%20Lua%20Memory%20%7C%200%20FPS%20Loss-brightgreen.svg)]()
[![English](https://img.shields.io/badge/Language-English%20Version-blue.svg)](README_EN.md)

[🌐 English Version / 查看英文版文档](README_EN.md)

---

> 本项目基于 **Waifu2x-CUnet（点阵融化去噪）＋ 4x_foolhardy_Remacri（艺术材质超分）** 级联深度学习神经网络，对魔兽世界当前版本全量 **33,069** 个图标进行 128px 原生 DXT5 BLP2 格式完全重构。
> **100% 全局全系统覆盖**（动作条、法术书、背包物品、装备面板、天赋树、大秘境地下城手册、成就、坐骑、宠物、WA 提示等），0 内存占用，永不报错！

---

## 🖼️ 7 大风格效果一览

![全系 7 大风格纯视觉矩阵对比大图](assets/pure_icon_matrix_7_schemes_poster.png)

---

## 📦 7 大全量方案直链下载与特性索引

所有方案均为独立完整压缩包（包含完整 33,069 个 BLP 文件），点击对应方案即可直接高速下载：

| 方案编号 | 方案名称 | 核心工艺与特征 | 官方 Release 直接下载 |
| :---: | :--- | :--- | :---: |
| **方案 1** | **实心纯黑版** | 5.5px 纯黑高对比外框 + 21px 经典圆角，原画主体最醒目 | [点击下载 Scheme 1](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_1_Solid_Black.zip) |
| **方案 2** | **双层内嵌暗槽版** | 2.0px 炭灰外圈 + 3.5px 纯黑凹槽，双层深凹立体下陷感 | [点击下载 Scheme 2](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_2_Inner_Groove.zip) |
| **方案 3** | **曜石暗青铜微丝版** | 纯黑曜石底框 + 1.2px 暗哑古青铜金丝，史诗奇幻感 | [点击下载 Scheme 3](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_3_Obsidian_Bronze.zip) |
| **方案 4** | **深空炭灰大师版** | 5.0px 极简深炭灰外框，低调柔和耐看，与原生暗色 UI 完美契合 | [点击下载 Scheme 4](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_4_Charcoal_Grey.zip) |
| **方案 5** | **暴雪钛金铁灰版** | 5.0px 暴雪经典冷铁灰外框，工业硬派金属质感 | [点击下载 Scheme 5](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_5_Titanium_Grey.zip) |
| **方案 6** | **磨砂哑光银灰版** | 5.0px 哑光银灰外框，高对比中浅色系，按键轮廓边界最清晰 | [点击下载 Scheme 6](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_6_Silver_Grey.zip) |
| **方案 7** | **3D 机械键帽大师版** | R=8px 方形微导角 + 宽斜坡四棱台 + 剥离白边深炭灰修边 | [点击下载 Scheme 7](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_7_3D_Keycap.zip) |

---

## 🚀 极简安装指南

1. **完全退出** 魔兽世界游戏客户端；
2. 在上方表格中点击下载你心仪的方案压缩包（.zip）；
3. 解压压缩包，将里面的 **Interface** 文件夹，直接复制粘贴到你正在游玩的魔兽版本目录中：
   - **正式服（地心之战 / 11.0 / 12.0）**：  
     放置在 World of Warcraft\_retail_\ 目录下（最终完整路径为 World of Warcraft\_retail_\Interface\ICONS\）
   - **怀旧服（大灾变 / WLK / 20周年）**：  
     放置在 World of Warcraft\_classic_\ 目录下（最终完整路径为 World of Warcraft\_classic_\Interface\ICONS\）
   - **永久 60 级时代服（Classic Era）**：  
     放置在 World of Warcraft\_classic_era_\ 目录下（最终完整路径为 World of Warcraft\_classic_era_\Interface\ICONS\）
4. 重新启动游戏即可生效！

> 💡 **提示**：本项目是暴雪原生贴图材质替换，**不是插件**，请直接放在版本目录下的 Interface\ 中，**切勿** 放入 Interface\AddOns\ 文件夹内。

### 🗑️ 卸载与还原
直接删除对应版本目录下的 Interface\ICONS 文件夹即可瞬间恢复暴雪默认图标，安全无残留。

---

## 🔬 生产流水线与技术重构架构

1. **点阵去噪**：使用 Waifu2x-CUnet (Denoise 3) 彻底溶解 2004 年老旧点阵噪点与杂色断层；
2. **艺术超分**：调用 4x_foolhardy_Remacri 神经网络重绘至 512x512 超清母版；
3. **边框处理**：剥离暴雪原版 4.5% 泛白毛边，应用 7 种高精度 3D 几何与光照着色器；
4. **平滑采样**：通过 Lanczos 算法等比凝聚至 128x128 黄金分辨率（内置亚像素抗锯齿）；
5. **硬件压缩**：使用 DirectX Texconv 工具链烘焙生成原生 DXT5/BC3_UNORM 贴图；
6. **金字塔打包**：写入 8 级硬件 Mipmaps 原生 BLP2 格式，实现客户端 100% 全局无缝实装。

---

## 📄 开源许可证

本项目代码基于 [MIT License](LICENSE) 开源。魔兽世界相关游戏素材知识产权归 Blizzard Entertainment 所有。
