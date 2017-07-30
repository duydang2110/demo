from django.db import models
from datetime import date
# Create your models here.


class Driver(models.Model):
    image = models.ImageField(upload_to="driver/%Y/%m/%d/", blank=True, null=True)
    name = models.CharField(max_length=50,verbose_name=u"Tên")
    license = models.CharField(max_length=50,verbose_name=u"Bằng Lái")
    address = models.CharField(max_length=100,verbose_name=u"Địa Chỉ")
    identity = models.CharField(max_length=50,verbose_name=u"CMNN")
    def __str__(self):
        return self.name

class History(models.Model):
    ngay = models.DateField(default=date.today, blank=True, null=True, verbose_name=u"Ngày")
    congviec = models.CharField(max_length=50,verbose_name=u"Công Việc")
    gia = models.PositiveIntegerField(null=True,blank=True,verbose_name=u"Giá")
    maasset = models.ForeignKey('Asset',on_delete=models.CASCADE)


class Asset(models.Model):
    GOOD = 1
    REPAIRING = 2
    BROKEN = 3
    STATUS = (
        (GOOD,'Tốt'),
        (REPAIRING,'Bảo Trì'),
        (BROKEN,'Hỏng'),
    )
    name = models.CharField(max_length=50,verbose_name=u"Tên")
    warranty_date = models.DateField(default=date.today,blank=True,null=True,verbose_name=u"Ngày Bảo Trì")
    producer = models.CharField(max_length=30, blank=True,verbose_name=u"Hãng SX")
    bienso = models.CharField(max_length=20,verbose_name=u"Biển Số")
    note = models.TextField(blank=True,verbose_name=u"Ghi Chú")
    made_in = models.CharField(max_length=30,blank=True,verbose_name=u"Nơi SX")
    status = models.PositiveSmallIntegerField(choices=STATUS,verbose_name=u"Tình Trạng")
    Madriver = models.ForeignKey('Driver', null=True,blank=True)
    total = models.PositiveSmallIntegerField(choices=STATUS,verbose_name=u"Tình Trạng",default=0)
    #Mahistory =  models.ManyToManyField('History',blank = True,null = True, )
    def __str__(self):
        return self.name
