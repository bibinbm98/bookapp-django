from django.db import models

class Book(models.Model):
    Book_name=models.CharField(max_length=20)
    Author = models.CharField(max_length=20)
    Pages = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)

    def __str__(self):
        return self.Price


