# -*- coding: utf-8 -*-
import os, sys, shutil, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

BASE_PACKS_DIR = r'C:/Users/csuzy/.gemini/antigravity/scratch/wow_icon_packs'
WOW_ICONS = r'F:/World of Warcraft/_retail_/Interface/ICONS'

packs_map = {
    '1': '魔兽12.1全量高清图标包_3阶段级联大师版', # 纯黑版
    '2': '魔兽12.1全量高清图标包_方案2_双层内嵌暗槽',
    '3': '魔兽12.1全量高清图标包_方案3_曜石暗青铜微丝',
    '4': '魔兽12.1全量高清图标包_方案4_深空炭灰大师版',
    '5': '魔兽12.1全量高清图标包_方案5_暴雪钛金铁灰',
    '6': '魔兽12.1全量高清图标包_方案6_磨砂哑光银灰',
    'b2': '魔兽12.1全量高清图标包_方案B2_深炭灰微修边3D机械键帽大师版',
    '8': '魔兽12.1全量高清图标包_方案B2_深炭灰微修边3D机械键帽大师版'
}

def switch(num):
    num_str = str(num).lower()
    if num_str not in packs_map:
        print(f'未知方案编号: {num}，可选: 1, 2, 3, 4, 5, 6, b2')
        return
    folder = packs_map[num_str]
    src_dir = os.path.join(BASE_PACKS_DIR, folder, 'Interface', 'ICONS')
    if not os.path.exists(src_dir):
        print(f'方案目录尚在生成中或不存在: {src_dir}')
        return
    
    print(f'正在将【全量 33,069 个图标·{folder}】全量部署至魔兽客户端...')
    blp_files = os.listdir(src_dir)
    for bf in blp_files:
        shutil.copy2(os.path.join(src_dir, bf), os.path.join(WOW_ICONS, bf))
    print(f'✔ 成功将【方案 {num}：{folder}】全量 33,069 个图标部署完毕！请重启游戏生效。')

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else 'b2'
    switch(arg)
