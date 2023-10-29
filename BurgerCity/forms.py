from django import forms
from .models import contactForm


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = contactForm
        fields = ['email', 'userQuestion']
