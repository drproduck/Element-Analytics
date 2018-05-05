from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponse, HttpResponseForbidden

import libs.analytics.analytics as anal
import libs.analytics.logpreprocessor as lp



@login_required
def error_analytics(request, file_name):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseForbidden()
    log_file = user.logfile_set.get(log_name=file_name)
    if not log_file:
        return HttpResponseForbidden()
    dframe = lp.read_log(request.user.username, file_name)
    json_obj = anal.error_analytics(dframe)
    return JsonResponse(json_obj, safe=False)


@login_required
def user_analytics(request):
    if request.user.is_authenticated:
        return JsonResponse(anal.user_analytics(request.user), safe=False)
    return HttpResponseForbidden()


@login_required
def regex_search(request, regex):
    pass