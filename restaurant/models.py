from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES = [
    ('AP', 'Appetizer'),
    ('SA', 'Salad'),
    ('BF', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Soup'),
    ('DS', 'Dessert'),
    ('SP', 'Special'),
]

class Menu(models.Model):
    user = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    name = models.CharField("Name of the dish",max_length=30)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='SP')
    description = models.TextField(max_length=300)
    dish_image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name
