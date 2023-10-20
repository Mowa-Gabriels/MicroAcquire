from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
     list_display = ("email", "is_active", "is_buyer", "is_seller", "is_staff", "is_verified", "password")

admin.site.register(User, UserAdmin)
