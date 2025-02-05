from django import forms
from .models import Cliente

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nif_cliente', 'pnome_cliente', 'unome_cliente', 'contacto_tel', 'morada', 'mail', 'password_client']
    