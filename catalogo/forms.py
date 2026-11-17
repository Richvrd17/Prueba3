from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'categoria', 'precio', 'fecha_lanzamiento', 'disponible']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }