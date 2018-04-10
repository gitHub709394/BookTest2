from django.db import models

# Create your models here.
class BookInfo(models.Model):
    # 图书名称
    bTitle = models.CharField(max_length=20)
    # 图书发布时间
    bPubDate = models.DateTimeField()

    def __str__(self):
        return self.bTitle

class HeroInfo(models.Model):
    hName = models.CharField(max_length=20)
    hGender = models.BooleanField()
    hContent = models.CharField(max_length=50)
    bBook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.hName+"-----"+self.bBook.bTitle

class AreaInfo(models.Model):
    code = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)

