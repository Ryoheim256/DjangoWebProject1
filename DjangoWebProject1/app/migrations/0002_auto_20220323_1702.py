# Generated by Django 2.2.27 on 2022-03-23 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 3, 23, 17, 2, 11, 644455), verbose_name='Опубликовано'),
        ),
    ]
