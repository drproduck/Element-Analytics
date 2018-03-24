from django import forms
from django.contrib.auth.models import User
from apps.upload.models import LogFile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class LogFileForm(forms.ModelForm):
    class Meta:
        model = LogFile
        fields = ('file', 'file_name',)
