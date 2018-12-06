from django.contrib import admin

from .models import UserInfo

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = []
    list_per_page = 5
    list_filter = []


admin.site.register(UserInfo, UserInfoAdmin)