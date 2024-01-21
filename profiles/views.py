from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
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


# Create new view and endpoint to be able to access choice options via front-end
class StatusChoicesView(APIView):
  def get(self, request, *args, **kwargs):
      STATUS_CHOICES = [
        {'value': 'ink slinger', 'label': 'Ink Slinger'},
        {'value': 'ink addict', 'label': 'Ink Addict'},
        {'value': 'looking for inspo', 'label': 'Looking for Inspo'},        
      ]
      
      return Response(STATUS_CHOICES, status=status.HTTP_200_OK)