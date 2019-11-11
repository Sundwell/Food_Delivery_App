from django.template import Library

register = Library()


@register.filter
def get_product_composition(product, kind):
    return product.composition[kind]