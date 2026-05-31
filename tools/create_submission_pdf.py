from pathlib import Path
import textwrap

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image as PdfImage,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT_DIR = Path(r"D:\Sem 10\mobile application\Quote app screenshots")
OUTPUT = ROOT / "submission" / "Quote_App_Submission_Mohamed_Ahmed_Abouelenein.pdf"
MAIN_DART = ROOT / "lib" / "main.dart"


def scaled_image(path, max_width, max_height):
    with Image.open(path) as image:
        width, height = image.size
    scale = min(max_width / width, max_height / height)
    return PdfImage(str(path), width=width * scale, height=height * scale)


def add_heading(story, text, style):
    story.append(Paragraph(text, style))
    story.append(Spacer(1, 0.14 * inch))


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title="Quote App Submission",
        author="Mohamed Ahmed Abouelenein",
    )

    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#2F3EAE"),
        spaceAfter=10,
    )
    subtitle = ParagraphStyle(
        "SubtitleCustom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#374151"),
    )
    heading = ParagraphStyle(
        "HeadingCustom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#2F3EAE"),
        spaceBefore=8,
        spaceAfter=6,
    )
    body = ParagraphStyle(
        "BodyCustom",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#111827"),
    )
    caption = ParagraphStyle(
        "CaptionCustom",
        parent=styles["BodyText"],
        fontName="Helvetica-Oblique",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#4B5563"),
        alignment=1,
    )
    code_style = ParagraphStyle(
        "CodeCustom",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=7.4,
        leading=9.2,
        textColor=colors.HexColor("#111827"),
    )

    story = []

    story.append(Paragraph("Flutter Bonus Assignment", title))
    story.append(Paragraph("Motivational Quote App", title))
    story.append(Spacer(1, 0.18 * inch))

    details = [
        ["Student Name", "Mohamed Ahmed Abouelenein"],
        ["Student ID", "211006095"],
        ["Email", "mohameed.ahmedd077@gmail.com"],
        ["Phone Number", "+201028239305"],
        ["GitHub Repository", "https://github.com/mosb23/Quote-App"],
        ["Project Type", "Flutter / Dart mobile application"],
    ]
    table = Table(details, colWidths=[1.7 * inch, 4.8 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EEF2FF")),
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#1F2A78")),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("LEADING", (0, 0), (-1, -1), 14),
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#CBD5E1")),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 0.35 * inch))

    add_heading(story, "Short Explanation", heading)
    explanation = (
        "This Flutter app displays motivational quotes one at a time. It uses "
        "MaterialApp, Scaffold, AppBar, StatefulWidget, a List<String> for the "
        "quotes, another list for the related local image assets, and an integer "
        "currentIndex. When the user presses the Next Quote button, setState "
        "updates currentIndex using modulo so the app returns to the first quote "
        "after the last one. The design uses a light background, centered layout, "
        "a motivational icon, rounded Card, readable typography, and local images."
    )
    story.append(Paragraph(explanation, body))
    story.append(Spacer(1, 0.25 * inch))

    add_heading(story, "Submission Contents", heading)
    contents = (
        "This PDF includes emulator screenshots of the app output, the full "
        "lib/main.dart source code, and a short explanation of how the app works."
    )
    story.append(Paragraph(contents, subtitle))

    screenshots = sorted(SCREENSHOT_DIR.glob("Screenshot 2026-05-31 *.png"))
    for index, screenshot in enumerate(screenshots, start=1):
        story.append(PageBreak())
        add_heading(story, f"App Screenshot {index}", heading)
        story.append(scaled_image(screenshot, max_width=6.15 * inch, max_height=8.45 * inch))
        story.append(Spacer(1, 0.1 * inch))
        story.append(Paragraph(f"Emulator output showing quote screen {index}.", caption))

    code = MAIN_DART.read_text(encoding="utf-8")
    story.append(PageBreak())
    add_heading(story, "Source Code - lib/main.dart", heading)

    wrapped_lines = []
    for line_number, line in enumerate(code.splitlines(), start=1):
        numbered = f"{line_number:>3}  {line}"
        wrapped = textwrap.wrap(
            numbered,
            width=96,
            subsequent_indent="     ",
            replace_whitespace=False,
            drop_whitespace=False,
        )
        wrapped_lines.extend(wrapped or [numbered])

    lines_per_page = 72
    for start in range(0, len(wrapped_lines), lines_per_page):
        if start:
            story.append(PageBreak())
            add_heading(story, "Source Code - lib/main.dart continued", heading)
        chunk = "\n".join(wrapped_lines[start : start + lines_per_page])
        story.append(Preformatted(chunk, code_style))

    doc.build(story)
    return OUTPUT


if __name__ == "__main__":
    print(build_pdf())
