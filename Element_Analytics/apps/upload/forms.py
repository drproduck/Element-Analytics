from django import forms

from apps.upload.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', 'file_name',)
