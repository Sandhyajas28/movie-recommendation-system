from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    cast = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    keywords = models.TextField()
    
    def __str__(self):
        return self.title

