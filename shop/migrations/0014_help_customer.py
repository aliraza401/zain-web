# Generated by Django 2.2.7 on 2020-08-06 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_remove_help_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Customer'),
        ),
    ]
