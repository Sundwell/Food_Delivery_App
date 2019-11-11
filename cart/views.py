from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from cart.models import Cart
from product.models import Product


class ViewCart(ListView):
    model = Cart
    template_name = 'cart/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.get(user__id=self.request.user.id)


class AddProduct(View):

    def get(self, request):
        cart = Cart.objects.get(user__id=self.request.user.id)
        name1 = request.GET.get('name', None)
        prod_price = Product.objects.get(name=name1).price

        if name1 in cart.products:
            cart.products[name1] += 1
            cart.cost += prod_price
        else:
            cart.products.update({name1: 1})
            cart.cost += prod_price
        cart.save()
        count = cart.count_products()
        data = {
            'msg': f'{name1} has been added to you cart!',
            'count': count,
        }
        return JsonResponse(data)


class ClearCart(View):

    def get(self, request):
        print('aaaa')
        id1 = request.GET.get('id', None)
        ca = Cart.objects.get(id=id1)
        ca.products.clear()
        ca.cost = 0
        ca.save()
        data = {
            'msg': 'Cart cleared',
        }
        return JsonResponse(data)
