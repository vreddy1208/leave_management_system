from django import forms
from .models import *
from django.utils import timezone
class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ['leave_type','start_date','end_date','reason','status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
        def clean(self):
            cleaned_data = super.clean()
            start_date = cleaned_data.get("start_date")
            end_date = cleaned_data.get("end_date")
            if start_date and end_date:
                if start_date > end_date:
                    raise forms.ValidationError("Start date cannot be after end date.")
            return cleaned_data
class ApplicationReviewForm(forms.ModelForm):
    status = forms.ChoiceField(choices=LeaveApplication.STATUS_CHOICES,label="Action", widget=forms.RadioSelect)
    class Meta:
        model = LeaveApplication
        fields = ['status']
class TypeLeaveForm(forms.ModelForm):
    class Meta:
        model = Type_leave
        fields = ['name', 'no_days']
    
        