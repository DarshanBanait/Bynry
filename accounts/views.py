from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.urls import reverse_lazy

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('accounts:login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Custom Login view (redirect to service_requests app dashboards)
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomLoginForm

    def get_success_url(self):
        # Redirect to the appropriate dashboard based on the user type
        if self.request.user.is_staff:
            return reverse_lazy('service:admin_dashboard')  # Redirect admin users to admin dashboard
        return reverse_lazy('service:user_dashboard')  # Redirect customers to user dashboard
