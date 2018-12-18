from django.conf.urls import url

from . import views

app_name = 'df_goods'

urlpatterns = [
    url('^$', views.index, name="index"),
    url('^list(\d+)_(\d+)_(\d+)/$', views.good_list),
    url('^(\d+)/$', views.detail),
    url(r'^search/', views.ordinary_search),  # 全文检索
]
