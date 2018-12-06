from django.contrib import admin

from df_cart import models


@admin.register(models.CartInfo)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = "__all__"
    list_per_page = 5
    list_filter = "__all__"
