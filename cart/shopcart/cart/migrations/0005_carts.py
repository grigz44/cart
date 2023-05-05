# Generated by Django 2.2 on 2023-05-05 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_delete_carts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Grocery')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.login')),
            ],
        ),
    ]