#!/usr/bin/env bash
# Замена hero-портрета и/или аватара профиля одним исходником.
#
#   scripts/replace_art.sh <src-image> [hero|avatar|both]
#
# Примеры:
#   scripts/replace_art.sh ~/image-2.png hero
#   GRAVITY=north scripts/replace_art.sh ~/image-2.jpg both
#
# Параметры кадрирования (опционально):
#   GRAVITY=center|north|south|...   точка фокуса при кропе (по умолчанию center)
#   OFFSET=+0-40                     сдвиг кропа относительно GRAVITY
#
# Из одного исходника пересобираются все responsive-варианты:
#   assets/hero-banner-{480,720,895}.{avif,webp,jpg}   (aspect 895:1200)
#   assets/avatar-{160,320}.{avif,webp,jpg}            (square)
# Качество как у существующих ассетов: JPG 82, WebP 92, AVIF 92.

set -euo pipefail

SRC="${1:-}"
TARGET="${2:-hero}"
GRAVITY="${GRAVITY:-center}"
OFFSET="${OFFSET:-+0+0}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if [[ -z "$SRC" || ! -f "$SRC" ]]; then
  echo "usage: $(basename "$0") <src-image> [hero|avatar|both]" >&2
  exit 1
fi

# Кадрирование под нужный aspect + ресайз под каждый размер.
variant() {  # variant <out-prefix> <width> <height>
  local prefix="$1" w="$2" h="$3"
  convert "$SRC" -auto-orient -strip \
    -resize "${w}x${h}^" -gravity "$GRAVITY" -extent "${w}x${h}" \
    -geometry "$OFFSET" "$TMP/${prefix}.png"
}

emit() {  # emit <png> <dest-base> <quality-avif> <quality-webp> <quality-jpg>
  local png="$1" base="$2" qa="$3" qw="$4" qj="$5"
  convert "$png" -quality "$qw" "${base}.webp"
  convert "$png" -quality "$qj" "${base}.jpg"
  convert "$png" -quality "$qa" "${base}.avif"
}

if [[ "$TARGET" == "hero" || "$TARGET" == "both" ]]; then
  for size in "480 643" "720 965" "895 1200"; do
    set -- $size
    variant "hero-$1" "$1" "$2"
    emit "$TMP/hero-$1.png" "$ROOT/assets/hero-banner-$1" "${AVIF_Q:-55}" 92 82
    echo "✓ assets/hero-banner-$1.{avif,webp,jpg}"
  done
fi

if [[ "$TARGET" == "avatar" || "$TARGET" == "both" ]]; then
  for size in "160 160" "320 320"; do
    set -- $size
    variant "avatar-$1" "$1" "$2"
    emit "$TMP/avatar-$1.png" "$ROOT/assets/avatar-$1" "${AVIF_Q:-55}" 92 82
    echo "✓ assets/avatar-$1.{avif,webp,jpg}"
  done
fi

echo "Готово. Проверьте результат: python3 -m http.server 8000"
