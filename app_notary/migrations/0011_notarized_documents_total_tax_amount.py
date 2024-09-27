# Generated by Django 5.0.6 on 2024-08-06 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_notary', '0010_notarized_documents_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notarized_documents',
            name='total_tax_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
