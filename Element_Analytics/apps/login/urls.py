from django.urls import path

from django.contrib.auth import views

app_name = 'login'
urlpatterns = [
    path('', views.LoginView.as_view(template_name='login/login.djt'), name='login'),
    path('logout', views.LogoutView.as_view(template_name='login:logout.djt', next_page='main'), name='logout')
]