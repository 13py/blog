from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255, db_index=True)
    slug = models.SlugField('Читаемый url', max_length=255, unique=True)
    text = models.TextField('Текст поста', blank=True, db_index=True)
    date_pub_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title
