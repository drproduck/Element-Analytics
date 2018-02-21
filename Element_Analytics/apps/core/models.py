from __future__ import unicode_literals

from django.db import models
import os


class Document(models.Model):
    def filename(self):
        return os.path.basename(self.document.name)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
