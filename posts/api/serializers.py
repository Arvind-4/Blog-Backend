from rest_framework import serializers

from posts.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("tag",)


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "author",
            "image_field",
            "tags",
            "width_field",
            "height_field",
            "image_alt",
            "reading_time",
            "short_summary",
            "content",
            "draft",
            "created_at",
            "updated_at",
        )

    def get_tags(self, obj, *args, **kwargs):
        try:
            _obj = Post.objects.get(slug__iexact=obj.slug)
            return TagSerializer(_obj.tags.all(), many=True).data
        except Post.DoesNotExist:
            return TagSerializer([], many=True).data
        except Post.MultipleObjectsReturned:
            return TagSerializer([], many=True).data
        except Exception as e:
            return TagSerializer([], many=True).data
