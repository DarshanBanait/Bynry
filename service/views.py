from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm, AssignServiceRequestForm

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('service:admin_dashboard')
    else:
        return redirect('service:user_dashboard')

@login_required
def user_dashboard(request):
    context = {
        'title': 'User Dashboard',
        'message': 'Welcome to your User Dashboard!',
    }
    return render(request, 'service/user_dashboard.html', context)

@login_required
def admin_dashboard(request):
    context = {
        'title': 'Admin Dashboard',
        'message': 'Welcome to the Admin Dashboard!',
    }
    return render(request, 'service/admin_dashboard.html', context)

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)  # Included request.FILES to handle attachments
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('service:user_dashboard')
    else:
        form = ServiceRequestForm()
    return render(request, 'service/submit_service_request.html', {'form': form})

@login_required
def manage_service_requests(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'service/manage_service_requests.html', {'service_requests': service_requests})

@login_required
def assign_service_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        form = AssignServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('service:manage_service_requests')
    else:
        form = AssignServiceRequestForm(instance=service_request)
    return render(request, 'service/assign_service_request.html', {'form': form, 'service_request': service_request})

@login_required
def track_requests(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)  # Corrected to filter by user
    return render(request, 'service/track_requests.html', {'service_requests': service_requests})

def customer_support(request):
    context = {
        'title': 'Customer Support',
        'toll_free_number': '1-800-123-4567',
        'support_email': 'support@bynry.com',
        'phone_notice': 'Customer support will get back to you shortly for phone-related queries.',
        'email_notice': 'For email inquiries, expect a response within 10 hours. Please be patient.',
    }
    return render(request, 'service/customer_support.html', context)
