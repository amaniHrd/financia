# Generated by Django 4.2.9 on 2024-03-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tab_banque",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=20)),
                ("libelle", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Tab_com",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=20)),
                ("libelle", models.CharField(max_length=255)),
            ],
        ),
    ]