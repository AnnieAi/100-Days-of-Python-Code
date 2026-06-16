# ══════════════════════════════════════════════════════════════════
#  替换 Cell 3 的前半段（到 DATASET = "..." 那一行为止）
#  后面的光学参数、SKIP_CALIBRATION 等等都不要动
# ══════════════════════════════════════════════════════════════════

from pathlib import Path

DATASET_ROOT = Path(r"D:\5StudyNotes\dissertation_project\Study_Resources\RunExperiment")

# ┌─────────────────────────────────────────────┐
# │  每次跑之前只改这两行！！                      │
# │                                             │
# │  第一步：选数据集                              │
CURRENT_DATASET = "diffuser"       # "diffuser" 或 "no_diffuser"
# │                                             │
# │  第二步：选NA值                               │
CURRENT_NA = 0.10                  # 从下面这些值里选一个：
# │  0.10, 0.20, 0.30, 0.40, 0.42,             │
# │  0.45, 0.47, 0.50, 0.55, 0.60, 0.70        │
# └─────────────────────────────────────────────┘

# ── 自动生成配置，不用动 ──
_PRESETS = {
    "diffuser":    dict(folder="20260515_PCO_20x_diffuser_USAF",
                        crop_cx=950, crop_cy=1223),
    "no_diffuser": dict(folder="20260515_PCO_20x_no_diffuser_USAF",
                        crop_cx=954, crop_cy=1319),
}

_p = _PRESETS[CURRENT_DATASET]
DATASET = f"NA_{CURRENT_NA:.2f}"     # 输出文件夹直接就叫 NA_0.10，不用改名

DATASETS = {
    DATASET: dict(
        folder=_p["folder"],
        crop_size=128,
        crop_cx=_p["crop_cx"],
        crop_cy=_p["crop_cy"],
        na=CURRENT_NA,
    )
}

# ══════════════════════════════════════════════════════════════════
#  跑完一个 NA 的完整流程：
#
#  1. 改上面两个变量（CURRENT_DATASET + CURRENT_NA）
#  2. Run All Cells
#  3. 等跑完（~12分钟）
#  4. Save notebook → 跑最后一个cell导出HTML
#  5. 改下一个NA值，重复
#
#  输出自动存到：
#  {数据集文件夹}/outputs/NA_0.10/
#  {数据集文件夹}/outputs/NA_0.20/
#  ...
#  跑完不用手动改文件夹名！
# ══════════════════════════════════════════════════════════════════
