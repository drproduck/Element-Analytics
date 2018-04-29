from django import forms
from ..upload.models import LogFile
from .models import Matrix

class SubModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, logfile):
        return logfile.log_name

class LogToMatForm(forms.Form):

    log = SubModelChoiceField(queryset=LogFile.objects.all(), label='Name of log file')
    mat_name = forms.CharField(max_length=500, label='Name of resulting csv file')
    PARSER_CHOICES = (('5fields', 'DATE NAME TYPE INFO MSSG'), ('asis', 'original file is csv parsable'))
    parser_name = forms.ChoiceField(choices=PARSER_CHOICES)

    def clean_mat_name(self):
        mat_name = self.cleaned_data['mat_name']
        some_mat = Matrix.objects.filter(mat_name=mat_name)
        if len(some_mat) > 0:
            raise forms.ValidationError("A matrix with this name already exists")
        return mat_name

class ParserRegexForm(forms.Form):

    regex = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Enter your regular expression here'}))

class ParserNameForm(forms.Form):
    PARSER_CHOICES = (('5felds', 'DATE NAME TYPE INFO MSSG'),)

    parser_name = forms.ChoiceField(choices=PARSER_CHOICES)
