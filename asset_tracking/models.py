from django.db import models
from datetime import date
# Create your models here.
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