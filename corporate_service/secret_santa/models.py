from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=False)
    name = models.CharField(max_length=40, blank=False, null=True)
    surname = models.CharField(max_length=40, blank=False, null=True)
    patronymic = models.CharField(max_length=40, blank=False, null=True)
    create_date = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=40, blank=False, null=True)
    city = models.CharField(max_length=40, blank=False, null=True)
    street = models.CharField(max_length=255, blank=False, null=True)
    house = models.CharField(max_length=10, blank=False, null=True)
    index = models.CharField(max_length=20, blank=False, null=True)
    avatar = models.ImageField(null=True)
    email = models.EmailField(null=True)
    wishes = models.ForeignKey('Wish', on_delete=models.CASCADE, null=True)

    @receiver(post_save, sender=user)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Wish(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    picture = models.ImageField(null=True)
    status = models.OneToOneField('WishStatus', on_delete=models.CASCADE)


class WishStatus(models.Model):
    techname = models.CharField(max_length=20)
    value = models.CharField(max_length=20)


class SantaMatch(models.Model):
    year = models.DateField(auto_now_add=True)
    sender = models.ForeignKey('Profile', on_delete=models.CASCADE,
                               null=True, related_name='sender')
    receiver = models.ForeignKey('Profile', on_delete=models.CASCADE,
                                 null=True, related_name='receiver')
