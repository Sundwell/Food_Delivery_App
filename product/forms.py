from django import forms
from django.core.validators import MinValueValidator


class CompositionAdminForm(forms.ModelForm):
    weight = forms.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(0, 'Wrong value')],
        initial=0,
    )
    calories = forms.IntegerField(
        validators=[MinValueValidator(0, 'Wrong value')],
        initial=0,
    )
    carbohydrates = forms.IntegerField(
        validators=[MinValueValidator(0, 'Wrong value')],
        initial=0,
    )
    proteins = forms.IntegerField(
        validators=[MinValueValidator(0, 'Wrong value')],
        initial=0,
    )
    fats = forms.IntegerField(
        validators=[MinValueValidator(0, 'Wrong value')],
        initial=0,
    )