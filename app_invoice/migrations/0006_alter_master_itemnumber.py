# Generated by Django 5.0.6 on 2024-07-30 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_invoice', '0005_alter_master_itemnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='itemnumber',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]