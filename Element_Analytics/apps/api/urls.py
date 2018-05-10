from django.urls import path
import apps.api.views as view

app_name = 'api'

urlpatterns = [
     path('error_analytics/<file_name>/', view.error_analytics),
     path('usage_analytics/<file_name>/', view.usage_analytics),
     path('gen_analytics/<file_name>/', view.analytics),
     path('user_analytics/', view.user_analytics),
     path('delete/', view.delete, name='delete'),
     path('download/<file_name>/', view.download),
     path('get_csv/<file_name>/', view.get_csv)
]