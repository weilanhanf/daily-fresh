from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from haystack.views import SearchView

from df_cart.models import CartInfo
from df_user.models import GoodsBrowser
from df_goods.models import GoodsInfo, TypeInfo


def index(request):
    # 查询各个分类的最新4条，最热4条数据
    typelist = TypeInfo.objects.all()
    print(len(typelist), 'asdf')
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

    # 判断是否存在登录状态
    try:
        user_id = request.session['user_id']
        cart_count = CartInfo.objects.filter(user_id=int(user_id)).count
    except:
        cart_count = 0
    context = {
        'title': '首页',
        'cart_count': cart_count,
        'guest_cart':1,
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


def list(request, tid, pindex, sort):
    # tid：商品种类信息  pindex：商品页码 sort：商品显示分类方式
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    # 根据主键查找当前的商品分类  海鲜或者水果
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    # list.html左侧最新商品推荐
    goods_list = []
    # list中间栏商品显示方式
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
        'guest_cart': 1,
        'page': page,
        'paginator': paginator,
        'typeinfo': typeinfo,
        'sort': sort,  # 排序方式
        'news': news,
    }
    return render(request, 'df_goods/list.html', context)


def detail(request, id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick+1  # 商品点击量
    goods.save()

    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title': goods.gtype.ttitle,
        'guest_cart': 1,
        'goods': goods,
        'news': news,
        'id': id,
    }
    response=render(request, 'df_goods/detail.html', context)

    # 使用列表   记录最近浏览， 在用户中心使用
    # goods_ids = request.COOKIES.get('goods_ids', '')#在cookie中建立一个商品id的对应最近浏览的商品
    # goods_id = '%d' %goods.id#将url转化为整型
    # if goods_ids != '':#判断是否存在浏览记录，如果存在则继续判断，
    #     goods_ids1 = goods_ids.split(',')#拆分为列表
    #     if goods_ids1.count(goods_id)>=1:#如果商品已经存在记录则删除旧纪录
    #         goods_ids1.remove(goods_id)
    #     goods_ids1.insert(0, goods_id)#将商品插入到第一页
    #     if len(goods_ids1)>=6:#每页只显示五个最近浏览的商品
    #         del goods_ids1[5]
    #     goods_ids = ','.join(goods_ids1)#将商品id拼接为字符串
    # else:
    #     goods_ids = goods_id#显然第一次查看detail页面时为空，则直接添加
    # response.set_cookie('goods_ids', goods_ids)#写入cookie

    # 将用户最近浏览商品记录进第三张表
    '''
    1,判断是否有用户登录， 如果没有直接结束
        2,判断在当前浏览表中是否存在这个用户，
            不存在则创建一个用户浏览记录，并且不用判断是否浏览过
            若存在则判断当前用户是否存在一个浏览过当前商品
                3，不管有没有浏览过当前商品都要先创建一个商品记录放入表中
                    如果浏览过则删除前期浏览的商品
                    若没有则不用删除
                    4，如果商品记录为五条，则将最后的一条删除

    '''
    try:
        user_id = request.session['user_id']
        # user_list = GoodsBrowser.objects.filter(user_id=int(user_id))
        goods_browser = GoodsBrowser()
        goods_browser.user_id = int(user_id)
        goods_browser.good_id = int(id)
        goods_browser.save()
        old_user_list = GoodsBrowser.objects.filter(user_id=int(user_id), good_id=int(id))
        if len(old_user_list) > 1:
            GoodsBrowser.objects.filter(good_id=int(id)).first().delete()
        if len(GoodsBrowser.objects.filter(user_id=int(user_id))) > 5:
            GoodsBrowser.objects.filter(user_id=int(user_id)).first().delete()
    except:
        pass
    return response

def cart_count(request):
    if request.session.has_key('user_id'):
        return CartInfo.objects.filter(user_id=request.session['user_id']).count
    else:
        return 0

class MySearchView(SearchView):
    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context['title'] = '搜索'
        context['guest_cart'] = 1
        context['cart_count'] = cart_count(self.request)
        return context

