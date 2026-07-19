"""Burn game titles into the bespoke raster covers.

SVG covers render their title in make_vector_covers.py. This helper does the same
for the nine JPG covers, keeping the title visible even when the image is viewed
outside the website.
"""
from pathlib import Path
import re
import subprocess
import tempfile
import textwrap

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "js" / "games.js"
COVERS = ROOT / "assets" / "covers"

# The map is deliberately read from games.js so the data does not get duplicated.
entries = re.findall(r'"([^"]+)": "(assets/covers/[^\"]+\.jpg)"', DATA.read_text(encoding="utf-8"))

for title, relative_path in entries:
    source = ROOT / relative_path
    if not source.exists() or source.parent != COVERS:
        continue

    lines = textwrap.wrap(title, width=22) or [title]
    label = "\n".join(lines[:3])
    with tempfile.NamedTemporaryFile(suffix=".jpg", dir=COVERS, delete=False) as tmp:
        target = Path(tmp.name)

    command = [
        "convert", str(source),
        "-fill", "rgba(3,5,15,0.78)", "-draw", "rectangle 0,720 672,900",
        "-font", "DejaVu-Sans-Bold", "-fill", "white", "-stroke", "#03050f",
        "-strokewidth", "1", "-gravity", "south", "-pointsize", "34",
        "-annotate", "+0+34", label, "-strip", "-interlace", "Plane",
        "-quality", "84", str(target),
    ]
    subprocess.run(command, check=True)
    target.replace(source)
    print(f"titled: {title}")
