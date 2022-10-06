from django.db import models
from jalali_date import datetime2jalali
from accounts.models import profileModel
# Create your models here.
class concertModel(models.Model):
    class Meta:
        verbose_name = 'کنسرت'
        verbose_name_plural = 'کنسرت ها'
    name = models.CharField(max_length=100,verbose_name='نام کنسرت')
    singer = models.CharField(max_length=100,verbose_name='نام خواننده')
    length = models.IntegerField(verbose_name='مدت زمان')
    poster = models.ImageField(upload_to = 'concertImages/',null=True,verbose_name='پوستر')

    def __str__(self):
        return self.singer

class locationModel(models.Model):
    class Meta:
        verbose_name = 'موقعیت'
        verbose_name_plural = 'موقعیت ها'
    name = models.CharField(max_length=100,verbose_name=' مکان')
    address = models.CharField(max_length=500,default='تهران-برج میلاد',verbose_name='آدرس')
    phone = models.CharField(max_length=11,null=True,verbose_name='تلفن')
    capacity = models.IntegerField(verbose_name='ظرفیت')

    def __str__(self):
        return self.name

class timeModel(models.Model):
    class Meta:
        verbose_name = 'زمان'
        verbose_name_plural = 'زمان ها'
    concert = models.ForeignKey("concertModel",on_delete=models.PROTECT,verbose_name='نام کنسرت')
    location = models.ForeignKey("locationModel",on_delete=models.PROTECT,verbose_name='موقعیت ')
    startdate = models.DateTimeField(verbose_name='تاریخ شروع ')
    seats = models.IntegerField(verbose_name=' صندلی باقی مانده')

    status_choices = (
        ('Start','فروش بلیط شروع شده است'),
        ('End','فروش بلیط تمام شده است'),
        ('Cancle','فروش بلیط کنسل شده است'),
        ('Sales','درحال فروش بلیط'),
    )
    status = models.CharField(choices=status_choices,max_length=200,verbose_name='وضعیت ')

    def __str__(self):
        return f" شروع:{self.startdate}| کنسرت :{self.concert.name}| سالن: {self.location.name}"

    # method for converting date to jalali date
    def get_jalali_date(self):
        return datetime2jalali(self.startdate)


class ticketModel(models.Model):
    class Meta:
        verbose_name = 'بلیت'
        verbose_name_plural = 'بلیت ها'
    profile = models.ForeignKey(profileModel,on_delete=models.PROTECT,verbose_name='پروفایل')
    time = models.ForeignKey('timeModel',on_delete=models.PROTECT,verbose_name='زمان ')
    ticket_img = models.ImageField(upload_to='ticketImages/',null=True,verbose_name='عکس')
    name = models.CharField(max_length=200,verbose_name='نام بلیت')
    price = models.IntegerField(verbose_name='قیمت ')

    def __str__(self):
        return f"TicketInfo : Profile :{self.profile.__str__()} ConcerInfo:{self.time.__str__()}"