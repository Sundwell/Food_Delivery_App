from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from cart.models import Cart
from order.forms import CheckoutForm, CardPaymentForm
from order.models import Order
from product.models import Product
from user.models import User


class CheckoutView(CreateView):
    model = Order
    template_name = 'order/checkout.html'
    form_class = CheckoutForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.request.user.slug
        context['cost'] = self.request.user.cart.cost
        return context

    def get_initial(self):
        initial = {
            'name': self.request.user.name,
            'address': self.request.user.address,
            'phone': self.request.user.phone,
            'user': self.request.user,
            'products': self.request.user.cart.products,
            'cost': self.request.user.cart.cost
        }
        return initial

    def get_success_url(self):
        return reverse_lazy('user:profile', args=[self.request.user.slug])

    def form_valid(self, form):
        if self.request.POST.get('payment') == 'cash':
            self.request.user.bonuses += self.request.user.cart.cost / 100
            self.request.user.save()
            self.request.user.cart.refresh()
            return super().form_valid(form)
        elif self.request.POST.get('payment') == 'bonuses':
            if self.request.user.bonuses >= self.request.user.cart.cost:
                user = User.objects.get(id=self.request.user.id)
                user.bonuses -= self.request.user.cart.cost
                user.save()
                self.request.user.cart.refresh()
                return super().form_valid(form)
            else:
                messages.add_message(self.request, messages.INFO, 'Not enough bonuses')
                return redirect(reverse_lazy('order:checkout'))
        else:
            order = form.save(commit=False)
            order.status = 'error'
            order.save()
            super().form_valid(form)
            return redirect(reverse_lazy('order:card', args=[self.request.user.orders.last().id]))


class PayByCard(UpdateView):
    template_name = 'order/card_payment.html'
    model = Order
    form_class = CardPaymentForm
    initial = {'status': 'in_process'}

    def get_success_url(self):
        return reverse_lazy('user:profile', args=[self.request.user.slug])

    def form_valid(self, form):
        self.request.user.bonuses += self.request.user.cart.cost / 100
        self.request.user.save()
        self.request.user.cart.refresh()
        return super().form_valid(form)


class ThanksPage(ListView):
    template_name = 'thanks.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.order_by('-created')[:5]

