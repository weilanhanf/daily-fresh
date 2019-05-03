# -*- coding: utf-8 -*-
__date__ = '2019/5/1 20:09'


def goods_recommend(user):
    pass

def load_data_set(user):

    """
    get_user_order
    :param user:
    :return: 返回用户的订单列表，列表中为商品的主键id
     for example [['1', '2'], ['2', '34']]：表示购买进行过两次采购，一次购买1和2号商品，二次购买2号和34号商品
    """

    user_order_list = []
    for big_order in user.orderinfo_set.all():
        user_little_order_list = [str(good.goods.id) for good in big_order.orderdetailinfo_set.all()]
        user_order_list.append(user_little_order_list)

    data_set = user_order_list
    return data_set