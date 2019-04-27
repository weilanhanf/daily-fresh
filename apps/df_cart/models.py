from django.db import models

from df_user.models import UserInfo
from df_goods.models import GoodsInfo
# 当一对多关系时例如生鲜分类对生鲜具体商品， 将关系维护在多的那张表中，即在具体商品表中维护
# 当多对多关系，则新建一张表，在再第三张表中维护表关系
# 用户表与商品表则将关系维护在购物车表中

# 在购物车的逻辑删除与物理删除  选择物理删除，
# 购物车中的商品不属于重要的信息，可以直接删除


class CartInfo(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品")
    count = models.IntegerField(verbose_name="", default=0)  # 记录用户买个多少单位的商品

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.uname + '的购物车'
