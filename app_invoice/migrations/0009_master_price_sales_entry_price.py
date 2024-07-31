# Generated by Django 5.0.6 on 2024-07-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_invoice', '0008_sales_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='sales_entry',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
