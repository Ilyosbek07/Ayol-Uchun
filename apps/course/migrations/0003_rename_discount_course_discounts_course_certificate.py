# Generated by Django 4.2.1 on 2023-08-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0002_remove_course_certificate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="discount",
            new_name="discounts",
        ),
        migrations.AddField(
            model_name="course",
            name="certificate",
            field=models.FileField(blank=True, null=True, upload_to="certificates/"),
        ),
    ]
