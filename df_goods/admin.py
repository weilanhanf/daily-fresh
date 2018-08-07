# superuser: root 123123...

from django.contrib import admin
from .models import TypeInfo,GoodsInfo

# Register your models here.
#注册模型类  普通方法
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']

# class GoodsInfoAdmin(admin.ModelAdmin):
#     list_per_page = 15
#     list_display = ['id', 'gtitle', 'gunit','gclick', 'gprice','gpic','gjianjie','gkucun','gcontent','gjianjie']

admin.site.register(TypeInfo, TypeInfoAdmin)
# admin.site.register(GoodsInfo, GoodsInfoAdmin)


# 装饰器方法
@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'gtitle', 'gunit','gclick', 'gprice','gpic','gjianjie','gkucun','gcontent','gjianjie']
