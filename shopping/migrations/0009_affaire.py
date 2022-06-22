# Generated by Django 4.0.3 on 2022-06-20 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_remove_toastmessage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_end', models.DateTimeField(verbose_name='la date TERMINE ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product', verbose_name='produit')),
            ],
        ),
    ]
