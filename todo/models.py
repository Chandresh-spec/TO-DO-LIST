from django.db import models

# Create your models here.


class Task(models.Model):
    text=models.TextField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)


    def __str__(self):
        return self.text
    
    