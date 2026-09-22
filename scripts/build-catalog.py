#!/usr/bin/env python3
"""Render docs/03-components/** from catalog/components.json + catalog/figma-inventory.json.

Usage:  python3 scripts/build-catalog.py
Idempotent: regenerates every page and the index. Hand-written content belongs in the
catalog, not in the generated markdown.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "catalog", "components.json")
INVENTORY = os.path.join(ROOT, "catalog", "figma-inventory.json")
OUT = os.path.join(ROOT, "docs", "03-components")

LEVEL_DIR = {"atom": "atoms", "molecule": "molecules", "organism": "organisms", "template": "templates", "page": "pages"}
LEVEL_BLURB = {
    "atom": "Atoms are the smallest usable UI units: a button, an icon, a checkbox. They do one thing, take tokens directly and never know about product data.",
    "molecule": "Molecules are small groups of atoms working as a unit: a labelled field, a status pill, a breadcrumb. They own a single, clear responsibility.",
    "organism": "Organisms are complex sections built from molecules and atoms: the data table, the top app bar, the dropdown list. They usually manage state or layout.",
    "template": "Templates are page-level layouts with slots and no real content. They fix where organisms go.",
    "page": "Pages are templates filled with real merchant data. They are documented as references to production, not built in the library.",
}
STRUCTURE_ADVICE = {
    1: "Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).",
    2: "Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.",
    3: "Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.",
    4: "Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.",
    5: "Build the **logic as a headless hook / controller** (state, keyboard, focus, ARIA) and a thin UI component on top. The hook must be usable with custom UI; document it with examples since it is invisible in Figma.",
}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def clean_value(v):
    v = v.strip()
    v = re.sub(r"^-+", "", v)
    return v


def clean_key(k):
    k = k.strip()
    k = re.sub(r"^-+", "", k)
    k = re.sub(r"\?$", "", k)
    return k


def find_frames(inv, names):
    """Return list of (section, frame, data) for frame names anywhere in the inventory (+ loose frames)."""
    out = []
    for sec, frames in inv["sections"].items():
        for fname, data in frames.items():
            if fname in names:
                out.append((sec, fname, data))
    for tag, name in inv.get("loose", []):
        if name in names:
            out.append(("(top level)", name, None))
    return out


def md_table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        lines.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(lines)


def render_props(props):
    if not props:
        return "_No public props beyond the base._"
    if isinstance(props, str):
        return props
    rows = []
    for k, v in props.items():
        if isinstance(v, list):
            rows.append((f"`{k}`", ", ".join(f"`{x}`" for x in v)))
        else:
            rows.append((f"`{k}`", v))
    return md_table(["Prop", "Values / type"], rows)


def render_list(items, empty="_none_"):
    if not items:
        return empty
    if isinstance(items, str):
        return items
    return "\n".join(f"- {x}" for x in items)


def render_figma(comp, inv):
    fig = comp.get("figma", {})
    names = fig.get("frames", [])
    frames = find_frames(inv, names)
    parts = []
    if fig.get("node"):
        parts.append(f"Figma node: `{fig['node']}`")
    if fig.get("componentSet"):
        parts.append(f"Figma component set: `{fig['componentSet']}`")
    if fig.get("library"):
        parts.append(f"Library: `{fig['library']}`")
    if fig.get("variantFilter"):
        parts.append(f"Variant filter: `{fig['variantFilter']}`")
    if fig.get("styles"):
        parts.append(f"Figma styles: `{fig['styles']}`")
    if fig.get("related"):
        parts.append(f"Related: {fig['related']}")
    head = "\n".join(f"- {p}" for p in parts)
    if not frames:
        body = "_No matching frame in the current Figma library._" if not names else "_Frames listed in the catalog were not found in figma-inventory.json: " + ", ".join(names) + "_"
        return (head + "\n\n" if head else "") + body
    rows = []
    for sec, fname, data in frames:
        if data is None:
            rows.append((f"`{fname}`", sec, "-", "-"))
            continue
        props = "; ".join(f"{clean_key(k)}: " + ", ".join(clean_value(x) for x in v) for k, v in data["props"].items())
        rows.append((f"`{fname}`", sec, data["variants"], props or "-"))
    return (head + "\n\n" if head else "") + md_table(["Figma frame", "Section today", "Variants", "Variant properties (cleaned)"], rows)


def render_component(comp, inv, by_id):
    s = comp["structure"]
    lines = []
    lines.append(f"# {comp['name']}")
    lines.append("")
    lines.append(f"> {comp['summary']}")
    lines.append("")
    lines.append(md_table(
        ["Atomic level", "Material category", "Structure type", "Status", "Storybook story"],
        [(comp["level"], comp["category"], f"{s} - {STRUCTURE_NAMES[str(s)]}", comp.get("status", "existing"), f"`{comp['storybook']}`" if comp.get("storybook") else "_not in Storybook_")],
    ))
    lines.append("")
    if comp.get("anatomy"):
        lines.append("## Anatomy")
        lines.append("")
        lines.append(render_list(comp["anatomy"]))
        lines.append("")
    lines.append("## Props")
    lines.append("")
    lines.append(render_props(comp.get("props")))
    lines.append("")
    if comp.get("states"):
        lines.append("## States")
        lines.append("")
        lines.append(render_list(comp["states"]))
        lines.append("")
    if comp.get("tokens"):
        lines.append("## Tokens")
        lines.append("")
        lines.append(render_list(comp["tokens"]))
        lines.append("")
    if comp.get("rtl"):
        lines.append("## RTL and localisation")
        lines.append("")
        lines.append(comp["rtl"])
        lines.append("")
    lines.append("## How to build it")
    lines.append("")
    lines.append(STRUCTURE_ADVICE[s])
    if comp.get("base"):
        lines.append("")
        lines.append(f"Base component: **{comp['base']}**.")
    if comp.get("headless"):
        lines.append("")
        lines.append(f"Headless layer: **{comp['headless']}**.")
    if comp.get("composes"):
        links = []
        for cid in comp["composes"]:
            c = by_id.get(cid)
            if c:
                links.append(f"[{c['name']}](../{LEVEL_DIR[c['level']]}/{cid}.md)")
            else:
                links.append(f"`{cid}` (not yet in catalog)")
        lines.append("")
        lines.append("Composes: " + ", ".join(links) + ".")
    if comp.get("template"):
        t = by_id.get(comp["template"])
        if t:
            lines.append("")
            lines.append(f"Template: [{t['name']}](../templates/{comp['template']}.md).")
    lines.append("")
    if comp.get("notes"):
        lines.append("## Notes and migration")
        lines.append("")
        lines.append(comp["notes"])
        lines.append("")
    lines.append("## Source in Figma today")
    lines.append("")
    lines.append(render_figma(comp, inv))
    lines.append("")
    lines.append("---")
    lines.append(f"_Generated from `catalog/components.json` (id `{comp['id']}`). Edit the catalog, not this file._")
    lines.append("")
    return "\n".join(lines)


def render_index(cat, by_level, by_cat):
    lines = ["# Components", "",
             "Every component classified by **atomic level** (how it composes) and **Material category** (how you find it), with its **structure type** (how it is built). Generated from `catalog/components.json`.",
             ""]
    total = len(cat["components"])
    existing = sum(1 for c in cat["components"] if c.get("status") == "existing")
    proposed = sum(1 for c in cat["components"] if c.get("status") == "proposed")
    lines.append(md_table(["Total", "Existing in Figma / Storybook", "Proposed (gap)", "Page references"], [(total, existing, proposed, total - existing - proposed)]))
    lines.append("")
    lines.append("## By atomic level")
    lines.append("")
    for level in cat["levels"]:
        comps = by_level.get(level, [])
        lines.append(f"### {level.capitalize()}s ({len(comps)})")
        lines.append("")
        lines.append(LEVEL_BLURB[level])
        lines.append("")
        rows = [(f"[{c['name']}]({LEVEL_DIR[level]}/{c['id']}.md)", c["category"], c["structure"], c.get("status", "existing"), c["summary"].split(".")[0] + ".") for c in comps]
        lines.append(md_table(["Component", "Material category", "Structure", "Status", "What it is"], rows))
        lines.append("")
    lines.append("## By Material category")
    lines.append("")
    for category in cat["categories"]:
        comps = by_cat.get(category, [])
        lines.append(f"### {category} ({len(comps)})")
        lines.append("")
        rows = [(f"[{c['name']}]({LEVEL_DIR[c['level']]}/{c['id']}.md)", c["level"], c["structure"], c.get("status", "existing")) for c in comps]
        lines.append(md_table(["Component", "Atomic level", "Structure", "Status"], rows))
        lines.append("")
    lines.append("## Structure types legend")
    lines.append("")
    lines.append(md_table(["#", "Pattern"], [(k, v) for k, v in cat["structureTypes"].items()]))
    lines.append("")
    lines.append("See [component-structure-types.md](../00-overview/component-structure-types.md) for when to use each.")
    lines.append("")
    return "\n".join(lines)


def render_level_readme(level, comps):
    lines = [f"# {level.capitalize()}s", "", LEVEL_BLURB[level], ""]
    rows = [(f"[{c['name']}]({c['id']}.md)", c["category"], c["structure"], c.get("status", "existing")) for c in comps]
    lines.append(md_table(["Component", "Material category", "Structure", "Status"], rows))
    lines.append("")
    return "\n".join(lines)


def main():
    cat = load(CATALOG)
    inv = load(INVENTORY)
    global STRUCTURE_NAMES
    STRUCTURE_NAMES = {k: v.split(" (")[0] for k, v in cat["structureTypes"].items()}
    by_id = {c["id"]: c for c in cat["components"]}
    by_level, by_cat = {}, {}
    for c in cat["components"]:
        by_level.setdefault(c["level"], []).append(c)
        by_cat.setdefault(c["category"], []).append(c)

    # wipe generated pages
    for level, d in LEVEL_DIR.items():
        path = os.path.join(OUT, d)
        os.makedirs(path, exist_ok=True)
        for f in os.listdir(path):
            if f.endswith(".md"):
                os.remove(os.path.join(path, f))

    written = 0
    for c in cat["components"]:
        path = os.path.join(OUT, LEVEL_DIR[c["level"]], c["id"] + ".md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_component(c, inv, by_id))
        written += 1
    for level in cat["levels"]:
        with open(os.path.join(OUT, LEVEL_DIR[level], "README.md"), "w", encoding="utf-8") as f:
            f.write(render_level_readme(level, by_level.get(level, [])))
    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as f:
        f.write(render_index(cat, by_level, by_cat))

    # coverage check: every Figma frame should be claimed by at least one component
    claimed = set()
    for c in cat["components"]:
        claimed.update(c.get("figma", {}).get("frames", []))
    all_frames = {fn for frames in inv["sections"].values() for fn in frames} | {n for _, n in inv.get("loose", [])}
    unclaimed = sorted(all_frames - claimed)
    print(f"wrote {written} component pages + index")
    if unclaimed:
        print(f"WARNING {len(unclaimed)} Figma frames not claimed by any component:")
        for u in unclaimed:
            print("  -", u)
        return 1
    print("all Figma frames are claimed by a component")
    return 0


if __name__ == "__main__":
    sys.exit(main())
