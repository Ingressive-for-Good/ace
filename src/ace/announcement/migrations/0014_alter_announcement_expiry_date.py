# Generated by Django 3.2.6 on 2021-10-29 10:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0013_alter_announcement_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 10, 30, 23, 454642, tzinfo=utc)),
        ),
    ]