from django.contrib.postgres.forms import DateRangeField
from django.core.validators import RegexValidator
from django.db import models
from django_extensions.db.fields.json import JSONField
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    ORDER_STATUSES = (
        ('done', 'Done'),
        ('in_process', 'In process'),
        ('error', 'For deleting'),
    )
    PAYMENT = (
        ('card', 'By card'),
        ('cash', 'By cash'),
        ('bonuses', 'By bonuses'),
    )
    # Relation
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    # Mandatory
    address = models.CharField(
        max_length=50,
    )
    comment = models.TextField(
        blank=True,
    )
    name = models.CharField(
        max_length=20,
    )
    phone = PhoneNumberField()
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUSES,
        default='in_process',
    )
    products = JSONField(
        default={'name': 5},
        null=True,
    )
    payment = models.CharField(
        max_length=10,
        choices=PAYMENT,
        default='cash',
    )
    # Card payment
    card_number = models.BigIntegerField(
        validators=[RegexValidator(r'^\d{16}$', 'Wrong card number')],
        help_text='Such as 1234567812345678',
        default=0000000000000000,
        blank=True,
    )
    card_date = models.CharField(
        max_length=5,
        validators=[RegexValidator(r'^\d{2}/\d{2}$', 'Wrong date')],
        help_text='Such as 11/11',
        blank=True,
    )
    card_cvs = models.IntegerField(
        validators=[RegexValidator(r'^\d{3}$')],
        help_text='Such as 913',
        default=000,
        blank=True,
    )
    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        null=True,
    )

    def __str__(self):
        return f'Order №{self.id}'
