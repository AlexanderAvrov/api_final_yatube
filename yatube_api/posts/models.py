from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Модель публикаций"""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        'Group',
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Сообщество',
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель комментариев"""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Group(models.Model):
    """Модель сообществ сайта"""

    title = models.CharField('Название сообщества', max_length=200)
    slug = models.SlugField('Адрес страницы сообщества', unique=True)
    description = models.TextField('Описание сообщества')

    def __str__(self):
        return self.title


class Follow(models.Model):
    """Модель подписок на авторов"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        unique_together = ('user', 'following',)
