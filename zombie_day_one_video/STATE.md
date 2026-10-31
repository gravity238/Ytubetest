# Production State

Current state: 5 — frame generation loop.

- User approved the proposed anchor set. Use the generated charcoal hoodie consistently; add the small backpack only after the escape decision.
- Batch 1: 8 accepted frames (`beat01m01.png`–`beat01m08.png`); 217 visual beats remain.
- Rejected: `beat01m03` first attempt was blurred; changed only “keep the protagonist blurred in the background” to “keep the protagonist in crisp focus in the background.” Accepted repair is sharp and readable.
- Contact sheet: `frames/contact_sheet_batch01.png` includes all 8 accepted frames and the rejected first attempt.
- New anchors: none. Thumbnail: not started.
- Next coverage: `slide_01m09`–`slide_01m10`, then `slide_02m01`–`slide_02m06`.
- Per-turn image cap reached (8-frame batch + 2 repair/QC generations).

- State 2 script approved by user.
- State 3 complete: 225 visual beats; selected opening hook #2 and thumbnail concept #3 (interpreted from “23”).
- Batch sizing: 7 frames per turn (floor(10 × 0.75)); 33 projected batches for 225 frames.
- Three generated style-test refs are in `refs/`: character, apartment, and escape. See exact prompts and source image paths in `continuity.md`.
- Ten unrelated random test images are also present; do not use them as story anchors.
- No sequence frame generation has begun.
