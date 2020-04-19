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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} {self.disease_name}'

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'


class Location(models.Model):
    city = models.CharField(max_length=100,
                            verbose_name='Населенный пункт')
    district = models.CharField(max_length=100,
                                verbose_name='Район')
    region = models.CharField(max_length=100,
                              verbose_name='Область')
    country = models.CharField(max_length=50,
                                 verbose_name='Населенный пункт')

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    where_is_it = models.ForeignKey('Location',
                                    on_delete=models.CASCADE)
    src_logo = models.ImageField(upload_to='logos/%Y/%m/%d/')
    src_name = models.CharField(max_length=250)
    src_url = models.URLField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    where_is_it = models.ForeignKey('Location',
                                    on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/%Y/%m/%d/')
    title = models.CharField(max_length=250)
    url = models.URLField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    where_is_it = models.ForeignKey('Location',
                                    on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    url = models.URLField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'
