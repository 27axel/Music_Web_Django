from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Anketa(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название трека")
    bpm = models.IntegerField(verbose_name="Темп")
    image = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name="Изображение")
    audio = models.FileField(upload_to="music/%Y/%m/%d/", verbose_name="Аудио")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, verbose_name="Жанр")
    tonal = models.ForeignKey('Tonal', on_delete=models.PROTECT, verbose_name="Тональность")
    price = models.ForeignKey('Price', on_delete=models.PROTECT, verbose_name="Цена")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('track', args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название жанра")

    def __str__(self):
        return self.name


class Tonal(models.Model):
    value = models.CharField(max_length=45, verbose_name="Тональность")

    def __str__(self):
        return self.value


class Price(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название тарифа")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.name


class Cart(models.Model):
    totalCost = models.IntegerField(blank=True, verbose_name="Итоговая цена")
    anketa = models.ForeignKey('Anketa', on_delete=models.PROTECT)

    def __str__(self):
        return self.totalCost

    def get_absolute_url(self):
        return reverse('cart', args=[str(self.id)])


class DrumKit(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название")
    file = models.FileField(upload_to="files/%Y/%m/%d/", verbose_name="Файл")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")

    def __str__(self):
        return self.name


class Catalog(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название плейлиста")
    image = models.ImageField(upload_to="playlists/%Y/%m/%d/", verbose_name="Изображение")
    audio = models.ManyToManyField(Anketa, verbose_name="Треки")
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/playlist/{self.slug}/'
