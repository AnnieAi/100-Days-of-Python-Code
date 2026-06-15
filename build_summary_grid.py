"""
Build the NA-sweep summary figure for one dataset.

读取 {DATASET_FOLDER}/outputs/NA_*/*_reconstructed_full.bmp，
拼成一张 grid（每个 NA 一格），存到 {DATASET_FOLDER}/outputs/ 根目录。

用法：改下面的 DATASET_FOLDER，然后直接运行这个脚本（在 FPM 环境下）。
不需要 notebook，不需要 kernel，纯读硬盘上已经存好的 BMP。
"""

from pathlib import Path
import re
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ┌──────────────────────────────────────────────────────────┐
# │  改这一行：指向某个数据集的文件夹                            │
# └──────────────────────────────────────────────────────────┘
DATASET_FOLDER = Path(
    r"D:\5StudyNotes\dissertation_project\Study_Resources\RunExperiment\20260515_PCO_20x_no_diffuser_USAF"
)

# ── 以下不用动 ────────────────────────────────────────────────
OUTPUTS_DIR = DATASET_FOLDER / "outputs"
DATASET_NAME = DATASET_FOLDER.name        # 用作图标题


def na_from_folder(folder_name: str):
    """从 'NA_0.10' 里抠出 0.10 用于排序和标题。"""
    m = re.search(r"NA[_-]?([0-9]*\.?[0-9]+)", folder_name)
    return float(m.group(1)) if m else None


# 找到所有 NA_x.xx 文件夹，按 NA 数值从小到大排
na_folders = []
for d in OUTPUTS_DIR.iterdir():
    if d.is_dir():
        na = na_from_folder(d.name)
        if na is not None:
            na_folders.append((na, d))
na_folders.sort(key=lambda t: t[0])

if not na_folders:
    raise RuntimeError(f"在 {OUTPUTS_DIR} 里没找到任何 NA_* 文件夹")

print(f"找到 {len(na_folders)} 个 NA 文件夹：{[f'{na:.2f}' for na, _ in na_folders]}")

# 逐个读取每个 NA 文件夹里的 reconstructed_full BMP
panels = []   # (na, image_array)
for na, folder in na_folders:
    bmps = list(folder.glob("*_reconstructed_full.bmp"))
    if not bmps:
        print(f"  [跳过] NA={na:.2f} 文件夹里没有 *_reconstructed_full.bmp")
        continue
    if len(bmps) > 1:
        print(f"  [注意] NA={na:.2f} 找到多个 bmp，用第一个：{bmps[0].name}")
    img = np.array(Image.open(bmps[0]).convert("L"))   # 灰度
    panels.append((na, img))
    print(f"  NA={na:.2f}  <-  {bmps[0].name}  shape={img.shape}")

if not panels:
    raise RuntimeError("一个 reconstructed_full.bmp 都没读到，检查文件名对不对")

# ── 排版：尽量接近方形的 grid ──
n = len(panels)
ncols = 3 if n <= 9 else 4          # 11 个 NA -> 4 列
nrows = int(np.ceil(n / ncols))

fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * 3.2, nrows * 3.2))
axes = np.atleast_1d(axes).ravel()

for ax, (na, img) in zip(axes, panels):
    ax.imshow(img, cmap="gray")
    ax.set_title(f"NA = {na:g}", fontsize=11)
    ax.axis("off")

# 多出来的空格子隐藏掉
for ax in axes[len(panels):]:
    ax.axis("off")

fig.suptitle(f"{DATASET_NAME} — reconstructed amplitude vs NA", fontsize=14)
fig.tight_layout(rect=[0, 0, 1, 0.97])

# ── 保存到 outputs 根目录 ──
out_path = OUTPUTS_DIR / f"{DATASET_NAME}_amplitude_vs_NA.png"
fig.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"\n✅ summary figure 已保存：{out_path}")
plt.show()
