# Generated by Django 4.2.1 on 2023-08-13 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0014_alter_video_resource_alter_video_video_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video",
            field=models.FileField(default=None, upload_to="videos/"),
        ),
        migrations.AlterField(
            model_name="video",
            name="video_url",
            field=models.URLField(default=None),
        ),
    ]
