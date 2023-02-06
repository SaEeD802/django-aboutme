from django.db import models


# Create your models here.
class Footer(models.Model):
    address = models.CharField(max_length=100, verbose_name="آدرس")
    city = models.CharField(max_length=30, verbose_name="شهز")
    phone = models.CharField(max_length=13, verbose_name="شماره همراه")
    email = models.EmailField(verbose_name="ایمیل")
    whatsapp = models.CharField(max_length=100, verbose_name="واتس اپ")
    telegram = models.CharField(max_length=100, verbose_name="تلگرام")
    instagram = models.CharField(max_length=100, verbose_name="اینستاگرام")



class Message(models.Model):
    fname = models.CharField(max_length=30, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    sub = models.CharField(max_length=100, verbose_name="موضوع")
    body = models.TextField(verbose_name="متن")

    def __str__(self):
        return f"{self.fname} - {self.email}"


    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'