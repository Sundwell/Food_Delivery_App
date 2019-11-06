from django.urls import path
from .views import ProductMainPageView

app_name = 'product'

urlpatterns = (
    path('shop/main', ProductMainPageView.as_view(), name='main'),
)
