# Generated by Django 4.2.9 on 2024-03-31 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_tab_com_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="tab_aux",
            name="date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]