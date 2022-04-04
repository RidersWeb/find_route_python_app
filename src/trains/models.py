from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set', verbose_name='Из какого города')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='to_city_set', verbose_name='В какой город')
    
    def __str__(self):
        return f'Поезд №{self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']

class TestTrain(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=255, null=True)

    # Отображение в панели администратора
    def __str__(self):
        return self.cost
    # отображение полей в таблицы
    class Meta:
        verbose_name = 'ТЕСТПоезд'
        verbose_name_plural = 'ТЕСТПоезда'
        ordering = ['id']