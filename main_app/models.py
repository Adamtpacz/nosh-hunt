from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


CATEGORIES = (
    ('A', 'American'),
    ('F', 'French'),
    ('I', 'Italian'),
    ('J', 'Japanese'),
    ('T', 'Thai')
)

CITIES = (
    ('NYC', 'New York City'),
    ('PAR', 'Paris'),
    ('ROM', 'Rome'),
    ('TKY', 'Tokyo')
)

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=1, choices=CATEGORIES)
    city = models.CharField(max_length=3, choices=CITIES)
    likes = models.IntegerField()

    def __str__(self):
        return self.title

