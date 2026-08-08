#!/usr/bin/env bash
set -euo pipefail
FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
render() {
  slug="$1"; title="$2"
  convert "covers_new/${slug}.png" -resize '600x800^' -gravity center -extent 600x800 \
    \( -size 600x210 gradient:'#05030dcc-none' \) -gravity north -compose over -composite \
    \( -size 530x175 -background none -fill '#fffafc' -stroke '#100817' -strokewidth 4 \
       -font "$FONT" -gravity center -pointsize 48 caption:"$title" \) \
    -gravity north -geometry +0+12 -compose over -composite \
    -quality 88 "covers_webp/${slug}.webp"
}
render An_Eggstremely_Hard_Game 'AN EGGSTREMELY HARD GAME'
render Crushed_In_Time 'CRUSHED IN TIME'
render BOKURA_planet 'BOKURA: planet'
render Cuphead 'CUPHEAD'
render Biped_2 'BIPED 2'
render MOUSE_PI_For_Hire 'MOUSE: P.I. FOR HIRE'
render The_Stanley_Parable_Ultra_Deluxe 'THE STANLEY PARABLE: ULTRA DELUXE'
render Resident_Evil_HD_Remaster 'RESIDENT EVIL HD REMASTER'
render Resident_Evil_2 'RESIDENT EVIL 2'
render Resident_Evil_3 'RESIDENT EVIL 3'
render Resident_Evil_4 'RESIDENT EVIL 4'
render Resident_Evil_7 'RESIDENT EVIL 7 BIOHAZARD'
render Resident_Evil_Village 'RESIDENT EVIL VILLAGE'
render Resident_Evil_Code_Veronica_Remake 'RESIDENT EVIL CODE: VERONICA REMAKE'
render A_Plague_Tale_Innocence 'A PLAGUE TALE: INNOCENCE'
render The_Quarry 'THE QUARRY'
render Trine 'TRINE'
render Trine_2 'TRINE 2'
render BrokenLore_FOLLOW 'BROKENLORE: FOLLOW'
render Creepy_Tale_2 'CREEPY TALE 2'
