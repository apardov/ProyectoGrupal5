# se debe importar forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# se debe importar el modelo creado anterirormente
from .models import Proveedores


class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['rut_proveedor', 'nombre_proveedor', 'nombre_representante', 'telefono', 'comuna', 'direccion']

class RegistroUsuariosForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
