from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView

from user.forms import UserUpdateForm
from user.models import User


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'


class UserRegisterView(CreateView):
    """
    Creates new user if form is valid and hashes it's password
    """
    model = User
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')
    fields = (
        'username',
        'email',
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


class UserProfileEditView(UpdateView):
    model = User
    template_name = 'user/update.html'
    context_object_name = 'user'
    form_class = UserUpdateForm

    def get_success_url(self):
        success_url = self.success_url = reverse_lazy('user:profile', args=[self.kwargs['slug']])
        return success_url
