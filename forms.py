from django import forms
from .models import Contact  # Ensure your model exists

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']