# Generated by Django 4.2.6 on 2023-10-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Publish",
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
                ("title", models.CharField(max_length=20)),
                ("content", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="upload/")),
            ],
        ),
    ]
