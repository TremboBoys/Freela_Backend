from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

def generate_pdf(title: str, text: str, name_freelancer: str, date_finished: str):
    data = [text, name_freelancer, date_finished]

    buffer = BytesIO()  
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    margin_top = 30
    margin_bottom = 80

    # Desenha o título no topo da página
    pdf.drawCentredString(width / 2, height - margin_top - 30, title)

    x = 40  
    y = height - margin_top - 70

    # Adiciona uma margem inicial e um espaço para parágrafo para data[0]
    y -= 30  # Adiciona uma margem inicial
    for line in wrap_text(data[0], width - 80, pdf):  # Apenas para data[0]
        pdf.drawString(x, y, line)
        y -= 20

    # Atualiza a posição para o próximo bloco de texto
    y -= 10  # Adiciona espaço extra entre os parágrafos

    # Renderiza os outros dados
    for i, row in enumerate(data[1:], start=1):  # Começa em 1 para ignorar o primeiro item
        for line in wrap_text(row, width - 80, pdf):
            if i == 1:
                pdf.drawString(x, y, f"Freelancer: {line}")
            elif i == 2:
                pdf.drawString(x, y, f"Price: {line}")
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
