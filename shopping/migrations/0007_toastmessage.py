# Generated by Django 4.0.3 on 2022-06-20 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_imagebanner_category_imagebanner_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToastMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='toast', verbose_name='photo')),
                ('title', models.CharField(max_length=50)),
                ('date_add', models.DateTimeField(auto_now=True, verbose_name='la date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product', verbose_name='produit')),
            ],
        ),
    ]
