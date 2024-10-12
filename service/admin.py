from django.contrib import admin
from .models import ServiceRequest, CustomerSupport  # Import your models here

# Register the Customer model to be managed in the admin interface
# Updated CustomerAdmin
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Updated to only valid fields
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'email')

admin.site.register(CustomerSupport, CustomerAdmin)


# Register the ServiceRequest model to be managed in the admin interface
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'request_type', 'status', 'created_at', 'updated_at', 'attachment')  # Updated fields
    search_fields = ('user__name', 'request_type', 'status')  # Search fields updated
    list_filter = ('status', 'request_type', 'created_at')  # Updated filter
    ordering = ('-created_at',)  # Orders the list based on the most recent service request

admin.site.register(ServiceRequest, ServiceRequestAdmin)

