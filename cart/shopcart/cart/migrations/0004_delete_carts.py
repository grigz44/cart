# Generated by Django 2.2 on 2023-05-05 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_carts_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Carts',
        ),
    ]
