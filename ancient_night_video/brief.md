# Brief — ancient_night_video

## Logline

You wake at 3am and think something is wrong with you. It isn't. For most of human history the middle of the night was not a malfunction — it was a scheduled, named, socially used hour. This video drops you into a cave at full dark and walks you through the night the way your ancestors actually lived it: the fire shift, the first sleep, the waking hour they called "the watch," the second sleep, and the light bulb that deleted all of it.

## Locked decisions

| Field | Value |
|---|---|
| Topic | What Did Ancient Humans Do in the Middle of the Night? |
| Target runtime | 10 minutes (~1,860 words @ ~3.1 wps) |
| Voice | `en-US-AndrewNeural` @ `--rate=+10%` (Edge-TTS) |
| POV | Second person ("you lie down on the hide…") |
| Style | Ink Explainer: round-headed stick figure, thick soft ink contour, flat muted fills, warm lamp/ember glow, paper grain |
| Aspect | 16:9 |
| Captions | None |
| Platform | YouTube long-form (~10:26 channel average) |

## Hard rules — MUST appear

1. The terms **"first sleep"** and **"second sleep"** spoken as named historical concepts.
2. The **"watch"** (also "the watching") named as the interval between them.
3. **A. Roger Ekirch** credited by name, with *Sleep We Have Lost* (2001) and/or *At Day's Close* (2005).
4. **Thomas Wehr / NIMH** — the 1990s long-darkness experiment producing biphasic sleep.
5. Ekirch's reference count (500+ sources, back to Homer).
6. The honest complication: Niall Boyce's re-examination of the evidence, and the fact that modern small-scale societies (Hadza, San, Tsimané) do **not** sleep in two shifts.
7. The fire: who fuels it, who is awake, what that obligates.
8. The closing turn: the 3am wake-up is not a defect.

## Hard rules — MUST NEVER appear

1. ❌ The Beautyrest / 1938 "invented eight hours of sleep" claim — **unsupported, do not use**.
2. ❌ "Before the Industrial Revolution everyone slept in two shifts, everywhere, always" — overstatement. Segmented sleep is documented in *pre-industrial Europe and early America*, not universally.
3. ❌ Any claim that science has "proven" ancestral sleep was healthier.
4. ❌ Specific modern medical advice ("you should try segmented sleep").
5. ❌ Naming a single "caveman" hominin species as *the* ancestor — use "early humans," and reserve Neanderthal/Homo sapiens specifics for where the evidence supports them.
6. ❌ On-screen text in frames other than intentional comic-book visual SFX lettering.
7. ❌ Modern objects (phones, clocks, light bulbs) inside the prehistoric scenes — the modern frame is a separate, clearly-drawn world.

## Accuracy posture

Everything is presented as *evidence and interpretation*, with the scholarly disagreement surfaced rather than smoothed over. Where a claim is contested, the narration says so out loud. This is the channel's stated differentiator (citations in descriptions) and it is also the thing that makes the video survive a comment section.

## Deliverable

`VIDEO.mp4` + `thumbnail.jpg` + `metadata.json` + `script.md` + `youtube.txt` packaged as `ancient_night_DELIVERABLE.zip`, built on Kaggle by `run_ancient_night_kaggle.sh`.
