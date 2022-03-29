from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name
    # вносим изменения в модель таблицы
    class Meta:
        verbose_name = 'Город' # Делаем отображения по имени в таблице
        verbose_name_plural = 'Города' # Изменяем название основной таблицы
        ordering = ['name'] # Сортировка по имени от А до Я
    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})

class Street(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Улица')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ['name']

