from django.urls import path

from apps.index.views import MainView

urlpatterns = [
    path('', MainView.as_view()),
]