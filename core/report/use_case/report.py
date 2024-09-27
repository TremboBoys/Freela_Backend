from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

def generate_pdf(title: str, text: str, name_freelancer: str, date_finished: str):
    data = [text, name_freelancer, date_finished]

    buffer = BytesIO()  

    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4

    margin_top = 30
    margin_sides_bottom = 80

    pdf.drawCentredString(width / 2, height - margin_top - 30, title)

    x = margin_sides_bottom
    y = height - margin_top - 70

    for row in data:
        pdf.drawString(x, y, row)
        y -= 20

    pdf.save()

    buffer.seek(0)

    return buffer


