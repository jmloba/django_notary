# Generated by Django 5.0.6 on 2024-07-17 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_import', '0003_phil_province_towns'),
    ]

    operations = [
        migrations.AddField(
            model_name='phil_province_towns',
            name='barangay_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phil_province_towns',
            name='municipal_class',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
