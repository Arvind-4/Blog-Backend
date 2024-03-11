from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

from posts.utils import (
    get_read_time,
    save_images,
)

# Create your models here.

post_images_directory_name = "post-images"
author_profile_images_directory_name = "author-profile-images"


def post_images_directory_path(instance, file_name):
    return save_images(file_name=file_name, directory_name=post_images_directory_name)


def author_profile_images_directory_path(instance, file_name):
    return save_images(
        file_name=file_name, directory_name=author_profile_images_directory_name
    )


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        self.tag = slugify(self.tag)
        return super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    author = models.CharField(max_length=225)

    author_profile_image = models.ImageField(
        blank=True,
        null=True,
        width_field="width_field_author",
        height_field="height_field_author",
        upload_to=author_profile_images_directory_path,
    )

    width_field_author = models.IntegerField(default=100)
    height_field_author = models.IntegerField(default=100)

    image_field = models.ImageField(
        blank=True,
        null=True,
        width_field="width_field",
        height_field="height_field",
        upload_to=post_images_directory_path,
    )

    tags = models.ManyToManyField(Tag, blank=True)
    width_field = models.IntegerField(default=400)
    height_field = models.IntegerField(default=400)
    image_alt = models.CharField(max_length=225, blank=True)
    reading_time = models.CharField(max_length=225, blank=True)
    short_summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.author}"

    class Meta:
        ordering = ["-created_at", "-updated_at"]


def pre_save_slug_and_image_alt_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.image_alt = slugify(instance.title)
        instance.save()


def pre_save_reading_time_generator(sender, instance, *args, **kwargs):
    if not instance.reading_time:
        generated_time = get_read_time(str(instance.content))
        instance.reading_time = f"{generated_time} min"
        instance.save()


pre_save.connect(pre_save_slug_and_image_alt_generator, sender=Post)
pre_save.connect(pre_save_reading_time_generator, sender=Post)
