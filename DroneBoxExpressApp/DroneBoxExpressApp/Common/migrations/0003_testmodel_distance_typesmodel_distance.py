# Generated by Django 4.2.1 on 2023-07-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0002_typesmodel_alter_testmodel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='distance',
            field=models.IntegerField(default=59),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='typesmodel',
            name='distance',
            field=models.IntegerField(default=59),
            preserve_default=False,
        ),
    ]