from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.CharField(max_length=200, verbose_name='توضیحات')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    image = models.ImageField(upload_to='resume', verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'
