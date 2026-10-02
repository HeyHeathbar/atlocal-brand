#!/usr/bin/env python3
"""Builds every atLocal logo file from the font and the pin geometry.

    pip install fonttools uharfbuzz
    python3 scripts/build_logos.py        # writes SVGs into logo/ symbol/ icon/ studio/
    for f in logo/*.svg symbol/*.svg icon/*.svg studio/*.svg; do
      rsvg-convert -z 4 "$f" -o "${f%.svg}.png"; done

The wordmark is outlined from Plus Jakarta Sans (fonts/, SIL OFL): ExtraBold
for the letters, SemiBold for the brackets. Nothing in the output depends on
the font being installed.

Construction (S = type size):
  - brackets are set at 1.22 x S from the same baseline, so they stand above
    every letter in "local"
  - tracking is -S/30 on every character
  - pin top sits on the bracket top
  - the shadow's lower edge sits on the bracket bottom and the pin's point
    lands in the middle of the shadow
  - the pin's right edge is 0.165 x S left of the wordmark's origin
"""
import re
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "fonts" / "PlusJakartaSans[wght].ttf"

PLUM, ROYAL, CORAL, RUBY, CLOUD, WHITE, BLACK = (
    "#21134F", "#3B20AB", "#FF7D80", "#E14565", "#F4F1FB", "#FFFFFF", "#000000")

S = 100.0                 # type size in SVG units
BRACKET = 1.22            # bracket size relative to S
TRACK = -S / 30           # tracking per character
PIN_GAP = 0.165 * S       # pin's right edge to the wordmark origin
SHADOW_RY = 0.04 * S
PAD = 0.12 * S            # margin around the artwork inside the viewBox

# Pin, drawn on a 196 x 258 box whose top-left is (52, 70).
PIN_BOX = (52.0, 70.0, 196.0, 258.0)
PIN_PATHS = [
    "M242.09 201.52A98 98 0 1 0 65.13 217.00L111.03 190.50A45 45 0 1 1 192.29 183.39A26.5 26.5 0 0 0 242.09 201.52Z",
    "M57.24 194.60L65.13 217.00L143.5 316.5Q152 328 160.5 316.5C177 294 203 268 203 252Q203 236 190 226L168.30 209.11A45 45 0 0 1 106.74 180.40Z",
]
PIN_DOT = (150.0, 168.0, 21.0)
PIN_TIP_X = 152.0


class Face:
    def __init__(self, weight):
        self.tt = instantiateVariableFont(TTFont(FONT), {"wght": weight})
        self.glyphs = self.tt.getGlyphSet()
        self.upm = self.tt["head"].unitsPerEm
        tmp = ROOT / f".face-{weight}.ttf"
        self.tt.save(tmp)
        self.hb = hb.Font(hb.Face(tmp.read_bytes()))
        tmp.unlink()

    def shape(self, text):
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hb, buf, {"kern": True, "liga": False})
        order = self.tt.getGlyphOrder()
        return [(order[i.codepoint], p.x_advance) for i, p in zip(buf.glyph_infos, buf.glyph_positions)]

    def bounds(self, glyph):
        pen = BoundsPen(self.glyphs)
        self.glyphs[glyph].draw(pen)
        return pen.bounds


BOLD, SEMI = Face(800), Face(600)


def fmt(n):
    return f"{n:.2f}".rstrip("0").rstrip(".")


def round_path(d):
    return re.sub(r"-?\d+\.\d+", lambda m: fmt(float(m.group())), d)


def set_run(face, text, size, x, baseline, tracking):
    """Outline a run of text. Returns (path data, x after the run)."""
    k = size / face.upm
    pen = SVGPathPen(face.glyphs)
    for glyph, advance in face.shape(text):
        face.glyphs[glyph].draw(TransformPen(pen, (k, 0, 0, -k, x, baseline)))
        x += advance * k + tracking
    return round_path(pen.getCommands()), x


def scale_pin_path(d, k, dx, dy):
    """Uniformly scale and move a path made of absolute M L Q C A Z commands."""
    out = []
    for cmd, args in re.findall(r"([MLQCAZ])([^MLQCAZ]*)", d):
        nums = [float(n) for n in re.findall(r"-?\d+\.?\d*", args)]
        if cmd == "A":
            for i in range(0, len(nums), 7):
                rx, ry, rot, large, sweep, x, y = nums[i:i + 7]
                out.append(f"A{fmt(rx * k)} {fmt(ry * k)} {fmt(rot)} {int(large)} {int(sweep)} {fmt(x * k + dx)} {fmt(y * k + dy)}")
        elif cmd == "Z":
            out.append("Z")
        else:
            pts = " ".join(f"{fmt(nums[i] * k + dx)} {fmt(nums[i + 1] * k + dy)}" for i in range(0, len(nums), 2))
            out.append(cmd + pts)
    return "".join(out)


def pin(x, top, height, fill):
    """The pin as SVG elements, fitted to a box with its top-left at (x, top)."""
    bx, by, bw, bh = PIN_BOX
    k = height / bh
    dx, dy = x - bx * k, top - by * k
    body = "".join(f'<path d="{scale_pin_path(p, k, dx, dy)}"/>' for p in PIN_PATHS)
    cx, cy, r = PIN_DOT
    dot = f'<circle cx="{fmt(cx * k + dx)}" cy="{fmt(cy * k + dy)}" r="{fmt(r * k)}"/>'
    return f'<g fill="{fill}">{body}{dot}</g>', bw * k, PIN_TIP_X * k + dx


def bracket_extent(baseline, size=S):
    _, y_min, _, y_max = SEMI.bounds("bracketleft")
    k = size * BRACKET / SEMI.upm
    return baseline - y_max * k, baseline - y_min * k


def svg(width, height, x0, y0, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(x0)} {fmt(y0)} {fmt(width)} {fmt(height)}" '
            f'width="{fmt(width * 2)}" height="{fmt(height * 2)}" role="img"><title>{title}</title>{body}</svg>\n')


def logo(main, accent, shadow, title, studio=None):
    """Pin, then at[local]. `studio` adds a divider and a city name."""
    baseline, tx = 0.0, 0.0
    top, bottom = bracket_extent(baseline)
    cy = bottom - SHADOW_RY
    pin_h = cy - top
    pin_w = pin_h * PIN_BOX[2] / PIN_BOX[3]
    px = tx - PIN_GAP - pin_w
    pin_svg, _, tip_x = pin(px, top, pin_h, main)

    x = tx
    d_at, x = set_run(BOLD, "at", S, x, baseline, TRACK)
    d_open, x = set_run(SEMI, "[", S * BRACKET, x, baseline, TRACK)
    d_local, x = set_run(BOLD, "local", S, x, baseline, TRACK)
    d_close, x = set_run(SEMI, "]", S * BRACKET, x, baseline, TRACK)
    right = x - TRACK

    body = ""
    if shadow:
        body += f'<ellipse cx="{fmt(tip_x)}" cy="{fmt(cy)}" rx="{fmt(pin_w * 0.3)}" ry="{fmt(SHADOW_RY)}" fill="{shadow}"/>'
    body += pin_svg
    body += f'<path d="{d_at}{d_open}{d_close}" fill="{accent}"/><path d="{d_local}" fill="{main}"/>'

    if studio:
        gap = 0.22 * S
        rule_x = right + gap
        body += f'<rect x="{fmt(rule_x)}" y="{fmt(top + 0.08 * S)}" width="{fmt(0.02 * S)}" height="{fmt(bottom - top - 0.16 * S)}" fill="{accent}"/>'
        size = 0.26 * S
        cap = SEMI.bounds("H")[3] * size / SEMI.upm
        d_city, end = set_run(SEMI, studio.upper(), size, rule_x + 0.02 * S + gap, (top + bottom) / 2 + cap / 2, 0.14 * size)
        body += f'<path d="{d_city}" fill="{main}"/>'
        right = end - 0.14 * size

    x0, y0 = px - PAD, top - PAD
    return svg(right + PAD - x0, bottom + PAD - y0, x0, y0, title, body)


def symbol(main, shadow, title):
    height = 258.0 * (S * 1.6 / 258.0)
    cy = height
    pin_svg, pin_w, tip_x = pin(0, 0, height, main)
    body = ""
    bottom = height
    if shadow:
        ry = height * 0.028
        body += f'<ellipse cx="{fmt(tip_x)}" cy="{fmt(cy)}" rx="{fmt(pin_w * 0.3)}" ry="{fmt(ry)}" fill="{shadow}"/>'
        bottom += ry
    body += pin_svg
    return svg(pin_w + 2 * PAD, bottom + 2 * PAD, -PAD, -PAD, title, body)


def app_icon(tile, main, shadow, title):
    size, radius = 512.0, 512.0 * 0.225
    height = size * 0.56
    ry = height * 0.028
    pin_w = height * PIN_BOX[2] / PIN_BOX[3]
    top = (size - height - ry) / 2
    pin_svg, _, tip_x = pin((size - pin_w) / 2, top, height, main)
    body = f'<rect width="{fmt(size)}" height="{fmt(size)}" rx="{fmt(radius)}" fill="{tile}"/>'
    body += f'<ellipse cx="{fmt(tip_x)}" cy="{fmt(top + height)}" rx="{fmt(pin_w * 0.3)}" ry="{fmt(ry)}" fill="{shadow}"/>'
    body += pin_svg
    return svg(size, size, 0, 0, title, body)


def write(path, content):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content)
    print("wrote", path)


def main():
    write("logo/atlocal-logo-light.svg", logo(PLUM, RUBY, RUBY, "atLocal logo, for light backgrounds"))
    write("logo/atlocal-logo-dark.svg", logo(WHITE, RUBY, RUBY, "atLocal logo, for dark backgrounds"))
    write("logo/atlocal-logo-black.svg", logo(BLACK, BLACK, None, "atLocal logo, one colour black"))
    write("logo/atlocal-logo-white.svg", logo(WHITE, WHITE, None, "atLocal logo, one colour white"))

    write("symbol/atlocal-pin-light.svg", symbol(PLUM, RUBY, "atLocal pin, for light backgrounds"))
    write("symbol/atlocal-pin-dark.svg", symbol(WHITE, RUBY, "atLocal pin, for dark backgrounds"))
    write("symbol/atlocal-pin-black.svg", symbol(BLACK, None, "atLocal pin, one colour black"))
    write("symbol/atlocal-pin-white.svg", symbol(WHITE, None, "atLocal pin, one colour white"))

    write("icon/atlocal-app-icon-plum.svg", app_icon(PLUM, WHITE, RUBY, "atLocal app icon on Plum"))
    write("icon/atlocal-app-icon-white.svg", app_icon(WHITE, PLUM, RUBY, "atLocal app icon on white"))

    for city in ("Central Arkansas", "Dallas", "Northwest Arkansas"):
        slug = city.lower().replace(" ", "-")
        write(f"studio/atlocal-studio-{slug}-light.svg", logo(PLUM, RUBY, RUBY, f"atLocal {city}, for light backgrounds", studio=city))
        write(f"studio/atlocal-studio-{slug}-dark.svg", logo(WHITE, RUBY, RUBY, f"atLocal {city}, for dark backgrounds", studio=city))


if __name__ == "__main__":
    main()
