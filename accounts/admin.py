from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # List of fields to display in the admin panel
    model = CustomUser
    list_display = ['username', 'full_name', 'email', 'phone_number', 'address', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'full_name']
    ordering = ['username']

# Register the custom user model in the admin panel
admin.site.register(CustomUser, CustomUserAdmin)
