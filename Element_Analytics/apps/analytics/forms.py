from django import forms

class ParserForm(forms.Form):
    parse_command = forms.CharField(initial='Enter your commands here', widget=forms.Textarea)
    parser_regex = forms.RegexField()


