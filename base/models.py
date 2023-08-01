from django.db import models
from django import forms

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=20)
    Phone_no = models.IntegerField(max_length=20)
    Messege = models.TextField(max_length=500)

