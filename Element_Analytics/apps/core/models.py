from __future__ import unicode_literals

from django.db import models
import os

class User(models.Model):
    """
    user model containing one user's information
    """

    def __str__(self):
        return self.user_name

    user_name = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    dob = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=200)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'dob', 'email', ]

class Document(models.Model):
    def filename(self):
        return os.path.basename(self.document.name)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
