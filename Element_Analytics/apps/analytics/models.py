from django.db import models
from django.forms import ModelForm
from ..upload.models import LogFile, User
from django.urls import reverse

#  Create your models here.

class Matrix(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log = models.ForeignKey(LogFile, on_delete=models.CASCADE)
    regex_history = models.CharField(max_length=1000)
    path = models.FilePathField()

    def get_absolute_url(self):
        """each matrix has its own view"""
        return reverse('analytics:middleboss', kwargs={'user':self.user.username, 'log':self.log.log_name})
