from reportlab.pdfgen import canvas
import os
import cloudinary, cloudinary.uploader
import io

def generate_pdf(title:str, text:str,name_freelancer:str, date_finished:str):
    pdf_buffer = io.BytesIO()
    
    pdf = canvas.Canvas(pdf_buffer)
    x = 100
    y = 750  
    data = [title, text, name_freelancer, date_finished]

    for row in data:
        pdf.drawString(x, y, row)
        y -= 20  

    pdf.save() 

    pdf_buffer.seek(0)

    upload_result = cloudinary.uploader.upload(pdf_buffer, resource_type='raw', public_id=title)

    return upload_result['secure_url']

    

    

        
        