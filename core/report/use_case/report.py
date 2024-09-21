from reportlab.pdfgen import canvas
from core.report.models import Pdf
from rest_framework.response import Response
from rest_framework import status
from uploader.models.document import document_file_path
import os

def generate_pdf(title:str, text:str,name_freelancer:str, date_finished:str):
    print('Erro em pdf')
    directory = 'report'
    data: list = [title, text, name_freelancer, date_finished]
    pdf_path = os.path.join(directory, f"{data[0]}.pdf")
    pdf = canvas.Canvas(pdf_path)
    x = 1
    y = 1
    for row in data:
        pdf.drawString(x, y, row)
        x+=1
        y+=1
    pdf.save()
    

        
        