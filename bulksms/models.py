from django.db import models

# Create your models here.
class Bulkmsg(models.Model):
    sender = models.EmailField()
    password = models.CharField(max_length=25)
    receiver = models.CharField(max_length=100,default=" ")
    msg = models.CharField(max_length=10000)

    def __str__(self):
        return self.sender


