# Generated by Django 5.0.6 on 2024-08-01 03:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_invoice', '0011_sales_entry_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_entry',
            name='itemnumber',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sales_entry',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(1)]),
        ),
    ]