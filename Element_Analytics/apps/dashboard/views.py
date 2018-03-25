from django.shortcuts import render
from django.http.response import HttpResponse
from  django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def main(request):
    return render(request, template_name='dashboard/main.html')
