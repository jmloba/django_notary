# Generated by Django 5.0.6 on 2024-08-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_notary', '0015_notarized_documents_is_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='notarized_documents',
            name='date_posted',
            field=models.DateField(blank=True, null=True),
        ),
    ]