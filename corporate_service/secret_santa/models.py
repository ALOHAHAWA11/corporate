from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    birth_date = models.DateField(null=False, verbose_name='Дата рождения')
    name = models.CharField(max_length=40, blank=False, null=True,
                            verbose_name='Имя')
    surname = models.CharField(max_length=40, blank=False, null=True,
                               verbose_name='Фамилия')
    patronymic = models.CharField(max_length=40, blank=False, null=True,
                                  verbose_name='Отчество')
    create_date = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=40, blank=False, null=True,
                               verbose_name='Страна')
    city = models.CharField(max_length=40, blank=False, null=True,
                            verbose_name='Город')
    street = models.CharField(max_length=255, blank=False, null=True,
                              verbose_name='Улица')
    house = models.CharField(max_length=10, blank=False, null=True,
                             verbose_name='Номер дома')
    index = models.CharField(max_length=20, blank=False, null=True,
                             verbose_name='Индекс')
    avatar = models.ImageField(null=True, verbose_name='Аватар')
    email = models.EmailField(null=True, verbose_name='Электронная почта')

    def __str__(self) -> str:
        return f'{self.name} {self.patronymic} {self.surname}'

    @receiver(post_save, sender=user)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Wish(models.Model):
    class Meta:
        verbose_name_plural = 'Желания'
        verbose_name = 'Желание'

    create_date = models.DateTimeField(auto_now=True)
    description = models.TextField(verbose_name='Описание')
    picture = models.ImageField(null=True, verbose_name='Изображение')
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True,
                                verbose_name='Профиль')
    status = models.OneToOneField('WishStatus', on_delete=models.CASCADE,
                                  verbose_name='Статус')

    def __str__(self) -> str:
        return f'Желание №{self.pk}'


class WishStatus(models.Model):
    class Meta:
        verbose_name_plural = 'Статусы выполнения желания'
        verbose_name = 'Статус выполнения желания'

    techname = models.CharField(max_length=20, verbose_name='Техническое имя')
    value = models.CharField(max_length=20, verbose_name='Значение')

    def __str__(self) -> str:
        return self.value


class SantaMatch(models.Model):
    class Meta:
        verbose_name_plural = 'Совпадения'
        verbose_name = 'Совпадение'

    sender = models.ForeignKey('Profile', on_delete=models.CASCADE,
                               null=True, related_name='sender',
                               verbose_name='Отправитель')
    receiver = models.ForeignKey('Profile', on_delete=models.CASCADE,
                                 null=True, related_name='receiver',
                                 verbose_name='Получатель')
    santa_case = models.ForeignKey('SantaCase', on_delete=models.CASCADE,
                                   null=True, verbose_name='Тайный санта')

    def __str__(self) -> str:
        return f'Совпадение №{self.pk}'


class SantaCase(models.Model):
    class Meta:
        verbose_name_plural = 'Тайные Санты'
        verbose_name = 'Тайный Санта'

    name = models.CharField(max_length=255, blank=False, null=True,
                            verbose_name='Название тайного санты')
    year = models.DateField(auto_now_add=True)
