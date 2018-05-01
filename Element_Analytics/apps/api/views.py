from django.contrib.auth.decorators import login_required

import libs.analytics.analytics as anal
import libs.analytics.logpreprocessor as lp
from django.http.response import JsonResponse, HttpResponseForbidden


@login_required
def error_analytics(request, file_name):
     if request.user.is_authenticated():
          dframe = lp.read_log(request.user.username, file_name)
          json_obj = anal.error_analytics(dframe)
          return JsonResponse(json_obj)
     return HttpResponseForbidden()


@login_required
def user_analytics(request):
     if request.user.is_authenticated():
          return anal.user_analytics(request.user)
     return HttpResponseForbidden()


@login_required
def regex_search(request, regex):
     pass