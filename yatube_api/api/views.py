from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post, User
from .mixins import CreateRetrieveViewSet
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для Постов"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Переопределение метода создания поста"""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для Групп"""

    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """Метод для определения сета комментариев"""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        new_queryset = post.comments.all()

        return new_queryset

    def perform_create(self, serializer):
        """Переопределение метода создания комментария"""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateRetrieveViewSet):
    """Вьюсет для Подписок"""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Метод для определения сета подписок"""
        following = get_object_or_404(
            User, username=self.request.user.username)

        return following.follower

    def perform_create(self, serializer):
        """Метод для определения создания подписок"""
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для Групп"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
