from django import forms
from .models import Ribbons, Paints, Tempaltes

class RibbonsCreate(forms.ModelForm):
    class Meta:
        model = Ribbons
        fields = ('color', 'length', 'base_price')

class PaintsCreate(forms.ModelForm):
    class Meta:
        model = Paints
        fields = ('color', 'length', 'base_price')

class TemplatesCreate(forms.ModelForm):
    class Meta:
        model = Tempaltes
        fields = ('image',)