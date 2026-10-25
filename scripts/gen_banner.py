#!/usr/bin/env python3
"""Gera os assets visuais do README: assets/banner.svg (animado) e assets/divider.svg.

Uso:
  python3 scripts/gen_banner.py                          # (re)gera os dois arquivos em assets/
  python3 scripts/gen_banner.py --frame 2.5 --out f.svg  # "congela" a animação no tempo T (s), só p/ preview

Tudo é desenhado com <rect>/<path> e uma fonte em pixel própria, sem fontes nem imagens
externas: o GitHub exibe o SVG como imagem, e nesse modo ele não pode carregar nada de fora.
Para mudar textos ou cores, edite o bloco "conteúdo" logo abaixo e rode o script de novo.
"""
import argparse
from pathlib import Path

# ---- conteúdo (troque à vontade) ----
WORDMARK = "RAFAFRD"
PHRASES = ["DEVSECOPS & PURPLE TEAM", "APPSEC // VULN MANAGEMENT", "SEGURANÇA DESDE A FUNDAÇÃO"]
LABEL_TL, LABEL_TR, LABEL_BR = "[ WHOAMI ]", "SP // BR", "BUILD > BREAK > FIX"
INK, PAPER, GRAY = "#0b0b0c", "#f2f2f2", "#6b6b6b"
VIOLET, VIOLET_L = "#7E30E1", "#A36BFF"

W, H = 1200, 400
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]

# Fonte bitmap 5x7 (só os caracteres usados). Acentos ficam em linhas extras acima/abaixo.
FONT = {
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "C": [".###.", "#...#", "#....", "#....", "#....", "#...#", ".###."],
    "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
    "G": [".###.", "#...#", "#....", "#.###", "#...#", "#...#", ".####"],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": [".###.", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "M": ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"],
    "N": ["#...#", "#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "V": ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "#.#.#", ".#.#."],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
    "&": [".##..", "#..#.", "#.#..", ".#...", "#.#.#", "#..#.", ".##.#"],
    "/": ["....#", "....#", "...#.", "..#..", ".#...", "#....", "#...."],
    "[": [".###.", ".#...", ".#...", ".#...", ".#...", ".#...", ".###."],
    "]": [".###.", "...#.", "...#.", "...#.", "...#.", "...#.", ".###."],
    ">": [".#...", "..#..", "...#.", "....#", "...#.", "..#..", ".#..."],
    " ": ["....."] * 7,
}
# letra base, linhas acima (de cima p/ baixo, a última encosta numa linha vazia), linhas abaixo
ACCENTS = {
    "Ã": ("A", [".##.#", "#..#.", "....."], []),
    "Ç": ("C", [], ["..#..", ".##.."]),
}
for ch, rows in FONT.items():
    assert len(rows) == 7 and all(len(r) == 5 for r in rows), ch


def f(v):
    if isinstance(v, float):
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        return s if s not in ("-0", "") else "0"
    return str(v)


def glyph_rows(ch):
    """Devolve [(y, linha)] incluindo acentos (y negativo = acima da letra, y >= 7 = abaixo)."""
    if ch in ACCENTS:
        base, above, below = ACCENTS[ch]
        rows = [(i - len(above), r) for i, r in enumerate(above)]
        rows += list(enumerate(FONT[base]))
        rows += [(7 + i, r) for i, r in enumerate(below)]
        return rows
    return list(enumerate(FONT[ch]))


def text_cells(text, bold=False, spacing=1):
    cells, cx = set(), 0
    gw = 5 + (1 if bold else 0)
    for ch in text:
        for y, row in glyph_rows(ch):
            for x, c in enumerate(row):
                if c == "#":
                    cells.add((cx + x, y))
                    if bold:  # negrito "falso": duplica cada pixel para a direita
                        cells.add((cx + x + 1, y))
        cx += gw + spacing
    return cells, cx - spacing


def cells_path(cells, s, ox, oy, grow=0, rows=None):
    """Converte pixels num único path, juntando pixels vizinhos da mesma linha em retângulos."""
    by_row = {}
    for x, y in cells:
        if rows is None or y in rows:
            by_row.setdefault(y, []).append(x)
    out = []
    for y in sorted(by_row):
        xs = sorted(by_row[y])
        runs, start, prev = [], xs[0], xs[0]
        for x in xs[1:]:
            if x == prev + 1:
                prev = x
            else:
                runs.append((start, prev))
                start = prev = x
        runs.append((start, prev))
        for a, b in runs:
            X, Y = ox + a * s - grow, oy + y * s - grow
            w, h = (b - a + 1) * s + 2 * grow, s + 2 * grow
            out.append(f"M{f(X)} {f(Y)}h{f(w)}v{f(h)}h{f(-w)}z")
    return "".join(out)


def dot_pattern(pid, k, cell, color):
    rects = "".join(
        f'<rect x="{x * cell}" y="{y * cell}" width="{cell}" height="{cell}"/>'
        for y in range(4) for x in range(4) if BAYER[y][x] < k
    )
    return (f'<pattern id="{pid}" width="{4 * cell}" height="{4 * cell}" patternUnits="userSpaceOnUse">'
            f'<g fill="{color}">{rects}</g></pattern>')


# ---- layout ----
S = 15                                    # pixel do wordmark
wm_cells, wm_w = text_cells(WORDMARK, bold=True)
OX, OY = (W - wm_w * S) // 2, 118

S2, ADV2 = 4, 24                          # subtítulo: pixel 4, avanço de 6 pixels por letra
BOX_X, BOX_Y, BOX_W, BOX_H = OX - 12, 262, wm_w * S + 24, 7 * S2 + 32
TX, TY = OX + 2 * ADV2, BOX_Y + 16        # início do texto digitado (depois do prompt ">")
CLIP_Y, CLIP_H = TY - 3 * S2 - 1, 12 * S2 + 2   # cobre acentos acima e cedilha abaixo
for _p in PHRASES:
    assert TX + len(_p) * ADV2 + 16 <= BOX_X + BOX_W, f"frase longa demais: {_p}"
    assert all(c in FONT or c in ACCENTS for c in _p), f"caractere sem glifo em: {_p}"

S3 = 3                                    # rótulos pequenos

# ---- tempos ----
T_TYPE, WIN, START, CH, CLEAR = 13.5, 4.5, 0.35, 0.06, 4.0   # digitação: 3 frases x 4,5 s
GLITCH, SCAN = 6.0, 7.0

# glitch: (percentual, opacidade, dx, dy), avaliado com steps(1,end)
SLICES = [
    dict(y=OY + S * 1 + 3, h=12, color=VIOLET_L, kf=[(0, 0, 0, 0), (88, 1, -18, 0), (90, 1, 14, 0), (92, 1, -6, 0), (94, 0, 0, 0), (100, 0, 0, 0)]),
    dict(y=OY + S * 3 + 5, h=8, color=PAPER, kf=[(0, 0, 0, 0), (89, 1, 22, 0), (91, 1, -10, 0), (93, 1, 4, 0), (95, 0, 0, 0), (100, 0, 0, 0)]),
    dict(y=OY + S * 5 + 2, h=14, color=VIOLET_L, kf=[(0, 0, 0, 0), (88.5, 1, -12, 0), (90.5, 1, 18, 0), (92.5, 1, -4, 0), (94.5, 0, 0, 0), (100, 0, 0, 0)]),
]
JIT = [(0, 1, 0, 0), (88, 1, 5, 0), (89.5, 1, -4, 2), (91, 1, 2, -1), (93, 1, 0, 0), (100, 1, 0, 0)]
TEAR = [(0, 0, 0, 0), (89, 0.9, 0, 0), (90, 0, 0, 0), (91.5, 0.9, 0, 0), (92.5, 0, 0, 0), (100, 0, 0, 0)]


def kf_at(kf, t, dur):
    pct = (t % dur) / dur * 100
    cur = kf[0]
    for k in kf:
        if k[0] <= pct:
            cur = k
    return cur


def css_keyframes(name, kf, with_transform=True):
    parts = []
    for pct, op, dx, dy in kf:
        tr = f";transform:translate({f(float(dx))}px,{f(float(dy))}px)" if with_transform else ""
        parts.append(f"{f(float(pct))}%{{opacity:{f(float(op))}{tr}}}")
    return f"@keyframes {name}{{{''.join(parts)}}}"


def phrase_track(p):
    base, n = p * WIN, len(PHRASES[p])
    pts = [(0.0, 0)]
    pts += [(base + START + (j - 1) * CH, j * ADV2) for j in range(1, n + 1)]
    pts += [(base + CLEAR, 0), (T_TYPE, 0)]
    return pts


def cursor_track():
    pts = [(0.0, TX)]
    for p in range(len(PHRASES)):
        base, n = p * WIN, len(PHRASES[p])
        pts += [(base + START + (j - 1) * CH, TX + j * ADV2) for j in range(1, n + 1)]
        pts.append((base + CLEAR, TX))
    pts.append((T_TYPE, TX))
    return pts


def value_at(pts, t):
    t %= T_TYPE
    cur = pts[0][1]
    for tt, v in pts:
        if tt <= t:
            cur = v
    return cur


def smil(attr, pts):
    kts = [round(t / T_TYPE, 5) for t, _ in pts]
    assert kts[0] == 0 and kts[-1] == 1 and all(a < b for a, b in zip(kts, kts[1:])), "keyTimes inválidos"
    kt_txt = [("%.5f" % k).rstrip("0").rstrip(".") or "0" for k in kts]
    assert len(set(kt_txt)) == len(kt_txt), "keyTimes duplicados depois de formatar"
    vals = ";".join(str(v) for _, v in pts)
    return (f'<animate attributeName="{attr}" dur="{f(T_TYPE)}s" repeatCount="indefinite" calcMode="discrete" '
            f'values="{vals}" keyTimes="{";".join(kt_txt)}"/>')


def label(text, x, y, color=PAPER, box=INK, pad=10):
    cells, w = text_cells(text)
    bw, bh = w * S3 + 2 * pad, 7 * S3 + 2 * pad
    if x < 0:
        x = W + x - bw
    return (f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="{box}"/>'
            f'<path d="{cells_path(cells, S3, x + pad, y + pad)}" fill="{color}"/>')


def build_banner(frame=None):
    baked = frame is not None
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'shape-rendering="crispEdges" role="img" aria-labelledby="t d">',
         f'<title id="t">{WORDMARK} — DevSecOps &amp; Purple Team</title>',
         '<desc id="d">Banner em estilo 1-bit: fundo com dithering, nome em pixel art com hachura e sombra roxa, '
         'efeito de glitch e um subtítulo sendo digitado.</desc>']

    if not baked:
        css = [".gl,.tear{opacity:0}", ".static{display:none}",
               f".jit{{animation:jit {f(GLITCH)}s steps(1,end) infinite}}",
               f".tear{{animation:tear {f(GLITCH)}s steps(1,end) infinite}}",
               f".scan{{animation:scan {f(SCAN)}s linear infinite}}",
               ".cur{animation:blink 1s steps(1,end) infinite}",
               css_keyframes("jit", JIT), css_keyframes("tear", TEAR, with_transform=False),
               "@keyframes scan{from{transform:translateY(-20px)}to{transform:translateY(420px)}}",
               "@keyframes blink{0%{opacity:1}50%{opacity:0}100%{opacity:1}}"]
        for i, sl in enumerate(SLICES):
            css.append(f".gl{i}{{animation:gl{i} {f(GLITCH)}s steps(1,end) infinite}}")
            css.append(css_keyframes(f"gl{i}", sl["kf"]))
        css.append("@media (prefers-reduced-motion: reduce){.jit,.tear,.scan,.cur,.gl{animation:none}"
                   ".gl,.tear,.scan,.typing{display:none}.static{display:inline}}")
        o.append(f"<style>{''.join(css)}</style>")

    # ---- defs ----
    d = ["<defs>"]
    d += [dot_pattern(f"d{k}", k, 6, GRAY) for k in range(1, 16)]
    d.append(dot_pattern("sh4", 4, 3, INK))
    d.append(dot_pattern("sh8", 8, 3, INK))
    d.append(f'<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
             f'<rect width="7" height="7" fill="{PAPER}"/><rect width="2" height="7" fill="{INK}"/></pattern>')
    d.append('<linearGradient id="sg" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{VIOLET_L}" stop-opacity="0"/>'
             f'<stop offset="1" stop-color="{VIOLET_L}" stop-opacity=".22"/></linearGradient>')
    d.append(f'<path id="wmo" d="{cells_path(wm_cells, S, OX, OY, grow=5)}"/>')
    d.append(f'<path id="wmf" d="{cells_path(wm_cells, S, OX, OY)}"/>')
    for i, sl in enumerate(SLICES):
        d.append(f'<clipPath id="c{i}"><rect x="0" y="{sl["y"]}" width="{W}" height="{sl["h"]}"/></clipPath>')
    for p in range(len(PHRASES)):
        if baked:
            wv = value_at(phrase_track(p), frame)
            d.append(f'<clipPath id="tp{p}"><rect x="{TX - 1}" y="{CLIP_Y}" height="{CLIP_H}" width="{wv}"/></clipPath>')
        else:
            d.append(f'<clipPath id="tp{p}"><rect x="{TX - 1}" y="{CLIP_Y}" height="{CLIP_H}" width="0">'
                     f'{smil("width", phrase_track(p))}</rect></clipPath>')
    d.append("</defs>")
    o += d

    # ---- fundo: faixas com dithering de Bayer (claro em cima, preto embaixo) ----
    o.append(f'<rect width="{W}" height="{H}" fill="{INK}"/>')
    for i in range((H + 23) // 24):
        k, y = max(0, 16 - i), i * 24
        h = min(24, H - y)
        if k == 16:
            o.append(f'<rect y="{y}" width="{W}" height="{h}" fill="{GRAY}"/>')
        elif k > 0:
            o.append(f'<rect y="{y}" width="{W}" height="{h}" fill="url(#d{k})"/>')

    # ---- wordmark: extrusão roxa + contorno + hachura + sombreado pontilhado ----
    if baked:
        _, _, dx, dy = kf_at(JIT, frame, GLITCH)
        o.append(f'<g transform="translate({dx} {dy})">')
    else:
        o.append('<g class="jit">')
    o += [f'<use href="#wmo" x="{dd}" y="{dd}" fill="{VIOLET}"/>' for dd in range(12, 0, -1)]
    o.append(f'<use href="#wmo" fill="{INK}"/>')
    o.append('<use href="#wmf" fill="url(#hatch)"/>')
    o.append(f'<path d="{cells_path(wm_cells, S, OX, OY, rows={4})}" fill="url(#sh4)"/>')
    o.append(f'<path d="{cells_path(wm_cells, S, OX, OY, rows={5, 6})}" fill="url(#sh8)"/>')
    o.append("</g>")

    # ---- glitch: fatias deslocadas + barras de "tearing" ----
    for i, sl in enumerate(SLICES):
        if baked:
            _, op, dx, dy = kf_at(sl["kf"], frame, GLITCH)
            inner = f'<g opacity="{op}" transform="translate({dx} {dy})">'
        else:
            inner = f'<g class="gl gl{i}">'
        o.append(f'<g clip-path="url(#c{i})">{inner}<use href="#wmf" fill="{sl["color"]}"/></g></g>')
    tear_attr = f' opacity="{kf_at(TEAR, frame, GLITCH)[1]}"' if baked else ' class="tear"'
    o.append(f'<g{tear_attr} fill="{VIOLET_L}">'
             + "".join(f'<rect x="0" y="{sl["y"] + sl["h"] // 2}" width="{W}" height="3"/>' for sl in SLICES[:2])
             + "</g>")

    # ---- subtítulo estilo terminal ----
    o.append(f'<rect x="{BOX_X}" y="{BOX_Y}" width="{BOX_W}" height="{BOX_H}" fill="{INK}"/>')
    o.append(f'<rect x="{BOX_X}" y="{BOX_Y}" width="4" height="{BOX_H}" fill="{VIOLET}"/>')
    o.append(f'<path d="{cells_path(text_cells(">")[0], S2, OX, TY)}" fill="{VIOLET_L}"/>')
    o.append('<g class="typing">')
    for p, phrase in enumerate(PHRASES):
        o.append(f'<g clip-path="url(#tp{p})"><path d="{cells_path(text_cells(phrase)[0], S2, TX, TY)}" fill="{PAPER}"/></g>')
    if baked:
        cx = value_at(cursor_track(), frame)
        cop = 1 if (frame % 1) < 0.5 else 0
        o.append(f'<rect x="{cx}" y="{TY}" width="16" height="{7 * S2}" fill="{VIOLET_L}" opacity="{cop}"/>')
    else:
        o.append(f'<rect class="cur" x="{TX}" y="{TY}" width="16" height="{7 * S2}" fill="{VIOLET_L}">'
                 f'{smil("x", cursor_track())}</rect>')
    o.append("</g>")
    if not baked:  # versão parada para quem ativa "reduzir movimento" no sistema
        n0 = len(PHRASES[0])
        o.append(f'<g class="static"><path d="{cells_path(text_cells(PHRASES[0])[0], S2, TX, TY)}" fill="{PAPER}"/>'
                 f'<rect x="{TX + n0 * ADV2}" y="{TY}" width="16" height="{7 * S2}" fill="{VIOLET_L}"/></g>')

    # ---- rótulos ----
    o.append(label(LABEL_TL, 24, 24))
    o.append(label(LABEL_TR, -24, 24))
    o.append(label(LABEL_BR, -24, H - 24 - (7 * S3 + 20), color=VIOLET_L))

    # ---- scanline ----
    if baked:
        o.append(f'<g transform="translate(0 {f(-20 + 440 * ((frame % SCAN) / SCAN))})">')
    else:
        o.append('<g class="scan">')
    o.append(f'<rect y="0" width="{W}" height="12" fill="url(#sg)"/>'
             f'<rect y="10" width="{W}" height="2" fill="{VIOLET_L}" opacity=".55"/></g>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


def build_divider():
    """Faixa pontilhada roxa, densa no centro e sumindo nas pontas; fundo transparente (tema claro e escuro)."""
    cell, cols, rows, peak = 6, W // 6, 2, 0.8
    rects = []
    for y in range(rows):
        for x in range(cols):
            dens = peak * (1 - abs((x + 0.5) / cols * 2 - 1))
            if BAYER[y % 4][x % 4] < dens * 16:
                rects.append(f'<rect x="{x * cell}" y="{y * cell}" width="{cell}" height="{cell}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {rows * cell}" width="{W}" '
            f'height="{rows * cell}" shape-rendering="crispEdges" aria-hidden="true">'
            f'<g fill="{VIOLET}">{"".join(rects)}</g></svg>\n')


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--frame", type=float, help="tempo (s) para congelar a animação num preview estático")
    ap.add_argument("--out", help="arquivo de saída do preview (usado com --frame)")
    a = ap.parse_args()
    if a.frame is not None:
        Path(a.out or "banner-frame.svg").write_text(build_banner(a.frame), encoding="utf-8")
    else:
        assets = Path(__file__).resolve().parent.parent / "assets"
        assets.mkdir(exist_ok=True)
        (assets / "banner.svg").write_text(build_banner(), encoding="utf-8")
        (assets / "divider.svg").write_text(build_divider(), encoding="utf-8")
        print(f"ok: {assets / 'banner.svg'} e {assets / 'divider.svg'}")
