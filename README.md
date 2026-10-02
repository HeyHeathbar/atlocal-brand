# atLocal Brand System

Published at **https://brand.atlocal.ai**. Start with [START_HERE.md](START_HERE.md).

This repo is the single source of truth for atLocal brand files that people and AI tools (ChatGPT, Claude, Cursor/Grok, Codex) read before making branded work.

| File | What it is |
|---|---|
| `START_HERE.md` | The rules, in plain language, with every value written out |
| `atlocal.css` | Canonical brand values. Edit this, never `tokens.json` |
| `tokens.json` | Generated from `atlocal.css` |
| `logo/`, `symbol/`, `icon/`, `studio/` | Official logo, pin, app icon and studio lockup files, SVG + transparent PNG (4×) |
| `fonts/` | Plus Jakarta Sans (SIL Open Font License) |
| `scripts/build_logos.py` | Generates every logo file from the font and the pin geometry |
| `index.html`, `llms.txt`, `CNAME` | The public site |

## Changing something

1. Colours, type or tokens: edit `atlocal.css`, then `START_HERE.md`. Run `npm run tokens`.
2. Logo, pin or studio lockups: edit `scripts/build_logos.py` (add a city to the list for a new studio), then rebuild:

   ```bash
   pip install fonttools uharfbuzz
   python3 scripts/build_logos.py
   for f in logo/*.svg symbol/*.svg icon/*.svg studio/*.svg; do rsvg-convert -z 4 "$f" -o "${f%.svg}.png"; done
   ```

   List any new file in `START_HERE.md`.
3. Run `npm run check`.
4. Open a PR. CI runs the same check. Merging to `main` publishes the site.
5. Copy `atlocal.css` unchanged into the site repos. Their CI fails until they match.
