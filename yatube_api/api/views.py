from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)

User = get_user_model()


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
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)

        return new_queryset

    def perform_create(self, serializer):
        """Переопределение метода создания комментария"""
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """Вьюсет для создания и просмотра всех экземпляров"""

    pass


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


class RetrieveViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """Вьюсет для просмотра единичного экземпляра и всех экземпляров"""

    pass


class GroupViewSet(RetrieveViewSet):
    """Вьюсет для Групп"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None
