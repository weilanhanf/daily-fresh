#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

app_name = 'df_user'

urlpatterns = [
    url(r'^register/$', register),
    url(r'^register_handle/$', register_handle),
    url(r'^register_exist/$', register_exist),
    url(r'^login/$', login),
    url(r'^login_handle/$', login_handle),
    url(r'^info/$', info),
    url(r'^order/(\d+)$', order),
    url(r'^site/$', site),
    # url(r'^place_order/$', views.place_order),
    url(r'^logout/$', logout)
]