# Generated by Django 2.2 on 2023-05-05 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20230505_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='user',
        ),
    ]