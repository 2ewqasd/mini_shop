from django.db import models
from django_quill.fields import QuillField


class EditMain(models.Model):
    """
    Set fields for main page
    """
    first_title = models.CharField(default='Первый заголовок', max_length=100)
    text = models.CharField(default='Текст', max_length=5000)
    second_title = models.CharField(default='Второй заголовок', max_length=100)
    datalatitude = models.CharField(default='55.76', max_length=10)
    datalongitude = models.CharField(default='37.64', max_length=10)

    def __str__(self):
        return self.first_title

class ImageForMain(models.Model):
    """
    Separate model for pictures on the main 
    """
    title = models.CharField(default='', max_length=50)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title