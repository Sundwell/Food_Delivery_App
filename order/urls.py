from django.urls import path

from order.views import CheckoutView, PayByCard

app_name = 'order'

urlpatterns = (
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('checkout/card/<int:pk>/', PayByCard.as_view(), name='card'),
)
