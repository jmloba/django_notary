# Generated by Django 5.0.6 on 2024-07-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_notary', '0005_notarized_documents_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notarized_documents',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='notarized_documents',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
