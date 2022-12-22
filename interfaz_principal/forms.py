from .models import contacto
from django import forms


class contacto_form(forms.ModelForm):
  class Meta:
    model = contacto
    fields = ["nombre", "correo", "telefono", "asunto", "mensaje"]
    labels = {'nombre': "Nombre", "correo": "Correo", "telefono": "Número Teléfonico", "asunto": "Asunto", "mensaje": "Mensaje"}