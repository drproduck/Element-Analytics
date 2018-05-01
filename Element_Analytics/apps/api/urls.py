from django.urls import path
import apps.api.views as view

app_name = 'api'

urlpatterns = [
     path('error_analytics/<file_name>/', view.error_analytics),
     path('user_analytics/', view.user_analytics),
     path('regex_search/<regex>', view.regex_search)
]