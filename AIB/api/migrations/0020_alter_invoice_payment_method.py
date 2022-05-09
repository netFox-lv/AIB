# Generated by Django 4.0.3 on 2022-05-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_invoice_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_method',
            field=models.TextField(choices=[('Online', 'Online'), ('Cash on delivery', 'On  Delivery'), ('Cash before delivery', 'Cash Before Delivery')], default='Online'),
        ),
    ]