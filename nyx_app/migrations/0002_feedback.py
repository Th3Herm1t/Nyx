# Generated by Django 5.0.1 on 2024-01-22 20:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nyx_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("feedback_text", models.TextField()),
                (
                    "user_input",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nyx_app.userinput",
                    ),
                ),
            ],
        ),
    ]
