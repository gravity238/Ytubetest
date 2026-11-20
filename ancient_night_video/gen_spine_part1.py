#!/usr/bin/env python3
"""Generate visuals.csv for ancient_night_video — PART 1 (slides 01-12).

Row schema (spec-mandated, 4 columns):
    slide_id, moment, moment_text, visual_prompt

visual_prompt holds ONLY the dynamic direction, tagged with its world and figure.
Full generation prompts are assembled by build_prompts.py, which imports the
verbatim ARTSTYLE / CHARACTER / WORLD blocks from continuity.md so those blocks
are never retyped by hand and can never drift.
"""
import csv, os

HEADER = ["slide_id", "moment", "moment_text", "visual_prompt"]

R = []


def row(slide, moment, text, prompt):
    R.append([f"{slide:02d}", f"{moment:02d}", text, prompt])


# ---------------------------------------------------------------- S01 MODERN 3AM
row(1, 1, "It's three in the morning,", "[MODERN_ROOM][NO_FIG] Extreme close-up on a wall clock face rendered as flat ink circles on cream, hands frozen at three, the numeral-less dial slightly cropped by frame edge, cold blue-grey wash bleeding in from the left.")
row(1, 2, "and you are awake.", "[MODERN_ROOM][THE_FIGURE] Wide low-angle shot from floor level, the figure slumped upright on the slate-blue sofa, head tilted back, two bean eyes fully open and staring at nothing, ceiling filling the upper third of frame.")
row(1, 3, "You're on the sofa.", "[MODERN_ROOM][NO_FIG] High-angle overhead shot looking down at the whole sofa, cushions compressed, mustard throw bunched at one end, empty mug on the side table, long soft elliptical shadow pooling beneath.")
row(1, 4, "The lamp is on.", "[MODERN_ROOM][NO_FIG] Tight detail shot of the thin table lamp, flat mustard shade glowing, a soft pale radial wash falling across the cream wall behind it, the mug's handle just entering frame at bottom.")
row(1, 5, "The television is doing that thing where it's technically off", "[MODERN_ROOM][NO_FIG] Straight-on medium shot of the wall-mounted television panel, the grid of muted colour rectangles rendered dim and desaturated, thin charcoal bezel, nothing reflected in the dark screen.")
row(1, 6, "but it's still glowing,", "[MODERN_ROOM][NO_FIG] Extreme close-up of one corner of the television panel, a faint flat pale rectangle of residual glow bleeding onto the cream wall, hard crop so the screen reads as an abstract shape.")
row(1, 7, "and your phone is up at that angle you always hold it,", "[MODERN_ROOM][THE_FIGURE] Over-the-shoulder shot from behind the figure's round head, the thin stick arm raised at a slight angle, small dark phone rectangle at the top of frame, sofa backrest filling the foreground.")
row(1, 8, "and your face is doing what your face does at three in the morning.", "[MODERN_ROOM][THE_FIGURE] Frontal close-up, the round white head centred and large, bean eyes half-lidded and flat, one thin eyebrow raised a hair, mouth a short level line, no other feature on the face at all.")
row(1, 9, "Nothing.", "[MODERN_ROOM][NO_FIG] Extreme close-up on the blank cream wall beside the sofa, absolutely empty except for paper grain and faint fiber texture, a single soft shadow edge at the frame's left.")
row(1, 10, "Just a soft blue wash.", "[MODERN_ROOM][THE_FIGURE] Wide side-on silhouette-ish shot, the figure and sofa reduced to charcoal outlines, a flat pale blue-grey rectangle of phone light falling across the lower half of the round head.")
row(1, 11, "And you're thinking the thing everyone thinks in this chair.", "[MODERN_ROOM][THE_FIGURE] Medium shot dead centre, figure seated upright with phone lowered to the knee, head turned slightly toward camera, both eyebrows drawn level and inward in a flat tired question.")
row(1, 12, "Why can't I sleep?", "[ABSTRACT][NO_FIG] Flat cream void with a single hand-inked question mark rendered in bold charcoal line, slightly rotated and off-centre, one small ink droplet at its base — no scenery, no figure, pure graphic beat.")

# ------------------------------------------------------- S02 THIS HAS HAPPENED
row(2, 1, "This has happened before.", "[MODERN_ROOM][THE_FIGURE] Wide static shot, the same sofa and lamp but the figure now smaller in frame at the far right, generous empty cream wall dominating, emphasising the ordinariness of the moment.")
row(2, 2, "Repeatedly, across years,", "[ABSTRACT][NO_FIG] Flat cream void showing a simple hand-inked horizontal timeline, twelve small ink tick marks evenly spaced along it, one tick near the end circled in terracotta.")
row(2, 3, "at intervals you've never been able to predict.", "[ABSTRACT][NO_FIG] Flat cream void, the same ink timeline redrawn with the tick marks scattered at irregular unpredictable spacing, three of them circled in charcoal with small question dashes above.")
row(2, 4, "And you've probably decided what it means.", "[MODERN_ROOM][THE_FIGURE] Low-angle close-up from knee height looking up at the figure's round head, chin slightly down, eyes angled to the side, mouth a flat line — the posture of someone reaching a private verdict.")
row(2, 5, "Your phone.", "[ABSTRACT][NO_FIG] Flat cream void, a single simple ink rectangle representing a phone floating centred with three short stubby antenna dashes radiating above it, bold charcoal outline only.")
row(2, 6, "Your cortisol.", "[ABSTRACT][NO_FIG] Flat cream void, one simple ink droplet-and-wave glyph suggesting a hormone signal, terracotta filled, with three small upward arrow ticks beside it, no labels.")
row(2, 7, "Your screen time.", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink bar chart of five flat blocks stepping upward in mustard and slate, hand-drawn uneven edges, no numbers, no axes.")
row(2, 8, "You've decided you're a bad sleeper,", "[MODERN_ROOM][THE_FIGURE] Medium shot, figure standing now beside the sofa, shoulders dropped, one thin arm hanging, head bowed forward so the round head sits low against the cream wall.")
row(2, 9, "the way some people are bad at maths,", "[ABSTRACT][NO_FIG] Flat cream void, a scrawled ink multiplication glyph with a crooked equals sign struck through by a single terracotta diagonal stroke, ink slightly dry and broken.")
row(2, 10, "and this is your particular defect to carry around.", "[CAVE][THE_ANCESTOR] Surreal but flat: the ancestor stands in near-darkness carrying a small ink-black cube under one thin arm, the cube rendered as a simple solid charcoal block, ember glow catching only the outline.")
row(2, 11, "But for almost the entire history of the species,", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink spiral of concentric arcs suggesting deep time, charcoal line only, the spiral's centre a single mustard dot.")
row(2, 12, "this was not a defect.", "[ABSTRACT][NO_FIG] Flat cream void, a bold hand-inked charcoal X placed decisively beside the wordless ink outline of a broken cog, the X drawn with visible pen pressure.")
row(2, 13, "It was a schedule.", "[ABSTRACT][NO_FIG] Flat cream void, a clean simple ink grid calendar of small squares, three squares filled mustard in a deliberate repeating pattern down one column, charcoal outline throughout.")

# --------------------------------------------------------- S03 NOT BROKEN
row(3, 1, "You are not broken.", "[MODERN_ROOM][THE_FIGURE] Heroic low-angle wide shot, the figure standing centred in the cream room at full height, thin limbs straight, head up, bean eyes level and calm — the most upright, confident posture in the modern section.")
row(3, 2, "That hour you spent watching the ceiling do nothing", "[MODERN_ROOM][THE_FIGURE] Extreme high-angle shot looking straight down onto the sofa, the figure sprawled with face turned up toward camera, two blank bean eyes aimed directly at the lens.")
row(3, 3, "has a name.", "[ABSTRACT][NO_FIG] Flat cream void, a small ink nameplate shape drawn as a simple rounded rectangle, empty inside, suspended by two thin ink lines from the top of frame — a label waiting to be filled.")
row(3, 4, "It is two thousand years old.", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink hourglass on its side pointing left, two thousand rendered only as a stack of twenty small ink ticks, terracotta accent on the final tick.")
row(3, 5, "People said it out loud", "[CAVE][THE_ANCESTOR] Medium shot of two ancestors seated opposite each other across the fire, both round heads in profile, mouths drawn as small open curves, the fire between them glowing flat mustard.")
row(3, 6, "and everyone in the room knew exactly what they meant.", "[CAVE][THE_ANCESTORS_GROUP] Wide shot across the cave floor, five figures in varying poses all turning their round heads toward one seated figure, firelight washing the rear slate wall, bodies reduced to clean silhouettes.")
row(3, 7, "But something is standing in the way.", "[ABSTRACT][NO_FIG] Flat cream void, a single tall ink-black rectangle standing upright dead centre, edges crisp and hand-drawn, a long soft shadow cast to the right.")
row(3, 8, "There's a lie in the road, and we have to break it first.", "[ABSTRACT][NO_FIG] Wide flat cream void, a simple ink road drawn as two converging charcoal lines running to a vanishing point, blocked three-quarters of the way along by a solid mustard wall.")

# ------------------------------------------------------- S04 THE LIE IS 8 HOURS
row(4, 1, "The lie is eight hours.", "[ABSTRACT][NO_FIG] Flat cream void, one thick hand-inked horizontal bar broken into eight equal segments by seven tick marks, rendered bold charcoal with a terracotta underline, no numbers.")
row(4, 2, "You've been told your whole life", "[MODERN_BED][THE_FIGURE] Wide shot of the modern bedroom, figure small and horizontal under the slate-blue duvet, cream pillows behind the round head, the dark window rectangle at frame edge.")
row(4, 3, "that a normal night is one unbroken block —", "[ABSTRACT][NO_FIG] Flat cream void, a single solid charcoal rectangle with perfectly square ends, floating with generous space around it, its uniformity slightly oppressive.")
row(4, 4, "seven, eight, nine, straight through.", "[ABSTRACT][NO_FIG] Flat cream void, three charcoal bars of increasing length stacked and left-aligned, all rendered flat and identical in width, each ending in a crisp square edge.")
row(4, 5, "One block, no interruptions.", "[ABSTRACT][NO_FIG] Flat cream void, the single charcoal bar now enclosed in a thin ink border with four small corner brackets, guarded and sealed, one soft shadow beneath.")
row(4, 6, "That's the target.", "[ABSTRACT][NO_FIG] Flat cream void, the sealed bar set dead centre with three concentric thin ink rings radiating from it, rendered like a target, the innermost ring mustard.")
row(4, 7, "That number is not ancient.", "[ABSTRACT][NO_FIG] Flat cream void, an ink chisel and a small clay tablet fragment drawn flat at the frame's left, both rendered small and lightly, with a large empty area where something ought to be.")
row(4, 8, "It is not biological.", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink outline of a heart and a lung pair rendered as two flat charcoal shapes, both stamped through with a single diagonal broken line.")
row(4, 9, "It is roughly two hundred years old.", "[ABSTRACT][NO_FIG] Flat cream void, a tight cluster of two hundred tiny ink tick marks packed into the lower right quadrant, the rest of the frame completely empty cream.")
row(4, 10, "To understand how a species lost half its night,", "[ABSTRACT][NO_FIG] Flat cream void, a large ink circle divided by a horizontal charcoal band, the lower half solid black and the upper half bare cream — a night cut in two.")
row(4, 11, "you have to go somewhere with no lamps.", "[CAVE_MOUTH][THE_FIGURE] Wide shot from inside blackness looking out, the cave mouth a ragged ink-edged opening of pale night beyond, the figure's back rendered as a small silhouette at the lower right, no fire visible.")

# --------------------------------------------------------------- S05 THE DARK
row(5, 1, "You're in a cave,", "[CAVE][NO_FIG] Extremely wide establishing shot, the cave interior rendered in near-total flat charcoal, only the faintest slate-blue shape of the rear wall visible, no fire lit yet, enormous negative dark space.")
row(5, 2, "and it is genuinely, absolutely dark.", "[CAVE][NO_FIG] Full-frame flat near-black with only paper grain and fiber texture visible, one barely perceptible slate edge at the top left, nothing else in frame.")
row(5, 3, "Not dark like a bedroom with the curtains shut.", "[MODERN_BED][NO_FIG] Very wide shot of the modern bedroom at night, curtains drawn but a thin flat pale line of light leaking around their edges, the bed a soft slate mass, everything still legible.")
row(5, 4, "Dark like the inside of your own skull.", "[ABSTRACT][NO_FIG] Flat cream void containing one large solid charcoal oval, the interior utterly flat black, a few thin ink fibres fanning from its edge like bone seams.")
row(5, 5, "Your eyes have given up trying.", "[CAVE][THE_FIGURE] Extreme close-up on just the two bean-shaped eyes floating in near-blackness, both rendered flat white with tiny highlights, the surrounding cave reduced to a single slate edge.")
row(5, 6, "There's nothing to see.", "[CAVE][NO_FIG] Flat charcoal frame broken only by the faintest rounded rock forms at the top edge, no fire, no figure, no detail — pure darkness with texture.")
row(5, 7, "The dark isn't an absence of light —", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink outline of a container jar with its lid off, interior filled solid charcoal, a small ink arrow pointing inward toward the fill.")
row(5, 8, "it's a substance, pressing on your face.", "[CAVE][THE_FIGURE] Tight frontal close-up, the round white head rendered dim and slate-tinted, two flat charcoal shapes pressing inward on either side of the face from the frame edges like soft walls.")
row(5, 9, "Then, thirty feet away,", "[CAVE][NO_FIG] Wide dark shot from a low angle at floor level, the floor a flat charcoal plane receding into blackness, a single small distance marker rendered as a thin ink measure line at the left.")
row(5, 10, "where you know the fire is,", "[CAVE][NO_FIG] Extreme wide shot, frame almost entirely black, one tiny warm mustard glow low and centred, its soft radial falloff barely reaching a yard.")
row(5, 11, "a small orange shape moves.", "[CAVE][NO_FIG] Extreme close-up on the fire's heart, one flat terracotta and mustard flame shape caught mid-lean, completely surrounded by black, no cave detail visible at all.")

# ------------------------------------------------------------ S06 FIRE IS GAME
row(6, 1, "Fire is the entire game.", "[CAVE][THE_ANCESTOR] Dramatic low-angle heroic shot from floor level, the ancestor standing feet planted wide beside the fire, flames rendered as bold flat mustard shapes, the firelight wash climbing the slate wall behind them.")
row(6, 2, "Every animal in the world has to survive the night,", "[CAVE_MOUTH][NO_FIG] Wide shot looking out of the cave mouth at flat blackness, three simple ink animal silhouettes standing at the very edge of the firelight's reach, all facing inward.")
row(6, 3, "and almost all of them do it by hiding and waiting.", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink curve showing a sun arcing down and back up, with a small charcoal huddle shape tucked beneath the lowest point of the curve.")
row(6, 4, "Fire is the one thing that lets a soft, slow, entirely edible primate", "[CAVE][THE_ANCESTOR] Medium shot of the ancestor seated calmly with legs folded, round head tilted, one thin arm resting, the fire bold and central — soft, unhurried, entirely at ease in the open.")
row(6, 5, "stop hiding.", "[CAVE][THE_ANCESTOR] Wide shot, the ancestor standing upright at the centre of a pool of firelight with arms slightly out, the cave walls sweeping away into black on both sides, nothing concealed.")
row(6, 6, "But fire isn't a thing you have.", "[CAVE][NO_FIG] Tight object shot of a single flat mustard flame shape held at arm's length distance, its lower edge unanchored and floating slightly above the flat umber floor, no fuel beneath it.")
row(6, 7, "It's a thing you do.", "[CAVE][THE_ANCESTOR] Close-up on two thin stick hands with round dot palms cupped around kindling, a small flat flame just beginning between them, ember glow on the wrists.")
row(6, 8, "It has to be fed —", "[CAVE][THE_ANCESTOR] Extreme close-up, one thin arm extending into frame to place a flat tan log shape onto the flames, fire leaping up around the point of contact.")
row(6, 9, "constantly, all night.", "[CAVE][NO_FIG] Wide static shot of the cave at night, fire small and central, three flat tan log shapes stacked beside it, blackness pressing in from all four frame edges.")
row(6, 10, "If nobody feeds it, it dies,", "[CAVE][NO_FIG] Close-up of the fire reduced to three flat charcoal lumps with a single dying mustard fleck, the radial glow contracted to almost nothing, floor going cold and grey.")
row(6, 11, "the dark comes all the way in,", "[CAVE][NO_FIG] Wide shot, the entire frame flooded with flat charcoal darkness except one narrow wedge of pale light entering from behind the camera's position, the cave wall vanishing.")
row(6, 12, "and whatever was standing at the edge of the light gets to come closer.", "[CAVE_MOUTH][NO_FIG] Low wide shot of the cave mouth, a simple ink animal silhouette now standing well inside the threshold, flat and featureless, eye-level with the lens, nothing but black behind it.")

# --------------------------------------------------------- S07 SOMEBODY SITS UP
row(7, 1, "So somebody sits up.", "[CAVE][THE_ANCESTOR] Wide shot from across the cave, the ancestor's silhouette rising from a low hide bed, one thin arm braced on the floor, the fire behind them throwing a long flat shadow toward camera.")
row(7, 2, "Thin arms, round head,", "[CAVE][THE_ANCESTOR] Isolated character study, the ancestor's full figure centred on a plain flat slate background, thin ink limbs and large round white head rendered with complete clarity, no fire, no scenery.")
row(7, 3, "a tan hide over one shoulder,", "[CAVE][THE_ANCESTOR] Close-up on the shoulder, a flat irregular tan shape draped diagonally across one thin ink line, the hide's edge a soft uneven curve, one charcoal fold line.")
row(7, 4, "cross-legged on packed earth,", "[CAVE][THE_ANCESTOR] High-angle shot looking down at the ancestor seated cross-legged, thin legs folded into flat ink angles, the umber floor filling most of the frame.")
row(7, 5, "feeding a fire that has to stay alive until dawn.", "[CAVE][THE_ANCESTOR] Wide side-on shot, ancestor seated in profile facing right toward the fire, one arm extended with fuel, the cave wall behind running in a long flat sweep.")
row(7, 6, "They're not being noble.", "[CAVE][THE_ANCESTOR] Frontal medium close-up, the round head neutral, eyes flat and half-lidded, eyebrows level, mouth a straight line — total absence of expression or heroism.")
row(7, 7, "It's their shift.", "[CAVE][THE_ANCESTOR] Symmetrical wide shot dead centre, the seated ancestor framed against the flat slate wall exactly between two ink tick marks scratched on either side of them like a workstation.")

# ------------------------------------------------------------ S08 THE OBLIGATION
row(8, 1, "Sitting up obligates you.", "[CAVE][THE_ANCESTOR] Medium shot, the seated ancestor's thin arm extends toward the fire while a second figure sleeps behind them, rendered flat in the background, the arm's line emphasised.")
row(8, 2, "Sit with the fire while everyone sleeps,", "[CAVE][THE_ANCESTORS_GROUP] Wide shot, four figures lying flat in hides across the umber floor, one figure upright and small at frame edge, the fire the only bright shape.")
row(8, 3, "and tomorrow, when there's meat,", "[CAVE][THE_ANCESTORS_GROUP] Overhead flat-lay shot of the cave floor, a simple irregular terracotta meat shape laid on a flat stone at centre, four round heads gathered around its edge, no gore.")
row(8, 4, "somebody hands you meat.", "[CAVE][THE_ANCESTOR] Close-up from the side, two thin stick arms meeting at the centre of frame, one passing a small flat terracotta shape into the other's round dot hand.")
row(8, 5, "Keep watch through the dark,", "[CAVE][NO_FIG] Wide night shot, absolutely still, the fire low, three sleeping forms and one upright silhouette at the far end of the cave facing the darkness.")
row(8, 6, "and when you're the one who's sick,", "[CAVE][THE_ANCESTOR] High-angle medium shot, the ancestor curled on their side on a hide, thin limbs drawn in toward the body, round head low, no injury or blood shown.")
row(8, 7, "someone keeps the fire alive for you.", "[CAVE][THE_ANCESTORS_GROUP] Reverse shot from behind the sick figure's head, a second figure seated upright feeding the fire in the middle distance, flames bold and warm.")
row(8, 8, "It's a debt system", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink balance scale rendered flat and two-dimensional, one pan holding small charcoal squares, the other holding small mustard circles.")
row(8, 9, "built out of the worst hours of the night.", "[ABSTRACT][NO_FIG] Flat cream void, a vertical column of twelve small ink squares stacked like a tower, the bottom four filled solid charcoal and the remaining eight left as bare outlines.")
row(8, 10, "Every single night, you are being measured", "[CAVE][THE_ANCESTOR] Tight shot of two flat ink hands holding a simple charcoal measuring rod across the firelight, the rod's tick marks rendered as small strokes.")
row(8, 11, "against your willingness to sit in the dark", "[CAVE][THE_ANCESTOR] Wide low shot, the ancestor's silhouette seated alone at the boundary of the fire's light, half of the figure in flat charcoal shadow, facing outward.")
row(8, 12, "so someone else can close their eyes.", "[CAVE][THE_ANCESTOR] Extreme close-up on a sleeping figure's face, two bean eyes rendered as simple closed downward curves, a flat tan hide rising to meet the chin.")

# ------------------------------------------------------------ S09 THE COALS
row(9, 1, "The fire burns down to a bed of coals.", "[CAVE][NO_FIG] High-angle close shot looking down into the fire pit, a flat oval of charcoal lumps with a scattered few terracotta embers, the radial glow gone, only a dim pool around the pit.")
row(9, 2, "It's barely a colour now.", "[CAVE][NO_FIG] Extreme close-up on two single ember shapes, one dull terracotta, one almost grey, the surrounding floor completely flat and unlit.")
row(9, 3, "And because the light has pulled back,", "[CAVE][NO_FIG] Wide shot, the pale firelight wash contracted into a tight central circle on the slate wall, the outer frame cold and nearly black, the circle's edge soft.")
row(9, 4, "you can see the mouth of the cave —", "[CAVE_MOUTH][THE_FIGURE] Wide shot from deep inside, the cave mouth opening visible as a ragged pale-edged gap in the far wall, the figure small and facing it.")
row(9, 5, "a rectangle of almost-black,", "[CAVE_MOUTH][NO_FIG] Straight-on medium shot of the cave mouth, framed as an irregular ink-edged rectangle barely lighter than the flat charcoal wall around it.")
row(9, 6, "barely lighter than the wall.", "[CAVE_MOUTH][NO_FIG] Tight side-by-side detail, the cave mouth's pale edge on the left meeting the flat slate wall on the right, only a few degrees of tonal difference between them.")
row(9, 7, "Beyond it, the world is doing whatever it does when nobody is watching.", "[CAVE_MOUTH][NO_FIG] Wide shot looking out through the mouth at flat black nothing, three simple ink grass-blade shapes at the sill, absolutely no detail beyond.")
row(9, 8, "Wind through grass.", "[CAVE_MOUTH][NO_FIG] Close-up on four flat ink grass blades bent hard to one side, drawn as simple curved strokes with no shading, blackness behind them.")
row(9, 9, "Something standing very still out there, listening.", "[CAVE_MOUTH][NO_FIG] Wide low shot, a single simple ink quadruped silhouette standing motionless at the boundary of the pale strip, its head turned flat toward the cave.")
row(9, 10, "You are inside a ring of light the size of a small room.", "[CAVE][THE_FIGURE] Extreme high-angle overhead shot looking straight down at the whole cave floor, the pale light pool rendered as a perfect flat circle, the figure standing inside it and the blackness absolute outside it.")
row(9, 11, "Everything outside it wants what you're made of.", "[CAVE][NO_FIG] Wide shot from outside the light ring looking in, the light circle a flat pale disc in a black field, four small ink silhouettes arranged evenly at its rim, all facing inward.")

# ------------------------------------------------------------- S10 LIE DOWN
row(10, 1, "So you lie down.", "[CAVE][THE_ANCESTOR] Wide shot, the ancestor lowering themselves onto a hide bed, thin arms bracing, round head tilting back, the fire's diminished glow behind them.")
row(10, 2, "The furs are warm, which is the point,", "[CAVE][NO_FIG] Extreme close-up on the texture of a hide rendered as a flat tan shape with two soft charcoal fold lines, no fibre detail, warmth implied only by the soft mustard tint.")
row(10, 3, "and they smell like horse and smoke.", "[CAVE][NO_FIG] Low shot across the cave floor, a flat tan hide draped over a rounded form, the fire's smoke rising as two simple flat charcoal curls against the slate wall.")
row(10, 4, "The rock under you is not flat —", "[CAVE][NO_FIG] Close-up on the umber floor rendered with two uneven flat rock plates, one tilted slightly, a visible seam between them running diagonally through frame.")
row(10, 5, "your hip finds a stone no matter which way you lie.", "[CAVE][THE_ANCESTOR] High-angle overhead close shot of the ancestor lying flat, one small charcoal stone rendered exactly beneath the hip line, the body's flat ink silhouette bending around it.")
row(10, 6, "You can hear the fire.", "[CAVE][NO_FIG] Tight shot of the fire pit from ground level, low flames and a single mustard spark shape lifting, the sound implied by three small flat ink motion dashes.")
row(10, 7, "You can hear the person on watch shift their weight.", "[CAVE][THE_ANCESTOR] Wide shot, the watcher's silhouette rendered mid-shift at frame edge, one thin arm repositioned, a long flat shadow sliding across the umber floor.")
row(10, 8, "Behind you, someone's breathing has already settled.", "[CAVE][THE_ANCESTOR] Extreme close-up on a sleeping face at frame edge, two closed curved eyes, the mouth a soft small oval, a flat tan hide rising and falling across the shoulder line.")
row(10, 9, "You close your eyes.", "[CAVE][THE_FIGURE] Frontal close-up, the round white head filling the frame, two bean eyes drawn as simple closed downward curves, thin brows relaxed, mouth a level line.")
row(10, 10, "Not because you're done.", "[CAVE][THE_FIGURE] Medium shot, the figure lying flat with eyes closed but the arrangement stiff and deliberate, arms straight at the sides, no curl, no comfort posture.")
row(10, 11, "Because it's dark, and this is what bodies do in the dark.", "[CAVE][THE_FIGURE] Very wide overhead shot of the whole cave, three flat figures lying in dark shapes among hides, the fire a tiny dull ember at centre, enormous black surround.")

# ------------------------------------------------------------ S11 FIRST SLEEP
row(11, 1, "First sleep.", "[ABSTRACT][FIG_NONE] Flat cream void, the words rendered as elaborate hand-inked display lettering in bold charcoal with a flat mustard fill, tilted two degrees, a soft flat shadow beneath — first and only time the screen becomes a title card.")
row(11, 2, "That's the first name.", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink label shape suspended by a single thin line, now filled with a solid mustard block, a small ink arrow pointing up at it.")
row(11, 3, "Not a modern word historians invented —", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink quill pen crossed out with a single terracotta diagonal stroke, resting beside an unrolled flat scroll shape.")
row(11, 4, "the actual phrase, written down in letters and diaries", "[ABSTRACT][NO_FIG] High-angle flat-lay composition of four simple ink document shapes scattered on cream, each a plain rectangle with three or four short horizontal strokes for lines.")
row(11, 5, "and court records and medical manuals,", "[ABSTRACT][NO_FIG] Overhead flat-lay of two more document shapes, one bearing a simple ink seal circle, the other a laid-flat open book of two facing pages.")
row(11, 6, "across hundreds of years,", "[ABSTRACT][NO_FIG] Flat cream void, four simple ink calendar blocks in a horizontal row, the gaps between them widening toward the right, one small charcoal bookmark on the first.")
row(11, 7, "in English, French, Italian.", "[ABSTRACT][NO_FIG] Flat cream void, three simple ink speech-bubble shapes arranged in a vertical stack, each empty except for a different short squiggle rendered as a flat line of varying curve.")
row(11, 8, "All of it.", "[ABSTRACT][NO_FIG] Flat cream void, the whole composition compressed — the four documents, the two bubbles and the seal all now small and clustered in a tight block at frame centre.")
row(11, 9, "First sleep.", "[ABSTRACT][NO_FIG] The display lettering from the opening of this slide, now larger, dead centre, fully filled mustard with a heavier flat shadow and two small ink underline strokes.")
row(11, 10, "It came soon after the fire was banked,", "[CAVE][THE_ANCESTOR] Wide shot, the ancestor's silhouette settling onto a hide with the fire behind them reduced to a smothered flat dome of ash, no flames.")
row(11, 11, "and it did not last the night.", "[CAVE][NO_FIG] Wide static shot of the dark cave, the fire almost out, everything flat and still — the frame deliberately under-populated with half of it empty blackness.")
row(11, 12, "Four hours, maybe.", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink arc divided into four equal segments by three tick marks, four of them filled solid charcoal and the remainder left as a bare line.")
row(11, 13, "It was often called the dead sleep,", "[ABSTRACT][NO_FIG] Flat cream void, lettering reading only as a bold charcoal ink phrase shape with no readable content, a single terracotta stroke beneath it like a date-tally.")
row(11, 14, "because it was the heavy one —", "[CAVE][THE_ANCESTOR] Low-angle shot of the sleeping figure pressed deep into a hide, the hide's flat tan surface dented around them, one thin arm hanging limp over the edge.")
row(11, 15, "the drop,", "[ABSTRACT][NO_FIG] Flat cream void, a single vertical ink line with a heavy solid charcoal circle at its base, three small downward motion dashes above the circle.")
row(11, 16, "the place where you stopped being a person lying down", "[CAVE][THE_ANCESTOR] Overhead shot, the figure rendered flat and simplified, limbs relaxed, the round head shown as a plain white disc with closed eyes, barely individuated.")
row(11, 17, "and became a warm weight that was not in the room.", "[CAVE][NO_FIG] Wide empty shot of the cave, the fire out, no figure at all in frame — only a flat tan hide mound on the umber floor, everything slate and still.")
row(11, 18, "You went down into it and you were gone.", "[CAVE][NO_FIG] Extreme wide, the cave interior almost entirely black, a single faint slate-blue suggestion of the rear wall, one smothered ember, nothing else.")

# ------------------------------------------------------------ S12 SURFACING
row(12, 1, "Then, around two in the morning,", "[ABSTRACT][NO_FIG] Flat cream void, a simple ink clock face rendered as a plain circle with two flat charcoal hands pointing to two, no numerals, small tick marks at the quarters.")
row(12, 2, "you came up out of it.", "[CAVE][THE_FIGURE] Low-angle shot from floor level, the figure rising from the hide, one thin arm pushing down, the round head lifting slowly, dim slate light behind.")
row(12, 3, "Not waking. Not a startle, not a sick feeling.", "[CAVE][THE_FIGURE] Frontal close-up, the round head calm and neutral, two bean eyes fully open and level, eyebrows flat, mouth unbothered — total absence of alarm.")
row(12, 4, "You surface, the way a diver surfaces,", "[CAVE][THE_FIGURE] Wide shot, the figure rendered as if rising through a flat charcoal plane, the upper half of the body breaking clear above it, the lower half still flat below.")
row(12, 5, "slowly, without knowing it's happening.", "[CAVE][THE_FIGURE] Very wide, the figure seated upright and small on the cave floor with huge empty dark walls around them, the fire's remains far off to one side, no urgency anywhere in frame.")
row(12, 6, "The fire has burned lower.", "[CAVE][NO_FIG] Tight shot of the fire pit, three flat charcoal lumps and one dull terracotta ember, the visual distance between the ember and the wall noticeably longer.")
row(12, 7, "The air has gone colder.", "[CAVE][NO_FIG] Wide shot with the palette shifted cool, slate and pale blue-grey dominating, the last warm mustard gone entirely from the frame, frost implied by two flat white patches.")
row(12, 8, "And you are not confused.", "[CAVE][THE_FIGURE] Straight-on medium shot, the figure seated with hands flat on their own knees, round head up, bean eyes aimed directly at the camera, entirely composed.")
row(12, 9, "You know exactly where you are and exactly what hour this is.", "[CAVE][THE_FIGURE] Over-the-shoulder shot from behind the figure looking across the cave at the fire's remains and the cave mouth beyond — a map they already hold.")
row(12, 10, "It's the hour you always wake.", "[ABSTRACT][NO_FIG] Flat cream void, twelve small ink clock faces in a row, eleven rendered as bare outlines, one at position two filled solid charcoal and circled in terracotta.")
row(12, 11, "It's the hour.", "[ABSTRACT][NO_FIG] Extreme close-up, a single clock face filling the frame, solid charcoal fill, one mustard hand pointing to two, everything else bare cream.")
row(12, 12, "You sit up.", "[CAVE][THE_FIGURE] Dramatic low-angle silhouette shot, the figure's whole body rendered as bold charcoal against the pale cave mouth behind them, upright and alone, the posture decisive.")

# ---------------------------------------------------------------- write file
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visuals.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(HEADER)
    w.writerows(R)

print(f"PART 1 rows: {len(R)} -> {out}")
print("last row:", R[-1][0], R[-1][1], R[-1][2][:60])
