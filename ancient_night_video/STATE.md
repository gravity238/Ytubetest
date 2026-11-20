# STATE — ancient_night_video

| Field | Value |
|---|---|
| Project | `ancient_night_video` |
| Branch | `arena/8408c759-ytubetest` |
| Opened | 2026-11-20 |
| Current state | **STATE 5 — FRAME GENERATION (Worker 1 in progress)** |

---

## State log

### STATE 0 — Repo discovery ✅
Repo was empty except `README.md`. No existing pipeline scripts. Conventions established from scratch: `<slug>_video/` folders, `frames/beatNNMNN.png`, `run_<slug>_kaggle.sh` in root.

### STATE 0.5 — Resume check ✅
No existing project folders. User chose fresh, topic sourced from gap analysis.

### STATE 1 — Brief ✅
Brief captured. Style deferred to user reference, delivered as `refs/reference1.png`.
**Locked:** `brief.md`

### STATE 2 — Scripting ✅ APPROVED
- `script.md` — 1,940 words, second person, projected 10:25 (channel average 10:26).
- All 8 "must appear" beats present; all 7 "must never appear" exclusions verified absent.
- Approved by user 2026-11-20. Defaults locked: watch beat kept clean of the mating reference; full micro-beat density.

### STATE 3 — The spine ✅
- `visuals.csv` — **316 rows across 21 slides**, exactly 1,940 words (100% script coverage).
- Validated: 0 missing tags, 0 invalid world/figure tags, **0 duplicate prompts**.
- Every row varies camera framing; consecutive rows never repeat room description.
- `build_prompts.py` assembles prompts from the verbatim blocks in `continuity.md` at runtime.
- `prompts.csv` — all 316 assembled prompts, avg 2,450 chars.

### STATE 4 — Anchors & dispatch ✅
- 3 style tests generated; **2 roll iterations required on the cave anchor**.
- **D1** hide wrap → tunic with torso. **D2** firelight → hard faceted wedges. **D3** mouth too high.
- All three defects fixed at the source in `continuity.md`, so every one of the 316 prompts inherits the fix.
- Final anchors: `style_test_cave_v3.png`, `style_test_night.png`, `style_test_abstract.png`.
- Rejected rolls retained in `refs/` for audit.
- Worker split calculated and packets issued.

### STATE 5 — Frame generation 🔄
- **Worker 1 (this chat): rows 1–79** (beat01m01 → beat09m10) — IN PROGRESS
- Worker 2: rows 80–158 (beat09m11 → beat15m04)
- Worker 3: rows 159–237 (beat15m05 → beat19m12)
- Worker 4: rows 238–316 (beat19m13 → beat21m28)
- Repair budget R=2 per batch; single-clause mutation rule enforced.

### STATE 5.1 — Swarm merge ⏸
Blocked on workers. See branch note below.

### STATE 5.5 — Thumbnail ✅
- `thumbnail.jpg` — 16:9, single text element "3AM", two dominant shapes (round face + lettering).
- Roll 1 rejected: the "M" was clipped by the frame edge (also where YouTube's duration overlay lands).
- Roll 2 approved. Reads at mobile scale.

### STATE 6 — Kaggle runner ✅
- `../run_ancient_night_kaggle.sh` written and syntax-checked.
- Verified independently: TTS text cleanup preserves all 1,940 words.
- Preflight dies on: missing files, missing frames, unresolvable voice, empty video.
- PIL pre-padding, concat demuxer, hard cuts only, aac 192k, -14 LUFS, yuv420p, 30fps.
- Packaging: VIDEO.mp4 + thumbnail.jpg + metadata.json + script.md + youtube.txt.

### STATE 7 — Handoff ⏸
Pending all 316 frames.

---

## Declared exceptions

| Frame | Issue | Resolution |
|---|---|---|
| — | none yet | — |

---

## Branch policy note

The spec's STATE 4 and STATE 5.1 assume workers push to `main` and merge from `main`. **They cannot.** This session is pinned to `arena/8408c759-ytubetest`, and `origin/main` contains only `README.md`. All worker packets therefore target `arena/8408c759-ytubetest`. Worker sub-branches are unsafe here (the platform can only push the session branch), so workers commit directly to the session branch in disjoint row ranges. STATE 5.1's merge is a no-op for this run; verification is a gap check on `frames/` instead.

## Audio boundary

No TTS, no FFmpeg, no audio mixing in this workspace. All deferred to `run_ancient_night_kaggle.sh` on Kaggle.
