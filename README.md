# atLocal Brand System

Published at **https://brand.atlocal.ai**. Start with [START_HERE.md](START_HERE.md).

This repo is the single source of truth for atLocal brand files that people and AI tools (ChatGPT, Claude, Cursor/Grok, Codex) read before making branded work.

| File | What it is |
|---|---|
| `START_HERE.md` | The rules, in plain language, with every value written out |
| `atlocal.css` | Canonical brand values. Edit this, never `tokens.json` |
| `tokens.json` | Generated from `atlocal.css` |
| `logo/`, `glyph/` | Official logo and glyph files, SVG + transparent PNG (4×) |
| `index.html`, `llms.txt`, `CNAME` | The public site |

## Changing something

1. Change the design in Figma first: "atlocal - claude", page "Guide". Logo exports come from the frame "Brand repo exports (brand.atlocal.ai)" on the Components page.
2. Update `atlocal.css` and/or the files in `logo/` and `glyph/`, then `START_HERE.md`.
3. Run `npm run tokens`, then `npm run check`.
4. Open a PR. CI runs the same check. Merging to `main` publishes the site.
5. Copy `atlocal.css` unchanged into the site repos. Their CI fails until they match.

PNG files are rendered from the SVGs: `rsvg-convert -z 4 logo/<name>.svg -o logo/<name>.png`.
