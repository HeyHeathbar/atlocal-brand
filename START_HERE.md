# START HERE: atLocal Brand Rules

This is the source of truth for every atLocal-branded deliverable: presentations, proposals, PDFs, documents, social and marketing assets, and web pages.

**Before you make anything branded:**

1. Read this whole file. Every value you need is written out below.
2. Use the official logo files linked here. Embed or place the file. **Never redraw, retype, recolor, stretch, or rebuild the logo**, and never generate one with an image model. Typing "at[local]" in a font is not the logo.
3. **Do not infer brand styling from any website**, including atlocal.com, atlocalmedia.com, or atlocal.ai. Those sites follow this file, not the other way round.
4. If something you need is not defined here (see [Not defined yet](#not-defined-yet)), **stop and ask Heath. Do not invent it.**

- Canonical URL: https://brand.atlocal.ai/START_HERE.md
- Source repo: https://github.com/HeyHeathbar/atlocal-brand
- Last updated: 2026-10-06 (color roles: where Plum, Royal, Ruby and Coral go; how to write atLocal; master tagline is Your Story Amplified, no periods; studio lockups use market codes; brand v2: the at[local] identity; it replaces the earlier @ logo, palette and fonts)

## Name

How to **write** the name, everywhere text appears (sentences, headlines, documents, email, slides, captions, file titles):

**atLocal**: lowercase "a" and "t", capital "L", lowercase "ocal". One word, no space.

- Always **atLocal**, even at the start of a sentence: "atLocal helps local businesses…"
- Keep it **atLocal** in headings and title case: "Why atLocal Works".
- Never: AtLocal, Atlocal, ATLOCAL, atlocal, At Local, at Local, @Local, or at[local].
- If a design sets text in all capitals, write the name as **atLocal** anyway rather than letting it become ATLOCAL.
- With a studio: "atLocal Dallas-Fort Worth" or "atLocal DFW".
- Web addresses, email addresses and social handles stay lowercase as registered (atlocal.ai, atlocalmedia.com, @atlocal.dallas). That's an address, not the written name.

**The logo is different.** The logo reads `at[local]`, all lowercase, inside brackets. That lettering belongs only in the logo files. Don't type "at[local]" in text, and don't capitalize the L in the logo.

## Tagline

**Your Story Amplified**

This is the master tagline. "Story" is always capitalized in it.

The tagline adapts to the audience. "Your" and "Amplified" never change; when we know who we are talking to, "Story" is replaced with an approved word that describes them. Audience words are lowercase.

| Audience | Tagline |
|---|---|
| Master / default | Your Story Amplified |
| Businesses | Your business Amplified |
| Retail | Your store Amplified |
| Healthcare and professional practices | Your practice Amplified |
| Organizations and associations | Your organization Amplified |
| Foundations | Your foundation Amplified |
| Nonprofits | Your nonprofit Amplified |

- Use **"Your Story Amplified"** as the master version: the primary brand lockup, general company materials, introductions to atLocal, and anywhere the audience is mixed or unknown.
- When the audience is known, use its word and keep that one version throughout the piece. Don't switch words inside one document.
- Only the words in the table are approved. For any other audience word, ask Heath.
- No periods, quotation marks or brackets in the finished tagline. It is written exactly as shown in the table. The middle word may carry the accent colour (Ruby).
- On a homepage the middle word may rotate through the audience words while "Your" and "Amplified" stay still. Don't let the surrounding text shift, and provide a static version for reduced-motion settings.
- Supporting line, for any audience: **We help the right people find you, understand what makes you different, and take action.** Make the outcome specific in the surrounding copy: purchases for a store, inquiries for a practice, donations or participation for a nonprofit.

Every variation carries the same atLocal promise: helping the right people discover, understand, and engage with what our clients have built.

## Colors

| Name | Hex | RGB | CSS token |
|---|---|---|---|
| Plum | `#21134F` | 33, 19, 79 | `--al-plum` |
| Royal | `#3B20AB` | 59, 32, 171 | `--al-royal` |
| Coral | `#FF7D80` | 255, 125, 128 | `--al-coral` |
| Ruby | `#E14565` | 225, 69, 101 | `--al-ruby` |
| Cloud | `#F4F1FB` | 244, 241, 251 | `--al-cloud` |
| White | `#FFFFFF` | 255, 255, 255 | `--al-white` |

### Color roles

Where each color goes, on every surface:

| Color | Use it for | Don't use it for |
|---|---|---|
| Plum | Dark backgrounds; text on light backgrounds; the hover state of a button | |
| Royal | Everyday buttons and links; focus rings | |
| Ruby | The logo; an accent word in a headline; **one** signature button on a page | Small buttons, body-size text, or more than one button on a page |
| Coral | Accents on Plum backgrounds (labels, icons, an accent word) | Anything on White or Cloud |
| Cloud and White | Light backgrounds | |

- **Buttons:** Royal with white text, turning Plum on hover.
- **The signature button:** a page may have one Ruby button with white text for its single most important action (on the homepage, "Press Play"). It must be large with a bold label, because white on Ruby is 4.0:1 contrast, which is enough for large bold text only. It turns Plum on hover.
- **Software** (atlocal.ai back office and client spaces) is a quiet tool: no Ruby buttons at all. There Ruby is the logo and a large accent word on branded moments such as sign-in.
- **Contrast, so the rules above are not guesswork:** white on Plum 16.5:1, white on Royal 10.6:1, Coral on Plum 6.7:1, white on Ruby 4.0:1, Coral on White 2.5:1. Body-size text needs 4.5:1.
- Use only these colors. No tints, shades, gradients, or extra accent colors unless Heath approves them.
- **Approved exception, software only:** a working tool needs a muted text color, borders, hover backgrounds and green / amber / red status colors. Heath approved a short list for the back office; it lives in that codebase's `tokens/back-office.css`. Don't use those values on marketing, print, slides or social, and don't add to them without asking Heath.

Machine-readable: https://brand.atlocal.ai/tokens.json · CSS: https://brand.atlocal.ai/atlocal.css

## Typography

One typeface: **Plus Jakarta Sans** (https://fonts.google.com/specimen/Plus+Jakarta+Sans, also in this repo under `fonts/`).

| Role | Weight |
|---|---|
| Headlines | ExtraBold (800) |
| Labels, small caps lines, buttons | SemiBold (600) |
| Body copy | Medium (500) |

- Market codes, city and section labels are set in capitals, SemiBold, with wide letter spacing (0.14em).
- If a tool cannot load Plus Jakarta Sans, say so. Don't silently substitute another typeface.

## Logo

The logo is the **pin followed by at[local]**. All files have transparent backgrounds. Use the SVG wherever the tool accepts it; use the PNG (4× size) otherwise.

| Version | Use it on | Files |
|---|---|---|
| Light | White or Cloud | [SVG](https://brand.atlocal.ai/logo/atlocal-logo-light.svg) · [PNG](https://brand.atlocal.ai/logo/atlocal-logo-light.png) |
| Dark | Plum | [SVG](https://brand.atlocal.ai/logo/atlocal-logo-dark.svg) · [PNG](https://brand.atlocal.ai/logo/atlocal-logo-dark.png) |
| One-color black | Light backgrounds when only one ink is available | [SVG](https://brand.atlocal.ai/logo/atlocal-logo-black.svg) · [PNG](https://brand.atlocal.ai/logo/atlocal-logo-black.png) |
| One-color white | Dark backgrounds when only one ink is available | [SVG](https://brand.atlocal.ai/logo/atlocal-logo-white.svg) · [PNG](https://brand.atlocal.ai/logo/atlocal-logo-white.png) |

How the colors work:

| | Light | Dark |
|---|---|---|
| Pin and "local" | Plum | White |
| "at", brackets and the shadow under the pin | Ruby | Ruby |

The one-color versions have no shadow.

### The pin

The pin alone is the symbol: app icons, avatars, favicons, map markers, stickers.

| Version | Files |
|---|---|
| Light (Plum pin, Ruby shadow) | [SVG](https://brand.atlocal.ai/symbol/atlocal-pin-light.svg) · [PNG](https://brand.atlocal.ai/symbol/atlocal-pin-light.png) |
| Dark (White pin, Ruby shadow) | [SVG](https://brand.atlocal.ai/symbol/atlocal-pin-dark.svg) · [PNG](https://brand.atlocal.ai/symbol/atlocal-pin-dark.png) |
| One-color black | [SVG](https://brand.atlocal.ai/symbol/atlocal-pin-black.svg) · [PNG](https://brand.atlocal.ai/symbol/atlocal-pin-black.png) |
| One-color white | [SVG](https://brand.atlocal.ai/symbol/atlocal-pin-white.svg) · [PNG](https://brand.atlocal.ai/symbol/atlocal-pin-white.png) |

App icons (the pin on a rounded tile):

| Tile | Files |
|---|---|
| Plum | [SVG](https://brand.atlocal.ai/icon/atlocal-app-icon-plum.svg) · [PNG](https://brand.atlocal.ai/icon/atlocal-app-icon-plum.png) |
| White | [SVG](https://brand.atlocal.ai/icon/atlocal-app-icon-white.svg) · [PNG](https://brand.atlocal.ai/icon/atlocal-app-icon-white.png) |

### Studio lockups

Each studio has its own lockup: the logo followed by the studio's **market code** in capitals. There is no divider between them.

| Code | Studio | Light | Dark |
|---|---|---|---|
| DFW | Dallas-Fort Worth | [SVG](https://brand.atlocal.ai/studio/atlocal-studio-dfw-light.svg) · [PNG](https://brand.atlocal.ai/studio/atlocal-studio-dfw-light.png) | [SVG](https://brand.atlocal.ai/studio/atlocal-studio-dfw-dark.svg) · [PNG](https://brand.atlocal.ai/studio/atlocal-studio-dfw-dark.png) |
| LIT | Little Rock (Central Arkansas) | [SVG](https://brand.atlocal.ai/studio/atlocal-studio-lit-light.svg) · [PNG](https://brand.atlocal.ai/studio/atlocal-studio-lit-light.png) | [SVG](https://brand.atlocal.ai/studio/atlocal-studio-lit-dark.svg) · [PNG](https://brand.atlocal.ai/studio/atlocal-studio-lit-dark.png) |
| NWA | Northwest Arkansas | [SVG](https://brand.atlocal.ai/studio/atlocal-studio-nwa-light.svg) · [PNG](https://brand.atlocal.ai/studio/atlocal-studio-nwa-light.png) | [SVG](https://brand.atlocal.ai/studio/atlocal-studio-nwa-dark.svg) · [PNG](https://brand.atlocal.ai/studio/atlocal-studio-nwa-dark.png) |

- Market codes favour the **airport code** people already know (DFW, LIT). Where a region is better known by another abbreviation, use that (NWA).
- In running text, write the studio name in full ("atLocal Dallas-Fort Worth") or as "atLocal DFW".
- For a studio that isn't listed, ask Heath for its code and lockup. Don't type a code next to the logo yourself.

### How the logo is built (for reference, not for rebuilding)

- The pin comes first, then the wordmark.
- The brackets are taller than every letter in "local".
- The pin is as tall as the brackets: its top sits on the bracket top.
- The shadow's lower edge sits on the bracket bottom, and the pin's point lands in the middle of the shadow.

## Not defined yet

The brand does not define these yet. **Ask Heath. Do not invent them**, and don't copy them from a website.

- Logo clear space and minimum size
- A stacked (two-line) logo and a wordmark-only logo without the pin
- Logo misuse (a "don't" list) beyond the rules above
- How much of each color to use in a layout (proportions), and what a button looks like on a Plum background. Where each color goes is defined under [Color roles](#color-roles).
- Type sizes and hierarchy for documents and slides. (`atlocal.css` has a web type scale for the websites. It is not a document standard.)
- Print values (Pantone, CMYK) for the colors
- Photography and image treatment: **TBD**
- Icons and graphic elements beyond the pin
- Voice and tone beyond the tagline and supporting line
- Presentation layouts: a Slides master is coming (see the Google Drive "atLocal Brand System" folder when it exists)

## For AI tools

- Fetch this file fresh when you start a branded task; don't rely on memory of an older version. The earlier atLocal brand (an @ logo, Midnight / Ruby Drive / Blush colors, Poppins and Yeseva One) is retired.
- In your answer, name which logo file and which colors you used, so a human can check.
- If you can't fetch a logo file, leave a clearly labeled placeholder ("atLocal logo here") rather than approximating it.
