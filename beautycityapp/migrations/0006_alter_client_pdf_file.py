# Generated by Django 4.2.7 on 2024-01-24 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautycityapp', '0005_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='pdf_file',
            field=models.FileField(upload_to='', verbose_name='Согласие на обработку персональных данных'),
        ),
    ]
