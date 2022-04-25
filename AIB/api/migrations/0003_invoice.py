# Generated by Django 4.0.3 on 2022-03-28 07:18

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_agreement_agreement_numurs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('invoice_number', models.TextField(unique=True, validators=[api.validators.val_num])),
                ('amount', models.FloatField()),
                ('invoice_date', models.DateField()),
                ('payment_to_date', models.DateField()),
                ('payment_period', models.TextField()),
            ],
        ),
    ]