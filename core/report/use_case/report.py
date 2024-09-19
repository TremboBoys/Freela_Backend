import os
from rest_framework.response import Response
from rest_framework import status
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from django.conf import settings

def generate_pdf(title, text, date_finished, price, name_freelancer):
    print("Estou sendo chamado")
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'reports',  'relatorio_reportlab.pdf')
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    pdf = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    
    pdf.setFont("Helvetica", 16)
    pdf.drawString(100, height - 50, "ManoPotas ataca novamente")

    pdf.setFont("Helvetica", 12)

    data = [
        [title, text, date_finished, price, name_freelancer]
    ]

    x_offset = 100
    y_offset = height - 100
    padding = 15

    for row in data:
        print(row)
        for col_num, item in enumerate[row]:
            pdf.drawString(x_offset, (col_num * 100), y_offset, item)
            print(d)
        y_offset -= padding

        pdf.showPage()
        pdf.save()
        with open(pdf_path, 'rb') as pdf_file:
            response = Response(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio_reportlab.pdf"'

        return response