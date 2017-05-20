from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=128)
    reg_date = models.DateField()
    active = models.BooleanField()

class Screenshot(models.Model):
    raw = models.FileField(upload_to='raw_screens/%Y/%m/%d')
    upload_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
