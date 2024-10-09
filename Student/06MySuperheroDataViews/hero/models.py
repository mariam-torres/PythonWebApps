from django.db import models

class Hero(models.Model):
    heropk = models.AutoField(primary_key=True)
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
