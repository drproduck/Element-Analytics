from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponseForbidden,\
    HttpResponse
import libs.analytics.analytics as anal
import libs.analytics.logpreprocessor as lp
import libs.utilities.dbutils as du
import libs.utilities.pathtools as pt
import os


@login_required
def validate_request(request, file_name):
    user = request.user
    if not user.is_authenticated:
        return False
    log_file = user.logfile_set.get(log_name=file_name)
    if not log_file:
        return False
    return True


@login_required
def analytics(request, file_name):
    if not validate_request(request, file_name):
        return HttpResponseForbidden("Content doesn't exist")
    if request.method == 'POST':
        sf = request.POST.get('search_field', '')
        reg = request.POST.get('keywords', '')
        if not sf or not reg:
            return HttpResponse("0")
        dframe = lp.read_log(request.user.username, file_name)
        json_obj = anal.analytics(dframe, reg.split("\n"), sf)
        return JsonResponse(json_obj, safe=False)
    return HttpResponseForbidden("ERROR: Wrong HTTP method. Expected: POST")


@login_required
def error_analytics(request, file_name):
    if not validate_request(request, file_name):
        return HttpResponseForbidden("Content doesn't exist")
    if request.method == 'GET':
        dframe = lp.read_log(request.user.username, file_name)
        json_obj = anal.error_analytics(dframe)
        return JsonResponse(json_obj, safe=False)
    return HttpResponseForbidden("ERROR: Wrong HTTP method. Expected: GET")


@login_required
def usage_analytics(request, file_name):
    if not validate_request(request, file_name):
        return HttpResponseForbidden("Content doesn't exist")
    if request.method == 'GET':
        dframe = lp.read_log(request.user.username, file_name)
        json_obj = anal.usercase_analytics(dframe)
        return JsonResponse(json_obj, safe=False)
    return HttpResponseForbidden("ERROR: Wrong HTTP method. Expected: GET")


@login_required
def user_analytics(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return JsonResponse(anal.user_analytics(request.user), safe=False)
        return HttpResponseForbidden("ERROR: Wrong HTTP method. Expected: GET")
    return HttpResponseForbidden("ERROR: User is not authenticated")


@login_required
def regex_search(request, regex):
    pass


@login_required
def delete(request):
    if request.user.is_authenticated:
        file_name = request.GET.get('file', ' ')
        if not file_name:
            return HttpResponse(1)
        du.delete_log(request.user, file_name)
        return HttpResponse(0)
    return HttpResponseForbidden()


@login_required
def download(request, file_name):
    user = request.user
    file_path = os.path.join(pt.get_log_dir_abs(user.username, file_name), file_name + ".csv")
    if not os.path.isfile(file_path):
        return HttpResponseForbidden("File doesn't exist")
    with open(file_path, 'r') as fp:
        response = HttpResponse(fp.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + file_name + ".csv"
        return response

