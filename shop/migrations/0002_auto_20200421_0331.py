# Generated by Django 2.2.7 on 2020-04-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=70),
        ),
    ]