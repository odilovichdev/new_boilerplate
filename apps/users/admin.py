from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users

@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ("phonenumber", "email", "is_staff", "is_active",)
    list_filter = ("phonenumber", "email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

