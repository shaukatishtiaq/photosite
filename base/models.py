from tkinter import image_types
from django.db import models

# Create your models here.
class ImageType(models.Model):
    image_type = models.CharField(max_length=50)

    def __str__(self):
        return self.image_type

class Image(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    image_type = models.ForeignKey(ImageType, null=True, on_delete = models.SET_NULL)
    original_url = models.ImageField(upload_to='photos')

    def __str__(self):
        return f'{self.original_url} {self.image_type} {self.price}'