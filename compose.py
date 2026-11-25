#!/usr/bin/env python3
"""Draw the Wednesday 25 November 2026 front page. Deterministic: no clock,
no randomness, no network. Fails loudly on any text overflow."""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stories as S

W = H = 1024
CREAM = (244, 238, 220)
INK = (22, 20, 18)
NAVY = (16, 28, 64)
RED = (168, 32, 40)
GREY = (96, 90, 82)
RULE = (120, 110, 95)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

_cache = {}


def fnt(path, size):
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]


def wrap(text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if font.getlength(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, font, fill, width, max_lines, leading):
    lines = wrap(text, font, width)
    if len(lines) > max_lines:
        raise ValueError("overflow: %r needs %d lines, max %d" % (text, len(lines), max_lines))
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def centre(d, cx, y, text, font, fill):
    d.text((cx - font.getlength(text) / 2, y), text, font=font, fill=fill)


def badge(d, x, y, num, r=9):
    d.ellipse([x - r, y - r, x + r, y + r], fill=RED, outline=(255, 255, 255), width=1)
    t = str(num)
    bf = fnt(SANS_B, 11)
    d.text((x - bf.getlength(t) / 2, y - 6), t, font=bf, fill=(255, 255, 255))


def art(d, box, kind):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    bg = {
        "rocket": (18, 34, 74), "treaty": (232, 222, 196), "blast": (214, 110, 32),
        "refinery": (52, 44, 66), "tariff": (24, 52, 96), "turkey": (122, 74, 40),
        "gaza": (110, 108, 100), "sorry": (14, 96, 96), "hack": (16, 20, 26),
        "oilfield": (196, 158, 92), "trophy": (30, 110, 60), "football": (36, 128, 64),
        "plane": (140, 190, 220),
    }[kind]
    d.rectangle(box, fill=bg)
    if kind == "rocket":
        for sx, sy in [(x0 + 14, y0 + 10), (x1 - 18, y0 + 22), (x0 + 40, y0 + 6), (x1 - 40, y1 - 12)]:
            d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
        # Earth limb along the bottom of the panel
        limb = [(x, y1 - 4 - int(20 * math.sin(math.pi * (x - x0) / w)))
                for x in range(x0, x1 + 1, 10)]
        d.polygon([(x0, y1)] + limb + [(x1, y1)], fill=(52, 110, 180))
        d.line(limb, fill=(140, 190, 235), width=2)
        # Tiangong module with solar wings, top right
        d.rounded_rectangle([cx + 52, y0 + 22, x1 - 16, y0 + 44], radius=8,
                            fill=(225, 228, 232), outline=INK)
        d.rectangle([cx + 58, y0 + 10, cx + 98, y0 + 20], fill=(28, 58, 150))
        d.rectangle([cx + 58, y0 + 46, cx + 98, y0 + 56], fill=(28, 58, 150))
        for wx in (cx + 66, cx + 84, cx + 102):
            d.ellipse([wx - 3, y0 + 29, wx + 3, y0 + 35], fill=(120, 180, 220))
        # Docking arm from the rocket nose to the module
        d.line([(cx + 8, cy - 38), (cx + 52, y0 + 33)], fill=(200, 200, 205), width=4)
        d.ellipse([cx + 48, y0 + 29, cx + 56, y0 + 37], fill=(255, 255, 255), outline=INK)
        # Rocket, enlarged to fill the panel
        d.polygon([(cx - 24, y1 - 26), (cx - 24, cy - 6), (cx, cy - 52), (cx + 24, cy - 6),
                   (cx + 24, y1 - 26)], fill=(240, 240, 235))
        d.polygon([(cx - 24, cy - 6), (cx - 40, cy + 14), (cx - 24, cy + 10)], fill=RED)
        d.polygon([(cx + 24, cy - 6), (cx + 40, cy + 14), (cx + 24, cy + 10)], fill=RED)
        d.polygon([(cx - 11, y1 - 26), (cx, y1 - 2), (cx + 11, y1 - 26)], fill=(255, 180, 40))
        d.polygon([(cx - 5, y1 - 26), (cx, y1 - 10), (cx + 5, y1 - 26)], fill=(255, 220, 90))
        d.ellipse([cx - 8, cy - 34, cx + 8, cy - 18], fill=(120, 180, 220), outline=INK)
    elif kind == "treaty":
        d.rectangle([x0 + 10, y0 + 8, cx - 4, y0 + h - 14], fill=(30, 60, 140))
        d.rectangle([cx + 4, y0 + 8, x1 - 10, y0 + h - 14], fill=(0, 90, 60))
        for fy in (y0 + 16, y0 + 26, y0 + 36):
            d.ellipse([x0 + 16, fy, x0 + 20, fy + 4], fill=(255, 255, 255))
        d.ellipse([cx + 12, y0 + 16, cx + 18, y0 + 22], fill=(255, 220, 0))
        d.rectangle([x0 + w // 4, y1 - 26, x1 - w // 4, y1 - 8], fill=(255, 255, 255), outline=INK)
        d.line([x0 + w // 4 + 6, y1 - 18, x1 - w // 4 - 6, y1 - 18], fill=INK, width=1)
        d.line([x0 + w // 4 + 6, y1 - 13, x0 + w // 2, y1 - 13], fill=INK, width=1)
    elif kind == "blast":
        for bx in (x0 + 12, x0 + 34, x0 + 56):
            d.rectangle([bx, y1 - 34, bx + 18, y1 - 10], fill=(90, 90, 96), outline=(40, 40, 44))
            d.line([bx, y1 - 26, bx + 18, y1 - 26], fill=(40, 40, 44), width=1)
        d.polygon([(cx, y0 + 4), (cx + 8, y0 + 18), (cx + 22, y0 + 14), (cx + 12, y0 + 26),
                   (cx + 20, y0 + 38), (cx + 4, y0 + 34), (cx, y0 + 46), (cx - 4, y0 + 34),
                   (cx - 20, y0 + 38), (cx - 12, y0 + 26), (cx - 22, y0 + 14), (cx - 8, y0 + 18)],
                  fill=(255, 210, 60))
        d.ellipse([x0 + 8, y0 + 6, x0 + 30, y0 + 22], fill=(230, 220, 210))
        d.ellipse([x1 - 34, y0 + 10, x1 - 12, y0 + 26], fill=(230, 220, 210))
    elif kind == "refinery":
        for tx, th in [(x0 + 12, 30), (x0 + 40, 44), (x0 + 72, 36)]:
            d.rectangle([tx, y1 - th, tx + 16, y1 - 8], fill=(200, 200, 205))
            d.polygon([(tx + 2, y1 - th), (tx + 8, y1 - th - 12), (tx + 14, y1 - th)], fill=(255, 150, 40))
        d.rectangle([x0 + 96, y1 - 24, x1 - 10, y1 - 8], fill=(160, 160, 165))
        d.ellipse([x1 - 40, y0 + 8, x1 - 16, y0 + 32], fill=(255, 190, 80))
    elif kind == "tariff":
        d.rectangle([cx - 26, y0 + 8, cx + 26, y1 - 8], fill=(255, 255, 255), outline=INK)
        d.text((cx - 16, y0 + 12), "%", font=fnt(SANS_B, 26), fill=RED)
        d.line([cx - 20, y1 - 18, cx + 20, y1 - 18], fill=INK, width=1)
        d.line([cx - 20, y1 - 13, cx + 2, y1 - 13], fill=INK, width=1)
    elif kind == "turkey":
        for a in range(-50, 51, 25):
            d.arc([cx - 34, y0 + 2, cx + 34, y0 + 52], a - 160, a - 110, fill=(200, 120, 40), width=5)
        d.ellipse([cx - 16, cy - 6, cx + 16, cy + 22], fill=(90, 50, 26))
        d.ellipse([cx - 7, cy - 20, cx + 7, cy - 6], fill=(90, 50, 26))
        d.polygon([(cx + 7, cy - 14), (cx + 16, cy - 12), (cx + 7, cy - 9)], fill=(255, 200, 60))
    elif kind == "gaza":
        for bx, bh in [(x0 + 10, 34), (x0 + 34, 48), (x0 + 62, 28)]:
            d.rectangle([bx, y1 - bh, bx + 20, y1 - 8], fill=(70, 70, 74))
            d.rectangle([bx + 5, y1 - bh + 6, bx + 9, y1 - bh + 10], fill=(255, 220, 120))
            d.rectangle([bx + 12, y1 - bh + 6, bx + 16, y1 - bh + 10], fill=(255, 220, 120))
        d.ellipse([x0 + 12, y0 + 4, x0 + 34, y0 + 20], fill=(210, 205, 195))
        d.ellipse([x0 + 28, y0 + 10, x0 + 48, y0 + 26], fill=(210, 205, 195))
    elif kind == "sorry":
        d.polygon([(cx - 22, y0 + 10), (cx, y0 + 22), (cx + 22, y0 + 10), (cx + 22, y0 + 30),
                   (cx, y0 + 18), (cx - 22, y0 + 30)], fill=(255, 220, 90))
        d.ellipse([cx - 16, cy + 2, cx + 16, cy + 26], fill=(220, 60, 80))
        d.polygon([(cx - 16, cy + 10), (cx, cy + 26), (cx + 16, cy + 10)], fill=(220, 60, 80))
    elif kind == "hack":
        d.rectangle([cx - 30, y0 + 10, cx + 30, y0 + h - 20], fill=(40, 52, 66), outline=(120, 200, 160))
        for i, ln in enumerate(["0101 1100", "1010 0011", "1100 0101"]):
            d.text((cx - 26, y0 + 14 + i * 9), ln, font=fnt(SANS, 7), fill=(120, 220, 160))
        d.polygon([(cx + 22, y1 - 12), (cx + 34, y1 - 12), (cx + 28, y1 - 2)], fill=(255, 200, 40))
        d.text((cx + 25, y1 - 11), "!", font=fnt(SANS_B, 8), fill=INK)
    elif kind == "oilfield":
        d.line([x0 + 10, y1 - 10, cx + 10, y0 + 12], fill=(60, 40, 20), width=3)
        d.line([cx - 24, y0 + 12, cx + 26, y0 + 12], fill=(60, 40, 20), width=3)
        d.line([cx + 22, y0 + 12, cx + 16, y1 - 22], fill=(60, 40, 20), width=2)
        d.ellipse([x0 + 8, y1 - 16, x0 + 22, y1 - 4], fill=(40, 40, 44))
        d.rectangle([x1 - 34, y1 - 26, x1 - 12, y1 - 8], fill=(120, 120, 125))
    elif kind == "trophy":
        d.polygon([(cx - 14, y0 + 10), (cx + 14, y0 + 10), (cx + 10, y0 + 30), (cx - 10, y0 + 30)],
                  fill=(255, 205, 40))
        d.arc([cx - 24, y0 + 8, cx - 8, y0 + 28], 90, 270, fill=(255, 205, 40), width=4)
        d.arc([cx + 8, y0 + 8, cx + 24, y0 + 28], -90, 90, fill=(255, 205, 40), width=4)
        d.rectangle([cx - 3, y0 + 30, cx + 3, y0 + 42], fill=(255, 205, 40))
        d.rectangle([cx - 12, y0 + 42, cx + 12, y0 + 47], fill=(255, 205, 40))
        d.text((cx - 5, y1 - 12), "1", font=fnt(SANS_B, 10), fill=(255, 255, 255))
    elif kind == "football":
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(255, 255, 255), outline=INK)
        d.polygon([(cx, cy - 7), (cx + 7, cy - 2), (cx + 4, cy + 6), (cx - 4, cy + 6), (cx - 7, cy - 2)],
                  fill=INK)
        d.rectangle([x0 + 8, y0 + 8, x0 + 30, y1 - 8], fill=(255, 255, 255), outline=INK)
        for gy in range(y0 + 12, y1 - 8, 8):
            d.line([x0 + 8, gy, x0 + 30, gy], fill=(180, 180, 180), width=1)
    elif kind == "plane":
        for ox, oy in [(x0 + 12, y0 + 8), (x1 - 30, y0 + 16), (x0 + 30, y1 - 14)]:
            d.ellipse([ox, oy, ox + 18, oy + 7], fill=(255, 255, 255))
        d.polygon([(x0 + 8, cy), (x0 + 30, cy - 8), (x1 - 22, cy - 8), (x1 - 8, cy - 2),
                   (x1 - 22, cy + 2), (x0 + 30, cy + 6)], fill=(40, 44, 52))
        d.polygon([(cx - 6, cy - 8), (cx + 2, cy - 22), (cx + 8, cy - 8)], fill=(40, 44, 52))


def render():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    # Top bar
    d.rectangle([0, 0, W, 24], fill=NAVY)
    d.text((16, 5), "ONE DAY, EVERYWHERE", font=fnt(SANS_B, 11), fill=(255, 255, 255))
    rb = "WEDNESDAY EDITION  •  No. 329"
    d.text((W - 16 - fnt(SANS_B, 11).getlength(rb), 5), rb, font=fnt(SANS_B, 11), fill=(255, 255, 255))
    # Masthead
    centre(d, W // 2, 30, S.MASTHEAD, fnt(SERIF_B, 52), INK)
    d.line([16, 86, W - 16, 86], fill=RULE, width=1)
    centre(d, W // 2, 90, S.SUBHEAD, fnt(SERIF, 14), INK)
    centre(d, W // 2, 110, S.COUNT_STRIP, fnt(SANS_B, 13), RED)
    d.line([16, 128, W - 16, 128], fill=RULE, width=1)
    # Numbers strip: 6 cells
    cw = (W - 32) // 6
    for i, (val, lab) in enumerate(S.NUMBERS):
        x = 16 + i * cw
        centre(d, x + cw // 2, 134, val, fnt(SERIF_B, 20), RED)
        centre(d, x + cw // 2, 158, lab, fnt(SANS, 9), INK)
        if i:
            d.line([x, 132, x, 172], fill=RULE, width=1)
    d.line([16, 176, W - 16, 176], fill=RULE, width=1)
    # Region bar, proportional
    total = sum(n for _, n, _ in S.REGIONS)
    x = 16
    for name, n, col in S.REGIONS:
        seg = int((W - 32) * n / total)
        d.rectangle([x, 182, x + seg, 200], fill=col)
        lab = "%s %d" % (name, n)
        lf = fnt(SANS_B, 9)
        if lf.getlength(lab) >= seg - 6:
            lf = fnt(SANS_B, 8)
        if lf.getlength(lab) < seg - 6:
            d.text((x + 4, 187), lab, font=lf, fill=(255, 255, 255))
        x += seg
    # Wednesday Wire dropped in fix pass 1 (chronology unverifiable); splash kept.
    # Splash: hero 1 full width
    y = 208
    d.rectangle([16, y, W - 16, y + 140], outline=INK, width=1)
    art(d, (17, y + 1, 377, y + 139), S.BIG[0][5])
    badge(d, 360, y + 16, 1)
    d.text((392, y + 8), S.BIG[0][1], font=fnt(SANS_B, 11), fill=RED)
    para(d, 392, y + 26, S.BIG[0][2], fnt(SERIF_B, 20), INK, W - 16 - 392 - 8, 2, 24)
    para(d, 392, y + 78, S.BIG[0][3], fnt(SANS, 11), INK, W - 16 - 392 - 8, 3, 13)
    d.text((392, y + 126), S.BIG[0][4], font=fnt(SANS, 8), fill=GREY)
    # Heroes 2-3, half width each
    y = 356
    hw = (W - 32 - 8) // 2
    for j, hero in enumerate(S.BIG[1:]):
        bx = 16 + j * (hw + 8)
        d.rectangle([bx, y, bx + hw, y + 128], outline=INK, width=1)
        art(d, (bx + 1, y + 1, bx + hw - 1, y + 60), hero[5])
        badge(d, bx + hw - 16, y + 16, hero[0])
        d.text((bx + 8, y + 65), hero[1], font=fnt(SANS_B, 9), fill=RED)
        para(d, bx + 8, y + 77, hero[2], fnt(SERIF_B, 13), INK, hw - 16, 2, 15)
    # Decks for heroes 2-3 drawn below headlines: recompute positions
    for j, hero in enumerate(S.BIG[1:]):
        bx = 16 + j * (hw + 8)
        hl = wrap(hero[2], fnt(SERIF_B, 13), hw - 16)
        dy = y + 77 + len(hl) * 15
        para(d, bx + 8, dy, hero[3], fnt(SANS, 9), INK, hw - 16, 1, 11)
        d.text((bx + 8, y + 116), hero[4], font=fnt(SANS, 7), fill=GREY)
    # Small leads: 5 x 2
    y0 = 492
    sw = (W - 32 - 4 * 8) // 5
    sh = 118
    for i, lead in enumerate(S.SMALL):
        r, c = divmod(i, 5)
        bx = 16 + c * (sw + 8)
        by = y0 + r * (sh + 8)
        d.rectangle([bx, by, bx + sw, by + sh], outline=INK, width=1)
        art(d, (bx + 1, by + 1, bx + sw - 1, by + 36), lead[5])
        badge(d, bx + sw - 14, by + 14, lead[0], r=8)
        d.text((bx + 6, by + 40), lead[1], font=fnt(SANS_B, 8), fill=RED)
        para(d, bx + 6, by + 52, lead[2], fnt(SERIF_B, 11), INK, sw - 12, 3, 12)
        hl = wrap(lead[2], fnt(SERIF_B, 11), sw - 12)
        dy = by + 52 + len(hl) * 12
        para(d, bx + 6, dy, lead[3], fnt(SANS, 8), INK, sw - 12, 2, 10)
    # Map dropped in fix pass 1 (no true continent outlines at this size);
    # the space goes to the lead tier and the briefs.
    # Briefs, two columns
    by = 744
    d.text((16, by), "THE REST OF THE DAY", font=fnt(SANS_B, 11), fill=RED)
    d.line([16, by + 15, W - 16, by + 15], fill=RULE, width=1)
    bf = fnt(SANS, 7)
    colw = (W - 32 - 16) // 2
    for i, b in enumerate(S.BRIEFS):
        col, row = divmod(i, 16)
        bx = 16 + col * (colw + 16)
        yy = by + 20 + row * 8
        d.text((bx, yy), "%d. %s" % (i + 1, b), font=bf, fill=INK)
    # DATE CHECK
    dy = 900
    d.rectangle([16, dy, W - 16, dy + 58], outline=RED, width=2)
    d.text((24, dy + 4), "DATE CHECK  —  NOT 25 NOVEMBER NEWS", font=fnt(SANS_B, 10), fill=RED)
    dcf = fnt(SANS, 8)
    for i, (what, when) in enumerate(S.DATE_CHECK):
        col, row = divmod(i, 4)
        bx = 24 + col * ((W - 48) // 2)
        yy = dy + 20 + row * 9
        d.text((bx, yy), "X  %s  —  %s" % (what, when), font=dcf, fill=INK)
    # Footer
    fy = 966
    d.line([16, fy, W - 16, fy], fill=RULE, width=1)
    para(d, 16, fy + 5, S.FOOTER_DATE, fnt(SANS_B, 9), INK, W - 32, 1, 11)
    para(d, 16, fy + 17, S.SOURCES, fnt(SANS, 8), GREY, W - 32, 1, 10)
    return img


def main():
    out = Path(__file__).resolve().parent / "entry.png"
    render().save(out, format="PNG", optimize=True)
    print("wrote %s (%d bytes)" % (out, out.stat().st_size))


if __name__ == "__main__":
    main()
