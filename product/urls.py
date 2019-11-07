from django.urls import path
from .views import ProductMainPageView, ProductAllView, ProductAboutView

app_name = 'product'

urlpatterns = (
    path('main/', ProductMainPageView.as_view(), name='main'),
    path('products/<str:slug>/', ProductAllView.as_view(), name='all'),
    path('products/<int:pk>/about/', ProductAboutView.as_view(), name='about'),
)
