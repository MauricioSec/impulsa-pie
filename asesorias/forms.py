from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    nombre_completo = forms.CharField(max_length=150, required=True, label="Nombre Completo")
    email = forms.EmailField(required=True, label="Correo Electrónico")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono de Contacto")
    institucion_educativa = forms.CharField(max_length=200, required=True, label="Institución Educativa / Colegio")
    rol = forms.ChoiceField(choices=Usuario.ROL_CHOICES, required=True, label="Su Rol / Cargo")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        """Valida que el correo electrónico sea único en el sistema."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado en la plataforma.")
        return email