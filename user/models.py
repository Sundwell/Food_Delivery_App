import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


def get_image_path(instance, filename):
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
    phone = models.CharField(
        max_length=13,
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
        # upload_to='user/images/',
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
    activities = models.ManyToManyField('user.Activity', related_name='users')

    REQUIRED_FIELDS = ('email', 'password',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save()

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ('username',)


class Activity(models.Model):

    activity = models.CharField(max_length=25)

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name_plural = 'Activities'
