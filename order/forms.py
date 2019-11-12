from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.forms import HiddenInput, RadioSelect

from order.models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'user',
            'name',
            'address',
            'phone',
            'comment',
            'payment',
            'products',
            'cost',
        )
        widgets = {
            'user': HiddenInput,
            'products': HiddenInput,
            'payment': RadioSelect,
            'cost': HiddenInput,
        }


class CardPaymentForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'card_number',
            'card_date',
            'card_cvs',
            'status',
        )
        widgets = {
            'card_date': DatePickerInput(format='%m/%y'),
            'status': HiddenInput,
        }
