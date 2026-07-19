from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / "assets" / "covers"
OUT.mkdir(parents=True, exist_ok=True)

# These are intentionally compact, art-directed SVG covers for games that did not
# receive a bespoke raster illustration. They keep the same Lunar1ya figure and
# change palette, props and geometry to echo each game's mood.
THEMES = {
    "little-misfortune": ("#f29ab6", "#182238", "storybook", "#ffd36e"),
    "cult-of-the-lamb": ("#e84b5f", "#26152f", "ritual", "#ffd36e"),
    "portal-2": ("#f2f5ee", "#243247", "portal", "#ef7a38"),
    "split-fiction": ("#ff477e", "#2830a8", "split", "#6ef7ff"),
    "little-nightmares-ii": ("#28324c", "#10111d", "night", "#ffbd64"),
    "stardew-valley": ("#f8b46d", "#3973a9", "farm", "#ffe28a"),
    "the-last-of-us-part-i": ("#6f8c73", "#151d22", "ruins", "#d5e4bf"),
    "outlast": ("#9d2938", "#11111b", "horror", "#f2d186"),
    "metro-last-light-redux": ("#b84245", "#111a1d", "tunnel", "#ffbd69"),
    "stray": ("#f07b56", "#192c47", "city", "#6de0d1"),
    "moomintroll-winters-warmth": ("#9fd4ee", "#5a6098", "snow", "#fff2c6"),
    "little-nightmares": ("#7a725e", "#131a27", "night", "#f3c068"),
    "little-nightmares-iii": ("#d17e54", "#241a2f", "night", "#ffdf78"),
    "resident-evil-requiem": ("#ad283b", "#120f1c", "horror", "#eecb8b"),
    "scam-line": ("#f05263", "#18213d", "neon", "#d5ff62"),
    "fran-bow": ("#9357b5", "#151125", "storybook", "#f4d47d"),
    "the-past-within": ("#d39b5d", "#1d3554", "split", "#9ce3ff"),
    "creepy-tale": ("#7658b3", "#16152a", "forest", "#e9af72"),
    "the-mortuary-assistant": ("#5b8b9f", "#101923", "horror", "#d8f4ed"),
    "we-were-here": ("#94cce2", "#1c325e", "ice", "#ffb85d"),
    "we-were-here-too": ("#8cc9db", "#1c2852", "ice", "#ffb85d"),
    "we-were-here-together": ("#61b8cc", "#1c274d", "ice", "#ffcf6d"),
    "we-were-here-forever": ("#88a9da", "#171a40", "ice", "#ffbf64"),
    "escape-the-backrooms": ("#d2a64b", "#31311a", "backrooms", "#f4ef9a"),
    "mafia-ii-definitive-edition": ("#aa7251", "#1d1b24", "mafia", "#f1cb89"),
    "mafia-definitive-edition": ("#c28a57", "#1a1921", "mafia", "#f4d693"),
    "reanimal": ("#557b68", "#111a1d", "horror", "#efc06e"),
    "we-were-here-expeditions-the-friendship": ("#5ba8cb", "#1c2450", "ice", "#ffcf6d"),
    "call-of-the-sea": ("#49b4bf", "#102a43", "ocean", "#f1c36b"),
    "labyrinthine": ("#6b58a2", "#121426", "maze", "#e9a75c"),
    "better-mart-simulator": ("#f3a742", "#23466b", "store", "#ffed9a"),
    "lost-in-play": ("#65c5c3", "#2e4e9f", "play", "#ffd971"),
    "there-is-no-game": ("#5c6dff", "#12132b", "glitch", "#ff6bce"),
    "it-takes-two": ("#f37c9b", "#284d9a", "garden", "#f8dc76"),
    "the-last-campfire": ("#dd8a54", "#24234b", "campfire", "#ffda74"),
    "metro-2033-redux": ("#667b65", "#12181d", "tunnel", "#f0af5b"),
}

TITLE_BY_SLUG = {'little-misfortune': 'Little Misfortune', 'cult-of-the-lamb': 'Cult of the Lamb', 'portal-2': 'Portal 2', 'split-fiction': 'Split Fiction', 'little-nightmares-ii': 'Little Nightmares II', 'stardew-valley': 'Stardew Valley', 'the-last-of-us-part-i': 'The Last of Us Part I', 'outlast': 'Outlast', 'metro-last-light-redux': 'Metro: Last Light Redux', 'stray': 'Stray', 'moomintroll-winters-warmth': "Moomintroll: Winter's Warmth", 'little-nightmares': 'Little Nightmares', 'little-nightmares-iii': 'Little Nightmares III', 'resident-evil-requiem': 'Resident Evil Requiem', 'scam-line': 'Scam Line', 'fran-bow': 'Fran Bow', 'the-past-within': 'The Past Within', 'creepy-tale': 'Creepy Tale', 'the-mortuary-assistant': 'The Mortuary Assistant', 'we-were-here': 'We Were Here', 'we-were-here-too': 'We Were Here Too', 'we-were-here-together': 'We Were Here Together', 'we-were-here-forever': 'We Were Here Forever', 'escape-the-backrooms': 'Escape the Backrooms', 'mafia-ii-definitive-edition': 'Mafia II: Definitive Edition', 'mafia-definitive-edition': 'Mafia: Definitive Edition', 'reanimal': 'Reanimal', 'we-were-here-expeditions-the-friendship': 'We Were Here Expeditions: The FriendShip', 'call-of-the-sea': 'Call of the Sea', 'labyrinthine': 'Labyrinthine', 'better-mart-simulator': 'Better Mart Simulator', 'lost-in-play': 'Lost in Play', 'there-is-no-game': 'There Is No Game', 'it-takes-two': 'It Takes Two', 'the-last-campfire': 'The Last Campfire', 'metro-2033-redux': 'Metro 2033 Redux'}


def svg_for(a, b, kind, accent, title):
    # Decorative layer is intentionally simple: it stays crisp at card size and
    # makes each fallback feel like a designed cover rather than a flat gradient.
    shapes = {
        "storybook": f'''<path d="M0 650 Q120 530 240 660 T480 640 T672 620V900H0Z" fill="{accent}" opacity=".16"/><path d="M40 300 Q130 190 220 300M450 310 Q540 180 630 290" fill="none" stroke="{accent}" stroke-width="10" opacity=".45"/><circle cx="560" cy="170" r="64" fill="{accent}" opacity=".5"/>''',
        "ritual": f'''<circle cx="510" cy="175" r="95" fill="{accent}" opacity=".8"/><circle cx="510" cy="175" r="120" fill="none" stroke="{accent}" stroke-width="5" opacity=".4"/><path d="M0 760L160 590 280 770 430 560 672 780V900H0Z" fill="#100d1e" opacity=".55"/>''',
        "portal": f'''<path d="M0 170H672M0 285H672M0 400H672M0 515H672M0 630H672M0 745H672" stroke="#b6c4c3" stroke-width="2" opacity=".42"/><circle cx="115" cy="300" r="88" fill="none" stroke="#45aef0" stroke-width="22"/><circle cx="560" cy="570" r="88" fill="none" stroke="{accent}" stroke-width="22"/><path d="M100 780L300 590 430 780Z" fill="#243247" opacity=".8"/>''',
        "split": f'''<path d="M0 0L672 900" stroke="{accent}" stroke-width="12" opacity=".8"/><path d="M0 720L300 0M390 900L672 260" stroke="#fff" stroke-width="3" opacity=".24"/><circle cx="150" cy="180" r="70" fill="{accent}" opacity=".5"/><circle cx="545" cy="720" r="74" fill="#ff5c92" opacity=".35"/>''',
        "night": f'''<circle cx="520" cy="180" r="96" fill="{accent}" opacity=".8"/><circle cx="520" cy="180" r="117" fill="none" stroke="{accent}" stroke-width="3" opacity=".5"/><path d="M0 720L120 545 220 690 340 480 460 650 555 520 672 720V900H0Z" fill="#080e18" opacity=".84"/><rect x="90" y="410" width="92" height="125" fill="#f5b85d" opacity=".5"/>''',
        "farm": f'''<circle cx="530" cy="180" r="90" fill="{accent}"/><path d="M0 615 Q150 500 300 625T672 585V900H0Z" fill="#4f8b65" opacity=".9"/><path d="M70 690h155v120H70zM104 637l44-40 44 40z" fill="#e79d70"/><path d="M0 820 Q220 680 420 820T672 760V900H0Z" fill="#2d5d61" opacity=".6"/>''',
        "ruins": f'''<circle cx="540" cy="180" r="100" fill="{accent}" opacity=".42"/><path d="M0 560L100 410 160 560 270 320 350 560 460 395 540 560 672 350V900H0Z" fill="#172b2b" opacity=".9"/><path d="M40 700h160v200H40zM260 620h110v280H260zM470 680h170v220H470z" fill="#0d151c" opacity=".9"/>''',
        "tunnel": f'''<path d="M-50 900 Q336 260 722 900" fill="none" stroke="#080b12" stroke-width="160" opacity=".8"/><path d="M40 900 Q336 400 632 900" fill="none" stroke="{accent}" stroke-width="4" opacity=".55"/><circle cx="336" cy="460" r="28" fill="{accent}" opacity=".9"/><path d="M110 900L260 590M562 900L412 590" stroke="#222b27" stroke-width="38"/>''',
        "city": f'''<path d="M0 660h94V420h80v240h110V300h88v360h110V470h90v190h100v-280h80v280H0Z" fill="#101b32" opacity=".92"/><circle cx="520" cy="180" r="92" fill="{accent}" opacity=".55"/><path d="M0 690h672" stroke="{accent}" stroke-width="5" opacity=".65"/>''',
        "snow": f'''<circle cx="520" cy="170" r="95" fill="{accent}"/><path d="M0 610Q180 490 360 620T672 600V900H0Z" fill="#d8eff4" opacity=".8"/><path d="M0 720Q200 600 410 730T672 700V900H0Z" fill="#b2d5ed" opacity=".8"/><g fill="#fff" opacity=".8"><circle cx="100" cy="220" r="5"/><circle cx="200" cy="370" r="4"/><circle cx="600" cy="400" r="6"/><circle cx="80" cy="500" r="4"/></g>''',
        "horror": f'''<circle cx="540" cy="170" r="105" fill="{accent}" opacity=".48"/><path d="M0 720Q80 440 170 720T340 720T510 720T672 720V900H0Z" fill="#090c14" opacity=".84"/><path d="M115 700V480M115 480l-55 74M115 480l55 74M560 710V470M560 470l-58 70M560 470l57 70" stroke="#0b111a" stroke-width="18"/>''',
        "neon": f'''<path d="M0 300L672 120M0 440L672 260M0 580L672 400M0 720L672 540" stroke="{accent}" stroke-width="8" opacity=".7"/><circle cx="130" cy="190" r="90" fill="{accent}" opacity=".34"/><path d="M0 780L180 570 350 780 500 560 672 780" fill="none" stroke="#57e6ff" stroke-width="9" opacity=".65"/>''',
        "forest": f'''<path d="M0 780L90 400 175 780M125 780L260 270 380 780M390 780L510 330 650 780" fill="#11142b"/><circle cx="535" cy="180" r="95" fill="{accent}" opacity=".7"/><path d="M0 760Q170 600 350 760T672 740V900H0Z" fill="#23244a"/>''',
        "ice": f'''<path d="M0 750L130 520 230 690 340 420 460 690 570 510 672 740V900H0Z" fill="#162653" opacity=".86"/><circle cx="515" cy="175" r="90" fill="{accent}" opacity=".5"/><path d="M90 740L180 600M550 740L465 590" stroke="{accent}" stroke-width="8" opacity=".65"/>''',
        "backrooms": f'''<path d="M0 0L190 95 190 900 0 900ZM672 0L480 95 480 900 672 900Z" fill="#5e4d24" opacity=".36"/><path d="M0 120H672M0 240H672M0 360H672M0 480H672M0 600H672M0 720H672" stroke="#e8ce6a" stroke-width="2" opacity=".38"/><rect x="40" y="120" width="150" height="220" fill="#e7da75" opacity=".3"/>''',
        "mafia": f'''<circle cx="510" cy="185" r="100" fill="{accent}" opacity=".42"/><path d="M0 660h120V470h72v190h95V350h90v310h120V510h72v150h103v240H0Z" fill="#171724" opacity=".95"/><path d="M0 755H672" stroke="{accent}" stroke-width="6" opacity=".6"/>''',
        "ocean": f'''<circle cx="520" cy="170" r="95" fill="{accent}" opacity=".8"/><path d="M0 610Q120 540 240 610T480 610T672 590V900H0Z" fill="#1c7092" opacity=".9"/><path d="M0 680Q120 610 240 680T480 680T672 660M0 750Q120 680 240 750T480 750T672 730" fill="none" stroke="#9ae8df" stroke-width="6" opacity=".45"/>''',
        "maze": f'''<path d="M40 180H250V300H110V460H320V590H70V790H280M632 130H430V260H560V420H350V560H600V780H420" fill="none" stroke="{accent}" stroke-width="14" opacity=".55"/><circle cx="530" cy="180" r="70" fill="{accent}" opacity=".35"/>''',
        "store": f'''<rect x="42" y="180" width="588" height="520" rx="16" fill="#18355d" opacity=".85"/><path d="M42 260H630M140 260V700M280 260V700M420 260V700M560 260V700" stroke="{accent}" stroke-width="8" opacity=".7"/><circle cx="520" cy="155" r="62" fill="{accent}" opacity=".7"/>''',
        "play": f'''<circle cx="520" cy="170" r="90" fill="{accent}" opacity=".85"/><path d="M0 670Q130 520 250 670T500 660T672 630V900H0Z" fill="#22467f" opacity=".8"/><circle cx="130" cy="380" r="55" fill="#ff7c8e" opacity=".8"/><path d="M320 360l48 96h-96z" fill="#ffda67"/>''',
        "glitch": f'''<path d="M0 230H672M0 300H672M0 370H672M0 440H672" stroke="{accent}" stroke-width="11" opacity=".28"/><rect x="60" y="180" width="210" height="300" fill="none" stroke="#76efff" stroke-width="8" opacity=".8"/><rect x="410" y="420" width="200" height="290" fill="none" stroke="#ff73d0" stroke-width="8" opacity=".7"/><path d="M0 760L672 620" stroke="#fff" stroke-width="3" opacity=".4"/>''',
        "garden": f'''<circle cx="530" cy="180" r="94" fill="{accent}" opacity=".8"/><path d="M0 740Q115 560 250 750T500 730T672 700V900H0Z" fill="#437d69" opacity=".9"/><path d="M110 810q-20-130 60-210M540 820q0-125-70-210" stroke="#f8d870" stroke-width="11" opacity=".6"/><circle cx="170" cy="590" r="20" fill="#ffb1d0"/><circle cx="510" cy="620" r="20" fill="#8ee5ff"/>''',
        "campfire": f'''<circle cx="520" cy="170" r="96" fill="{accent}" opacity=".7"/><path d="M0 750Q160 570 300 750T672 720V900H0Z" fill="#1b1d43"/><path d="M300 790q-45-100 35-180 45 85 90 120 20-65-5-105 95 80 40 165z" fill="#ffb84f"/><path d="M318 805q-25-58 20-96 25 46 56 65-3 48-76 31z" fill="#fff09b"/>''',
    }
    deco = shapes.get(kind, shapes["neon"])
    pattern = f'''<pattern id="grain" width="38" height="38" patternUnits="userSpaceOnUse"><circle cx="4" cy="6" r="1" fill="#fff" opacity=".12"/><circle cx="25" cy="21" r="1" fill="#fff" opacity=".08"/><path d="M0 37L38 0" stroke="#fff" stroke-width="1" opacity=".025"/></pattern>'''
    words = title.split()
    lines, current = [], ""
    for word in words:
        if current and len(current) + len(word) + 1 > 22:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    title_svg = "".join(
        f'<text x="34" y="{82 + index * 32}" fill="#fff" font-family="system-ui,sans-serif" font-size="28" font-weight="900">{escape(line)}</text>'
        for index, line in enumerate(lines[:3])
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 672 900" role="img" aria-label="Обложка игры Lunar1ya">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient><linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#050811" stop-opacity=".08"/><stop offset=".7" stop-color="#050811" stop-opacity=".08"/><stop offset="1" stop-color="#050811" stop-opacity=".88"/></linearGradient>{pattern}</defs>
<rect width="672" height="900" fill="url(#bg)"/>{deco}<rect width="672" height="900" fill="url(#grain)"/>
<image xlink:href="../character/lunar1ya-ferret-figure.webp" x="137" y="156" width="398" height="650" preserveAspectRatio="xMidYMax meet" opacity=".98"/>
<rect width="672" height="900" fill="url(#shade)"/>
<rect x="22" y="18" width="628" height="142" rx="12" fill="#050811" fill-opacity=".58" stroke="#c5eaff" stroke-opacity=".72" stroke-width="2"/><path d="M34 38H190" stroke="{accent}" stroke-width="4"/><text x="34" y="61" fill="#fff" font-family="system-ui,sans-serif" font-size="13" font-weight="700" letter-spacing="4">LUNAR1YA</text><text x="638" y="61" text-anchor="end" fill="#fff" opacity=".72" font-family="system-ui,sans-serif" font-size="11" letter-spacing="2">GAME LIBRARY</text>
{title_svg}
</svg>'''

# These titles use bespoke raster illustrations generated with the character
# reference. They are kept out of the SVG fallback set when regenerating.
BESPOKE_RASTER = {
    "constance", "grime-ii", "rv-there-yet", "peak", "valorant",
    "hollow-knight", "hollow-knight-silksong", "replaced",
    "bendy-and-the-ink-factory", "cult-of-the-lamb", "portal-2",
    "little-nightmares-ii", "stardew-valley", "the-last-of-us-part-i",
    "outlast", "metro-last-light-redux", "stray", "resident-evil-requiem",
    "it-takes-two",
}

for slug, (a, b, kind, accent) in THEMES.items():
    if slug in BESPOKE_RASTER:
        continue
    (OUT / f"{slug}.svg").write_text(svg_for(a, b, kind, accent, TITLE_BY_SLUG[slug]), encoding="utf-8")

print(f"wrote {len(THEMES) - len(BESPOKE_RASTER)} SVG covers to {OUT}")
