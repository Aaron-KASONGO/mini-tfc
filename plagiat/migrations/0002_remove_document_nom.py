# Generated by Django 4.1.1 on 2022-09-10 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plagiat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='nom',
        ),
    ]
