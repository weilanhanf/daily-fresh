from django.db import models
# Create your models here.

class UserInfo(models.Model):

    uname = models.CharField(max_length=20, verbose_name="用户名")
    upwd = models.CharField(max_length=40, verbose_name="用户密码")
    uemail = models.EmailField(verbose_name="邮箱")
    ushou = models.CharField(max_length=20,default="", verbose_name="收货地址")
    uaddress = models.CharField(max_length=100,default="", verbose_name="地址")
    uyoubian = models.CharField(max_length=6,default="", verbose_name="邮编")
    uphone = models.CharField(max_length=11,default="", verbose_name="手机号")
    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

class GoodsBrowser(models.Model):

    user = models.ForeignKey('UserInfo', on_delete=models.CASCADE, verbose_name="用户ID")
    good = models.ForeignKey('df_goods.GoodsInfo', on_delete=models.CASCADE, verbose_name="商品ID")
