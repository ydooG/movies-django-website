from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from accounts.models import CustomUser

admin.site.unregister(Group)
admin.site.site_header = "Аниме Админка"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'sex')
    list_filter = ('sex', )

