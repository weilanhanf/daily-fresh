#!/user/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
from .views import MySearchView

app_name = 'df_goods'

urlpatterns = [
    url('^$', views.index),
    url('^list(\d+)_(\d+)_(\d+)/$', views.list),
    url('^(\d+)/$', views.detail),
    url(r'^search/', MySearchView()),  # 全文检索
]