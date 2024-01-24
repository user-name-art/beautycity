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


class Order(models.Model):
    client = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True
    )
    question = models.CharField('Комментарий к заказу', max_length=300)
    service = models.ForeignKey(
        'Service',
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True
    )
    promocode = models.CharField(blank=True,null=True, max_length=20)
    slot = models.ForeignKey(
        'Slot',
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True
    )
    cost = models.DecimalField('Итоговая цена', max_digits=7, decimal_places=2)
    # studio тут вопросы возникли

    def __str__(self):
        return f'{self.client}_{self.service}'


class Comment(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.SET_NULL,
        related_name='comments',
        null=True
    )
    client = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        related_name='comments',
        null=True
    )
    text = models.TextField('Текст комментария')
    date = models.DateField('Дата комментария')

    def __str__(self):
        return f'{self.client}_{self.order}'

