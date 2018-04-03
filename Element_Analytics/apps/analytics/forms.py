from django import forms
from ..upload.models import LogFile

class ParserRegexForm(forms.Form):

    log_name = forms.ModelChoiceField(queryset=LogFile.objects.all(), to_field_name="log_name")
    mat_name = forms.CharField()
    regex = forms.CharField(max_length=1000, initial='Enter your regular expression here', widget=forms.Textarea)


