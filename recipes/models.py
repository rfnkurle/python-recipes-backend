from django.db import models

class Recipe(models.Model):
    recipeId = models.AutoField(primary_key=True)
    recipeName = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=300)
    instructions = models.CharField(max_length=400)
