from django.contrib import admin

from df_user.models import UserInfo, GoodsBrowser


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["uname", "uemail", "ushou", "uaddress", "uyoubian", "uphone"]
    list_per_page = 5
    list_filter = ["uname", "uyoubian"]
    search_fields = ["uname", "uyoubian"]
    readonly_fields = ["uname"]


class GoodsBrowserAdmin(admin.ModelAdmin):
    list_display = ["user", "good"]
    list_per_page = 50
    list_filter = ["user__uname", "good__gtitle"]
    search_fields = ["user__uname", "good__gtitle"]
    readonly_fields = ["user", "good"]
    refresh_times = [3, 5]


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(GoodsBrowser, GoodsBrowserAdmin)