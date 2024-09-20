from reportlab.pdfgen import canvas
from rest_framework.response import Response

def hello(c):
    c.drawString(1, 2,"Hello World")
c = canvas.Canvas("treino.pdf")
hello(c)
c.showPage()
c.save()

def generate_pdf(title:str, text:str,name_freelancer:str, date_finished:str):
    print('Erro em pdf')
    data: list = [title, text, name_freelancer, date_finished]
    pdf = canvas.Canvas(f"{data[0]}.pdf")
    x = 1
    y = 1
    for row in data:
        pdf.drawString(x, y, row)
        x+=1
        y+=1
    pdf.showPage()
    pdf.save()
    return Response("O pdf foi gerado", pdf)

        

        
        
        