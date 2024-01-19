from django.contrib import admin

# Register your models here.
from usuarios.models import Usuario
admin.site.register(Usuario)

# para aparecer na tela admin o usuario, devemos colocar na admin.py o usuario 