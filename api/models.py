from django.db import models
from django.contrib.auth.models import User


class Fact(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    where_is_it = models.ForeignKey('Location',
                                    on_delete=models.CASCADE)
    disease_name = models.CharField(
        max_length=250,
        verbose_name='Название болезни')
    sick = models.IntegerField(verbose_name='Количество заболевших')
    dead = models.IntegerField(verbose_name='Количество умерших')
    recovered = models.IntegerField(verbose_name='Количество выздоровевших')
    tests_made = models.IntegerField(verbose_name='Сделано тестов')
    measured_at = models.DateTimeField(
        blank=True, null=True)  # time when measure was made
    created_at = models.DateTimeField(
        auto_now_add=True)  # time of adding to DB
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} {self.disease_name}'

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'


class Location(models.Model):
    city = models.CharField(max_length=100,
                            verbose_name='Населенный пункт',
                            blank=True)
    district = models.CharField(max_length=100,
                                verbose_name='Район',
                                blank=True)
    region = models.CharField(max_length=100,
                              verbose_name='Область',
                              blank=True)
    country = models.CharField(max_length=50,
                               default=1,
                               verbose_name='Населенный пункт')

    def __str__(self):
        return f'{self.city}/{self.country} '

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'


class Post(models.Model):
    source_name = models.CharField(max_length=250)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    author = models.CharField(max_length=250, default='author', blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    url = models.URLField(default='https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU:ru')
    img_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    where_is_it = models.ForeignKey('Location',
                                    on_delete=models.CASCADE,
                                    default=1)

    def __str__(self):
        return self.title


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    where_is_it = models.ForeignKey('Location',
                                    on_delete=models.CASCADE)
    logo_url = models.URLField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    project_contact = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=250)
    photo_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    where_is_it = models.ForeignKey('Location',
                                    on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    url = models.URLField()
    photo = models.ImageField(upload_to='img/photo/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
