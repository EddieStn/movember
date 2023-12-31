# Generated by Django 4.2.7 on 2023-11-25 00:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("fullname", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("interests", models.CharField(max_length=250)),
                ("bio", models.TextField(max_length=500)),
                (
                    "why_you_want_to_become_a_facilitator",
                    models.TextField(max_length=500),
                ),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
