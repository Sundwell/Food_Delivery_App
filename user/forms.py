from django import forms

from user.models import User


class UserUpdateForm(forms.ModelForm):
    activities = forms.ModelMultipleChoiceField

    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'phone',
            'age',
            'gender',
            'activities',
            'photo',
            'birthday',
        )
