from django.urls import path
import apps.api.views as view

app_name = 'api'

urlpatterns = [
     path('error_analytics/<file_name>/', view.error_analytics),
     path('user_analytics/', view.user_analytics),
     path('regex_search/<regex>', view.regex_search),
     path('delete/', view.delete, name='delete'),
     path('download/<file_name>', view.download),
     path('regex_search/', view.regex_search)
]