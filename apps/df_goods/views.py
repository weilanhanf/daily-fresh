from django.core.paginator import Paginator
from django.shortcuts import render

from .models import GoodsInfo, TypeInfo
from df_cart.models import CartInfo
from df_user.models import GoodsBrowser


def index(request):
    # 查询各个分类的最新4条，最热4条数据
    typelist = TypeInfo.objects.all()
    # 连表操作（了不起的双下划线）利用双下划线和 _set将表之间的操作连接起来
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]  # 按照最新上传的水果显示
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]  # 按照用户点击量上传
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    cart_count = 0
    # 判断是否存在登录状态
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        cart_count = CartInfo.objects.filter(user_id=int(user_id)).count()

    context = {
        'title': '首页',
        'cart_count': cart_count,
        'guest_cart': 1,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    """
    
    context = {
        'guest_cart':1,
        'title': '首页'
    }

    #获取最新的4个商品
    hot = GoodsInfo.objects.all().order_by('-gclick')[0:4]
    context.setdefault('hot', hot)

    #*******获取各分类下的点击商品*******
    #首先获取分类
    typelist = TypeInfo.objects.all()
    for i in range(len(typelist)):
    #获取type对象
        type = typelist[i]
        #根据type对象获取商品列表
        #通过外键关联获取商品
        #获取对应列表中的通过id倒序排列的前四个
        goods1 = type.goodinfo_set.order_by('-id')[0:4]
        goods2 = type.goodinfo_set.order_by('-gclick')[0:4]
        key1 = 'type' + str(i)  # 根据id 倒叙排列
        key2 = 'type' + str(i) + str(i)  # 根据点击量倒序排列
        context.setdefault(key1, goods1)
        context.setdefault(key2, goods2)

    print(context)
    """
    return render(request, 'df_goods/index.html', context)


def good_list(request, tid, pindex, sort):
    # tid：商品种类信息  pindex：商品页码 sort：商品显示分类方式
    typeinfo = TypeInfo.objects.get(pk=int(tid))

    # 根据主键查找当前的商品分类  海鲜或者水果
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    # list.html左侧最新商品推荐
    goods_list = []
    # list中间栏商品显示方式
    cart_count, guest_cart = 0, 0
    user_id = request.session['user_id']
    if user_id:
        guest_cart = 1
        cart_count = CartInfo.objects.filter(user_id=int(user_id)).count()

    if sort == '1':  # 默认最新
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':  # 按照价格
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3':  # 按照人气点击量
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')

    # 创建Paginator一个分页对象
    paginator = Paginator(goods_list, 4)
    # 返回Page对象，包含商品信息
    page = paginator.page(int(pindex))
    context = {
        'title': '商品列表',
        'guest_cart': guest_cart,
        'cart_count': cart_count,
        'page': page,
        'paginator': paginator,
        'typeinfo': typeinfo,
        'sort': sort,  # 排序方式
        'news': news,
    }
    return render(request, 'df_goods/list.html', context)


def detail(request, id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick + 1  # 商品点击量
    goods.save()

    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title': goods.gtype.ttitle,
        'guest_cart': 1,
        'goods': goods,
        'news': news,
        'id': id,
    }
    response = render(request, 'df_goods/detail.html', context)

    if request.session.has_key("user_id"):
        user_id = request.session["user_id"]
        try:
            browsed_good = GoodsBrowser.objects.get(user_id=int(user_id), good_id=int(id))
        except Exception as e:
            browsed_good = None
        if browsed_good:
            from datetime import datetime
            browsed_good.browser_time = datetime.now()
            browsed_good.save()
        else:
            GoodsBrowser.objects.create(user_id=int(user_id), good_id=int(id))
            browsed_goods = GoodsBrowser.objects.filter(user_id=int(user_id))
            browsed_good_count = browsed_goods.count()
            if browsed_good_count > 5:
                ordered_goods = browsed_goods.order_by("-browser_time")
                for _ in ordered_goods[5:]:
                    _.delete()
    return response


def cart_count(request):
    if request.session.has_key("user_id"):
        return CartInfo.objects.filter(user_id=request.session['user_id']).count
    else:
        return 0


def ordinary_search(request):

    from django.db.models import Q
    search_keywords = request.GET.get('q', '')
    pindex = request.GET.get('pindex', 1)
    search_status = True
    cart_count, guest_cart = 0, 0
    user_id = request.session['user_id']
    if user_id:
        guest_cart = 1
        cart_count = CartInfo.objects.filter(user_id=int(user_id)).count()

    if search_keywords:
        goods_list = GoodsInfo.objects.filter(Q(gtitle__icontains=search_keywords) |
                                         Q(gcontent__icontains=search_keywords) |
                                         Q(gjianjie__icontains=search_keywords)).order_by("gclick")
    else:
        search_status = False
        goods_list = GoodsInfo.objects.all().order_by("gclick")

    paginator = Paginator(goods_list, 4)
    page = paginator.page(int(pindex))

    context = {
        'title': '搜索列表',
        'search_status': search_status,
        'guest_cart': guest_cart,
        'cart_count': cart_count,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'df_goods/ordinary_search.html', context)
