from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import logout

@login_required
def home(request):
    """test page"""
    return render(request, 'dummy/loginsuccess.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('main')
