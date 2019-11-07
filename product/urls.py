from django.urls import path
from .views import ProductMainPageView, ProductAllView

app_name = 'product'

urlpatterns = (
    path('main/', ProductMainPageView.as_view(), name='main'),
    path('products/<str:slug>/', ProductAllView.as_view(), name='all'),
    # path('products/<str:slug>/', ProductAllView.as_view(), name='sort_by'),
)
