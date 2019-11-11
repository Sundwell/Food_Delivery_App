from django.contrib.postgres.forms import DateRangeField
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    ORDER_STATUSES = (
        ('done', 'Done'),
        ('in_process', 'In process'),
    )
    # Relation
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='orders',
        null=True,
        blank=True,
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
    # Card payment
    card_number = models.BigIntegerField(
        validators=[RegexValidator(r'^\d{16}$', 'Wrong card number')],
        null=True,
        help_text='Such as 1234-5678-1234-5678',
    )
    card_date = models.DateField(
        help_text='Such as 11/11',
    )
    card_cvs = models.IntegerField(
        validators=[RegexValidator(r'^\d{3}$')],
        help_text='Such as 913',
    )
