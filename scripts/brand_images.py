"""Bake the transparent logo badge into the site images.

Reads the unbranded originals from brand_assets/unbranded-images/ and writes
branded WebP files to src/assets/images/. Re-run after replacing an original.
Usage: python scripts/brand_images.py <path-to-logo.png>
(logo = public/logo-full.png, the lockup on a transparent background)

The badge is sized and placed relative to each image, so it works for the
different image sizes (1152x928 headers, 1120x960 homepage photos, 1264x848
tile). Every image is shown at roughly its native aspect ratio, so a small
margin from the bottom-right corner survives the page crop.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "brand_assets" / "unbranded-images"
OUT = ROOT / "src" / "assets" / "images"

BADGE_OPACITY = 0.92    # 1.0 = solid, lower = more see-through
LOGO_WIDTH_FRAC = 0.36  # logo width as a fraction of the image width
MARGIN_FRAC = 0.04      # distance from the right/bottom edge, as a fraction of image width
PAD_FRAC = 0.016        # padding inside the white pill, as a fraction of image width


def badge(logo_path: Path, image_width: int) -> Image.Image:
    width = round(image_width * LOGO_WIDTH_FRAC)
    pad = round(image_width * PAD_FRAC)
    logo = Image.open(logo_path).convert("RGBA")
    logo = logo.crop(logo.getbbox())
    h = round(logo.height * width / logo.width)
    logo = logo.resize((width, h), Image.LANCZOS)
    w, hh = logo.width + pad * 2, logo.height + pad * 2
    pill = Image.new("RGBA", (w, hh), (0, 0, 0, 0))
    ImageDraw.Draw(pill).rounded_rectangle((0, 0, w - 1, hh - 1), radius=round(pad * 1.3), fill=(255, 255, 255, 230))
    pill.alpha_composite(logo, (pad, pad))
    pill.putalpha(pill.getchannel("A").point(lambda a: round(a * BADGE_OPACITY)))
    return pill


def main(logo_path: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src in sorted(SRC.glob("*.webp")):
        im = Image.open(src).convert("RGBA")
        pill = badge(Path(logo_path), im.width)
        margin = round(im.width * MARGIN_FRAC)
        x = im.width - margin - pill.width
        y = im.height - margin - pill.height
        im.alpha_composite(pill, (x, y))
        im.convert("RGB").save(OUT / src.name, "WEBP", quality=86)
        print("branded", src.name)


if __name__ == "__main__":
    main(sys.argv[1])
