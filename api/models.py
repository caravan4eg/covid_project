from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Location(models.Model):
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, default='Беларусь')
    province = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.country} / {self.province} / {self.city}'


class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    image_url = models.URLField(blank=True)
    author = models.CharField(max_length=100, default='author', blank=True)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    published_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'


class Fact(models.Model):
    location = models.ForeignKey(
        Location, on_delete=models.DO_NOTHING, blank=True)
    confirmed = models.IntegerField(verbose_name='Количество заболевших')
    deaths = models.IntegerField(verbose_name='Количество умерших')
    recovered = models.IntegerField(verbose_name='Количество выздоровевших')
    tests_made = models.IntegerField(
        verbose_name='Сделано тестов', blank=True)
    published_at = models.DateTimeField(
        default=datetime.now, blank=True)  # time when measure was made

    def __str__(self):
        return f'{self.published_at} {self.country}'

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'


class Post(models.Model):
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    author = models.CharField(
        max_length=250, default='author', blank=True)
    source_name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    img_main = models.ForeignKey(
        Image, on_delete=models.DO_NOTHING, blank=True)
    img_1 = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True)
    img_2 = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True)
    img_main_url = models.URLField(blank=True, null=True)
    img_1 = models.URLField(blank=True, null=True)
    img_2 = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        Location, on_delete=models.DO_NOTHING, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=180, blank=True)
    description = models.TextField()
    url = models.URLField(blank=True)
    main_img = models.ForeignKey(
        Image, on_delete=models.DO_NOTHING, blank=True, related_name='main_img')
    img_1 = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True, related_name='img_1')
    img_2 = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True, related_name='img_2')
    location = models.ForeignKey('Location',
                                 on_delete=models.DO_NOTHING, blank=True)
    published_at = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
