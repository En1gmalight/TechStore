# Generated by Django 5.1 on 2024-08-29 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("name", models.CharField(max_length=100)),
                (
                    "email",
                    models.EmailField(
                        max_length=254, primary_key=True, serialize=False
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="iPhoneCategory",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="iPhoneModel",
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
                ("name", models.CharField(max_length=100)),
                ("memory", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.iphonecategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="review",
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
                ("title", models.CharField(max_length=250)),
                ("content", models.TextField()),
                (
                    "post_type",
                    models.CharField(
                        choices=[("c", "copyright"), ("p", "public")], max_length=1
                    ),
                ),
                ("issued", models.DateTimeField()),
                ("image", models.ImageField(upload_to="uploads")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.author"
                    ),
                ),
            ],
        ),
    ]
