from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import libs.analytics.analytics 

# Create your views here.
COMMON_ERROR_KEYS = [
     'exception',
     'warn',
     'error',
     'fail',
     'unauthorized',
     'timeout',
     'refused',
     'NoSuchPageException',
     '404',
     '401',
     '505'
]


@login_required
def error_analytics(request, file_name):
     
     pass


@login_required
def user_analytics(request):
     
     pass
