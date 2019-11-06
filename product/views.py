from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from product.models import Product


class ProductMainPageView(ListView):
    pass


class ProductAllView(ListView):
    pass


class ProductAddView(FormView):
    pass


class ProductAboutView(DetailView):
    pass
