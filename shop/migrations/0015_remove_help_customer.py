# Generated by Django 2.2.7 on 2020-08-06 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_help_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='help',
            name='customer',
        ),
    ]
