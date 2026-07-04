from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf(url: str, analysis: str, filename="report.pdf"):
    file_path = filename
    c = canvas.Canvas(file_path, pagesize=letter)

    width, height = letter
    y = height - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Geko AI - Company Research Report")

    y -= 30
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated on: {datetime.now()}")

    y -= 20
    c.drawString(50, y, f"Source URL: {url}")

    y -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "AI Analysis:")

    y -= 20
    c.setFont("Helvetica", 9)

    lines = analysis.split("\n")
    max_chars = 90

    for line in lines:

        while len(line) > max_chars:
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 9)

            c.drawString(50, y, line[:max_chars])
            line = line[max_chars:]
            y -= 15

        if y < 50:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 9)

        c.drawString(50, y, line)
        y -= 15

    c.save()

    return file_path