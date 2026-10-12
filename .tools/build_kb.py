"""Build the Projekt Wania graph page from the vault's [[wikilinks]] and frontmatter.
Usage: python3 build_kb.py <vault dir> <out.html>   (kb_template.html must sit next to this script)"""
import json, re, glob, os, sys
root, out = sys.argv[1], sys.argv[2]
SKIP = ("templates/", "raw/", "output/", ".tools/", "brand-assets/")
pages = {}
for p in sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True)):
    rel = os.path.relpath(p, root)
    if rel.startswith(SKIP) or rel in ("CLAUDE.md", "log.md"): continue
    text = open(p, encoding="utf-8").read()
    meta = {}
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1); meta[k.strip()] = v.strip()
        text = text[m.end():]
    name = os.path.splitext(os.path.basename(rel))[0]
    kind = meta.get("type", "index")
    if kind == "entity": kind = {"person": "person", "company": "company"}.get(meta.get("kind"), "service")
    pages[name] = {"id": name, "label": meta.get("title", name), "kind": kind, "path": rel, "text": text}
links, seen = [], set()
for n, p in pages.items():
    for t in re.findall(r"\[\[([^\]|#]+)", p["text"]):
        t = t.strip()
        if t in pages and t != n:
            key = tuple(sorted((n, t)))
            if key not in seen:
                seen.add(key); links.append({"source": n, "target": t})
data = {"docs": {n: p["text"] for n, p in pages.items()},
        "paths": {n: p["path"] for n, p in pages.items()},
        "nodes": [{k: p[k] for k in ("id", "label", "kind")} for p in pages.values()],
        "links": links}
tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kb_template.html"), encoding="utf-8").read()
open(out, "w", encoding="utf-8").write(tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(len(pages), "pages", len(links), "links")
