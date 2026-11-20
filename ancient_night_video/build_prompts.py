#!/usr/bin/env python3
"""Assemble full generation prompts for ancient_night_video.

Prompt formula (spec):
    [Verbatim Art Style & Character Invariants] + [Dynamic Framing, Action & Visual SFX]

The verbatim blocks are EXTRACTED FROM continuity.md at runtime via regex, so the
continuity document remains the single source of truth. Nothing is retyped.

Each row's visual_prompt carries a world tag and a figure tag:
    [WORLD][FIGURE] dynamic direction
WORLD maps to a WORLD BLOCK from continuity.md section 3.
FIGURE maps to the CHARACTER BLOCK plus a role line.

Usage:
    python3 build_prompts.py            # print all prompts
    python3 build_prompts.py 5          # print prompt for row index 5 (1-based)
    python3 build_prompts.py --csv      # write prompts.csv alongside visuals.csv
"""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONT = os.path.join(HERE, "continuity.md")
VISUALS = os.path.join(HERE, "visuals.csv")


def load_blocks():
    """Extract the three verbatim blocks from continuity.md."""
    src = open(CONT, encoding="utf-8").read()

    def grab(section_header, next_header):
        start = src.index(section_header)
        end = src.index(next_header, start)
        seg = src[start:end]
        # the block is the first '> ' quoted run
        lines = [l[2:].strip() for l in seg.splitlines() if l.startswith("> ")]
        return " ".join(lines).strip()

    art = grab("## 1. ARTSTYLE BLOCK", "## 2. CHARACTER BLOCK")
    char = grab("## 2. CHARACTER BLOCK", "## 3. WORLD BLOCKS")
    worlds = {}
    sect = src[src.index("## 3. WORLD BLOCKS"):src.index("## 4. PALETTE")]
    # split on the ### headers so each chunk is exactly one world block
    chunks = re.split(r"^### ", sect, flags=re.M)[1:]
    for ch in chunks:
        header, _, rest = ch.partition("\n")
        # header looks like:  3a. NIGHT CAVE (used for ~70% of frames)
        name = re.sub(r"^3[a-z]\.\s*", "", header).split("(")[0].strip()
        body = " ".join(
            line[2:].strip() for line in rest.splitlines() if line.startswith("> ")
        )
        if name and body:
            worlds[name] = body
    return art, char, worlds


ART, CHAR, WORLDS = load_blocks()

WORLD_KEY = {
    "MODERN_ROOM": "MODERN ROOM",
    "MODERN_BED": "MODERN BEDROOM",
    "CAVE": "NIGHT CAVE",
    "CAVE_MOUTH": "NIGHT CAVE",
    "ABSTRACT": None,  # no scenery block
}

FIG_ROLE = {
    "NO_FIG": None,
    "THE_FIGURE": "THE FIGURE in this frame is THE FIGURE: the modern second-person protagonist, drawn in the modern room or bedroom world.",
    "THE_ANCESTOR": "THE FIGURE in this frame is THE ANCESTOR: the prehistoric protagonist, wearing the flat tan animal-hide wrap.",
    "THE_ANCESTORS_GROUP": "THE FIGURES in this frame are THE ANCESTORS: a small group, all built to the identical stick-figure construction, differing only in pose.",
}

ABSTRACT_BLOCK = (
    "This frame has NO scenery and NO environment. It is a flat, bare paper-cream field "
    "with nothing in it except the described diagram elements and the paper grain. No room, "
    "no wall, no floor, no fire, no horizon, no vignette."
)


def build(row):
    prompt_tag = row["visual_prompt"]
    tags = re.findall(r"\[([A-Z_]+)\]", prompt_tag)
    world_tag = tags[0] if tags else "ABSTRACT"
    fig_tag = tags[1] if len(tags) > 1 else "NO_FIG"
    direction = re.sub(r"^(\[[A-Z_]+\])+", "", prompt_tag).strip()

    parts = [ART]

    world_name = WORLD_KEY.get(world_tag)
    if world_name and world_name in WORLDS:
        parts.append(WORLDS[world_name])
    else:
        parts.append(ABSTRACT_BLOCK)

    role = FIG_ROLE.get(fig_tag)
    if role:
        parts.append(CHAR + " " + role)
    else:
        parts.append("No characters, no figures, no faces in this frame.")

    parts.append("SPECIFIC SHOT: " + direction)
    parts.append("Do not render any text, lettering, labels or numerals anywhere in this image.")

    return " ".join(parts)


def main():
    rows = list(csv.DictReader(open(VISUALS, encoding="utf-8")))
    if "--csv" in sys.argv:
        out = os.path.join(HERE, "prompts.csv")
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow(["file", "slide_id", "moment", "moment_text", "prompt"])
            for r in rows:
                fn = f"frames/beat{int(r['slide_id']):02d}m{int(r['moment']):02d}.png"
                w.writerow([fn, r["slide_id"], r["moment"], r["moment_text"], build(r)])
        print(f"wrote {out} ({len(rows)} prompts)")
        return

    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        i = int(sys.argv[1]) - 1
        r = rows[i]
        print(f"--- ROW {i+1}/{len(rows)}  beat{int(r['slide_id']):02d}m{int(r['moment']):02d} ---")
        print(f"TEXT: {r['moment_text']}")
        print()
        print(build(r))
        return

    for i, r in enumerate(rows, 1):
        print(f"{i}\tbeat{int(r['slide_id']):02d}m{int(r['moment']):02d}\t{r['moment_text']}")


if __name__ == "__main__":
    main()
