# Generated by Django 5.1.3 on 2025-02-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food_items",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_name", models.CharField(max_length=200)),
                ("item_desc", models.CharField(max_length=200)),
                ("item_price", models.IntegerField()),
            ],
        ),
    ]
