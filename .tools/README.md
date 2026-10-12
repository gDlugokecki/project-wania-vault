# Rebuilding the graph page

The graph page (https://claude.ai/artifact/5oVWTTrNNb4y8FB8XyEvia) is generated from the vault's [[wikilinks]] and frontmatter.

1. `python3 build_kb.py /mnt/project-files/second-brain <out>/wania-map.html`
2. Republish `wania-map.html` to the same artifact URL.

Pages in templates/, raw/, output/ and brand-assets/ are left out, as are CLAUDE.md and log.md.
