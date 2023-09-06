from django import forms
from .models import Hoja

class HojaForm(forms.ModelForm):
    class Meta:
        model=Hoja
        fields = '__all__' #vamos a usar todos los campos
    