from django import forms

from bobvance.base.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "firstname",
            "lastname",
            "email",
            "phonenumber",
            "address",
            "postal_code",
            "city",
            "country",
        ]
        widgets = {
            "firstname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Erhan"}
            ),
            "lastname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Citil"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "erhancitil94@gmail.com",
                }
            ),
            "phonenumber": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+31 6 12345678",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Straatnaam 123",
                }
            ),
            "postal_code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "1234 AB"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Amsterdam"}
            ),
            "country": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nederland"}
            ),
        }
        labels = {
            "firstname": "Voornaam",
            "lastname": "Achternaam",
            "email": "Email",
            "phonenumber": "Telefoonnummer",
            "address": "Adres",
            "postal_code": "Postcode",
            "city": "Stad",
            "country": "Land",
        }
