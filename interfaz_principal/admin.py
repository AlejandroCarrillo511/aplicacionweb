from django.contrib import admin
from .models import contacto

# registering the model
class contactos_mostrar(admin.ModelAdmin):
    list_display = ["nombre", "correo", "telefono", "asunto", "mensaje"]

admin.site.register(contacto, contactos_mostrar)