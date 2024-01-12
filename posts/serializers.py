from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()

    def validate_image(self, value):
      if value.size > 1024 * 1024 * 2:
        raise serializers.ValidationError(
          'Image size should be less than 2MB'
        )
      if value.image.width > 4096:
        raise serializers.ValidationError(
          'Image width should be less than 4096px'
        )
      if value.image.height > 4096:
        raise serializers.ValidationError(
          'Image height should be less than 4096px'
        )
      return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_tags'
        ]