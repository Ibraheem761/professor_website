from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    timing = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name 