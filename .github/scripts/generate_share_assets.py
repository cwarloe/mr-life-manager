#!/usr/bin/env python3
"""Generate social share images and the printable partner pilot handout."""

from __future__ import annotations

from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[2]
SHARE_DIR = ROOT / "products" / "landing" / "assets" / "share"
PDF_PATH = ROOT / "products" / "guides-pdf" / "partner-pilot.pdf"
TMP = ROOT / "tmp" / "pdfs"

INK = "#12161C"
PAPER = "#FBF9F4"
BLUE = "#1F4E79"
BLUE_SOFT = "#E7EEF5"
AMBER = "#B4741A"
SLATE = "#6B7280"

SANS = "/usr/share/fonts/opentype/urw-base35/NimbusSans-Regular.otf"
SANS_BOLD = "/usr/share/fonts/opentype/urw-base35/NimbusSans-Bold.otf"
SERIF = "/usr/share/fonts/opentype/urw-base35/NimbusRoman-Regular.otf"
PDF_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
PDF_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
PDF_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

SHARES = {
    "home.png": ("Practical systems for running a home", "Run your home without carrying all of it in your head."),
    "first-night.png": ("Start here", "Your first night in a new place."),
    "guests.png": ("Start here", "Someone's coming over. Start here."),
    "underwater.png": ("Start here", "You're not lazy. You're underwater."),
    "one-room.png": ("Start here", "Take back one usable part of the room."),
    "first-place.png": ("First Place - planned founding price $39", "Your first 30 days, already decided."),
    "partners.png": ("For parents, mentors, churches, and campuses", "Give them one useful page, not another talk."),
}

PILOT_PAGES = [
    ("Parent or family friend", "parent", "Send the page that matches what is happening today."),
    ("Mentor or coach", "mentor", "Try one practical page with one person before assigning more."),
    ("Church or young-adult ministry", "church", "Pilot one task with up to five people and report only aggregate results."),
    ("Campus or residence life", "campus", "A small task-first pilot, not a program commitment."),
]


def wrapped(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def social_image(kicker: str, headline: str, output: Path) -> None:
    image = Image.new("RGB", (1200, 630), PAPER)
    draw = ImageDraw.Draw(image)
    brand = ImageFont.truetype(SANS_BOLD, 30)
    kicker_font = ImageFont.truetype(SANS_BOLD, 23)
    headline_font = ImageFont.truetype(SANS_BOLD, 72)
    footer_font = ImageFont.truetype(SERIF, 27)

    draw.rectangle((0, 0, 22, 630), fill=AMBER)
    draw.rectangle((22, 0, 1200, 14), fill=INK)
    draw.text((78, 62), "MR. LIFE MANAGER", font=brand, fill=INK)
    draw.text((78, 142), kicker.upper(), font=kicker_font, fill=BLUE)

    y = 205
    for line in wrapped(draw, headline, headline_font, 990):
        draw.text((78, y), line, font=headline_font, fill=INK)
        y += 82

    draw.rectangle((78, 531, 1122, 533), fill="#D9D5CC")
    draw.text((78, 554), "One useful action, in the order you need it.", font=footer_font, fill=SLATE)
    image.save(output, format="PNG", optimize=True)


def make_qr(url: str, path: Path) -> None:
    code = qrcode.QRCode(version=None, box_size=9, border=3, error_correction=qrcode.constants.ERROR_CORRECT_M)
    code.add_data(url)
    code.make(fit=True)
    code.make_image(fill_color=INK, back_color="white").convert("RGB").save(path)


def draw_pdf_page(pdf: canvas.Canvas, audience: str, source: str, intro: str) -> None:
    width, height = letter
    url = f"https://mrlifemanager.com/partners.html?from={source}"
    qr_path = TMP / f"pilot-{source}.png"
    make_qr(url, qr_path)

    pdf.setFillColor(HexColor(PAPER))
    pdf.rect(0, 0, width, height, fill=1, stroke=0)
    pdf.setFillColor(HexColor(INK))
    pdf.rect(0, height - 12, width, 12, fill=1, stroke=0)
    pdf.setFillColor(HexColor(AMBER))
    pdf.rect(0, 0, 10, height, fill=1, stroke=0)

    pdf.setFillColor(HexColor(INK))
    pdf.setFont("MlmSansBold", 13)
    pdf.drawString(42, 744, "MR. LIFE MANAGER")
    pdf.setFillColor(HexColor(BLUE))
    pdf.setFont("MlmSansBold", 9)
    pdf.drawString(42, 715, audience.upper())

    pdf.setFillColor(HexColor(INK))
    pdf.setFont("MlmSansBold", 29)
    pdf.drawString(42, 670, "Give them one useful page,")
    pdf.drawString(42, 636, "not another talk.")
    pdf.setFillColor(HexColor(SLATE))
    pdf.setFont("MlmSerif", 13)
    pdf.drawString(42, 603, intro)

    steps = [
        ("1", "Match the problem", "Use what is happening today: first night, overwhelmed, guests, or one lost room."),
        ("2", "Let them do it", "The free page speaks to the person doing the work. No account is required."),
        ("3", "Ask one question", "Later ask what helped or where they stopped. No names or private details."),
    ]
    y = 535
    for number, title, body in steps:
        pdf.setFillColor(HexColor(BLUE_SOFT))
        pdf.roundRect(42, y - 9, 30, 30, 4, fill=1, stroke=0)
        pdf.setFillColor(HexColor(BLUE))
        pdf.setFont("MlmSansBold", 14)
        pdf.drawCentredString(57, y, number)
        pdf.setFillColor(HexColor(INK))
        pdf.setFont("MlmSansBold", 12)
        pdf.drawString(86, y + 6, title)
        pdf.setFillColor(HexColor(SLATE))
        pdf.setFont("MlmSerif", 10.5)
        pdf.drawString(86, y - 10, body)
        y -= 66

    pdf.setFillColor(HexColor("#FFFFFF"))
    pdf.setStrokeColor(HexColor("#B8B2A6"))
    pdf.roundRect(42, 170, 528, 150, 6, fill=1, stroke=1)
    pdf.drawImage(ImageReader(str(qr_path)), 61, 188, 112, 112, preserveAspectRatio=True, mask="auto")
    pdf.setFillColor(HexColor(INK))
    pdf.setFont("MlmSansBold", 16)
    pdf.drawString(197, 276, "Scan to choose the right starting page")
    pdf.setFillColor(HexColor(SLATE))
    pdf.setFont("MlmSerif", 11)
    pdf.drawString(197, 251, "Try it with one person - or up to five - and tell us")
    pdf.drawString(197, 235, "only what helped and where someone stopped.")
    pdf.setFillColor(HexColor(BLUE))
    pdf.setFont("MlmSansBold", 9.5)
    pdf.drawString(197, 205, url)

    pdf.setFillColor(HexColor(SLATE))
    pdf.setFont("MlmSerif", 9.5)
    pdf.drawString(42, 126, "Free learning pilot. No account, participant report, or institutional commitment.")
    pdf.drawString(42, 108, "The source label in the link identifies this route only; it does not create a visitor profile.")
    pdf.setFillColor(HexColor(INK))
    pdf.setFont("MlmSansBold", 9.5)
    pdf.drawString(42, 66, "mrlifemanager.com")
    pdf.setFillColor(HexColor(SLATE))
    pdf.setFont("MlmSans", 9.5)
    pdf.drawRightString(570, 66, "Practical systems for running a home")
    pdf.showPage()


def main() -> int:
    pdfmetrics.registerFont(TTFont("MlmSans", PDF_SANS))
    pdfmetrics.registerFont(TTFont("MlmSansBold", PDF_SANS_BOLD))
    pdfmetrics.registerFont(TTFont("MlmSerif", PDF_SERIF))
    SHARE_DIR.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    for filename, (kicker, headline) in SHARES.items():
        social_image(kicker, headline, SHARE_DIR / filename)

    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(PDF_PATH), pagesize=letter, pageCompression=1)
    pdf.setTitle("Mr. Life Manager - Five-Person Pilot Handouts")
    pdf.setAuthor("Mr. Life Manager")
    for page in PILOT_PAGES:
        draw_pdf_page(pdf, *page)
    pdf.save()

    for path in TMP.glob("pilot-*.png"):
        path.unlink()
    if TMP.exists() and not any(TMP.iterdir()):
        TMP.rmdir()
    parent = TMP.parent
    if parent.exists() and not any(parent.iterdir()):
        parent.rmdir()

    print(f"Generated {len(SHARES)} social images and {PDF_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
