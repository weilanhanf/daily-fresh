from django.contrib import admin

from .models import OrderDetailInfo, OrderInfo


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):

    list_display = ["oid", "user", "odate", "ototal", "oaddress"]
    list_per_page = 5
    list_filter = ["user", "odate", "oaddress"]
    search_fields = ["user__uname"]
    ordering = ["-odate"]


@admin.register(OrderDetailInfo)
class OrderDetailInfoAdmin(admin.ModelAdmin):

    list_display = ["goods", "order", "price", "count"]
    list_per_page = 5
    list_filter = ["goods"]
