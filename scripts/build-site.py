#!/usr/bin/env python3
"""Build the single-file documentation site: site/index.html

Bundles every markdown page under docs/, the component catalog, the CSS tokens and the
live examples from preview/index.html into one HTML file with client-side navigation.
Markdown is rendered in the browser with marked (cdnjs).

Usage: python3 scripts/build-site.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT = os.path.join(ROOT, "site", "index.html")

NAV = [
    ("Overview", [
        ("00-overview/introduction", "Introduction"),
        ("00-overview/methodology", "Atomic × Material"),
        ("00-overview/component-structure-types", "Structure types"),
        ("00-overview/naming-conventions", "Naming conventions"),
        ("00-overview/current-state-audit", "Current state audit"),
        ("00-overview/migration-map", "Migration map"),
    ]),
    ("Foundations", [
        ("01-foundations/design-tokens", "Design tokens"),
        ("01-foundations/layout", "Layout & adaptive"),
        ("01-foundations/interaction-states", "Interaction states"),
        ("01-foundations/accessibility", "Accessibility"),
        ("01-foundations/content-and-localization", "Content & localisation"),
    ]),
    ("Styles", [
        ("02-styles/color", "Color"),
        ("02-styles/typography", "Typography"),
        ("02-styles/spacing", "Spacing"),
        ("02-styles/shape", "Shape"),
        ("02-styles/elevation", "Elevation"),
        ("02-styles/icons", "Icons"),
        ("02-styles/illustrations", "Illustrations"),
        ("02-styles/motion", "Motion"),
    ]),
]
LEVEL_DIR = {"atom": "atoms", "molecule": "molecules", "organism": "organisms", "template": "templates", "page": "pages"}


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def collect_docs():
    pages = {}
    for dirpath, _, files in os.walk(DOCS):
        for fn in files:
            if fn.endswith(".md"):
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, DOCS)[:-3].replace(os.sep, "/")
                pages[rel] = read(full)
    return pages


def intro_markdown(readme):
    # Use the repo README as the introduction, minus the repository map code block noise.
    body = readme.split("## Repository map")[0]
    rest = readme.split("## Quick start")[1] if "## Quick start" in readme else ""
    return body + "\n## Quick start" + rest


def extract_examples(preview_html):
    css = re.search(r'<style id="sds-examples-css">(.*?)</style>', preview_html, re.S).group(1)
    examples = {}
    for m in re.finditer(r'<section class="ex" data-example="([^"]+)"><h3>(.*?)</h3>(.*?)</section>', preview_html, re.S):
        examples[m.group(1)] = {"title": m.group(2), "html": m.group(3).strip()}
    return css, examples


def main():
    pages = collect_docs()
    readme = read(os.path.join(ROOT, "README.md"))
    pages["00-overview/introduction"] = intro_markdown(readme)
    catalog = json.load(open(os.path.join(ROOT, "catalog", "components.json"), encoding="utf-8"))
    tokens_css = read(os.path.join(ROOT, "tokens", "css", "tokens.css"))
    examples_css, examples = extract_examples(read(os.path.join(ROOT, "preview", "index.html")))
    harvest = json.load(open(os.path.join(ROOT, "catalog", "figma-tokens-harvest.json"), encoding="utf-8"))

    comp_nav = []
    for level in catalog["levels"]:
        items = [(f"03-components/{LEVEL_DIR[level]}/{c['id']}", c["name"]) for c in catalog["components"] if c["level"] == level]
        comp_nav.append((level.capitalize() + "s", items))

    data = {
        "pages": pages,
        "nav": NAV,
        "compNav": comp_nav,
        "catalog": catalog,
        "examples": examples,
        "harvestMeta": {"colors": len(harvest["colors"]), "spacing": len(harvest["spacing"]), "frames": 20},
    }
    data_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    html = TEMPLATE.replace("/*__TOKENS_CSS__*/", tokens_css).replace("/*__EXAMPLES_CSS__*/", examples_css).replace("__DATA__", data_json)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {OUT} ({len(html)//1024} KB, {len(pages)} pages, {len(examples)} live examples)")


TEMPLATE = r"""<!doctype html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Salla Design System</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/*__TOKENS_CSS__*/
</style>
<style>
/*__EXAMPLES_CSS__*/
</style>
<style>
  :root {
    --doc-ground: #f3f6f6;
    --doc-surface: #ffffff;
    --doc-surface-2: #eef3f3;
    --doc-ink: #17282b;
    --doc-ink-2: #55696d;
    --doc-ink-3: #8a9a9d;
    --doc-line: #dde5e6;
    --doc-accent: #004956;
    --doc-accent-ink: #ffffff;
    --doc-mint: #a4ffe5;
    --doc-mint-soft: #e6fff9;
    --doc-code: #f4f7f7;
    --doc-font: "IBM Plex Sans Arabic", "Ping AR + LT", "PingARLT", system-ui, sans-serif;
    --doc-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
    --doc-side: 272px;
    color-scheme: light;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --doc-ground: #0d1a1c; --doc-surface: #132326; --doc-surface-2: #182c30; --doc-ink: #eaf2f2; --doc-ink-2: #a8b9bc; --doc-ink-3: #74878b; --doc-line: #24393d; --doc-accent: #a4ffe5; --doc-accent-ink: #062e35; --doc-mint: #1f5f57; --doc-mint-soft: #123a38; --doc-code: #0f1f22; color-scheme: dark;
    }
  }
  :root[data-theme="dark"] {
    --doc-ground: #0d1a1c; --doc-surface: #132326; --doc-surface-2: #182c30; --doc-ink: #eaf2f2; --doc-ink-2: #a8b9bc; --doc-ink-3: #74878b; --doc-line: #24393d; --doc-accent: #a4ffe5; --doc-accent-ink: #062e35; --doc-mint: #1f5f57; --doc-mint-soft: #123a38; --doc-code: #0f1f22; color-scheme: dark;
  }
  * { box-sizing: border-box; }
  html, body { height: 100%; }
  body { margin: 0; background: var(--doc-ground); color: var(--doc-ink); font: 400 15px/1.6 var(--doc-font); }
  a { color: var(--doc-accent); }
  .shell { display: grid; grid-template-columns: var(--doc-side) 1fr; min-height: 100%; }
  .side { position: sticky; top: env(safe-area-inset-top, 0px); height: 100vh; overflow: auto; background: var(--doc-surface); border-inline-end: 1px solid var(--doc-line); padding: 20px 16px 40px; }
  .brand { display: flex; align-items: center; gap: 10px; padding: 4px 8px 16px; text-decoration: none; color: inherit; }
  .brand .mark { width: 32px; height: 32px; border-radius: 8px; background: #004956; display: grid; place-content: center; color: #a4ffe5; font-weight: 700; font-size: 14px; }
  .brand b { font-size: 15px; letter-spacing: 0; }
  .brand small { display: block; color: var(--doc-ink-3); font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: .06em; }
  .search { width: 100%; padding: 8px 10px; border: 1px solid var(--doc-line); border-radius: 8px; background: var(--doc-ground); color: var(--doc-ink); font: inherit; font-size: 13px; margin-block-end: 12px; }
  .search:focus { outline: 2px solid var(--doc-mint); outline-offset: 1px; }
  .group { margin-block: 10px; }
  .group > summary { list-style: none; cursor: pointer; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: .08em; color: var(--doc-ink-3); padding: 6px 8px; display: flex; justify-content: space-between; align-items: center; }
  .group > summary::-webkit-details-marker { display: none; }
  .group > summary::after { content: "▾"; font-size: 12px; transition: transform .15s; }
  .group:not([open]) > summary::after { transform: rotate(-90deg); }
  .group a { display: flex; justify-content: space-between; align-items: center; gap: 8px; padding: 6px 8px; border-radius: 6px; text-decoration: none; color: var(--doc-ink-2); font-size: 13.5px; }
  .group a:hover { background: var(--doc-surface-2); color: var(--doc-ink); }
  .group a.active { background: var(--doc-mint-soft); color: var(--doc-accent); font-weight: 600; }
  .group a .tag { font-size: 10px; color: var(--doc-ink-3); font-weight: 500; }
  .group a.hidden { display: none; }
  .main { min-width: 0; }
  .topbar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; display: flex; align-items: center; gap: 12px; padding: 10px 24px; background: color-mix(in srgb, var(--doc-ground) 88%, transparent); backdrop-filter: blur(8px); border-block-end: 1px solid var(--doc-line); }
  .crumbs { flex: 1; font-size: 13px; color: var(--doc-ink-3); min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .crumbs b { color: var(--doc-ink); font-weight: 600; }
  .tb { border: 1px solid var(--doc-line); background: var(--doc-surface); color: var(--doc-ink); border-radius: 8px; padding: 6px 10px; font: 500 12.5px var(--doc-font); cursor: pointer; }
  .tb:hover { border-color: var(--doc-ink-3); }
  .menu-btn { display: none; }
  .content { max-width: 880px; padding: 28px 24px 96px; }
  .content h1 { font-size: 30px; line-height: 1.2; font-weight: 700; margin: 0 0 12px; text-wrap: balance; letter-spacing: -.01em; }
  .content h2 { font-size: 20px; font-weight: 700; margin: 36px 0 10px; padding-block-start: 12px; border-block-start: 1px solid var(--doc-line); text-wrap: balance; }
  .content h3 { font-size: 16px; font-weight: 600; margin: 24px 0 8px; }
  .content p, .content li { max-width: 72ch; }
  .content blockquote { margin: 0 0 16px; padding: 12px 16px; border-inline-start: 3px solid var(--doc-mint); background: var(--doc-mint-soft); border-radius: 8px; color: var(--doc-ink); }
  .content blockquote p { margin: 0; }
  .content code { font-family: var(--doc-mono); font-size: .88em; background: var(--doc-code); border: 1px solid var(--doc-line); border-radius: 4px; padding: 1px 5px; }
  .content pre { background: var(--doc-code); border: 1px solid var(--doc-line); border-radius: 8px; padding: 14px 16px; overflow-x: auto; font-size: 12.5px; line-height: 1.5; }
  .content pre code { background: none; border: 0; padding: 0; }
  .table-wrap { overflow-x: auto; margin: 12px 0 20px; border: 1px solid var(--doc-line); border-radius: 8px; }
  .content table { border-collapse: collapse; width: 100%; font-size: 13.5px; }
  .content th { text-align: start; background: var(--doc-surface-2); font-weight: 600; padding: 9px 12px; border-block-end: 1px solid var(--doc-line); white-space: nowrap; }
  .content td { padding: 8px 12px; border-block-end: 1px solid var(--doc-line); vertical-align: top; }
  .content tr:last-child td { border-block-end: 0; }
  .content img { max-width: 100%; }
  .content hr { border: 0; border-block-start: 1px solid var(--doc-line); margin: 32px 0; }
  .swatch-inline { display: inline-block; width: 12px; height: 12px; border-radius: 3px; border: 1px solid rgb(0 0 0 / .12); vertical-align: -2px; margin-inline-end: 4px; }
  .classify { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 20px; }
  .pill { display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 600; background: var(--doc-surface-2); color: var(--doc-ink-2); border: 1px solid var(--doc-line); }
  .pill.level { background: var(--doc-mint-soft); color: var(--doc-accent); border-color: transparent; }
  .example { margin: 8px 0 28px; border: 1px solid var(--doc-line); border-radius: 10px; overflow: hidden; background: var(--doc-surface); }
  .example__bar { display: flex; justify-content: space-between; align-items: center; gap: 12px; padding: 8px 14px; background: var(--doc-surface-2); font-size: 12px; color: var(--doc-ink-2); font-weight: 500; }
  .example__stage { padding: 24px; background: #fff; color: #333; overflow-x: auto; }
  .example__stage.rtl { direction: rtl; }
  .cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; margin: 16px 0; }
  .card { display: block; text-decoration: none; color: inherit; background: var(--doc-surface); border: 1px solid var(--doc-line); border-radius: 10px; padding: 14px; }
  .card:hover { border-color: var(--doc-accent); }
  .card b { display: block; font-size: 14.5px; margin-block-end: 4px; }
  .card span { font-size: 12.5px; color: var(--doc-ink-2); display: block; }
  .card .meta { margin-block-start: 8px; display: flex; gap: 6px; flex-wrap: wrap; }
  .card .meta i { font-style: normal; font-size: 10.5px; padding: 2px 7px; border-radius: 999px; background: var(--doc-surface-2); color: var(--doc-ink-3); }
  .filters { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0 4px; }
  .filters select, .filters input { padding: 7px 10px; border: 1px solid var(--doc-line); border-radius: 8px; background: var(--doc-surface); color: var(--doc-ink); font: inherit; font-size: 13px; }
  .stat-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin: 16px 0 24px; }
  .stat { background: var(--doc-surface); border: 1px solid var(--doc-line); border-radius: 10px; padding: 12px 14px; }
  .stat b { display: block; font-size: 24px; font-weight: 700; line-height: 1.1; font-variant-numeric: tabular-nums; }
  .stat span { font-size: 12px; color: var(--doc-ink-2); }
  .hero { padding: 28px; border-radius: 14px; background: linear-gradient(135deg, #004956, #0a6a78 70%, #1f8f95); color: #fff; margin-block-end: 24px; }
  .hero h1 { color: #fff; margin: 0 0 8px; }
  .hero p { color: #d7f5ee; margin: 0; max-width: 60ch; }
  .hero .mint { color: #a4ffe5; }
  .pager { display: flex; justify-content: space-between; gap: 12px; margin-block-start: 48px; padding-block-start: 16px; border-block-start: 1px solid var(--doc-line); font-size: 13.5px; }
  .pager a { text-decoration: none; }
  .pager small { display: block; color: var(--doc-ink-3); font-size: 11px; }
  .empty { color: var(--doc-ink-3); padding: 24px; text-align: center; }
  @media (max-width: 900px) {
    .shell { grid-template-columns: 1fr; }
    .side { position: fixed; inset-inline-start: 0; inset-block: 0; width: min(88vw, 320px); transform: translateX(-100%); transition: transform .2s; z-index: 20; box-shadow: 0 10px 40px rgb(0 0 0 / .25); height: 100vh; }
    [dir="rtl"] .side { transform: translateX(100%); }
    .side.open { transform: none; }
    .menu-btn { display: inline-block; }
    .content { padding: 20px 16px 80px; }
    .content h1 { font-size: 24px; }
    .scrim { position: fixed; inset: 0; background: rgb(0 0 0 / .35); z-index: 15; }
  }
  @media (prefers-reduced-motion: reduce) { .side, .group > summary::after { transition: none; } }
</style>
</head>
<body>
<div class="shell">
  <aside class="side" id="side">
    <a class="brand" href="#/00-overview/introduction"><span class="mark">S</span><span><b>Salla Design System</b><small>Atomic × Material · v0.2</small></span></a>
    <input class="search" id="search" type="search" placeholder="Search pages and components…" aria-label="Search">
    <nav id="nav"></nav>
  </aside>
  <div class="scrim" id="scrim" hidden></div>
  <div class="main">
    <div class="topbar">
      <button class="tb menu-btn" id="menuBtn" aria-label="Open navigation">☰</button>
      <div class="crumbs" id="crumbs"></div>
      <button class="tb" id="dirBtn" title="Flip the live examples between LTR and RTL">Examples: LTR</button>
      <a class="tb" href="https://www.figma.com/design/zuGhoKg2BaBIYUreKuSBGY/Merchant---Storybook-DS?node-id=3678-29170" target="_blank" rel="noopener">Figma ↗</a>
      <a class="tb" href="https://dashboard-ui-components.pages.dev/" target="_blank" rel="noopener">Storybook ↗</a>
    </div>
    <main class="content" id="content"></main>
  </div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
const DATA = __DATA__;
const LEVEL_DIR = {atom:"atoms",molecule:"molecules",organism:"organisms",template:"templates",page:"pages"};
const byId = Object.fromEntries(DATA.catalog.components.map(c => [c.id, c]));
let exampleDir = "ltr";
try { exampleDir = localStorage.getItem("sds-example-dir") || "ltr"; } catch (e) {}

// ---------- navigation ----------
function buildNav() {
  const nav = document.getElementById("nav");
  const groups = [...DATA.nav, ["Components", [["03-components/README", "Components index"]]], ...DATA.compNav];
  nav.innerHTML = groups.map(([title, items], gi) => `
    <details class="group" ${gi < 4 ? "open" : ""} data-group="${title}">
      <summary>${title}</summary>
      ${items.map(([id, label]) => {
        const c = byId[id.split("/").pop()];
        const tag = c ? `<span class="tag">${c.category}</span>` : "";
        return `<a href="#/${id}" data-id="${id}" data-text="${(label + " " + (c ? c.category + " " + c.summary : "")).toLowerCase().replace(/"/g, "")}">${label}${tag}</a>`;
      }).join("")}
    </details>`).join("");
}

function currentId() {
  const h = location.hash.replace(/^#\/?/, "");
  return h || "00-overview/introduction";
}

// resolve a relative markdown link from a page id to another page id
function resolveLink(fromId, href) {
  if (/^(https?:|mailto:|#)/.test(href)) return href;
  let [path, anchor] = href.split("#");
  if (!path) return "#" + anchor;
  if (!path.endsWith(".md")) return href;
  path = path.replace(/\.md$/, "");
  const base = fromId.split("/").slice(0, -1);
  for (const seg of path.split("/")) {
    if (seg === "..") base.pop(); else if (seg !== ".") base.push(seg);
  }
  const id = base.join("/");
  return "#/" + id + (anchor ? "#" + anchor : "");
}

function colorize(html) {
  return html.replace(/<code>(#[0-9a-fA-F]{6})<\/code>/g, (m, hex) => `<code><span class="swatch-inline" style="background:${hex}"></span>${hex}</code>`);
}

// Minimal fallback renderer so the site still reads if the marked CDN is unreachable.
function fallbackMarkdown(id, md) {
  const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const inline = s => esc(s)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/_([^_]+)_/g, "<em>$1</em>")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, (m, t, h) => `<a href="${resolveLink(id, h)}">${t}</a>`);
  const lines = md.split("\n"); const out = []; let i = 0;
  while (i < lines.length) {
    const l = lines[i];
    if (l.startsWith("```")) { const buf = []; i++; while (i < lines.length && !lines[i].startsWith("```")) buf.push(lines[i++]); i++; out.push(`<pre><code>${esc(buf.join("\n"))}</code></pre>`); continue; }
    const h = l.match(/^(#{1,6})\s+(.*)/);
    if (h) { out.push(`<h${h[1].length}>${inline(h[2])}</h${h[1].length}>`); i++; continue; }
    if (l.startsWith("|")) { const rows = []; while (i < lines.length && lines[i].startsWith("|")) rows.push(lines[i++]); const cells = r => r.replace(/^\||\|$/g, "").split(/(?<!\\)\|/).map(c => inline(c.trim().replace(/\\\|/g, "|"))); const head = cells(rows[0]); const body = rows.slice(2); out.push(`<div class="table-wrap"><table><thead><tr>${head.map(c => `<th>${c}</th>`).join("")}</tr></thead><tbody>${body.map(r => `<tr>${cells(r).map(c => `<td>${c}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`); continue; }
    if (/^\s*[-*]\s+/.test(l)) { const items = []; while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*[-*]\s+/, "")); out.push(`<ul>${items.map(x => `<li>${inline(x)}</li>`).join("")}</ul>`); continue; }
    if (/^\s*\d+\.\s+/.test(l)) { const items = []; while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*\d+\.\s+/, "")); out.push(`<ol>${items.map(x => `<li>${inline(x)}</li>`).join("")}</ol>`); continue; }
    if (l.startsWith(">")) { const buf = []; while (i < lines.length && lines[i].startsWith(">")) buf.push(lines[i++].replace(/^>\s?/, "")); out.push(`<blockquote><p>${inline(buf.join(" "))}</p></blockquote>`); continue; }
    if (l.trim() === "---") { out.push("<hr>"); i++; continue; }
    if (l.trim() === "") { i++; continue; }
    const buf = []; while (i < lines.length && lines[i].trim() !== "" && !/^(#|\||```|>|\s*[-*]\s|\s*\d+\.\s)/.test(lines[i])) buf.push(lines[i++]);
    out.push(`<p>${inline(buf.join(" "))}</p>`);
  }
  return colorize(out.join("\n"));
}

function renderMarkdown(id, md) {
  if (typeof marked === "undefined") return fallbackMarkdown(id, md);
  const renderer = new marked.Renderer();
  const origLink = renderer.link.bind(renderer);
  renderer.link = (href, title, text) => {
    if (typeof href === "object") { const t = href; href = t.href; title = t.title; text = t.text; }
    const target = resolveLink(id, href);
    const ext = /^https?:/.test(target) ? ' target="_blank" rel="noopener"' : "";
    return `<a href="${target}"${ext}>${text}</a>`;
  };
  marked.use({ renderer, gfm: true, breaks: false });
  let html = marked.parse(md);
  html = html.replace(/<table>/g, '<div class="table-wrap"><table>').replace(/<\/table>/g, "</table></div>");
  return colorize(html);
}

function exampleBlock(exId) {
  const ex = DATA.examples[exId];
  if (!ex) return "";
  return `<div class="example"><div class="example__bar"><span>Live example · ${ex.title}</span><span>rendered from tokens.css</span></div><div class="example__stage sds ${exampleDir === "rtl" ? "rtl" : ""}" dir="${exampleDir}">${ex.html}</div></div>`;
}

function componentHeader(c) {
  const st = DATA.catalog.structureTypes[String(c.structure)].split(" (")[0];
  const tw = (c.twilight || []).map(t => `<span class="pill">&lt;${t.tag}&gt;</span>`).join("");
  const src = (c.sources || []).length ? (c.sources || []).map(s => `<span class="pill">${s === "storybook" ? "in Twilight" : "in Figma"}</span>`).join("") : `<span class="pill">not built yet</span>`;
  return `<div class="classify"><span class="pill level">${c.level}</span><span class="pill">${c.category}</span><span class="pill">Structure ${c.structure} · ${st}</span><span class="pill">${c.status}</span>${src}${tw}</div>`;
}

function componentsIndex() {
  const cat = DATA.catalog;
  const total = cat.components.length, existing = cat.components.filter(c => c.status === "existing").length, proposed = cat.components.filter(c => c.status === "proposed").length;
  return `
    <div class="hero"><h1>Components</h1><p>Every component classified by <span class="mint">atomic level</span>, <span class="mint">Material category</span> and <span class="mint">structure type</span>. Filter the catalog or browse by level in the sidebar.</p></div>
    <div class="stat-row"><div class="stat"><b>${total}</b><span>components</span></div><div class="stat"><b>${existing}</b><span>in Figma / Storybook today</span></div><div class="stat"><b>${proposed}</b><span>proposed to fill gaps</span></div><div class="stat"><b>${Object.keys(DATA.examples).length}</b><span>with live examples</span></div></div>
    <div class="filters">
      <input id="fq" type="search" placeholder="Filter by name…" aria-label="Filter components">
      <select id="fl" aria-label="Level"><option value="">All levels</option>${cat.levels.map(l => `<option>${l}</option>`).join("")}</select>
      <select id="fc" aria-label="Category"><option value="">All categories</option>${cat.categories.map(l => `<option>${l}</option>`).join("")}</select>
      <select id="fs" aria-label="Structure"><option value="">All structures</option>${Object.entries(cat.structureTypes).map(([k, v]) => `<option value="${k}">${k} · ${v.split(" (")[0]}</option>`).join("")}</select>
      <select id="ft" aria-label="Status"><option value="">Any status</option><option>existing</option><option>proposed</option><option>reference</option></select>
      <select id="fo" aria-label="Source"><option value="">Any source</option><option value="both">Figma + Twilight</option><option value="figma">Figma only</option><option value="storybook">Twilight only</option><option value="none">Neither yet</option></select>
    </div>
    <div class="cards" id="cards"></div>
    <h2>Structure types</h2>
    <div class="table-wrap"><table><thead><tr><th>#</th><th>Pattern</th></tr></thead><tbody>${Object.entries(cat.structureTypes).map(([k, v]) => `<tr><td>${k}</td><td>${v}</td></tr>`).join("")}</tbody></table></div>`;
}

function drawCards() {
  const q = (document.getElementById("fq").value || "").toLowerCase();
  const fl = document.getElementById("fl").value, fc = document.getElementById("fc").value, fs = document.getElementById("fs").value, ft = document.getElementById("ft").value, fo = document.getElementById("fo").value;
  const srcOk = c => { const s = c.sources || []; if (!fo) return true; if (fo === "both") return s.length === 2; if (fo === "none") return s.length === 0; return s.length === 1 && s[0] === fo; };
  const list = DATA.catalog.components.filter(c => (!q || (c.name + " " + c.id + " " + c.summary + " " + (c.storybook || "")).toLowerCase().includes(q)) && (!fl || c.level === fl) && (!fc || c.category === fc) && (!fs || String(c.structure) === fs) && (!ft || c.status === ft) && srcOk(c));
  const el = document.getElementById("cards");
  el.innerHTML = list.length ? list.map(c => `<a class="card" href="#/03-components/${LEVEL_DIR[c.level]}/${c.id}"><b>${c.name}</b><span>${c.summary.split(". ")[0]}.</span><div class="meta"><i>${c.level}</i><i>${c.category}</i><i>structure ${c.structure}</i>${(c.sources || []).map(s => `<i>${s === "storybook" ? "twilight" : s}</i>`).join("")}${DATA.examples[c.id] ? "<i>live</i>" : ""}</div></a>`).join("") : `<div class="empty">No components match.</div>`;
}

function render() {
  const id = currentId();
  const content = document.getElementById("content");
  const md = DATA.pages[id];
  document.querySelectorAll("#nav a").forEach(a => a.classList.toggle("active", a.dataset.id === id));
  const active = document.querySelector("#nav a.active");
  if (active) { active.closest("details").open = true; }
  const parts = id.split("/");
  const compId = parts[0] === "03-components" && parts.length === 3 ? parts[2] : null;
  const c = compId ? byId[compId] : null;
  document.getElementById("crumbs").innerHTML = parts.slice(0, -1).map(p => p.replace(/^\d+-/, "")).join(" / ") + (parts.length > 1 ? " / " : "") + `<b>${c ? c.name : (parts.at(-1) === "README" ? "Index" : parts.at(-1).replace(/-/g, " "))}</b>`;

  if (id === "03-components/README") {
    content.innerHTML = componentsIndex();
    ["fq", "fl", "fc", "fs", "ft", "fo"].forEach(i => document.getElementById(i).addEventListener("input", drawCards));
    drawCards();
  } else if (md !== undefined) {
    let html = renderMarkdown(id, md);
    if (c) {
      html = html.replace(/(<\/h1>)/, "$1" + componentHeader(c) + exampleBlock(c.id));
    }
    if (id === "00-overview/introduction") {
      html = html.replace(/(<\/h1>)/, "$1");
      html = `<div class="hero"><h1>Salla Design System</h1><p>The merchant dashboard design system, restructured on <span class="mint">Atomic Design</span> with <span class="mint">Material Design 3</span> as the structural reference. Tokens and component specs are read directly from the Merchant – Storybook DS Figma library.</p></div>
        <div class="stat-row"><div class="stat"><b>${DATA.catalog.components.length}</b><span>components catalogued</span></div><div class="stat"><b>117</b><span>Figma frames mapped</span></div><div class="stat"><b>${DATA.harvestMeta.colors}</b><span>colour variables verified</span></div><div class="stat"><b>4,049</b><span>icons inventoried</span></div></div>` + html.replace(/^[\s\S]*?<\/h1>/, "");
    }
    content.innerHTML = html;
  } else {
    content.innerHTML = `<h1>Not found</h1><p>No page at <code>${id}</code>.</p>`;
  }
  // pager
  const flat = [...DATA.nav, ["Components", [["03-components/README", "Components index"]]], ...DATA.compNav].flatMap(([g, items]) => items.map(([i, l]) => ({ id: i, label: l, group: g })));
  const idx = flat.findIndex(p => p.id === id);
  if (idx >= 0) {
    const prev = flat[idx - 1], next = flat[idx + 1];
    content.insertAdjacentHTML("beforeend", `<div class="pager"><span>${prev ? `<a href="#/${prev.id}"><small>Previous</small>← ${prev.label}</a>` : ""}</span><span style="text-align:end">${next ? `<a href="#/${next.id}"><small>Next</small>${next.label} →</a>` : ""}</span></div>`);
  }
  const anchor = location.hash.split("#")[2];
  if (anchor) { const t = document.getElementById(anchor); if (t) t.scrollIntoView(); } else { window.scrollTo(0, 0); }
  closeSide();
}

// ---------- chrome ----------
function openSide() { document.getElementById("side").classList.add("open"); document.getElementById("scrim").hidden = false; }
function closeSide() { document.getElementById("side").classList.remove("open"); document.getElementById("scrim").hidden = true; }
document.getElementById("menuBtn").addEventListener("click", openSide);
document.getElementById("scrim").addEventListener("click", closeSide);
document.getElementById("dirBtn").addEventListener("click", () => {
  exampleDir = exampleDir === "ltr" ? "rtl" : "ltr";
  try { localStorage.setItem("sds-example-dir", exampleDir); } catch (e) {}
  document.getElementById("dirBtn").textContent = "Examples: " + exampleDir.toUpperCase();
  document.querySelectorAll(".example__stage").forEach(s => { s.dir = exampleDir; s.classList.toggle("rtl", exampleDir === "rtl"); });
});
document.getElementById("dirBtn").textContent = "Examples: " + exampleDir.toUpperCase();
document.getElementById("search").addEventListener("input", e => {
  const q = e.target.value.trim().toLowerCase();
  document.querySelectorAll("#nav a").forEach(a => a.classList.toggle("hidden", !!q && !a.dataset.text.includes(q)));
  document.querySelectorAll("#nav details").forEach(d => { if (q) d.open = true; });
});
buildNav();
window.addEventListener("hashchange", render);
render();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
