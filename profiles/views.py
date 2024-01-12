from rest_framework import generics, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from pp5_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List view allows all users to see all profiles
    """
    queryset = Profile.objects.annotate(
      posts_count=Count('owner__post', distinct=True),
      followers_count=Count('owner__followed', distinct=True),
      following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
      filters.OrderingFilter,
      DjangoFilterBackend,
    ]
    filterset_fields = [
      'owner__following__followed__profile',
      'owner__followed__owner__profile',
    ]
    ordering_fields = [
      'posts_count',
      'followers_count',
      'following_count',
      'owner__following__created_at',
      'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Detail view allows users to see individual profiles
    Allows logged in users to update their own profile
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
      posts_count=Count('owner__post', distinct=True),
      followers_count=Count('owner__followed', distinct=True),
      following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer