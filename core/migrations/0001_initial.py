# Generated by Django 4.2.4 on 2023-09-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FileUploads",
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
                ("file", models.FileField(upload_to="files/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
