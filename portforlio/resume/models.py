from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=150)
    mobile=models.CharField( max_length=50)
    msg=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"