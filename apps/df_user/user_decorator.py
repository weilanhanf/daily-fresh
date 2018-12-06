#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
import re

#如果未登录则转到登陆页面
def login(func):
    def login_fun(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())
            print(request.get_full_path(), 'user_decorator')
            #保证用户再登陆验证之后仍点击到希望的页面
            return red
    return login_fun

"""
http://127.0.0.1:8000/200/?type=10
request.path :表示当前路径，为/200/
request.get_full_path():表示完整路径，为/200/?type=10
"""

#判断是否是从detail页面进来的请求
def request_detail(func):
    def request_detail_test(request, *args, **kwargs):
        # url_pattern = re.compile(r'\/\d+\/')
        # url = request.get_full_path()
        # print(url, 'decorator')
        # if re.match(url_pattern, url):
        #     red = HttpResponseRedirect('/user/login/')
        #     red.set_cookie('url', request.get_full_path())
        #     return red
        # else:
        #     return func(request, *args, **kwargs)
        print(request.get_full_path())
        print(request.path)
        return HttpResponseRedirect('/1/')
    return request_detail_test

