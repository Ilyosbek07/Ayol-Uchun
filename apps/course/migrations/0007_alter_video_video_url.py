# Generated by Django 4.2.1 on 2023-08-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0006_alter_video_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video_url",
            field=models.URLField(blank=True),
        ),
    ]