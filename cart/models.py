from django.core.validators import MinValueValidator
from django.db import models
from django_extensions.db.fields.json import JSONField

from product.models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        'user.User',
        on_delete=models.CASCADE,
        related_name='cart',
    )

    products = JSONField(
        default={},
        blank=True
    )

    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0, 'Wrong cost')],
        default=0,
    )

    def refresh(self):
        self.cost = 0
        self.products = {}
        self.save()

    def count_products(self):
        count = 0
        for key, value in self.products.items():
            count += value
        return count

    def __str__(self):
        return f'{self.user.username}\'s cart'
