# Generated by Django 4.2.1 on 2023-07-24 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commercial', '0005_alter_ordersmodel_order_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='weight',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(50.0)]),
        ),
    ]