# -*- coding: utf-8 -*-
"""
World of Warcraft 12.1 AI High-Definition Icon Remaster Pipeline
- Step 1: Waifu2x-CUnet (Denoise 3) dissolves 2004 legacy pixel dithering
- Step 2: 4x_foolhardy_Remacri AI model re-draws 4K artistic textures
- Step 3: Geometry & 3D Lighting Shaders (7 Schemes)
- Step 4: Texconv BC3_UNORM + BLP2 Mipmap Packaging
"""

import os, sys, io, struct, zipfile, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.ndimage import sobel, distance_transform_edt

SIZE = 128
SS = 4
SW, SH = SIZE * SS, SIZE * SS # 512x512
SR = int(21 * SS)

# 128x128 DXT5 BLP2 Header (8-level Mipmaps)
MIP_LENGTHS_128 = [16384, 4096, 1024, 256, 64, 16, 16, 16]
OFFSETS_128 = [0] * 16
LENGTHS_128 = [0] * 16
cur_offset = 148
for i, l in enumerate(MIP_LENGTHS_128):
    OFFSETS_128[i] = cur_offset
    LENGTHS_128[i] = l
    cur_offset += l

BLP_HEADER_128 = struct.pack(
    '<4s I B B B B I I 16I 16I',
    b'BLP2', 1, 2, 8, 7, 1, 128, 128,
    *OFFSETS_128, *LENGTHS_128
)

def build_scheme_4_charcoal_grey(core_img):
    """Scheme 4: Deep Space Charcoal Grey (#2a2d36)"""
    bw = int(5.0 * SS)
    hw = bw // 2
    inner_mask = Image.new('L', (SW, SH), 0)
    ImageDraw.Draw(inner_mask).rounded_rectangle([(bw, bw), (SW - bw - 1, SH - bw - 1)], radius=max(0, SR - bw), fill=255)
    canvas = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
    canvas.paste(core_img.resize((SW, SH), Image.Resampling.LANCZOS), (0, 0), mask=inner_mask)
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([(hw, hw), (SW - hw - 1, SH - hw - 1)], radius=SR - hw, outline=(42, 45, 54, 255), width=bw)
    
    outer_mask = Image.new('L', (SW, SH), 0)
    ImageDraw.Draw(outer_mask).rounded_rectangle([(2, 2), (SW - 3, SH - 3)], radius=SR - 2, fill=255)
    outer_mask = outer_mask.filter(ImageFilter.GaussianBlur(radius=1.8))
    
    final_l = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
    final_l.paste(canvas, (0, 0), mask=outer_mask)
    return final_l.resize((SIZE, SIZE), Image.Resampling.LANCZOS)

def build_scheme_b2_3d_keycap(core_img):
    """Scheme B-2: 3D Mechanical Keyboard Keycap (R=8px, 3D Bevel, Stripped White Edge)"""
    w_raw, h_raw = core_img.size
    crop_margin = int(w_raw * 0.045)
    core_stripped = core_img.crop((crop_margin, crop_margin, w_raw - crop_margin, h_raw - crop_margin))
    
    corner_r, bevel_w = 8, 14
    sr = int(corner_r * SS)
    margin = 20
    bw_bevel = int(bevel_w * SS)
    top_margin = margin + bw_bevel
    top_w = SW - top_margin * 2
    top_r = max(0, sr - bw_bevel//3)
    
    mask_outer = Image.new('L', (SW, SH), 0)
    ImageDraw.Draw(mask_outer).rounded_rectangle([(margin, margin), (SW - margin - 1, SH - margin - 1)], radius=sr, fill=255)
    mask_top = Image.new('L', (SW, SH), 0)
    ImageDraw.Draw(mask_top).rounded_rectangle([(top_margin, top_margin), (SW - top_margin - 1, SH - top_margin - 1)], radius=top_r, fill=255)
    
    arr_out = np.array(mask_outer, dtype=np.float32) / 255.0
    arr_top = np.array(mask_top, dtype=np.float32) / 255.0
    dist_out = distance_transform_edt(arr_out > 0.5)
    slope = np.clip(dist_out / float(bw_bevel), 0.0, 1.0)
    slope_curve = np.sin(slope * (np.pi / 2.0)) ** 0.85
    heightmap = slope_curve * (arr_out > 0.5)
    heightmap[arr_top > 0.5] = 1.0
    
    dz_dx = sobel(heightmap, axis=1) * 12.0
    dz_dy = sobel(heightmap, axis=0) * 12.0
    nz = np.ones((SH, SW), dtype=np.float32)
    norm = np.sqrt(dz_dx**2 + dz_dy**2 + nz**2)
    nx, ny, nz = -dz_dx/norm, -dz_dy/norm, nz/norm
    
    lx, ly, lz = -0.58, -0.68, 0.45
    l_len = np.sqrt(lx**2 + ly**2 + lz**2)
    lx, ly, lz = lx/l_len, ly/l_len, lz/l_len
    dot_l = np.clip(nx * lx + ny * ly + nz * lz, 0.0, 1.0)
    
    fx, fy, fz = 0.50, 0.60, 0.62
    f_len = np.sqrt(fx**2 + fy**2 + fz**2)
    fx, fy, fz = fx/f_len, fy/f_len, fz/f_len
    dot_f = np.clip(nx * fx + ny * fy + nz * fz, 0.0, 1.0)
    
    vx, vz = 0.0, 1.0
    hx, hy, hz = lx + vx, ly, lz + vz
    h_len = np.sqrt(hx**2 + hy**2 + hz**2)
    hx, hy, hz = hx/h_len, hy/h_len, hz/h_len
    spec = np.clip(nx * hx + ny * hy + nz * hz, 0.0, 1.0) ** 18.0
    
    base_r, base_g, base_b = 50.0, 54.0, 68.0
    frame_r = base_r * (0.30 + 1.10 * dot_l + 0.35 * dot_f) + 140.0 * spec
    frame_g = base_g * (0.30 + 1.10 * dot_l + 0.35 * dot_f) + 155.0 * spec
    frame_b = base_b * (0.30 + 1.10 * dot_l + 0.35 * dot_f) + 180.0 * spec
    
    frame_alpha = (arr_out * 255.0).astype(np.uint8)
    frame_rgba = np.stack([np.clip(frame_r, 0, 255).astype(np.uint8),
                          np.clip(frame_g, 0, 255).astype(np.uint8),
                          np.clip(frame_b, 0, 255).astype(np.uint8),
                          frame_alpha], axis=2)
    frame_img = Image.fromarray(frame_rgba, 'RGBA')
    
    shadow_mask_deep = Image.new('L', (SW, SH), 0)
    ImageDraw.Draw(shadow_mask_deep).rounded_rectangle([(margin - 2, margin + 12), (SW - margin + 1, SH - margin + 14)], radius=sr, fill=220)
    shadow_mask_deep = shadow_mask_deep.filter(ImageFilter.GaussianBlur(radius=10.0))
    
    shadow_mask_tight = Image.new('L', (SW, SH), 0)
    ImageDraw.Draw(shadow_mask_tight).rounded_rectangle([(margin, margin + 6), (SW - margin - 1, SH - margin + 6)], radius=sr, fill=255)
    shadow_mask_tight = shadow_mask_tight.filter(ImageFilter.GaussianBlur(radius=4.0))
    
    shadow_layer = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
    shadow_layer.paste((0, 0, 0, 240), (0, 0), mask=shadow_mask_deep)
    shadow_layer.paste((0, 0, 0, 255), (0, 0), mask=shadow_mask_tight)
    
    canvas = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
    canvas = Image.alpha_composite(canvas, shadow_layer)
    canvas = Image.alpha_composite(canvas, frame_img)
    
    mask_top_local = Image.new('L', (top_w, top_w), 0)
    ImageDraw.Draw(mask_top_local).rounded_rectangle([(0, 0), (top_w - 1, top_w - 1)], radius=top_r, fill=255)
    
    sheen = Image.new('RGBA', (top_w, top_w), (0, 0, 0, 0))
    for y in range(top_w):
        prog = y / float(top_w)
        if prog < 0.35:
            alpha = int(20 * ((0.35 - prog) / 0.35))
            for x in range(top_w):
                sheen.putpixel((x, y), (255, 255, 255, alpha))
        elif prog > 0.70:
            alpha = int(24 * ((prog - 0.70) / 0.30))
            for x in range(top_w):
                sheen.putpixel((x, y), (0, 0, 0, alpha))
                
    art_scaled = core_stripped.resize((top_w, top_w), Image.Resampling.LANCZOS)
    art_printed = Image.alpha_composite(art_scaled, sheen)
    art_layer = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
    art_layer.paste(art_printed, (top_margin, top_margin), mask=mask_top_local)
    canvas = Image.alpha_composite(canvas, art_layer)
    
    d_tr = ImageDraw.Draw(canvas)
    d_tr.rounded_rectangle([(top_margin, top_margin), (SW - top_margin - 1, SH - top_margin - 1)], radius=top_r, outline=(30, 34, 44, 255), width=int(1.5 * SS))
    
    ridge_layer = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
    d_rd = ImageDraw.Draw(ridge_layer)
    c_out_tl = (margin + int(sr * 0.35), margin + int(sr * 0.35))
    c_in_tl = (top_margin, top_margin)
    c_out_tr = (SW - margin - int(sr * 0.35), margin + int(sr * 0.35))
    c_in_tr = (SW - top_margin, top_margin)
    c_out_bl = (margin + int(sr * 0.35), SH - margin - int(sr * 0.35))
    c_in_bl = (top_margin, SH - top_margin)
    c_out_br = (SW - margin - int(sr * 0.35), SH - margin - int(sr * 0.35))
    c_in_br = (SW - top_margin, SH - top_margin)
    d_rd.line([c_out_tl, c_in_tl], fill=(225, 235, 255, 170), width=int(1.6 * SS))
    d_rd.line([c_out_tr, c_in_tr], fill=(160, 175, 200, 120), width=int(1.2 * SS))
    d_rd.line([c_out_bl, c_in_bl], fill=(50, 55, 66, 140), width=int(1.2 * SS))
    d_rd.line([c_out_br, c_in_br], fill=(20, 24, 32, 170), width=int(1.8 * SS))
    ridge_layer = ridge_layer.filter(ImageFilter.GaussianBlur(radius=1.8))
    canvas = Image.alpha_composite(canvas, ridge_layer)
    
    return canvas.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
