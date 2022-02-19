# Generated by Django 4.0.2 on 2022-02-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("post_id", models.IntegerField()),
                ("author_name", models.CharField(max_length=700)),
                ("content", models.CharField(max_length=500)),
                ("creation_date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=400)),
                ("content", models.TextField()),
                ("link", models.URLField()),
                ("creation_date", models.DateField(auto_now=True)),
                ("upvotes", models.IntegerField(default=0)),
                ("author_name", models.CharField(max_length=700)),
            ],
        ),
    ]
