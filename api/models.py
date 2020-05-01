from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os
import uuid

# work with pictures
import PIL
from PIL import Image
# from imagekit.models.fields import ImageSpecField
# from imagekit.processors import ResizeToFit, Adjust, ResizeToFill


class Fact(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True, default='')
    country = models.CharField(max_length=100, default='Беларусь')
    province = models.CharField(
        max_length=100, blank=True, null=True, default='')
    confirmed = models.IntegerField(verbose_name='Количество заболевших')
    deaths = models.IntegerField(verbose_name='Количество умерших')
    recovered = models.IntegerField(verbose_name='Количество выздоровевших')
    tests_made = models.IntegerField(
        verbose_name='Сделано тестов', blank=True, null=True)
    published_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.published_at} {self.country}'

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'


class Post(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField()
    author = models.CharField(
        max_length=250, default='author', blank=True, null=True)
    source_name = models.CharField(max_length=250)
    url = models.URLField(blank=True)

    img = models.ImageField(upload_to='images/', blank=True, null=True)
    img_author = models.CharField(
        max_length=50, default='author', blank=True, null=True)
    img_title = models.CharField(max_length=100, blank=True, null=True)

    country = models.CharField(max_length=100, default='Беларусь')
    published_at = models.DateTimeField(
        default=datetime.now, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    img_url = models.URLField(blank=True, null=True,
                              verbose_name='Ссылка на оригинальный имидж')

    def __str__(self):
        return f'{self.title} {self.published_at}'


class Project(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=180, blank=True)
    description = models.TextField()
    url = models.URLField(blank=True)

    img = models.ImageField(upload_to='images/', blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)

    country = models.CharField(max_length=100, default='Беларусь')

    published_at = models.DateTimeField(
        default=datetime.now, blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
