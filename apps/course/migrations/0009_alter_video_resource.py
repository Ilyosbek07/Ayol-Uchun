# Generated by Django 4.2.1 on 2023-08-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0008_alter_video_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="resource",
            field=models.ManyToManyField(blank=True, to="course.resource"),
        ),
    ]