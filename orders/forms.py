from django import forms
from .models import Orders


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['ribbon', 'paint', 'template', 'class_list', 'teacher_name',
                'deploy', 'school', 'class_number', 'client_phone',
                'count', 'rhinestones', 'count_rhinestones', 'address']