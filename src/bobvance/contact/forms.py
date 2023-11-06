from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Erhan"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "erhan@maykinmedia.nl",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Dit is een test bericht!",
                }
            ),
        }
