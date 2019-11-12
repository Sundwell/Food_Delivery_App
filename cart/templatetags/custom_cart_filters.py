from django.template import Library

from product.models import Product

register = Library()


@register.filter
def get_product_photo_url(name):
    return Product.objects.get(name=name).main_photo.url


@register.filter
def get_product_price(name):
    return Product.objects.get(name=name).price
