# Generated by Django 4.0.2 on 2022-02-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_remove_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="creation_date",
            field=models.DateField(auto_now_add=True),
        ),
    ]
