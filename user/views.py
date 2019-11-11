from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView

from cart.models import Cart
from user.forms import UserUpdateForm, UserLoginForm
from user.models import User


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm


class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'


class UserRegisterView(CreateView):
    """
    Creates new user if form is valid and hashes it's password
    """
    model = User
    template_name = 'user/register.html'
    success_url = reverse_lazy('product:main')
    fields = (
        'username',
        'email',
        'password',
    )

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                            )
        Cart.objects.create(user_id=user.id)
        login(self.request, user)
        return super().form_valid(form)


class UserProfileView(DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'user'

    # def get_queryset(self):
    #     return User.objects.get(id=self.request.user.id)


class UserProfileEditView(UpdateView):
    model = User
    template_name = 'user/update.html'
    context_object_name = 'user'
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse_lazy('user:profile', args=[self.kwargs['slug']])
