# World of Warcraft 12.1 Full 33,069 HD Icons AI Remaster System
### 魔兽世界 12.1 全量 33,069 原生高清 AI 超分重构图标包体系

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![World of Warcraft](https://img.shields.io/badge/WoW-12.1%20%7C%20Retail%20%7C%20Classic-blue.svg)](https://worldofwarcraft.blizzard.com/)
[![Resolution](https://img.shields.io/badge/Resolution-128x128%20Native%20BLP2-green.svg)]()
[![Performance](https://img.shields.io/badge/Performance-0%20Lua%20Memory%20%7C%200%20FPS%20Loss-brightgreen.svg)]()
[![Chinese](https://img.shields.io/badge/Language-简体中文-red.svg)](README.md)

[🇨🇳 简体中文版 / View Simplified Chinese Document](README.md)

---

> An end-to-end AI Super-Resolution remaster system for all **33,069** icons in World of Warcraft 12.1.
> Powered by **Waifu2x-CUnet (artifact melting) + 4x_foolhardy_Remacri (neural texture reconstruction)** in native 128x128 DXT5 BLP2 format with full 8-level Mipmaps.
> **100% full-game coverage** (Action bars, Spellbook, Bags, Talents, Adventure Guide, Mounts, Macros, WeakAuras). Zero Lua memory, zero FPS impact, zero errors!

---

## 🖼️ Style Showcase

![All 7 Styles Matrix Comparison](assets/pure_icon_matrix_7_schemes_poster.png)

---

## 📦 Direct Download Links & 7 Distinct Style Variants

Each scheme is packaged as a standalone full archive containing all 33,069 BLP files:

| Scheme | Style Name | Visual Craft & Geometry | Official Release Download |
| :---: | :--- | :--- | :---: |
| **Scheme 1** | **Solid Black** | 5.5px Solid Black Border + 21px Classic Radius, maximum artwork pop | [Download Scheme 1](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_1_Solid_Black.zip) |
| **Scheme 2** | **Dual Inner Groove** | 2.0px Charcoal Outer + 3.5px Pure Black Groove, sunken 3D depth | [Download Scheme 2](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_2_Inner_Groove.zip) |
| **Scheme 3** | **Obsidian Bronze** | Obsidian Base + 1.2px Ancient Bronze Filigree, epic fantasy mood | [Download Scheme 3](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_3_Obsidian_Bronze.zip) |
| **Scheme 4** | **Charcoal Grey** | 5.0px Minimalist Deep Charcoal Border, highly ergonomic & subtle with default UI | [Download Scheme 4](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_4_Charcoal_Grey.zip) |
| **Scheme 5** | **Titanium Grey** | 5.0px Blizzard Cold Iron Grey Border, industrial metallic hardness | [Download Scheme 5](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_5_Titanium_Grey.zip) |
| **Scheme 6** | **Matte Silver** | 5.0px Matte Silver Grey Border, high-contrast & ultra-clear button outlines | [Download Scheme 6](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_6_Silver_Grey.zip) |
| **Scheme 7** | **3D Keycap Master** | R=8px Square Bevel + PBT Convex Keycap + Charcoal Trim | [Download Scheme 7](https://github.com/tzdy1993/wow-hd-icons-remaster/releases/download/v1.0.0/WoW_12.1_HD_Icons_Scheme_7_3D_Keycap.zip) |

---

## 🚀 Simple Installation

1. Exit the World of Warcraft client completely;
2. Click to download your preferred scheme `.zip` from the table above;
3. Extract and place files into the exact destination folder:

- **Retail Path**:  
  `F:\World of Warcraft\_retail_\Interface\ICONS\`

- **Classic Path**:  
  `F:\World of Warcraft\_classic_\Interface\ICONS\`

- **Classic Era Path**:  
  `F:\World of Warcraft\_classic_era_\Interface\ICONS\`

*(Note: Replace `F:\` with your actual game installation drive)*

4. Launch the game and enjoy!

> 💡 **Note**: Place directly under `Interface\ICONS\`, **DO NOT** put it into `Interface\AddOns\`.

### 🗑️ Uninstallation
Simply delete the `Interface\ICONS\` folder from your game directory.

---

## 🔬 Technical Pipeline Architecture

1. **Artifact Denoising**: `Waifu2x-CUnet (Denoise 3)` dissolves legacy 2004 pixel dithering and compression noise;
2. **Neural Upscaling**: `4x_foolhardy_Remacri` reconstructs 512x512 ultra-crisp master artwork;
3. **Border Geometry**: Strips 4.5% Blizzard white bleed and bakes 7 distinct 3D lighting/bevel shaders;
4. **Sub-pixel Downsampling**: Lanczos downscaling to 128x128 with sub-pixel anti-aliasing;
5. **DirectX Compression**: Hardware-native DXT5/BC3_UNORM texture baking via Texconv;
6. **BLP2 Packaging**: 8-level Mipmap packaging for 100% native in-game deployment.

---

## 📄 License

Code is licensed under the [MIT License](LICENSE). All World of Warcraft game assets and intellectual property belong to Blizzard Entertainment.
