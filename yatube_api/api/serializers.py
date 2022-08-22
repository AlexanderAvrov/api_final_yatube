from django.contrib.auth import get_user_model
from posts.models import Comment, Follow, Group, Post
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов"""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев"""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок"""

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = '__all__'
        model = Follow

    def validate(self, data):
        """Проверка подписки на самого себя"""
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписываться на самого себя')
        return data


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп"""

    class Meta:
        fields = '__all__'
        model = Group
