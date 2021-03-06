# Generated by Django 4.0.3 on 2022-04-04 23:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_invoice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_period_month',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_period_year',
            field=models.PositiveIntegerField(),
        ),
    ]
