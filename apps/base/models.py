from django.db import models

# Create your models here.

class Settings(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название сайта'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    address = models.CharField(
        max_length=100,
        verbose_name='Адрес'
    )
    instagram = models.URLField(
        verbose_name='Instagram'
    )
    facebook = models.URLField(
        verbose_name='Facebook'
    )
    twitter = models.URLField(
        verbose_name='Twitter'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'