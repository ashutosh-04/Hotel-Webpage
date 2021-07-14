from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
        return self.name
