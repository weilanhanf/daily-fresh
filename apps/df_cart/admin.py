from django.contrib import admin

from .models import CartInfo


@admin.register(CartInfo)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods', 'count']
    list_per_page = 5
    list_filter = ['user', 'goods', 'count']
    search_fields = ['user_uname', 'goods__gtitle']
    readonly_fields = ['user', 'goods', 'count']