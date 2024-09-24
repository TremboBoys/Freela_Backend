from reportlab.pdfgen import canvas
import os
import cloudinary, cloudinary.uploader
import io
from django.conf import settings
import os

def generate_pdf(title:str, text:str,name_freelancer:str, date_finished:str):
    data = [title, text, name_freelancer, date_finished]
    print("Chad")

    x = 100
    y = 750  
    pdf = canvas.Canvas(f"{data[0]}.pdf")

    for row in data:
        pdf.drawString(x, y, row)
        y -= 20  
    pdf.save() 
    return pdf
