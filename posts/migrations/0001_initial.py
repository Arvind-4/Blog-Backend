# Generated by Django 3.2.9 on 2021-12-13 13:44

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225, unique=True)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("author", models.CharField(max_length=225)),
                (
                    "author_profile_image",
                    models.ImageField(
                        blank=True,
                        height_field="height_field_author",
                        null=True,
                        upload_to=posts.models.author_profile_images_directory_path,
                        width_field="width_field_author",
                    ),
                ),
                ("width_field_author", models.IntegerField(default=100)),
                ("height_field_author", models.IntegerField(default=100)),
                (
                    "image_field",
                    models.ImageField(
                        blank=True,
                        height_field="height_field",
                        null=True,
                        upload_to=posts.models.post_images_directory_path,
                        width_field="width_field",
                    ),
                ),
                ("width_field", models.IntegerField(default=400)),
                ("height_field", models.IntegerField(default=400)),
                ("image_alt", models.CharField(blank=True, max_length=225)),
                ("reading_time", models.CharField(blank=True, max_length=225)),
                ("short_summary", models.TextField()),
                ("content", models.TextField()),
                ("draft", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("tags", models.ManyToManyField(blank=True, to="posts.Tag")),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
            },
        ),
    ]
