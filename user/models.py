import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField


def get_image_path(instance, filename):
    """
    :param instance:    instance of object such as object 'serhii' which has slugField same as name,
                        ie serhii.slug == 'serhii'
                        type of instance: <user.models.User>

    :param filename:    just name of the file like 'apple.png'
                        type of filename: <str>

    :return: simply     returning path where django should save our file
    """
    return os.path.join('user/images/', str(instance.slug), filename)


class User(AbstractUser):
    """
    Stores a single User entry with basic customer fields.

    def save also slugify 'slug' field.
    """

    # constants for user fields
    GENDERS = (
        (None, '-'),
        ('M', 'Male'),
        ('F', 'Female'),
    )

    # user custom fields
    address = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    phone = PhoneNumberField(
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        default=''
    )
    bonuses = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        default=None,
        null=True
    )
    photo = models.ImageField(
        upload_to=get_image_path,
        default='user/images/user_default.jpg',
        null=True
    )
    age = models.IntegerField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=12,
        choices=GENDERS,
        default=None,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        null=True,
        blank=True
    )
    email = models.EmailField(
        'email address',
        unique=True,
    )
    EMAIL_FIELD = 'email'
    is_staff = models.BooleanField(
        default=False,
        blank=False,
        null=True,
        help_text='Staff can Add products and send requests for removing products',
    )
    categories = models.ManyToManyField(
        'product.Category',
        blank=True,
        related_name='users',
    )
    REQUIRED_FIELDS = ('email', 'password',)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ('username', 'email')
