from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

def generate_pdf(title: str, text: str, name_freelancer: str, price: float):
    print("Olá")
    data = [text, name_freelancer, price]

    buffer = BytesIO()  
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    margin_top = 30
    margin_bottom = 80

    pdf.drawCentredString(width / 2, height - margin_top - 30, title)

    x = 40  
    y = height - margin_top - 70

    y -= 30 
    for line in wrap_text(data[0], width - 80, pdf):  
        pdf.drawString(x, y, line)
        y -= 20

    y -= 10  

    for i, row in enumerate(data[1:], start=1):
        for line in wrap_text(str(row), width - 80, pdf):
            if i == 1:
                pdf.drawString(x, y, f"Freelancer: {line}")
            elif i == 2:
                pdf.drawString(x, y, f"Price: R${line}")
            y -= 20 

            if y < margin_bottom:
                pdf.showPage()  
                y = height - margin_top - 70  

    pdf.save()
    buffer.seek(0)
    return buffer

def wrap_text(text: str, max_width: float, pdf_canvas: canvas.Canvas) -> list:
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        if pdf_canvas.stringWidth(test_line, "Helvetica", 12) <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))  
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines
