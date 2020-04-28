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
    img = models.ImageField(
        verbose_name='Original image', upload_to='images/', max_length=256, blank=True, null=True)
    # img_small = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #                             ResizeToFill(100, 100)], source='img',
    #                            format='JPEG', options={'quality': 90})

    # img_medium = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #                              ResizeToFit(400, 300)], source='img',
    #                             format='JPEG', options={'quality': 90})

    # img_big = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #                           ResizeToFit(750, 450)], source='img',
    #                          format='JPEG', options={'quality': 90})
    # # make address

    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField()
    author = models.CharField(
        max_length=250, default='author', blank=True, null=True)
    source_name = models.CharField(max_length=250)
    url = models.URLField(blank=True)

    img_author = models.CharField(
        max_length=50, default='author', blank=True, null=True)
    img_title = models.CharField(max_length=100, blank=True, null=True)

    country = models.CharField(max_length=100, default='Беларусь')
    published_at = models.DateTimeField(
        default=datetime.now, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    img_url = models.URLField(blank=True, null=True,
                              verbose_name='Ссылка на оригинальный имидж')

    # img_small = ImageSpecField(source='img',
    #                                   processors=[ResizeToFill(50, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})
    # img_small = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #                         ResizeToFill(100, 100)],
    #                         format='JPEG', options={'quality': 90})

    # img_medium = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #                         ResizeToFit(400, 300)],
    #                         format='JPEG', options={'quality': 90})

    # img_big = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #                         ResizeToFit(750, 450)],
    #                         format='JPEG', options={'quality': 90})
    # photo = models.ImageField(verbose_name=u'Poster',upload_to=get_file_path,max_length=256, blank=True, null=True)
    # photo_small =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #     ResizeToFill(50, 50)], image_field='photo',
    #     format='JPEG', options={'quality': 90})
    # photo_medium = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #     ResizeToFit(300, 200)], image_field='photo',
    #     format='JPEG', options={'quality': 90})
    #    photo_big =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #         ResizeToFit(640, 480)], image_field='photo',
    #         format='JPEG', options={'quality': 90})

    def __str__(self):
        return self.title


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
