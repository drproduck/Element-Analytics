from django import forms
from ..upload.models import LogFile

class SubModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, logfile):
        return logfile.log_name

class LogToMatForm(forms.Form):

    log = SubModelChoiceField(queryset=LogFile.objects.all(), label='Name of log file')
    mat_name = forms.CharField(max_length=500, label='Name of resulting csv file')
    PARSER_CHOICES = (('5felds', 'DATE NAME TYPE INFO MSSG'),)
    parser_name = forms.ChoiceField(choices=PARSER_CHOICES)

class ParserRegexForm(forms.Form):

    regex = forms.CharField(max_length=1000, initial='Enter your regular expression here', widget=forms.Textarea)

class ParserNameForm(forms.Form):
    PARSER_CHOICES = (('5felds', 'DATE NAME TYPE INFO MSSG'),)

    parser_name = forms.ChoiceField(choices=PARSER_CHOICES)