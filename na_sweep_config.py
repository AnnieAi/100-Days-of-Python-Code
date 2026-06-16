# ══════════════════════════════════════════════════════════════════
#  复制下面这整块替换到 notebook Cell 3 的对应位置
# ══════════════════════════════════════════════════════════════════

from pathlib import Path

DATASET_ROOT = Path(r"D:\5StudyNotes\dissertation_project\Study_Resources\RunExperiment")

# ── NA sweep 配置 ──────────────────────────────────────────────
# crop_cx / crop_cy 沿用 Teerameth 原始配置
#   diffuser USAF:    crop_cx=950,  crop_cy=1223
#   no_diffuser USAF: crop_cx=954,  crop_cy=1319
#
# 第一次跑之前建议用 Step 3a histogram explorer 确认一下 crop 中心
# 对不对，不对的话改这里的 crop_cx / crop_cy 就行

NA_VALUES = [0.10, 0.20, 0.30, 0.40, 0.42, 0.45, 0.47, 0.50, 0.55, 0.60, 0.70]

DATASETS = {}

# ── Dataset 1: diffuser + USAF ──
for na in NA_VALUES:
    key = f"usaf_diffuser_NA{na:.2f}"
    DATASETS[key] = dict(
        folder="20260515_PCO_20x_diffuser_USAF",
        crop_size=128,
        crop_cx=950,
        crop_cy=1223,
        na=na,
    )

# ── Dataset 2: no_diffuser + USAF ──
for na in NA_VALUES:
    key = f"usaf_no_diffuser_NA{na:.2f}"
    DATASETS[key] = dict(
        folder="20260515_PCO_20x_no_diffuser_USAF",
        crop_size=128,
        crop_cx=954,
        crop_cy=1319,
        na=na,
    )

# ══════════════════════════════════════════════════════════════════
#  每次跑一个 NA 值，改下面这一行就行：
# ══════════════════════════════════════════════════════════════════

DATASET = "usaf_diffuser_NA0.10"    # ← 改这里，然后 Run All Cells

# ══════════════════════════════════════════════════════════════════
#  所有可用的 key（方便复制粘贴）：
#
#  --- diffuser USAF ---
#  "usaf_diffuser_NA0.10"
#  "usaf_diffuser_NA0.20"
#  "usaf_diffuser_NA0.30"
#  "usaf_diffuser_NA0.40"
#  "usaf_diffuser_NA0.42"
#  "usaf_diffuser_NA0.45"
#  "usaf_diffuser_NA0.47"
#  "usaf_diffuser_NA0.50"
#  "usaf_diffuser_NA0.55"
#  "usaf_diffuser_NA0.60"
#  "usaf_diffuser_NA0.70"
#
#  --- no_diffuser USAF ---
#  "usaf_no_diffuser_NA0.10"
#  "usaf_no_diffuser_NA0.20"
#  "usaf_no_diffuser_NA0.30"
#  "usaf_no_diffuser_NA0.40"
#  "usaf_no_diffuser_NA0.42"
#  "usaf_no_diffuser_NA0.45"
#  "usaf_no_diffuser_NA0.47"
#  "usaf_no_diffuser_NA0.50"
#  "usaf_no_diffuser_NA0.55"
#  "usaf_no_diffuser_NA0.60"
#  "usaf_no_diffuser_NA0.70"
# ══════════════════════════════════════════════════════════════════
