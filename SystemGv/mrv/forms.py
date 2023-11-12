# forms.py

from django import forms
from .models import Receituario

class ReceituarioForm(forms.ModelForm):
    class Meta:
        model = Receituario
        fields = ['paciente_nome', 'medico_nome', 'medicamentos']
