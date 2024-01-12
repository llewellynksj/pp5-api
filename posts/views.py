from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from pp5_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List view allows all users to view all posts
    Allows logged in users to create a post
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
      likes_count=Count('likes', distinct=True),
      comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
      filters.OrderingFilter,
      filters.SearchFilter,
      DjangoFilterBackend,
    ]
    filterset_fields = [
      'owner__followed__owner__profile',
      'likes__owner__profile',
      'owner__profile',
    ]
    search_fields = [
      'owner__username',
      'title',
      'image_tags',
    ]
    ordering_fields = [
      'likes_count',
      'comments_count',
      'likes__created_at',
    ]

    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view allows users to view the specific post
    Allows logged in users to edit or delete their own post
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
      likes_count=Count('likes', distinct=True),
      comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')