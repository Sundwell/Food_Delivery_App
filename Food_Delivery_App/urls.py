from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from django.views.generic import TemplateView

from order.views import ThanksPage
from product.models import Product

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('user.urls', namespace='user')),
    path('', TemplateView.as_view(template_name='index.html'), name='main'),
    path('shop/', include('product.urls', namespace='product')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('shop/', include('cart.urls', namespace='cart')),
    path('shop/cart/', include('order.urls', namespace='order')),
    path('thanks/', ThanksPage.as_view(), name='thanks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
