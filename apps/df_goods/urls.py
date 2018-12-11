#!/user/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from df_goods import views

app_name = 'df_goods'

urlpatterns = [
    url('^$', views.index),
    url('^list(\d+)_(\d+)_(\d+)/$', views.list),
    url('^(\d+)/$', views.detail),
    url(r'^search/', views.ordinary_search),  # 全文检索
]