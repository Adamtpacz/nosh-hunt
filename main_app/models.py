from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


TYPES = (
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
    ('TKY', 'Tokyo'),
    ('LAX', 'Los Angeles')
)

CATEGORIES = (
    ('F', 'Fine Dining'),
    ('C', 'Casual'),
    ('S', 'Street Food')
)

PRICES = (
    ('CHP', '$'),
    ('LOW', '$$'),
    ('MID', '$$$'),
    ('EXP', '$$$$')
)

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    food_type = models.CharField(max_length=1, choices=TYPES)
    price = models.CharField(max_length=3, choices=PRICES)
    visited = models.BooleanField()

    def __str__(self):
        return self.name

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=1, choices=CATEGORIES)
    city = models.CharField(max_length=3, choices=CITIES)
    likes = models.IntegerField(default=1)
    restaurants = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} posted {self.content}"