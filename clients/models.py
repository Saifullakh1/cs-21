from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    age = models.IntegerField(default=0, verbose_name="Возраст")
    email = models.CharField(max_length=255, blank=True, unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=255, blank=True, verbose_name="Номер телефона")
    balance = models.IntegerField(default=0, verbose_name="Баланс")
    avatar = models.FileField(upload_to="avatar", blank=True, verbose_name="Аватар")
    address = models.CharField(max_length=255, blank=True, verbose_name="Адрес")
    password = models.CharField(max_length=200, verbose_name="Пароль", blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


