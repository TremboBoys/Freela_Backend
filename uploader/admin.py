from django.contrib import admin

from uploader.models import Document, Image
from core.perfil.models import MyProjects

admin.site.register(Image)
admin.site.register(Document)
admin.site.register(MyProjects)
