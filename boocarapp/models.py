from django.db import models
from django.utils import timezone


class CarPart(models.Model):
    purchaser = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    purchased = models.CharField(max_length=200)

    def purchase(self, purchaser):
        self.purchased = "True"
        self.purchaser = purchaser
        self.save()

    def __str__(self):
        return self.name