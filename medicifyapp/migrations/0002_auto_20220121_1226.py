# Generated by Django 2.1 on 2022-01-21 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicifyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 21, 12, 26, 3, 89736)),
        ),
        migrations.AlterField(
            model_name='posted_jobs',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 21, 12, 26, 3, 89736)),
        ),
    ]
