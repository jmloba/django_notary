# Generated by Django 5.0.6 on 2024-08-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_notary', '0017_posted_transaction_file_serials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notarized_documents',
            name='date_posted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]