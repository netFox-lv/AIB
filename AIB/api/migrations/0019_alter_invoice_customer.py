# Generated by Django 4.0.3 on 2022-05-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_invoice_customer_invoice_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.TextField(),
        ),
    ]