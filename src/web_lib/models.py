from django.db import models

class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(verbose_name='Возраст автора')
    tlt_type = models.CharField(max_length=1, verbose_name='тип литературы', choices=TYPES, default='a')

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    page_num = models.PositiveIntegerField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
