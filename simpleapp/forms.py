from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'discription',
            'category',
            'price',
            'quantity',
        ]

    def clean(self):
        cleaned_data = super().clean()
        discription = cleaned_data.get("discription")
        if discription is not None and len(discription) < 20:
            raise ValidationError({
                "discription": "Описание не может быть менее 20 символов."
            })

        name = cleaned_data.get("name")
        if name == discription:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data
    