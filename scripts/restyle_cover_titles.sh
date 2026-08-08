#!/usr/bin/env bash
set -euo pipefail
SANS=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
SERIF=/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf
MONO=/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf

# Rebuild MOUSE from clean generated art when available.
if [[ -f covers_new/MOUSE_PI_For_Hire.png ]]; then
  convert covers_new/MOUSE_PI_For_Hire.png -resize '600x800^' -gravity center -extent 600x800 -quality 88 covers_webp/MOUSE_PI_For_Hire.webp
fi

# Replace the generic title panel with game-specific typography.
style() {
  slug="$1" title="$2" font="$3" fill="$4" stroke="$5" bg="$6" size="$7"
  src="covers_webp/${slug}.webp"; tmp="/tmp/${slug}-styled.webp"
  convert "$src" \
    -fill "$bg" -draw 'rectangle 0,0 600,205' \
    \( -size 540x172 -background none -font "$font" -pointsize "$size" \
       -gravity center -fill "$fill" -stroke "$stroke" -strokewidth 4 caption:"$title" \) \
    -gravity north -geometry +0+16 -compose over -composite -quality 88 "$tmp"
  mv "$tmp" "$src"
}

style An_Eggstremely_Hard_Game 'AN EGGSTREMELY HARD GAME' "$SANS" '#fff4a8' '#a64d20' '#263656' 43
style Crushed_In_Time 'CRUSHED IN TIME' "$SERIF" '#e8d6ff' '#41256f' '#100b27' 49
style BOKURA_planet 'BOKURA: planet' "$SANS" '#fff7e6' '#476ca8' '#78b9d5' 54
style Cuphead 'CUPHEAD' "$SERIF" '#f7df8d' '#671f18' '#e8d5a5' 70
style Biped_2 'BIPED 2' "$SANS" '#ffffff' '#087b9b' '#5dc9ed' 67
style MOUSE_PI_For_Hire 'MOUSE: P.I. FOR HIRE' "$SERIF" '#f4f0df' '#171717' '#171717' 44
style The_Stanley_Parable_Ultra_Deluxe 'THE STANLEY PARABLE: ULTRA DELUXE' "$MONO" '#f1d64f' '#241b08' '#59634c' 37
style Resident_Evil_HD_Remaster 'RESIDENT EVIL HD REMASTER' "$SANS" '#ece7df' '#6e0808' '#09090c' 41
style Resident_Evil_2 'RESIDENT EVIL 2' "$SANS" '#e9e5df' '#8e0909' '#09090c' 58
style Resident_Evil_3 'RESIDENT EVIL 3' "$SANS" '#eeeae2' '#a00c08' '#120908' 58
