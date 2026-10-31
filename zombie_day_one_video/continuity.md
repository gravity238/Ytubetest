# Continuity Log — Day One: Locked In

## Style and character invariants (proposed)
- Master style: hand-drawn 2D storyboard; bold, slightly irregular black ink outlines; flat muted fills; warm cream apartment walls, slate-blue couch, brown floor, yellow blanket when visible.
- Protagonist: white circular head, simple black dot eyes and mouth, thin black stick-figure limbs; preserve the same scale and silhouette from shot to shot. The new generated character test adds a charcoal hoodie; confirm whether to keep it or revert to the bare stick figure in the supplied reference. Add a small backpack only after the escape decision.
- Mood: readable staging and expressive simple poses; tension through framing, shadows, smoke, and props rather than gore.
- Zombie/affected figures: distant, indistinct silhouettes with restrained unnatural posture; no visible injury or gore.
- Story-state rules: opening apartment door stays barricaded and closed until the protagonist exits through the kitchen window/fire escape. Power fails before smoke forces the escape. Backpack has only basic supplies. The ending is outside at the alley/street, not a return indoors.
- Hook: selected concept #2 — phone warning and pounding door, shown in the opening frame.
- Thumbnail: selected concept #3 — protagonist between the breached-door threat and window escape route, high-contrast “NO WAY OUT” idea.

## User-provided style refs
- `refs/user_room_style.png` — source attachment `Screenshot Capture - 2026-10-28 - 08-14-55.png`; primary supplied character + apartment reference.
- `refs/user_figure_style.png` — source attachment `Screenshot Capture - 2026-10-28 - 08-14-25.png`; supplementary loose hand-drawn figure reference.
- `refs/user_character_style.png` — source attachment `Screenshot Capture - 2026-10-28 - 08-14-40.png`; supplementary minimal stick-figure line-weight reference.

## Generated style-test refs (approved by user as anchor set)
1. `refs/style_test_character.png` — character design test. Exact prompt: “Create a clean character reference image for the same hand-drawn visual language as the supplied image references. Show one consistent protagonist, full body: oversized white circular head, tiny black dot eyes, small tense mouth, thin black stick-figure body and limbs, bold slightly irregular black ink outlines. Add a simple charcoal hoodie and small dark backpack, neutral standing pose on a warm off-white plain background. Preserve the simple flat cartoon drawing style, no text, no gore.” Images used: `user_character_style.png`, `user_room_style.png`.
2. `refs/style_test_apartment.png` — location test. Exact prompt: “Create an apartment location style test for a hand-drawn 2D survival animation matching the supplied references. Modest living room with slate-blue couch, coffee table, yellow blanket, warm cream walls, brown floor and a closed front door; one simple white-headed stick figure nearby for scale. Bold slightly imperfect black outlines, flat restrained colors, readable clean composition, 16:9 landscape, no text, no gore.” Images used: `user_room_style.png`, `user_character_style.png`.
3. `refs/style_test_escape.png` — action/location test. Exact prompt: “Create a location and action style test matching the supplied hand-drawn cartoon references: a simple white-headed stick-figure survivor with a small backpack climbing out an apartment window onto a metal fire escape at dusk. Bold slightly irregular black outlines, simple expressive figure, flat muted colors, cream apartment wall, slate shadows, clear landscape 16:9 composition. The apartment window is behind the figure; distant street below. Bloodless, no text.” Images used: `user_room_style.png`, `user_figure_style.png`.

## Other generated files
- `refs/random_retry.png` and `refs/random_retry_02.png` through `refs/random_retry_10.png` were generated as unrelated random test images at the user’s request. Do not use them as story anchors.
- Earlier generation attempts initially returned 403. A later retry succeeded; no account/device cause is known.

## Frame QC log
- Batch 1 accepted: `beat01m01`–`beat01m08`. Rejected first `beat01m03` attempt for strong background blur; changed only the focus clause to make the protagonist crisp, and accepted the reroll.
- Batch 2 accepted: `beat01m09`, `beat01m10`, `beat02m02`–`beat02m06`.
- Rejected first `beat01m10` attempt because it invented an “EVACUATION ORDER”; changed only the alert wording clause to request a generic banner with no legible words. Accepted the replacement.
- `beat02m01` first attempt contained gibberish UI. One repair requested abstract/unreadable UI, but still produced malformed symbols. Further reroll was blocked by the 10-image turn cap. Candidate is not accepted; see `frames/candidate_beat02m01_reroll02.png`. Repair next turn.
- Batch 2 contact sheet includes accepted images, rejected thumbnails, and the pending candidate.

## Moderation
- No moderation block encountered.

## Approval gate
- State 4 is pending user approval of the generated style refs and character clothing choice. Suggested anchors: apartment test for location, character test for protagonist, escape test for action/composition.
