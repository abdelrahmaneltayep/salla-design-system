#!/usr/bin/env python3
"""Parse catalog/storybook-twilight.md (the Storybook capture) into catalog/storybook-inventory.json.

Extracts per component: tag, related elements, storybook entry id, description, props, events,
slots, stories and the rendered markup of the default story. Also extracts the token tables
(colour palette, roundness, shadows, global CSS variables) into catalog/storybook-tokens.json.

Usage: python3 scripts/parse-storybook.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "catalog", "storybook-twilight.md")
OUT = os.path.join(ROOT, "catalog", "storybook-inventory.json")
OUT_TOKENS = os.path.join(ROOT, "catalog", "storybook-tokens.json")


def parse_table(lines):
    """Parse a markdown table (list of lines starting with |) into list of dicts."""
    rows = [l for l in lines if l.startswith("|")]
    if len(rows) < 2:
        return []
    split = lambda r: [c.strip() for c in re.split(r"(?<!\\)\|", r.strip().strip("|"))]
    head = split(rows[0])
    out = []
    for r in rows[2:]:
        cells = split(r)
        if len(cells) < len(head):
            cells += [""] * (len(head) - len(cells))
        out.append({head[i]: cells[i].strip("`").replace("\\|", "|") for i in range(len(head))})
    return out


def sections(text, level):
    pat = re.compile(rf"^{'#' * level} (.*)$", re.M)
    idx = [(m.start(), m.group(1)) for m in pat.finditer(text)]
    for i, (start, title) in enumerate(idx):
        end = idx[i + 1][0] if i + 1 < len(idx) else len(text)
        yield title, text[start:end]


def block_after(body, heading):
    m = re.search(rf"\*\*{re.escape(heading)}\*\*\s*\n(.*?)(?=\n\*\*|\n---|\Z)", body, re.S)
    return m.group(1).strip().splitlines() if m else []


def parse_components(text):
    comps = {}
    comp_text = text.split("## 2. Components", 1)[1].split("## 3. Appendix", 1)[0]
    for title, body in sections(comp_text, 3):
        name = re.sub(r"^\d+\.\d+\s+", "", title).strip()
        tag = re.search(r"\*\*Tag:\*\* `<([^>]+)>`", body)
        related = re.findall(r"`<(s-[a-z0-9-]+)>`", body.split("**Storybook:**")[0])
        sb = re.search(r"\*\*Storybook:\*\* `([^`]+)` · <([^>]+)>", body)
        desc_m = re.search(r"\*\*Storybook:\*\*[^\n]*\n\n(.*?)\n\n\*\*", body, re.S)
        desc = desc_m.group(1).strip() if desc_m else ""
        props = parse_table(block_after(body, "Props"))
        events = parse_table(block_after(body, "Events"))
        slots = parse_table(block_after(body, "Slots"))
        stories = parse_table(block_after(body, "Stories"))
        markup = re.search(r"```html\n(.*?)```", body, re.S)
        entry = sb.group(1) if sb else ""
        comps[entry.replace("components-", "")] = {
            "name": name,
            "tag": tag.group(1) if tag else "",
            "related": [r for r in related if tag and r != tag.group(1)],
            "entry": entry,
            "url": sb.group(2) if sb else "",
            "description": desc,
            "props": [{"name": p.get("Prop", ""), "type": p.get("Type", ""), "control": p.get("Control", ""), "default": p.get("Default", ""), "options": [o.strip() for o in p.get("Options", "").split(",") if o.strip()], "description": p.get("Description", "")} for p in props],
            "events": [{"name": e.get("Event", ""), "description": e.get("Description", "")} for e in events],
            "slots": [{"name": s.get("Slot", ""), "description": s.get("Description", "")} for s in slots],
            "stories": [{"name": s.get("Story", ""), "id": s.get("id", ""), "args": s.get("Key args", "")} for s in stories],
            "markup": markup.group(1).strip() if markup else "",
        }
    return comps


def parse_tokens(text):
    tok = text.split("## 1. Design tokens", 1)[1].split("## 2. Components", 1)[0]
    palette = {}
    for group, body in re.findall(r"\*\*([A-Za-z]+)\*\*\s*\n\n(\| Token.*?)(?=\n\n\*\*|\n### |\Z)", tok, re.S):
        for row in parse_table(body.splitlines()):
            palette[row["Token"]] = {"group": group, "cssVar": row["CSS variable"], "hsl": row["HSL"], "hex": row["Hex"].upper(), "tailwind": row["Tailwind"]}
    def simple(heading):
        m = re.search(rf"### {re.escape(heading)}.*?\n(\| Class.*?)(?=\n### |\Z)", tok, re.S)
        return {r["Class"]: r["Value"] for r in parse_table(m.group(1).splitlines())} if m else {}
    m = re.search(r"### 1\.5 Global CSS variables.*?\n(\| Variable.*?)(?=\n---|\Z)", tok, re.S)
    css_vars = {r["Variable"]: r["Value"] for r in parse_table(m.group(1).splitlines())} if m else {}
    return {"$description": "Design tokens as shipped in the Twilight Storybook (dashboard-ui-components.pages.dev), captured 2026-09-22. Colours are HSL channels on :root; hex values are the computed equivalents.", "palette": palette, "roundness": simple("1.3 Roundness"), "shadows": simple("1.4 Shadows"), "cssVariables": css_vars}


def main():
    text = open(SRC, encoding="utf-8").read()
    comps = parse_components(text)
    tokens = parse_tokens(text)
    json.dump({"$description": "Machine-readable inventory of the Twilight Storybook, parsed from catalog/storybook-twilight.md by scripts/parse-storybook.py.", "source": "https://dashboard-ui-components.pages.dev", "captured": "2026-09-22", "components": comps}, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(tokens, open(OUT_TOKENS, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    n_stories = sum(len(c["stories"]) for c in comps.values())
    n_props = sum(len(c["props"]) for c in comps.values())
    print(f"components: {len(comps)}, stories: {n_stories}, props: {n_props}, palette tokens: {len(tokens['palette'])}, css vars: {len(tokens['cssVariables'])}")
    for k, c in comps.items():
        print(f"  {k:18} {c['tag']:20} props={len(c['props']):2} events={len(c['events']):2} slots={len(c['slots'])} stories={len(c['stories'])}")


if __name__ == "__main__":
    main()
