# Generated by Django 2.2.7 on 2020-04-21 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200421_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(default='', max_length=500),
        ),
    ]