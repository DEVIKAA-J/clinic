from django import forms
from .models import *
class AppointmentForm(forms.ModelForm):
    class Meta: #build in class to create form from model
        model = Appointment
        fields = '__all__'