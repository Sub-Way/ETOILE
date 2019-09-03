from django.db import models

# Create your models here.

class temp(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'