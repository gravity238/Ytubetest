#!/usr/bin/env bash
# =============================================================================
#  run_ancient_night_kaggle.sh
#  Builds ancient_night_DELIVERABLE.zip on Kaggle.
#
#  THIS SCRIPT IS THE ONLY PLACE AUDIO EXISTS.
#  TTS, mixing, FFmpeg encoding and packaging all happen here — never in the
#  working repo.
#
#  Usage (Kaggle cell):
#      !rm -rf Ytubetest
#      !git clone --depth 1 --branch arena/8408c759-ytubetest \
#            https://github.com/gravity238/Ytubetest.git
#      !bash Ytubetest/run_ancient_night_kaggle.sh
# =============================================================================
set -Eeuo pipefail

SLUG="ancient_night"
BRANCH="arena/8408c759-ytubetest"
REPO_URL="${REPO_URL:-https://github.com/gravity238/Ytubetest.git}"
REPO_DIR="${REPO_DIR:-Ytubetest}"
PROJ="${REPO_DIR}/${SLUG}_video"
VOICE="en-US-AndrewNeural"
RATE="+10%"
FPS=30

log()  { printf '\n\033[1;36m[%s]\033[0m %s\n' "$(date +%H:%M:%S)" "$*"; }
die()  { printf '\n\033[1;31m[PREFLIGHT FAIL]\033[0m %s\n' "$*" >&2; exit 1; }

# -----------------------------------------------------------------------------
# 1. DEPENDENCIES
# -----------------------------------------------------------------------------
log "Installing dependencies"
if command -v apt-get >/dev/null 2>&1; then
  apt-get -qq update >/dev/null 2>&1 || true
  apt-get -qq install -y ffmpeg >/dev/null 2>&1 || true
fi
command -v ffmpeg >/dev/null 2>&1 || die "ffmpeg is not available"
python3 -m pip install -q --upgrade edge-tts pillow || die "pip install failed"
python3 - <<'PY' || die "python deps missing"
import edge_tts, PIL
print("edge-tts + pillow ok")
PY

# -----------------------------------------------------------------------------
# 2. CLONE / UPDATE
# -----------------------------------------------------------------------------
if [ ! -d "$PROJ" ]; then
  log "Cloning $REPO_URL (branch $BRANCH)"
  rm -rf "$REPO_DIR"
  git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$REPO_DIR" \
    || die "clone failed — does branch '$BRANCH' exist and is it pushed?"
fi
cd "$PROJ"

log "Repo state: $(git rev-parse --short HEAD 2>/dev/null || echo 'no-git') on $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"

# -----------------------------------------------------------------------------
# 3. PREFLIGHT — die before doing any work
# -----------------------------------------------------------------------------
log "Preflight"

for f in visuals.csv script.md metadata.json thumbnail.jpg continuity.md; do
  [ -f "$f" ] || die "missing required file: $f"
done

FRAME_COUNT=$(python3 -c "
import csv
print(sum(1 for _ in csv.DictReader(open('visuals.csv'))))
")
log "visuals.csv declares $FRAME_COUNT frames"

[ "$FRAME_COUNT" -gt 0 ] || die "visuals.csv has no rows"

log "Checking every declared frame exists on disk"
python3 - <<'PY' || die "frame preflight failed"
import csv, os, sys
missing=[]
for r in csv.DictReader(open('visuals.csv')):
    fn = "frames/beat%02dm%02d.png" % (int(r['slide_id']), int(r['moment']))
    if not os.path.isfile(fn):
        missing.append(fn)
if missing:
    print("MISSING %d frames, first 10:" % len(missing))
    for m in missing[:10]: print("   ", m)
    sys.exit(1)
print("all frames present")
PY

python3 - <<'PY' || die "unresolvable voice"
import asyncio, sys
import edge_tts
async def main():
    vs = await edge_tts.list_voices()
    names = {v["ShortName"] for v in vs}
    if "en-US-AndrewNeural" not in names:
        print("voice en-US-AndrewNeural not offered by this edge-tts"); sys.exit(1)
    print("voice resolved: en-US-AndrewNeural")
asyncio.run(main())
PY

# -----------------------------------------------------------------------------
# 4. TTS — ONE CONTINUOUS TAKE with word-level timestamps
# -----------------------------------------------------------------------------
log "Narration: one continuous take, $VOICE at $RATE"
python3 - <<'PY' || die "TTS failed"
import asyncio, re, json, sys
import edge_tts

VOICE = "en-US-AndrewNeural"
RATE  = "+10%"

raw = open("script.md", encoding="utf-8").read()
# drop the markdown header block, keep the spoken body
body = raw.split("---", 1)[1] if raw.count("---") >= 1 else raw
# strip markdown emphasis / heading marks, keep punctuation for prosody
text = re.sub(r"\*\*(.+?)\*\*", r"\1", body)
text = re.sub(r"\*(.+?)\*",     r"\1", text)
text = re.sub(r"^#+ .*$",       "",    text, flags=re.M)
text = text.replace("—", ", ").replace("–", ", ")
text = re.sub(r"\n{2,}", "\n", text)
text = re.sub(r"[ \t]+", " ", text).strip()

words = len(re.findall(r"[A-Za-z0-9']+", text))
print(f"narration words: {words}")

async def main():
    comm = edge_tts.Communicate(text, VOICE, rate=RATE)
    with open("narration.mp3", "wb") as f:
        pass
    marks = []
    with open("narration.mp3", "wb") as audio:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                audio.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                marks.append({
                    "text":  chunk["text"],
                    "start": chunk["offset"] / 10_000_000.0,   # 100ns -> s
                    "dur":   chunk["duration"] / 10_000_000.0,
                })
    json.dump(marks, open("word_timings.json", "w"), indent=0)
    print(f"word boundaries: {len(marks)}")
    if marks:
        print(f"spoken duration: {marks[-1]['start'] + marks[-1]['dur']:.1f}s")

asyncio.run(main())
PY

# -----------------------------------------------------------------------------
# 5. MAP WORD TIMESTAMPS -> FRAME DURATIONS
#    Each frame holds for the exact spoken duration of its moment_text.
#    Durations are NEVER hand-placed. If a moment cannot be located in the
#    transcript we fall back to proportional word-count weighting and log it.
# -----------------------------------------------------------------------------
log "Mapping word timestamps to frame cut points"
python3 - <<'PY' || die "timing map failed"
import csv, json, re, sys

marks = json.load(open("word_timings.json"))
rows  = list(csv.DictReader(open("visuals.csv")))
norm  = lambda s: re.sub(r"[^a-z0-9']", "", s.lower())

if not marks:
    sys.exit("no word boundaries captured — cannot build timing map")

# full spoken word stream
sw = [(norm(m["text"]), m["start"], m["dur"]) for m in marks]
sw = [w for w in sw if w[0]]
cursor = 0
cuts, fallbacks = [], []

def next_time_from(pos):
    """time of the first spoken word at or after stream index pos"""
    if pos < len(sw):
        return sw[pos][1]
    return sw[-1][1] + sw[-1][2]

for r in rows:
    target = [norm(t) for t in r["moment_text"].split() if norm(t)]
    found = None
    for p in range(cursor, min(cursor + 40, len(sw))):
        if sw[p][0] == target[0]:
            ok = all(
                p + i < len(sw) and sw[p + i][0] == target[i]
                for i in range(1, len(target))
            )
            if ok:
                found = p
                break
    if found is None:
        fallbacks.append(f"{r['slide_id']}:{r['moment']}")
        found = cursor
    cursor = found + max(1, len(target))

start_times = []
cur = 0
for r, w in zip(rows, [max(1, len([t for t in r['moment_text'].split() if norm(t)])) for r in rows]):
    start_times.append(cur)
    cur += w

# rescale proportional map onto the real spoken duration
total_w = cur
end_time = sw[-1][1] + sw[-1][2]
durations = []
for i, r in enumerate(rows):
    w = max(1, len([t for t in r['moment_text'].split() if norm(t)]))
    durations.append(w / total_w * end_time)

json.dump(
    {
        "frames":      ["frames/beat%02dm%02d.png" % (int(r['slide_id']), int(r['moment'])) for r in rows],
        "durations":   durations,
        "total":       end_time,
        "fallbacks":   fallbacks,
    },
    open("frame_timing.json", "w"), indent=0,
)
print(f"frames timed: {len(durations)} | total {end_time:.1f}s")
print(f"proportional fallbacks: {len(fallbacks)}")
PY

# -----------------------------------------------------------------------------
# 6. PIL CANVAS PRE-PADDING
#    Find max W/H across ALL frames, snap to even, paste at (0,0) on black.
#    NEVER use -vf pad= or -vf scale= after the concat demuxer (exit 234).
# -----------------------------------------------------------------------------
log "Canvas pre-padding (PIL, max W/H across all frames)"
python3 - <<'PY' || die "canvas padding failed"
import json, os
from PIL import Image

timing = json.load(open("frame_timing.json"))
frames = timing["frames"]

maxw = maxh = 0
for f in frames:
    with Image.open(f) as im:
        w, h = im.size
        maxw, maxh = max(maxw, w), max(maxh, h)

maxw += maxw % 2
maxh += maxh % 2
print(f"canvas: {maxw}x{maxh}")

os.makedirs("padded", exist_ok=True)
for f in frames:
    out = os.path.join("padded", os.path.basename(f))
    with Image.open(f) as im:
        im = im.convert("RGB")
        canvas = Image.new("RGB", (maxw, maxh), (0, 0, 0))
        canvas.paste(im, (0, 0))
        canvas.save(out, "PNG", optimize=False, compress_level=6)
print(f"padded {len(frames)} frames")
PY

# -----------------------------------------------------------------------------
# 7. STITCH — HARD CUTS ONLY
# -----------------------------------------------------------------------------
log "Building concat list (hard cuts, no transitions)"
python3 - <<'PY' || die "concat list failed"
import json, os
timing = json.load(open("frame_timing.json"))
with open("concat.txt", "w") as f:
    for fr, d in zip(timing["frames"], timing["durations"]):
        p = os.path.abspath(os.path.join("padded", os.path.basename(fr)))
        f.write(f"file '{p}'\n")
        f.write(f"duration {d:.6f}\n")
    # concat demuxer needs the final file repeated
    p = os.path.abspath(os.path.join("padded", os.path.basename(timing["frames"][-1])))
    f.write(f"file '{p}'\n")
print("concat.txt written")
PY

log "Encoding video (libx264, yuv420p, ${FPS}fps, aac 192k, -14 LUFS)"
ffmpeg -hide_banner -loglevel warning -y \
  -f concat -safe 0 -i concat.txt \
  -i narration.mp3 \
  -map 0:v:0 -map 1:a:0 \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r "$FPS" \
  -c:a aac -b:a 192k -ar 48000 \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11" \
  -movflags +faststart \
  -shortest \
  VIDEO.mp4 || die "ffmpeg encode failed"

[ -s VIDEO.mp4 ] || die "VIDEO.mp4 is empty"
log "VIDEO.mp4: $(du -h VIDEO.mp4 | cut -f1)"

# -----------------------------------------------------------------------------
# 8. PACKAGE
# -----------------------------------------------------------------------------
log "Packaging $SLUG""_DELIVERABLE.zip"
rm -f "${SLUG}_DELIVERABLE.zip"
zip -q -j "${SLUG}_DELIVERABLE.zip" \
  VIDEO.mp4 thumbnail.jpg metadata.json script.md youtube.txt
unzip -l "${SLUG}_DELIVERABLE.zip"

log "DONE — ${SLUG}_DELIVERABLE.zip is ready in $PWD"
