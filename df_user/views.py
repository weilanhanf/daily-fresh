from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from .models import UserInfo
from df_goods.models import GoodsInfo
from df_user.models import GoodsBrowser
from df_order.models import *
from hashlib import sha1
from . import user_decorator
from django.core.paginator import Paginator,Page

def register(request):
    context={
        'title':'用户注册',
    }
    return render(request, 'df_user/register.html', context)

def register_handle(request):
    #接受用户输入
    post = request.POST
    print(request.method)
    uname=post.get('user_name')
    upwd=post.get('pwd')
    upwd2=post.get('cpwd')
    uemail=post.get('email')

    #判断两次密码一致性
    if upwd != upwd2:
        return redirect('/user/register/')
    #密码加密
    s1=sha1()
    s1.update(upwd.encode('utf8'))
    upwd3=s1.hexdigest()
    # sha = hashlib.sha1(upwd.encode('utf8'))
    # sha.hexdigest()

    #创建对象
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail=uemail
    user.save()
    print(uname, upwd3,uemail)
    #注册成功
    context = {
        'title': '用户登陆',
        'uname': uname,
    }
    # return redirect('/user/login/')
    return render(request, 'df_user/login.html', context)

def register_exist(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    if count == 0:
        print('当前用户名可用')
    return JsonResponse({'count':count})

# @user_decorator.request_detail
def login(request):
    print(request.get_full_path(), 'request.get_full_path')
    uname=request.COOKIES.get('uname', '')
    context={
        'title': '用户登陆',
        'error_name':0,
        'error_pwd':0,
        'uname':uname,
    }
    return render(request, 'df_user/login.html', context)

def login_handle(request):#没有利用ajax提交表单
    #接受请求信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    #根据用户名查询对象
    # print(uname, upwd, jizhu, request.method)
    users = UserInfo.objects.filter(uname=uname)#[]
    print(uname,len(users), users)

    #判断如果未查到则用户名错误，如果查到则判断密码是否正确，正确则转到用户中心
    if len(users)==1:
        s1 = sha1()
        s1.update(upwd.encode('utf8'))
        if s1.hexdigest()==users[0].upwd:
            print("验证成功")
            # request.COOKIES['url'] = '/8/'
            url = request.COOKIES.get('url','/')
            print(url)
            red = HttpResponseRedirect(url)#继承与HttpResponse 在跳转的同时 设置一个cookie值
            #是否勾选记住用户名，设置cookie
            if jizhu!=0:
                red.set_cookie('uname', uname)
                # print('设置cookie', request.COOKIES['uname'])
            else:
                red.set_cookie('uname', '',max_age=-1)#设置过期cookie时间，立刻过期
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {
                'title':'用户名登陆',
                'error_name': 0,
                'error_pwd':1,
                'uname':uname,
                'upwd':upwd,
            }
            # print('密码错误')
            return render(request, 'df_user/login.html', context)
    else:
        context = {
            'title': '用户名登陆',
            'error_name': 1,
            'error_pwd': 0,
            'uname': uname,
            'upwd': upwd,
        }
        print('不存在当前用户')
        return render(request, 'df_user/login.html', context)

def logout(request):
    request.session.flush()#清空当前用户所有session
    return redirect('/')

@user_decorator.login
def info(request):
    username =request.session.get('user_name')
    # print(username)
    user = UserInfo.objects.filter(uname = username).first()
    # user = UserInfo.objects.get(id=request.session['user_id'])
    # print(request.session['user_name'])

    #列表形式最近浏览
    # goods_ids = request.COOKIES.get('goods_ids', '')
    # print('cookies', goods_ids)
    #在cookie中goods_id以{ 'gooids':'1,5,6,7,8,9'}形式存入
    # goods_ids1 = goods_ids.split(',')#拆分为列表
    # print('最近浏览商品序号',goods_ids1)
    # goods_list1 = GoodsInfo.objects.filter(id__in=goods_ids1)#会破坏浏览商品的先后顺序
    # if goods_ids1[0] != '' :
    #     goods_list = [GoodsInfo.objects.get(id=int(goods_id)) for goods_id in goods_ids1]
    #     # for goods_id in goods_ids1:
    #     #     goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))#pk与id区别
    #     # 每次只查询一个商品并放入列表的最后，保证了浏览商品的顺序
    #     explain = '最近浏览'
    # else:
    #     goods_list = []
    #     explain = '无最近浏览'

    # 最近浏览计入第三张那个表
    goods_ids = GoodsBrowser.objects.filter(user_id=request.session['user_id'])
    # print(goods_ids)
    goods_ids1 = [good_browser.good_id for good_browser in goods_ids]
    # print(goods_ids1)
    # goods_ids2 = []
    # for good_id in goods_ids1:
    #     if good_id not in goods_ids2:
    #         goods_ids2.append(good_id)
    # print(goods_ids2)

    if len(goods_ids1) != 0:
        goods_list = [GoodsInfo.objects.get(id=goods_id) for goods_id in goods_ids1]
        goods_list.reverse()
        # print(goods_list)
        explain = '最近浏览'
    else:
        goods_list = []
        explain = '无最近浏览'


    context={
        'title':'用户中心',
        'page_name': 1,
        'user_phone':user.uphone,
        'user_address':user.uaddress,
        'user_name':request.session['user_name'],
        'goods_list': goods_list,
        'explain': explain,
    }
        # print(user.uname, user.uaddress, user.uphone)
    return render(request, 'df_user/user_center_info.html', context)

@user_decorator.login
def order(request, index):
    user_id = request.session['user_id']
    orders_list = OrderInfo.objects.filter(user_id=int(user_id)).order_by('-odate')
    # print(len(orders_list))
    # print(orders_list)
    paginator = Paginator(orders_list,2)
    page = paginator.page(int(index))
    context={
        'paginator': paginator,
        'page':page,
        # 'orders_list':orders_list,
        'title':"用户中心",
        'page_name':1,
    }
    return render(request, 'df_user/user_center_order.html', context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    # print(user, type(user), user.uphone,user.uaddress)

    if request.method=="POST":
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {
        'page_name': 1,
        'title': '用户中心',
        'user':user,
    }
    return render(request, 'df_user/user_center_site.html', context)
