# Generated by Django 4.2.7 on 2024-01-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautycityapp', '0011_typeservice_service_type_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Название студии'),
        ),
        migrations.AlterField(
            model_name='typeservice',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Тип услуги'),
        ),
    ]
