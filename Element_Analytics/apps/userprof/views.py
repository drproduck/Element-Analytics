from django.shortcuts import render, HttpResponse
from apps.upload.models import User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    args = {'user':request.user}
    return render(request, 'userprof/userprof.djt', args)
