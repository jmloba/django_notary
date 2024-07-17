# Generated by Django 5.0.6 on 2024-07-17 00:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_import', '0002_phil_city_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phil_Province_Towns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=80)),
                ('towns', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
