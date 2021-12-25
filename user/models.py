from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=30)

class Post(models.Model):
    user = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=30)
    username=models.ForeignKey(User,on_delete=CASCADE,default=None)