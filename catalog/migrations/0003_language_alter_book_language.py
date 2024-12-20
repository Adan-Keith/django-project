# Generated by Django 4.2.11 on 2024-03-19 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_book_language"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
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
        migrations.AlterField(
            model_name="book",
            name="language",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="catalog.language",
            ),
        ),
    ]
