from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profileModel(models.Model):
    class Meta:
        verbose_name = 'کنسرت'
        verbose_name_plural = 'پروفایل ها'

    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='کاربری',related_name='profile')

    # we comment name and surname because django user in admin panel has this features
    # name = models.CharField(max_length=200)
    # surname = models.CharField(max_length=200)

    profile_img = models.ImageField(upload_to = 'profileImages/',null=True,verbose_name='عکس پروفایل',default='defaultImagesProfile/download.png')
    status_choices = [
        ('Man','مرد'),
        ('Woman','زن'),
    ]
    gender = models.CharField(choices=status_choices,max_length=10)

    credit = models.IntegerField(verbose_name='اعتبار',default=0)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

        