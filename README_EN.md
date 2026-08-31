# ⚔️ World of Warcraft 12.1 Full 33,069 HD Icons AI Remaster System
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

## 🖼️ Style Matrix Showcase

![All 7 Styles Matrix Comparison](assets/pure_icon_matrix_7_schemes_poster.png)

---

## 🎨 7 Distinct Style Variants

| Scheme | Style Name | Visual Craft & Geometry | Best For |
| :---: | :--- | :--- | :--- |
| **Scheme 1** | **Solid Black** | 5.5px Solid Black Border + 21px Classic Radius | High contrast, maximum artwork pop |
| **Scheme 2** | **Dual Inner Groove** | 2.0px Charcoal Outer + 3.5px Pure Black Groove | Dark dungeon style, sunken 3D depth |
| **Scheme 3** | **Obsidian Bronze** | Obsidian Base + 1.2px Ancient Bronze Filigree | Classic Warcraft high-fantasy epic mood |
| **Scheme 4** | **Charcoal Grey** | 5.0px #2a2d36 Minimalist Deep Charcoal | Highly ergonomic, subtle, perfect with default UI |
| **Scheme 5** | **Titanium Grey** | 5.0px #484c58 Blizzard Cold Iron Grey | Industrial metallic hardness, crisp & solid |
| **Scheme 6** | **Matte Silver** | 5.0px #737887 Light Matte Silver Grey | Ultra-clear button outlines during intense raids |
| **Scheme 7** | **3D Keycap Master** | =8\text{px}$ Square Bevel + PBT Convex Keycap | Custom mechanical keyboard physical keycap feel |

---

## 🚀 Quick Installation

1. Exit the World of Warcraft client completely;
2. Download your preferred scheme .zip from the [Releases](https://github.com/tzdy1993/wow-hd-icons-remaster/releases) page;
3. Extract and copy the **Interface** folder directly into your WoW root directory:
   - **Retail Path**: World of Warcraft\_retail_\
   - **Classic Path**: World of Warcraft\_classic_\
4. Launch the game and enjoy!

### 🗑️ Uninstallation
Simply delete the Interface\ICONS folder from your WoW directory.

---

## ⚡ Fast Scheme Switcher

`ash
# Switch to Scheme 4 (Charcoal Grey)
python switch_full_pack.py 4

# Switch to Scheme 7 (3D Keycap)
python switch_full_pack.py b2

# Switch to Scheme 5 (Titanium Grey)
python switch_full_pack.py 5
`

---

## 🔬 Technical Pipeline Architecture

`mermaid
graph TD
    A[Raw 64x64 CleanIcons 33,069 Icons] --> B[Waifu2x-CUnet Denoise 3 Dissolve 2004 Dithering]
    B --> C[4x_foolhardy_Remacri DirectML GPU 512x512 Upscaling]
    C --> D[Edge Trimming: Strip 4.5% Blizzard Bleed]
    D --> E[Multi-scheme 3D Lighting & Geometry Baking]
    E --> F[Lanczos 128x128 Sub-pixel Anti-Aliasing]
    F --> G[DirectX Texconv Hardware BC3_UNORM Compression]
    G --> H[Native BLP2 Packaging with 8 Mipmap Levels]
    H --> I[WoW Client Interface/ICONS 100% In-Game Coverage]
`

---

## 📄 License

Code is licensed under the [MIT License](LICENSE). All World of Warcraft game assets and intellectual property belong to Blizzard Entertainment.
