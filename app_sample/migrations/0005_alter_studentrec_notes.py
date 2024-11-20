# Generated by Django 5.0.6 on 2024-11-20 02:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sample', '0004_studentrec_notes_alter_studentrec_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrec',
            name='notes',
            field=models.CharField(blank=True, max_length=2000, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]+$', message='only AlphaNumeric are allowed')]),
        ),
    ]