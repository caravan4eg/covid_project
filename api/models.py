from django.db import models


class Facts(models.Model):
    city = models.CharField(max_length=250)
    rayon = models.CharField(max_length=250)
    oblast = models.CharField(max_length=250)
    sick = models.IntegerField()  # заболело
    dead = models.IntegerField()  # умерло
    recovered = models.IntegerField()  # выздоровело
    tests_made = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # sick_day_changes = models.IntegerField()  # изменение числа заболевших за сутки
    # recovered_day_changes = models.IntegerField()  # выздоровело
    # dead_day_changes =  models.IntegerField()  # изменение числа умерших за сутки
