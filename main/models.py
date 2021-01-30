from django.db import models
from django.core.validators import ValidationError
from django_quill.fields import QuillField
from django.utils import timezone


class EditMain(models.Model):
    """
    Set fields for main page
    """
    url = models.CharField(default='', max_length=100, blank=True)
    title = models.CharField(default='Главная', max_length=100)
    keywords = models.CharField(default='', max_length=100, blank=True)
    description = models.CharField(default='', max_length=100, blank=True)
    first_head = models.CharField(default='Первый заголовок', max_length=100, blank=True)
    second_head = models.CharField(default='Второй заголовок', max_length=100, blank=True)
    datalatitude = models.CharField(default='55.76', max_length=10, blank=True)
    datalongitude = models.CharField(default='37.64', max_length=10, blank=True)

    def save(self, *args, **kwargs):
        """ Lock down create more then one model"""
        if not self.pk and EditMain.objects.exists():
            raise ValidationError('There is can be only one EditMain instance')
        return super(EditMain, self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Extra_Text(models.Model):
    editmain = models.ForeignKey(EditMain, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        return self.text
class ImageForMain(models.Model):
    """
    Separate model for pictures on the main 
    """
    title = models.CharField(default='', max_length=50)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class Products(models.Model):
    """
    Model with fields of good
    """
    url = models.CharField(default='', max_length=100, blank=True)
    title = models.CharField(default='Продукт test', max_length=100)
    keywords = models.CharField(default='', max_length=100, blank=True)
    description = models.CharField(default='', max_length=100, blank=True)
    image = models.ImageField(upload_to='products', default='', blank=True)
    product_name = models.CharField(default='Название продукта',max_length=100, blank=True)
    first_head = models.CharField(default='Заголовок 1', max_length=100, blank=True)
    first_text_1 = models.CharField(default='Текст первого заголовка', max_length=1000, blank=True)
    first_text_2 = models.CharField(default='', max_length=1000, blank=True)
    first_text_3 = models.CharField(default='', max_length=1000, blank=True)
    second_head = models.CharField(default='Заголовок 2', max_length=100, blank=True)
    second_text_1 = models.CharField(default='Текст второго заголовка', max_length=1000, blank=True)
    second_text_2 = models.CharField(default='', max_length=1000, blank=True)
    second_text_3 = models.CharField(default='', max_length=1000, blank=True)
    third_head = models.CharField(default='Заголовок 3', max_length=100, blank=True)
    third_text_1 = models.CharField(default='Текст третьего заголовка', max_length=1000, blank=True)
    third_text_2 = models.CharField(default='', max_length=1000, blank=True)
    third_text_3 = models.CharField(default='', max_length=1000, blank=True)
    pub_date = models.DateTimeField(default= timezone.now)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title