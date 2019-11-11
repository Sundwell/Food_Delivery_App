from django.template import Library

from product.models import Product

register = Library()


@register.filter
def get_product_photo_url(name):
    try:
        return Product.objects.get(name=name).main_photo.url
    except (AttributeError, Product.DoesNotExist, Product.MultipleObjectsReturned):
        return None


@register.filter
def get_product_price(name):
    try:
        return Product.objects.get(name=name).price
    except (AttributeError, Product.DoesNotExist, Product.MultipleObjectsReturned):
        return None
