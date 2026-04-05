# 古风素材切片说明（像素级还原）

请把你提供的整张概念图放到：

- `assets/source_concept.png`

然后运行：

```bash
python tools/slice_assets.py
```

会自动输出以下小图（供 `index.html` 精确绑定）：

- `assets/bg_scene.png`（主背景战场）
- `assets/leaderboard_stone.png`（英豪录石碑）
- `assets/fx_slash_ji.png`（击字特效）
- `assets/fx_hit_po.png`（破字受击特效）
- `assets/scroll_panel.png`（卷轴题干框）
- `assets/option_a_red.png`（A 朱红）
- `assets/option_b_blue.png`（B 深蓝）
- `assets/option_c_green.png`（C 墨绿）
- `assets/option_d_gold.png`（D 金纹）

> 坐标按当前上传图（约 2048x1365）手工标定。如你换了不同尺寸图片，可在 `tools/slice_assets.py` 里调整坐标。
