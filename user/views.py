from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, FormView, CreateView

from user.models import User


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'


class UserRegisterView(CreateView):
    model = User
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')
    fields = (
        'username',
        'email',
        'address',
        'phone',
        'password',
    )

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)


class UserProfileView(DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'user'

