from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(title: str, text: str, name_freelancer: str, date_finished: str):
    data = [title, text, name_freelancer, date_finished]

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)

    x = 100
    y = 750

    for row in data:
        pdf.drawString(x, y, row)
        y -= 20  

    pdf.save()

    buffer.seek(0)

    return buffer
