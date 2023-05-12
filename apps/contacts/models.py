from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name = "Номер телефона"
    )
    email = models.EmailField(
        verbose_name="Почта",
        null=True,blank=True
    )
    website = models.CharField(
        max_length=255,
        verbose_name = "website",
        null=True, blank=True
    )
    message = models.TextField(
        max_length=255,
        verbose_name="Введите ваше сообщение"
    )



    def __str__(self):
        return self.call
    
    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
