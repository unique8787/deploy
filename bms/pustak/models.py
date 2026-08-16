from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_description = models.TextField()
    book_image = models.ImageField(upload_to='bookimage')
    
    
    def __str__(self):
        return self.book_name