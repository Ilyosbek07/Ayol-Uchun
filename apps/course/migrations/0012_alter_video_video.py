# Generated by Django 4.2.1 on 2023-08-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0011_alter_video_resource_alter_video_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video",
            field=models.FileField(blank=True, default=None, upload_to="videos/"),
        ),
    ]
