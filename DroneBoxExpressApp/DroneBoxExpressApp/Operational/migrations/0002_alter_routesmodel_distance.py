# Generated by Django 4.2.1 on 2023-07-22 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operational', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routesmodel',
            name='distance',
            field=models.FloatField(editable=False, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]