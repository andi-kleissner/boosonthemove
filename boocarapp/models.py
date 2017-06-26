from django.db import models
from django.utils import timezone


class CarPart(models.Model):
    name = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    purchased = models.CharField(max_length=200)
    note = models.CharField(max_length=500)
    amount = models.CharField(max_length=15)

    def purchase(self, name):
        self.purchased = "True"
        self.name = name
        self.save()

    def set_note(self, text):
        self.note = text
        self.save()

    def __str__(self):
        return self.item_name