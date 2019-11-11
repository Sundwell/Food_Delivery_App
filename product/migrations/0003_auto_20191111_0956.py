# Generated by Django 2.2.6 on 2019-11-11 09:56

from django.db import migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191108_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='carbohydrates',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fats',
        ),
        migrations.RemoveField(
            model_name='product',
            name='proteins',
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AddField(
            model_name='product',
            name='composition',
            field=django_extensions.db.fields.json.JSONField(default={}, null=True),
        ),
    ]
