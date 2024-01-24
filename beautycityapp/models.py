from django.db import models


class Studio(models.Model):
    addres = models.CharField('Адрес студии', max_length=200)
    photo = models.ImageField('Фото студии')

    def __str__(self):
        return self.addres

class Master(models.Model):
    name = models.CharField('Имя мастера', max_length=50)
    studio = models.ForeignKey(
        'Studio',
        on_delete=models.SET_NULL,
        related_name='masters',
        null=True)
    photo = models.ImageField('Фото')

    def __str__(self):
        return self.name