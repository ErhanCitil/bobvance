# Generated by Django 3.2.21 on 2023-10-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_auto_20231010_1508"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(
                decimal_places=0, default=0, max_digits=5
            ),
        ),
    ]
