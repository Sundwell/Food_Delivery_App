from django.urls import path

from user.views import UserProfileView
from .views import UserLogoutView, UserLoginView, UserRegisterView


app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<slug:slug>/', UserProfileView.as_view(), name='profile'),
]