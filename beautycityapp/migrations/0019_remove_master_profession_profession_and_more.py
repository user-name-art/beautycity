# Generated by Django 4.2.7 on 2024-01-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautycityapp', '0018_client_is_active_client_is_admin_client_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='profession',
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название специальности')),
                ('master', models.ManyToManyField(related_name='professions', to='beautycityapp.master')),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='profession',
            field=models.ManyToManyField(related_name='masters', to='beautycityapp.profession'),
        ),
    ]
