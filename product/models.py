from django.core.validators import MinValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel
from product.add_functions import get_additional_images_path, get_image_path


class Product(TimeStampedModel, models.Model):
    # Relations
    categories = models.ManyToManyField(
        'product.Category',
        related_name='products',
    )
    user = models.ForeignKey(
        'user.User',
        on_delete=models.SET_NULL,
        related_name='products',
        null=True,
        blank=True,
    )
    # Main
    name = models.CharField(
        max_length=20,
        unique=True
    )
    description = models.TextField(default='No description')
    short_description = models.CharField(
        max_length=200,
        default='No description'
    )
    main_photo = models.ImageField(
        upload_to=get_image_path,
        default='product/images/no_image.png'
    )
    price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0, 'Wrong price')]
    )
    # Composition
    weight = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(0, 'Wrong weight')],
        default=0,
        null=True,
    )
    calories = models.PositiveIntegerField(
        verbose_name='Calories',
        default=0,
        null=True,
    )
    carbohydrates = models.PositiveIntegerField(
        default=0,
        null=True,
    )
    proteins = models.PositiveIntegerField(
        default=0,
        null=True,
    )
    fats = models.PositiveIntegerField(
        default=0,
        null=True,
    )
    # Additional
    views = models.IntegerField(default=0)
    to_remove = models.BooleanField(verbose_name='Marked for deleting', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'


class Image(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='add_photos'
    )
    image = models.ImageField(upload_to=get_additional_images_path)

    def __str__(self):
        return f'Belongs to: {self.product.name}'

    class Meta:
        verbose_name_plural = 'images'


class Category(models.Model):
    category = models.CharField(max_length=30)
    image = models.ImageField(default='product/images/no_image.png')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'categories'
