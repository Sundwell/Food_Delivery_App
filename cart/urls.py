from django.urls import path

from cart.views import ViewCart, AddProduct, ClearCart

app_name = 'cart'

urlpatterns = (
    path('cart/', ViewCart.as_view(), name='cart'),
    path('ajax/cart/add/', AddProduct.as_view(), name='ajax_add'),
    path('ajax/cart/clear/', ClearCart.as_view(), name='ajax_clear'),
)
