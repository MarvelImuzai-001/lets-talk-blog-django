# Generated by Django 5.1.1 on 2024-09-11 07:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0005_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="Comment",
            new_name="comment",
        ),
    ]
