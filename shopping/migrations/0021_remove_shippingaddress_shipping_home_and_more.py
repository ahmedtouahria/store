# Generated by Django 4.0.3 on 2022-06-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0020_shippingaddress_shipping_home'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='shipping_home',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='is_stopdesk',
            field=models.BooleanField(default=True),
        ),
    ]
