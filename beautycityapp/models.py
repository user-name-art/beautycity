from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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


class Slot(models.Model):
    day = models.DateField()
    time = models.TimeField()
    master = models.ForeignKey(
        'Master',
        on_delete=models.CASCADE,
        related_name='slots',
        null=True)
    
    def __str__(self):
        return f'{self.day}_{self.master}'


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=200)
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
    picture = models.ImageField('Фото')
    master = models.ForeignKey(
        'Master',
        on_delete=models.CASCADE,
        related_name='services',
        null=True)
    
    def __str__(self):
        return f'{self.title}_{self.master}'


class Client(models.Model):
    name = models.CharField('Имя клиента', max_length=50)
    phone_number = PhoneNumberField('Номер телефона')
    pdf_file = models.FileField('Согласие на обработку персональных данных')

    def __str__(self):
        return self.name

    

