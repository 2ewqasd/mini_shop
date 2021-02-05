from django.db import models
from django.core.validators import ValidationError
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


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
        return super(EditMain, self).save(*args, **kwargs)

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
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    def validate_file_extension(value):
        import os
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.jpg', '.jpeg']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported!')

    title = models.CharField(default='', max_length=50)
    image = models.ImageField(upload_to='', validators=[validate_image, validate_file_extension])

    def save(self):
        """
        Save in needed size
        """
        # Opening the uploaded image
        im = Image.open(self.image)
        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1240, 833))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(ImageForMain, self).save()

    def __str__(self):
        return self.title


class Products(models.Model):
    """
    Model with fields of good
    """
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    def validate_file_extension(value):
        import os
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.jpg', '.jpeg']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported!')

    url = models.CharField(default='', max_length=100, blank=True)
    title = models.CharField(default='Продукт test', max_length=100)
    keywords = models.CharField(default='', max_length=100, blank=True)
    description = models.CharField(default='', max_length=100, blank=True)
    image = models.ImageField(upload_to='products', default='', blank=True, validators=[validate_image, validate_file_extension])
    product_name = models.CharField(default='Название продукта', max_length=100, blank=True)
    first_head = models.CharField(default='Заголовок 1', max_length=100, blank=True)
    second_head = models.CharField(default='Заголовок 2', max_length=100, blank=True)
    third_head = models.CharField(default='Заголовок 3', max_length=100, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def save(self):
        """
        Save in needed size
        """
        # Opening the uploaded image
        im = Image.open(self.image)
        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1240, 992))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Products, self).save()

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Extra_Text_Product(models.Model):
    """
    Extra text for products
    """
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    nubmer = models.IntegerField(blank=True, null=True)
    text = models.CharField(default='', max_length=1000)

    def __str__(self):
        return self.text
