from django import forms
from django_svg_image_form_field import SvgAndImageFormField

from beautycityapp.models import (
    Studio,
    Service,
    Master
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
