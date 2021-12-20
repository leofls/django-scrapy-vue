from django.db import models

class Quotes(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__(self):
        return self.text
        
    class Meta:
        ordering = ['author']