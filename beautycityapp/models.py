from django.db import models

class Master(models.Model):
    name = models.CharField('Имя мастера', max_length=50)
    # studio = models.ForeignKey(
    #     'Studio',
    #     on_delete=models.SET_NULL,
    #     related_name='masters')
    photo = models.ImageField('Фото')

    def __str__(self):
        return self.name