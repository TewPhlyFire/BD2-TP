from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(label="Reintroduzir Password", widget=forms.PasswordInput(attrs={'placeholder': 'Reintroduzir Password'}))
    morada = forms.CharField(label="Morada", max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Morada'}))
    contacto = forms.CharField(label="Contacto", max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Contacto'}))
