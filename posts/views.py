from rest_framework import generics, permissions, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
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
        'owner__following__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
      'owner__username',
      'caption',
      'image_tag',
      'image_tag2',
      'image_tag3',
      'image_tag4',
      'image_tag5',

    ]
    ordering_fields = [
      'likes_count',
      'comments_count',
      'likes__created_at',
    ]

    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)
    

  # Allow view to handle GET requests to retrieve choices data
    def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)


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


# Create new view and endpoint to be able to access choice options via front-end
class TagChoicesView(APIView):
  def get(self, request, *args, **kwargs):
      TAG_CHOICES = [
          {'value': 'tribal', 'label': 'Tribal'},
          {'value': 'geometric', 'label': 'Geometric'},
          {'value': 'realism', 'label': 'Realism'},
          {'value': 'portraits', 'label': 'Portraits'},
          {'value': 'illustrative', 'label': 'Illustrative'},
          {'value': 'dotwork', 'label': 'Dotwork'},
          {'value': 'watercolour', 'label': 'Watercolour'},
          {'value': 'neo-traditional', 'label': 'Neo-traditional'},
          {'value': 'abstract', 'label': 'Abstract'},
          {'value': 'animals', 'label': 'Animals'},
          {'value': 'lettering', 'label': 'Lettering'},
          {'value': 'traditional', 'label': 'Traditional'},
      ]
      
      return Response(TAG_CHOICES, status=status.HTTP_200_OK)