# Generated by Django 4.1.1 on 2022-09-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagiat', '0002_remove_document_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='percent',
            field=models.IntegerField(null=True),
        ),
    ]