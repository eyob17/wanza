# forms.py

from django import forms
from django.contrib.auth.models import User

class EnrollmentForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput())
