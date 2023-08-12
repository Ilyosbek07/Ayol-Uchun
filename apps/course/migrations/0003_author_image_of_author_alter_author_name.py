# Generated by Django 4.2.1 on 2023-08-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0002_alter_course_discount"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="image_of_author",
            field=models.ImageField(default="/default.jpg", upload_to="author/images"),
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(default="User", max_length=300),
        ),
    ]