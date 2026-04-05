from pathlib import Path
from PIL import Image

src = Path('assets/source_concept.png')
out = Path('assets')

if not src.exists():
    raise SystemExit('未找到 assets/source_concept.png')

img = Image.open(src).convert('RGBA')

# 针对当前示例图的裁剪坐标（left, top, right, bottom）
regions = {
    'bg_scene.png': (45, 75, 1220, 735),
    'leaderboard_stone.png': (1240, 75, 2015, 525),
    'fx_slash_ji.png': (1290, 545, 1600, 785),
    'fx_hit_po.png': (1600, 535, 1960, 795),
    'scroll_panel.png': (85, 760, 1220, 1130),
    'option_a_red.png': (1285, 810, 1475, 1135),
    'option_b_blue.png': (1505, 810, 1695, 1135),
    'option_c_green.png': (1725, 810, 1915, 1135),
    'option_d_gold.png': (1840, 810, 2025, 1135),
}

for name, box in regions.items():
    crop = img.crop(box)
    crop.save(out / name)
    print('saved', name)
