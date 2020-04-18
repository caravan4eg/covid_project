from django.db import models
from django.contrib.auth.models import User


class Fact(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    rayon = models.CharField(max_length=250)
    oblast = models.CharField(max_length=250)
    sick = models.IntegerField()  # заболело
    dead = models.IntegerField()  # умерло
    recovered = models.IntegerField()  # выздоровело
    tests_made = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} {self.disease_name}'

    # sick_day_changes = models.IntegerField()  # изменение числа заболевших за сутки
    # recovered_day_changes = models.IntegerField()  # выздоровело
    # dead_day_changes =  models.IntegerField()  # изменение числа умерших за сутки
