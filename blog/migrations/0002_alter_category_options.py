# Generated by Django 4.2.7 on 2024-07-07 05:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
    ]
