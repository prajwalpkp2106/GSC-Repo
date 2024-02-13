from django.db import models
from django.contrib.auth.models import User
#to create database schema

# Create your models here.

class Recipe(models.Model):
    user= models.ForeignKey(User ,on_delete=models.SET_NULL , null =True , blank=True)
    recipe_name=models.CharField(max_length=100)
    recipe_description = models.TextField(null=True)
    recipe_image=models.ImageField(upload_to="recipe images")