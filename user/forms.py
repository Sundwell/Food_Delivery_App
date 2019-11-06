from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django_select2.forms import Select2MultipleWidget

from user.models import User


class UserLoginForm(AuthenticationForm):
    """
    changing label of username field while authorization
    """
    username = UsernameField(label='Username/Email', widget=forms.TextInput(attrs={'autofocus': True}))


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'email',
            'phone',
            'age',
            'gender',
            'categories',
            'photo',
            'birthday',
        )
        widgets = {
            'categories': Select2MultipleWidget(),
        }
        labels = {
            'categories': 'Preferences',
        }
