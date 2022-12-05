from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateField()
    # body = models.TextField()
    
    def __str__(self):
        return self.title + f' Created on {self.created_on}'
    
    
