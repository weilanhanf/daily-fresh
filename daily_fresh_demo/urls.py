from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('df_goods.urls', namespace='goods')),
    url(r'^user/', include('df_user.urls', namespace='user')),
    url(r'^goods/', include('df_goods.urls')),
    url(r'^cart/', include('df_cart.urls', namespace='cart')),
    url(r'^order/', include('df_order.urls', namespace='order')),
    url(r'^search/', include('haystack.urls')),  # 全文检索
    url(r'^tinymce/', include('tinymce.urls')),  # 使用富文本编辑框配置confurl
]
