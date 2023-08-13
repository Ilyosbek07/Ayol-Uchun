# Generated by Django 4.2.1 on 2023-08-13 01:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0010_alter_video_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="resource",
            field=models.ManyToManyField(default=None, to="course.resource"),
        ),
        migrations.AlterField(
            model_name="video",
            name="video",
            field=models.FileField(default=None, upload_to="videos/"),
        ),
    ]