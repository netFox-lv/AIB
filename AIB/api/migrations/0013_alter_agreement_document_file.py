# Generated by Django 4.0.3 on 2022-04-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_agreement_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='document_file',
            field=models.FileField(blank=True, upload_to='agreements'),
        ),
    ]