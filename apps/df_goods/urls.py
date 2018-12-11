#!/user/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from df_goods.views import MySearchView, index, list, detail

app_name = 'df_goods'

urlpatterns = [
    url('^$', index),
    url('^list(\d+)_(\d+)_(\d+)/$', list),
    url('^(\d+)/$', detail),
    url(r'^search/', MySearchView()),  # 全文检索
]