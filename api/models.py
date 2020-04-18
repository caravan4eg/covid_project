from django.db import models
from django.contrib.auth.models import User


class Fact(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    where_is_it = models.ForeignKey('Location', on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=250, verbose_name = 'Название болезни')
    sick = models.IntegerField(verbose_name = 'Количество заболевших')  # заболело
    dead = models.IntegerField(verbose_name = 'Количество умерших')  # умерло
    recovered = models.IntegerField(verbose_name = 'Количество выздоровевших')  # выздоровело
    tests_made = models.IntegerField(verbose_name = 'Сделано тестов')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} {self.disease_name}'

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'


class Location(models.Model):
    place = models.CharField(max_length=250, verbose_name = 'Населенный пункт')
    rayon = models.CharField(max_length=250, verbose_name = 'Район')
    oblast = models.CharField(max_length=250, verbose_name = 'Область')

    def __str__(self):
        return f'{self.place} / {self.rayon} / {self.oblast}'

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'
