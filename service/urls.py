from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('manage/', views.manage_service_requests, name='manage_service_requests'),
    path('assign/<int:request_id>/', views.assign_service_request, name='assign_service_request'),
    path('dashboard/user/', views.user_dashboard, name='user_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('customer-support/', views.customer_support, name='customer_support'),
    path('track/', views.track_requests, name='track_requests'),
]
