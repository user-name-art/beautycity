from django import forms
from django_svg_image_form_field import SvgAndImageFormField

from beautycityapp.models import (
    Studio,
    Service,
    Master,
    Client
)


class StudioForm(forms.ModelForm):
    class Meta:
        model = Studio
        exclude = []
        field_classes = {
            "photo": SvgAndImageFormField,
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = []
        field_classes = {
            "picture": SvgAndImageFormField,
        }


class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        exclude = []
        field_classes = {
            "photo": SvgAndImageFormField,
        }


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    verification_method = forms.ChoiceField(
        choices=Client.VERIFICATION_TYPE,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Client
        fields = ('phone_number', 'password', 'verification_method')


class UserLoginForm(forms.Form):
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
