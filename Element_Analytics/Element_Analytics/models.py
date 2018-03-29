"""Register models on admin site here"""

from django.contrib import admin
from apps.upload.models import LogFile


class Admin(admin.ModelAdmin):
    """Admin site model"""
    pass


# Register LogFile model
admin.site.register(LogFile, Admin)