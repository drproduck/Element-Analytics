from django.db import models
from django.forms import ModelForm


# Create your models here.
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
