# Continuity — ancient_night_video

**Locked:** 2026-11-20
**Anchor reference:** `refs/reference1.png` (supplied by user, 1376×752)

---

## 1. ARTSTYLE BLOCK — copy verbatim into every frame prompt

> Flat 2D cartoon illustration in the style of a modern hand-drawn YouTube explainer. Bold uniform ink outlines of even weight, slightly soft and rounded at the corners, never sketchy or tapered. Characters are simple stick figures with thin black line limbs and large round pure-white heads with no hair, no nose, no ears; faces carry only two bean-shaped black eyes with small white highlights plus a single thin curved mouth line placed at the lower centre of the face, and simple expressive eyebrows drawn as short thin strokes. Flat muted color fills with absolutely no gradients, no airbrush, no cell-shading, no texture maps. Limited palette of warm paper cream, dusty slate blue, muted mustard yellow, soft terracotta, sage green and charcoal ink. Warm single-source lamp or fire glow rendered as ONE single soft even flat ellipse of pale yellow with a feathered edge, with a simple soft elliptical drop shadow under every object; absolutely NO faceted segments, NO angular wedges, NO polygon or crystal shapes, NO rays, NO beams, NO sunburst, NO banding, NO geometric light shapes. Subtle paper grain and faint fiber texture across the whole image. Composition is calm, centered, spacious and clean with generous negative space. No photorealism, no 3D, no rendered lighting, no lens effects, no HUD, no UI.

## 2. CHARACTER BLOCK — copy verbatim into every frame prompt that contains a figure

> The figure is a stick figure: a large perfect circle head roughly one third of the figure's total height, drawn in pure white with a clean black outline, thin straight black line arms and legs with small round black dot hands and dot feet, NO torso shape, NO body mass, NO clothing texture — the thin black stick lines remain bare and visible everywhere. The face is drawn with two black bean-shaped eyes with tiny white glint highlights, thin arched black eyebrows, and a small simple flat mouth line. The figure's proportions stay identical across every frame. When more than one figure appears, all figures share this exact construction and differ only in pose. Any prehistoric figure may additionally carry an animal-hide wrap, and that wrap is ONLY a small flat irregular tan shape draped over ONE shoulder like a short cape, hanging no lower than the elbow; it never becomes a tunic, a dress, a shirt or a torso, and it never covers the bare stick limbs.

**Naming convention in prompts:**
- `THE FIGURE` — the modern second-person protagonist (present-day framing, cream room, sofa, lamp)
- `THE ANCESTOR` — the prehistoric protagonist (same construction, hide wrap)
- `THE ELDERS` / `THE CHILD` / `THE WATCHER` — group members, identical construction

---

## 3. WORLD BLOCKS

### 3a. NIGHT CAVE (used for ~70% of frames)

> Deep cave interior at night. Rear cave wall is a broad surface of dusty slate blue-grey and charcoal drawn in soft rounded rock forms with completely FLAT single-tone fills and only one flat darker slate tone used for shadow, no gradient or blending across the rock. Floor is flat packed earth in muted umber. A low campfire of flat two-tone mustard and terracotta flame shapes with crisp hard edges sits at the center, and its firelight on the cave wall is ONE single soft even flat ellipse of pale yellow with a feathered edge, with no faceted segments, no angular wedges and no geometric light shapes. Furs and hides are flat irregular tan and cream shapes on the floor. Absolute blackness beyond the firelight at the cave mouth. No stars, no moon, no gradient sky.

### 3b. MODERN ROOM (frame 1, frame 78–80 bookends)

> Modern apartment interior at 3am in flat explainer style. Cream-painted wall with faint vertical seam, dusty slate-blue sofa with simple rounded cushions and visible piping, a small wooden side table with a thin modern lamp and a mug, a large flat dark television panel mounted on the wall showing a grid of muted colored rectangles, a simple potted plant at frame edge, and one single soft even flat ellipse of warm pale yellow with a feathered edge radiating from the lamp, never faceted, never wedged, never a sunburst. Muted mustard throw blanket rumpled on the sofa.

### 3c. MODERN BEDROOM (frames 74–77)

> Modern bedroom at night in flat explainer style. Cream wall, a simple low bed with a flat slate-blue duvet and two cream pillows, a wooden nightstand with a small thin lamp switched off, a dark window rectangle at frame edge with flat black night beyond it, a soft device glow as a flat pale rectangle if a phone is present. Cold flat blue-grey ambient tone when dark, one soft even single ellipse of warm pale yellow when a light is on, never faceted and never wedged.

---

## 4. PALETTE (locked hex targets)

| Role | Hex | Use |
|---|---|---|
| Paper cream | `#F2E6C8` | Walls, backgrounds, paper base |
| Warm cream light | `#F7DFA8` | Lamp/fire radial wash |
| Mustard | `#E3B23C` | Flame, lamp shade, blanket, accents |
| Terracotta | `#C4714B` | Flame cores, earth, hide wraps |
| Dusty slate blue | `#7E9BB0` | Cave wall, sofa, duvet |
| Deep slate | `#3E4A54` | Cave shadows, night interiors |
| Sage green | `#8FAE87` | Plants, minor organic accents |
| Charcoal ink | `#22201E` | All line work |

## 5. LINE WEIGHT

Uniform ~4px at 1920×1080 for figure lines, ~6px for object contours, ~7px for cave wall and architecture. Rounded caps and joins. No hatching for shadow — all shadow is flat, single-tone.

---

## 6. MODERN / ANCIENT SEPARATION RULE

The video has three visual worlds and they **never mix within a frame**:

1. **Modern** (frames 1, 74–80): cream, lamp, sofa, bed, device glow.
2. **Cave night** (frames 2–73): fire, rock, hide, darkness.
3. **Abstract / diagram** (evidence beats): a flat cream void with simple ink diagram elements and no scenery at all, used sparingly for clock, brain, sleep-lab and timeline beats.

Anachronism is a hard fail. No clocks, no phones, no metal, no glass, no printed text inside cave frames.

---

## 7. SFX LETTERING RULES

Reserved for high-impact beats. Style: **bold hand-inked comic display lettering, charcoal ink with a flat mustard or terracotta fill, slight rotation, soft flat drop shadow, no glow, no gradient, no bevel.**

Approved SFX words (keep this list closed, log additions here):
- `FWOOSH` — fire catch/flare (frame 12)
- `CRACK` — fire and bone (frame 13)
- `SNAP` — twig/grunt punctuation
- `TICK` — dripping water, nail in wood
- `HUSH` — the settling to first sleep (frame 18)
- `SIGH` — the exhale into first sleep

SFX lettering is **not** a text defect for QC purposes.

---

## 8. CONTENT MODERATION LOG

Checked `script.md` and `visuals.csv` against image-model filters, 2026-11-20.

| Term in script | Risk | Handling |
|---|---|---|
| "had sex" (frame ~30 area) | Medium — blocked/softened by some image models if depicted | Narration may say it plainly; **no frame depicts it**. That beat is drawn as two figures sharing a hide, faces only, or as an abstract diagram. |
| "died" / "death" | Low | Not depicted literally; fire and ember imagery only. |
| "child" | Low | Drawn, non-sexualised, normal proportions. |
| "corpse" | Medium | **Avoided** — not used in script or prompts. |
| "your ancestors" | None | Safe. |
| "hide", "furs", "skins" | Low | Drawn as clean flat tan shapes, no gore, no blood. |
| "butchering" | Medium | **Avoided** — replaced with "cutting meat." |
| Blood / injury | Medium | **Avoided entirely.** No injuries depicted in this video. |

**No blocked words required replacement.** Two narration lines were written around the "mating" beat to keep frames depictable (see rows 30–32).

---

## 9. QC DEFECT FLOOR

A frame passes if:
1. Its `moment_text` is legible from the image alone.
2. Figure construction matches the CHARACTER BLOCK (round white head, dot hands, thin limbs).
3. Palette is within the locked six-color family, flat fills only.
4. No gradient, no photorealism, no 3D, no text other than approved SFX lettering.
5. Environment matches the assigned world block for that row.
6. No anachronism in cave frames.

**Reject reasons:** human-looking rendered face, hair, torso mass, gradient shading, photographic texture, busy/cluttered composition, wrong world, anachronism.

---

## 10. ANCHOR LOG

| # | File | Role | Prompt summary | Verdict |
|---|---|---|---|---|
| A0 | `refs/reference1.png` | **MASTER ANCHOR** (user-supplied) | Modern room, sofa, figure with phone, lamp, TV panel | **APPROVED — canonical style source** |
| T1 | `refs/style_test_cave.png` | First cave-world test | fire + ancestor + cave wall | **REJECTED** — hide wrap became a full tunic with torso; firelight rendered as hard faceted wedges |
| T1v2 | `refs/style_test_cave_v2.png` | Tunic fix | cape-only hide | **REJECTED** — tunic fixed, but firelight still faceted into crystal wedges |
| **T1v3** | **`refs/style_test_cave_v3.png`** | **CANONICAL CAVE ANCHOR** | soft even glow, bare stick limbs, cape-only hide | **APPROVED** |
| **T2** | **`refs/style_test_night.png`** | **CANONICAL DARKNESS ANCHOR** | near-black, dying embers, no figure | **APPROVED** — first roll |
| **T3** | **`refs/style_test_abstract.png`** | **CANONICAL DIAGRAM ANCHOR** | flat cream void, ink bar diagram | **APPROVED** — first roll |

### Defects found and permanently fixed in the canonical blocks

| # | Defect | Frames affected | Fix applied to `continuity.md` |
|---|---|---|---|
| D1 | Animal-hide wrap inflated into a **full tunic with a torso**, destroying the bare stick-figure silhouette | every `[THE_ANCESTOR]` / `[THE_ANCESTORS_GROUP]` frame (~90 rows) | CHARACTER BLOCK now forbids tunic/dress/shirt/torso and restricts the hide to a shoulder cape hanging no lower than the elbow |
| D2 | Firelight rendered as **hard faceted wedges / crystal polygons** instead of a soft wash | every firelit frame (~180 rows) | ARTSTYLE BLOCK + NIGHT CAVE block now mandate ONE soft even flat ellipse with a feathered edge and explicitly ban faceted segments, wedges, polygons, rays, beams, sunburst and banding |
| D3 | Mouth drawn too high, close to the eyes | every figural frame | ARTSTYLE BLOCK now specifies the mouth line at the lower centre of the face |

Style tests are generated once and **not committed as frames** — they are the visual contract for the swarm.

---

## 11. SCRIPTURE OF THE NIGHT (canonical scene order)

1. Modern 3am wake-up *(modern room)*
2. Direct address: this has happened to you before *(modern room)*
3. You are not broken *(modern bedroom)*
4. The lie: eight hours *(abstract diagram)*
5. Drop: the dark before light *(cave)*
6. Fire is the whole game *(cave)*
7. Who feeds it *(cave)*
8. The obligation *(cave)*
9. Full dark, and what's out there *(cave mouth)*
10. Settling into furs *(cave)*
11. First sleep *(cave)*
12. You come up out of it *(cave)*
13. **The watch** *(cave, named)*
14. What they did in the watch *(cave, sequence)*
15. The record: Ekirch *(abstract)*
16. The second sleep *(cave)*
17. Dawn *(cave mouth)*
18. The kill: gaslight, electricity *(abstract → modern)*
19. Wehr's lab *(abstract diagram)*
20. The small societies do not do this *(abstract map/diagram)*
21. Boyce's critique *(abstract)*
22. Return to you at 3am *(modern bedroom)*
23. The closing line *(modern room)*
