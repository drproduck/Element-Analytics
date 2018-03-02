from django.urls import path

from django.contrib.auth import views

urlpatterns = [
    path('', views.LoginView.as_view(template_name='login/login.html'), name='login'),
]