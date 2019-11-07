from django.views.generic import ListView, DetailView, FormView

from product.models import Product, Category


class ProductMainPageView(ListView):
    queryset = Product.objects.order_by('-views')[:4]
    context_object_name = 'products'
    template_name = 'product/main.html'


class ProductAllView(ListView):
    model = Product
    template_name = 'product/all.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        if self.kwargs.get('slug', False) != 'all':
            queryset = queryset.filter(categories__category=self.kwargs['slug'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'slug': self.kwargs['slug'],
            'categories': Category.objects.exclude(category=self.kwargs['slug'])
        })
        return context


class ProductAddView(FormView):
    pass


class ProductAboutView(DetailView):
    pass
