# Generated by Django 4.0.2 on 2022-02-06 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_post_creation_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="content",
        ),
    ]
