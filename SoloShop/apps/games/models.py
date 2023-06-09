from django.db import models


class Game(models.Model):
    """Модель игр."""
    name = models.CharField(
        max_length=300,
        verbose_name="Название"
    )
    slug = models.SlugField(
        default='empty',
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    price = models.IntegerField(
        verbose_name="Цена"
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='products/',
        blank=True
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    genre = models.ManyToManyField(
        'Genre',
        related_name='genre',
    )
    publisher = models.CharField(
        max_length=100,
        null=True
    )
    developer = models.CharField(
        max_length=100,
        null=True
    )
    release_date = models.DateField(
        verbose_name="Дата выпуска"
    )

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ("pub_date",)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    """Модель жанров"""
    name = models.CharField(
        max_length=254,
        unique=True,
        verbose_name="Название"
    )
    slug = models.SlugField(
        default='empty',
        unique=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self) -> str:
        return self.name
