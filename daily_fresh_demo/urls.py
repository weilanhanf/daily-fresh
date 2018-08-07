"""daily_fresh_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('df_goods.urls',namespace='goods')),
    url(r'^user/', include('df_user.urls', namespace='user')),
    url(r'^goods/', include('df_goods.urls')),
    url(r'^cart/',include('df_cart.urls', namespace='cart')),
    url(r'^order/',include('df_order.urls', namespace='order')),
    url(r'^search/', include('haystack.urls')),#全文检索
    url(r'^tinymce/', include('tinymce.urls')),#使用富文本编辑框配置confurl
]
