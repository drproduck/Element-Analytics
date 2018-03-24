from django.shortcuts import render, HttpResponse
from apps.upload.models import User
from django.contrib.auth.models import User


def profile(request):
    args = {'user':request.user}
    return render(request, 'userprof/userprof.html', args)






