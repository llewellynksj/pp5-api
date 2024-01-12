from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
  """
  Comment Serializer
  """
  owner = serializers.ReadOnlyField(source='owner.username')
  profile_id = serializers.ReadOnlyField(source='owner.profile.id')
  profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
  is_owner = serializers.SerializerMethodField()
  created_at = serializers.SerializerMethodField()
  updated_at = serializers.SerializerMethodField()

  def get_is_owner(self, obj):
    request = self.context['request']
    return request.user == obj.owner
  
  def get_created_at(self, obj):
    return naturaltime(obj.created_at)

  def get_updated_at(self, obj):
    return naturaltime(obj.updated_at)

  class Meta:
    model = Comment
    fields = [
      'id',
      'owner',
      'is_owner',
      'profile_id',
      'profile_image',
      'post',
      'created_at',
      'updated_at',
      'content'
    ]


class CommentDetailSerializer(CommentSerializer):
  """
  Serializer for Comment model that will be used in the Detail view
  """
  post = serializers.ReadOnlyField(source='post.id')