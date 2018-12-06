from django.contrib import admin

from df_order import models


@admin.register(models.OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):

    list_display = "__all__"
    list_per_page = 5
    list_filter = "__all__"


@admin.register(models.OrderDetailInfo)
class OrderDetailInfoAdmin(admin.ModelAdmin):

    list_display = "__all__"
    list_per_page = 5
    list_filter = "__all__"

