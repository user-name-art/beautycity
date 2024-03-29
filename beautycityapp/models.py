from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class Studio(models.Model):
    title = models.CharField('Название студии', max_length=100, null=True)
    address = models.CharField('Адрес студии', max_length=200)
    photo = models.ImageField('Фото студии')

    def __str__(self):
        return self.title


class Profession(models.Model):
    title = models.CharField('Название специальности', max_length=25)
    master = models.ManyToManyField(
        'Master',
        related_name='professions'
    )

    def __str__(self):
        return self.title


class Master(models.Model):
    name = models.CharField('Имя мастера', max_length=50)
    studio = models.ForeignKey(
        'Studio',
        on_delete=models.SET_NULL,
        related_name='masters',
        null=True
    )
    photo = models.ImageField('Фото')
    profession = models.ManyToManyField(
        'Profession',
        related_name='masters'
    )
    experience = models.IntegerField('Стаж работы в годах', null=True)
    service = models.ManyToManyField(
        'Service',
        related_name='masters'
    )

    def __str__(self):
        return self.name


class Slot(models.Model):
    day = models.DateField()
    time = models.TimeField()
    master = models.ForeignKey(
        'Master',
        on_delete=models.CASCADE,
        related_name='slots',
        null=True
    )

    def __str__(self):
        return f'{self.day}_{self.master}'


class Service(models.Model):
    type_service = models.ForeignKey(
        'TypeService',
        on_delete=models.SET_NULL,
        related_name='services',
        null=True
    )
    title = models.CharField('Название услуги', max_length=200)
    picture = models.ImageField('Фото', blank=True)
    price = models.IntegerField('Минимальная цена услуги', null=True)
    master = models.ManyToManyField(
        'Master',
        related_name='services',
    )


    def __str__(self):
        return f'{self.title}'


class Client(AbstractBaseUser):
    VERIFICATION_TYPE = [
        ('sms', 'SMS'),
    ]
    name = models.CharField('Имя клиента', max_length=50)
    phone_number = PhoneNumberField('Номер телефона', unique=True)
    verification_method = models.CharField(max_length=10, choices=VERIFICATION_TYPE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    pdf_file = models.FileField('Согласие на обработку персональных данных')

    USERNAME_FIELD = 'phone_number'
    objects = UserManager()

    def __str__(self):
        return str(self.phone_number)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


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
    promocode = models.CharField(blank=True, null=True, max_length=20)
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


class Pay(models.Model):
    payment = models.DecimalField('Сумма оплаты', max_digits=7, decimal_places=2)
    tips = models.DecimalField('Чаевые', max_digits=6, decimal_places=2)
    order = models.ForeignKey(
        'Order',
        on_delete=models.SET_NULL,
        related_name='payments',
        null=True
    )


class TypeService(models.Model):
    title = models.CharField('Тип услуги', max_length=300)

    def __str__(self):
        return self.title
      
     
class MastersService(models.Model):
    master = models.ForeignKey(
        'Master',
        on_delete=models.CASCADE,
        related_name='master_services',
        null=True)
    service = models.ForeignKey(
        'Service',
        on_delete=models.CASCADE,
        related_name='master_services',
        null=True)
    price = models.IntegerField('Цена')