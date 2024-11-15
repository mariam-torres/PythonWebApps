from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class Reporter(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)

    realName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse('reporter_detail', args=[Reporter.pk])

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def heroes(self):
        return Hero.objects.filter(author=self)

    @staticmethod
    def get_me(user):
        return Reporter.objects.get_or_create(user=user)[0]
    
    @receiver(post_save, sender=User)
    def create_reporter_for_new_user(sender, instance, created, **kwargs):
        if created:
            Reporter.objects.get_or_create(user=instance)

class Hero(models.Model):

    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, editable=False)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    realName = models.CharField(max_length=200)
    strength1 = models.CharField(max_length=200)
    strength2 = models.CharField(max_length=200)
    strength3 = models.CharField(max_length=200)
    weakness1 = models.CharField(max_length=200)
    weakness2 = models.CharField(max_length=200)
    weakness3 = models.CharField(max_length=200)
    imagePath = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.heropk}. {self.title} - {self.realName}"
