# Generated by Django 2.2.7 on 2020-08-06 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
    ]
