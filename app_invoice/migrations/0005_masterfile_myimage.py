# Generated by Django 5.0.6 on 2024-07-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_invoice', '0004_alter_category_sales_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterfile',
            name='myimage',
            field=models.ImageField(blank=True, null=True, upload_to='myimages/'),
        ),
    ]