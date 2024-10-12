from django import forms
from .models import ServiceRequest
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']

    def __init__(self, *args, **kwargs):
        super(ServiceRequestForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Provide details about the service request',
        })

class AssignServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'assigned_to', 'status', 'attachment']

    def __init__(self, *args, **kwargs):
        super(AssignServiceRequestForm, self).__init__(*args, **kwargs)
        # Filtering only staff members who can be assigned the service request
        self.fields['assigned_to'].queryset = User.objects.filter(is_staff=True)

class TrackServiceRequestForm(forms.Form):
    status = forms.ChoiceField(choices=[('all', 'All'), *ServiceRequest.STATUS_CHOICES], required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(TrackServiceRequestForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({
            'placeholder': 'Filter by status (optional)',
        })

class CustomerSupportForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    query = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your question or concern here'}))

    def __init__(self, *args, **kwargs):
        super(CustomerSupportForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Your Name',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Your Email',
        })
        self.fields['query'].widget.attrs.update({
            'rows': 4,
            'placeholder': 'Please describe your query or issue in detail.',
        })
