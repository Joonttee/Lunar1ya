#!/usr/bin/env bash
# Замена hero-портрета и/или аватара профиля одним исходником.
#
#   scripts/replace_art.sh <src-image> [hero|avatar|both]
#
# Примеры:
#   scripts/replace_art.sh assets/src/hero-source.jpg hero
#   GRAVITY=north scripts/replace_art.sh assets/src/hero-source.jpg hero
#   GRAVITY=center OFFSET_Y=-40 scripts/replace_art.sh assets/src/hero-source.jpg both
#
# Управление кадрированием:
#   GRAVITY=center|north|south|west|east   точка фокуса (по умолчанию center)
#   OFFSET_Y=-40                           дополнительный сдвиг окна по вертикали,
#                                          в пикселях в масштабе 895x1200 (отрицательный — выше)
#
# Из одного исходника пересобираются все responsive-варианты существующего пайплайна:
#   assets/hero-banner-{480,720,895}.{avif,webp,jpg}   (кадр 895:1200)
#   assets/avatar-{160,320}.{avif,webp,jpg}            (квадрат)
# Качество как у текущих ассетов: JPG 82, WebP 92, AVIF 55.

set -euo pipefail

SRC="${1:-}"
TARGET="${2:-hero}"
GRAVITY="${GRAVITY:-center}"
OFFSET_Y="${OFFSET_Y:-0}"
REF_H=1200
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if [[ -z "$SRC" || ! -f "$SRC" ]]; then
  echo "usage: $(basename "$0") <src-image> [hero|avatar|both]" >&2
  exit 1
fi

# Кроп под нужный кадр: ресайз «вписать по меньшей стороне» + окно с фокусом.
variant() { # variant <out-name> <width> <height>
  local name="$1" w="$2" h="$3"
  convert "$SRC" -auto-orient -strip -resize "${w}x${h}^" "$TMP/filled.png"
  local dims fw fh ox oy
  dims="$(identify -format "%w %h" "$TMP/filled.png")"
  fw="${dims%% *}"; fh="${dims##* }"
  ox=$(( (fw - w) / 2 )); oy=$(( (fh - h) / 2 ))
  case "$GRAVITY" in
    north) oy=0 ;;
    south) oy=$(( fh - h )) ;;
    west)  ox=0 ;;
    east)  ox=$(( fw - w )) ;;
  esac
  oy=$(( oy + OFFSET_Y * h / REF_H ))
  (( oy < 0 )) && oy=0
  (( oy > fh - h )) && oy=$(( fh - h ))
  (( ox < 0 )) && ox=0
  (( ox > fw - w )) && ox=$(( fw - w ))
  convert "$TMP/filled.png" -crop "${w}x${h}+${ox}+${oy}" +repage "$TMP/${name}.png"
}

# JPG — только для старшего размера: он единственный fallback в index.html,
# младшие размеры живут парами AVIF+WebP (так исторически сложилось в assets/).
emit() { # emit <png> <dest-base> [jpg]
  local png="$1" base="$2" want_jpg="${3:-}"
  convert "$png" -quality "${AVIF_Q:-55}" "${base}.avif"
  convert "$png" -quality 92 "${base}.webp"
  [[ -n "$want_jpg" ]] && convert "$png" -quality 82 "${base}.jpg"
  echo "  ✓ $(basename "${base}").{avif,webp${want_jpg:+,jpg\}}"
}

if [[ "$TARGET" == "hero" || "$TARGET" == "both" ]]; then
  echo "hero (кадр 895:1200, GRAVITY=$GRAVITY, OFFSET_Y=$OFFSET_Y):"
  variant hero-480 480 643
  variant hero-720 720 965
  variant hero-895 895 1200
  emit "$TMP/hero-480.png" "$ROOT/assets/hero-banner-480"
  emit "$TMP/hero-720.png" "$ROOT/assets/hero-banner-720"
  emit "$TMP/hero-895.png" "$ROOT/assets/hero-banner-895" jpg
fi

if [[ "$TARGET" == "avatar" || "$TARGET" == "both" ]]; then
  echo "avatar (квадрат, GRAVITY=$GRAVITY, OFFSET_Y=$OFFSET_Y):"
  variant avatar-160 160 160
  variant avatar-320 320 320
  emit "$TMP/avatar-160.png" "$ROOT/assets/avatar-160"
  emit "$TMP/avatar-320.png" "$ROOT/assets/avatar-320" jpg
fi

echo "Готово: python3 -m http.server 8000"
