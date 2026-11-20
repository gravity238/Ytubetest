# STATE — ancient_night_video

| Field | Value |
|---|---|
| Project | `ancient_night_video` |
| Branch | `arena/8408c759-ytubetest` |
| Opened | 2026-11-20 |
| Current state | **STATE 2 — SCRIPTING (awaiting approval)** |

---

## State log

### STATE 0 — Repo discovery ✅
Repo was empty except `README.md`. No existing pipeline scripts, no naming conventions to follow. Established conventions from scratch: `<slug>_video/` project folders, `frames/beatNNMNN.png`, `run_<slug>_kaggle.sh` in repo root.

### STATE 0.5 — Resume check ✅
Scanned root only. No existing project folders found. User chose to start fresh with a new topic sourced from gap analysis.

### STATE 1 — Brief ✅
Brief captured from user answers + gap analysis. Defaults applied for voice, pace, POV, aspect, captions. Style deferred to user-supplied reference, which arrived as `refs/reference1.png`.

**Brief locked:** `brief.md`

### STATE 2 — Scripting 🔄
- `script.md` written — 1,867 words, second person.
- Header printed for approval.
- **Awaiting explicit user approval.**

### STATE 3 — Spine ❌ not started
### STATE 4 — Anchors & dispatch ❌ not started
### STATE 5 — Frames ❌ not started
### STATE 5.1 — Merge ❌ not started
### STATE 5.5 — Thumbnail ❌ not started
### STATE 6 — Kaggle runner ❌ not started
### STATE 7 — Handoff ❌ not started

---

## Declared exceptions

*None.*

---

## Notes

- **Branch policy override:** the spec's STATE 4/5.1 instructs workers to push to `main` and merge from `main`. This session is pinned to `arena/8408c759-ytubetest` and cannot leave it. Worker packets will target the current branch with worker sub-branches only if the platform allows; otherwise workers commit directly to this branch. Merge protocol (5.1) is therefore a no-op for this run.
- **Audio boundary:** no TTS, no FFmpeg, no audio mixing in this workspace. All of it is deferred to `run_ancient_night_kaggle.sh`.
