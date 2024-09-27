# Generated by Django 5.0.6 on 2024-08-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_invoice', '0013_alter_sales_entry_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_type', models.CharField(max_length=50, unique=True)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Tax Percentage(%)')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]