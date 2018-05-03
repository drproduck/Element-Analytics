from django import forms
from django.contrib.auth.models import User
from apps.upload.models import LogFile


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']


class LogFileForm(forms.ModelForm):
    log_name = forms.CharField(max_length=50, required=False, help_text='Optional')

    class Meta:
        model = LogFile
        fields = ["log_name", "file", "regex"]

    def clean(self):
        cleaned_data = super().clean()
        #TODO: add method to check for name conflict
