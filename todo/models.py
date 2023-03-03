from django.db import models

# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
