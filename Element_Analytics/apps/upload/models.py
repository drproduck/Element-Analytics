from django.contrib.auth.models import User

from django.db import models
import os


#
# class User(models.Model):
#     """
#     user model containing one user's information
#     """
#
#     def __str__(self):
#         return self.user_name
#
#     user_name = models.CharField(max_length=200)
#     pwd = models.CharField(max_length=200)
#     dob = models.DateTimeField()
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)
#     email = models.EmailField(max_length=200)


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['user_name', 'dob', 'email', ]

# class User(models.Model):
#     user = models.OneToOneField(DefaultUser, on_delete=models.CASCADE)


from Element_Analytics.settings import MEDIA_URL


def get_store_path(file_instance, filename):
    return 'document/' + file_instance.user.username + '/' + file_instance.file_name


class LogFile(models.Model):

    def get_username(self):
        return self.user.username

    def get_filepath(self):
        return MEDIA_URL + 'document/' + self.get_username() + '/' + self.log_name

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=get_store_path)
    path = models.CharField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
