from rest_framework import generics, permissions
from pp5_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
# from django_filters.rest_framework import DjangoFilterBackend


class CommentList(generics.ListCreateAPIView):
    """
    List view allows a logged in user to view a 
    list of comments and create a comment
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view allows all users to view a specific comment,
    and allows logged in users to edit and delete their own comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()