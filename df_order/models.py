from django.db import models

# Create your models here.
class OrderInfo(models.Model):#大订单
    oid = models.CharField(max_length=20, primary_key=True)#订单号
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE)#确定哪个用户的订单
    odate = models.DateTimeField(auto_now=True)
    oIsPay = models.BooleanField(default=False)#当前订单是否支付，默认为否
    ototal = models.DecimalField(max_digits=8, decimal_places=2)
    oaddress = models.CharField(max_length=150)
    #虽然订单总价可以由多个商品的单价以及数量求得，但是由于用户订单的总价的大量使用，忽略total的冗余度

#无法实现：真实支付，物流信息

class OrderDetailInfo(models.Model):#大订单中的具体某一商品订单
    goods = models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE)#关联商品信息
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE)#关联大订单，确定属于某一个大订单中
    price = models.DecimalField(max_digits=6, decimal_places=2)#某一类商品订单的价格最高达9999.99
    count = models.IntegerField()
