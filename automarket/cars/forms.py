from django import forms
from .models import LeadRequest


class LeadForm(forms.ModelForm):
    class Meta:
        model = LeadRequest
        fields = ['name', 'phone', 'car', 'request_type', 'message']
        widgets = {
            'name':         forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'phone':        forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+996 (___) ___-___'}),
            'car':          forms.Select(attrs={'class': 'form-select'}),
            'request_type': forms.Select(attrs={'class': 'form-select'}),
            'message':      forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Сообщение...'}),
        }