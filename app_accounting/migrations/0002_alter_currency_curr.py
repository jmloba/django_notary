# Generated by Django 5.0.6 on 2024-09-19 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='curr',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]