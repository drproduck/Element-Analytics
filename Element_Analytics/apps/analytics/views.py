from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from Element_Analytics.settings import MEDIA_URL
from django.views.generic import FormView
from .forms import ParserRegexForm, LogToMatForm, ParserNameForm
from .models import Matrix
from Element_Analytics.settings import DOCUMENT_ROOT
from ..upload.models import LogFile

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from apps.upload.models import User
import seaborn as sb
# import ray.dataframe as pdr
import libs.parser.logparser as parser
import libs.parser.logfields as lf
import itertools, functools
current_file = None
current_file_name = None
current_frame = None
headers = None
temp_dir = None
path = None
MAX_TEMP_FIG = 5

def  file_parser(file_path):
    parsed_file = parser.parse_file_parallel(file_path)
    parser.to_csv(parsed_file)

COMMON_ERROR_REGEX  = 'exception|warn|error|fail|unauthorized|timeout|refused|NoSuchPageException|[^0-9]404[^0-9]|[^0-9]401[^0-9]|[^0-9]505[^0-9]'

def make_error_regex(list, append_common=True):
    agg_terms = functools.reduce(lambda x,y: x+'|'+y, list)
    return agg_terms if not append_common else COMMON_ERROR_REGEX+'|'+agg_terms

def build_file_list(user_log_dir):
    """return a list of tuples each containing the file name and its path"""
    return [(f, os.path.join(user_log_dir, f)) for f in os.listdir(user_log_dir) if not f.endswith('.raw')
            or f.endswith('.csv')]

def parser_box(request):
    if request.method == 'POST':
        parser_form = ParserRegexForm(request.POST['parser_command'])
        if parser_form.is_valid():
            print('OK')
    else:
        parser_form = ParserRegexForm()
        return render()

def parse_by_regex(path, regex):
    ""

def get_user_log_dir(user, log, mat_name):
    """root -> user dir -> log dir -> bunch of .csv and a single .raw"""
    return os.path.join(DOCUMENT_ROOT, user, log+'_dir', mat_name+'.csv')

def ParserFormView(request):

    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':

        # if 'logtomatform' in request.POST:
        logtomatform = LogToMatForm(request.POST)
        if logtomatform.is_valid():
            log = logtomatform.cleaned_data['log']
            mat_name = logtomatform.cleaned_data['mat_name']
            save_path = get_user_log_dir(user.username, log.log_name, mat_name)
            log_path = log.get_filepath()

            # if 'regexform' in request.POST:
            #     regexform = ParserRegexForm(request.POST, prefix='regex')
            #     if regexform.is_valid():
            #         # parse the log by regex
            #         regex_history = regexform.cleaned_data['regex']
            #         processed = parse_by_regex(log_path, regex_history)
            #
            #         # save mat file
            #         parser.to_csv(processed, path)
            #         mat = Matrix(user, log, regex_history, path)
            #         mat.save()
            #
            #         return redirect(mat)

            regex_history = logtomatform.cleaned_data['parser_name']
            processed = parser.parse_file(log_path)

            # save mat file
            parser.to_csv(processed, save_path)
            mat = Matrix(user=user, log=log, regex_history=regex_history, path=save_path, mat_name=mat_name)
            mat.save()
            print('Im here')
            return redirect(mat)

    else:
        logtomatform = LogToMatForm()
        # regexform = ParserRegexForm()
        # parserform = ParserNameForm()
        logtomatform.fields['log'].queryset = LogFile.objects.filter(user=user)
        log_list = LogFile.objects.filter(user=user)
        mat_list = Matrix.objects.filter(user=user)
        return render(request, 'analytics/parser.djt',
                      context={'logtomatform': logtomatform,
                             'log_list': log_list, 'mat_list': mat_list})


def MainView(request, log, mat):
    return HttpResponse("hello there")


def file_home(request, file_name):
    print("Why am I here?")
    global current_file, current_frame, current_file_name, headers, temp_dir, path
    current_file_name = file_name
    path = os.path.join(MEDIA_URL, 'documents/'+file_name)
    temp_dir = os.path.join(MEDIA_URL, 'temp/'+file_name+'/')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    if not path.endswith(('.csv', '.log')):
        return HttpResponse("incorrect format")
    current_file = path
    current_frame = pd.read_csv(path)
    headers = list(current_frame)

    return render(request, 'analytics/file_home.djt', {'name':file_name, 'frame':current_frame,
                                                        'headers':headers})

def variable_plot(request, file_name):
    header = headers[1]
    print(header)
    if request.method == 'POST':
        col_name = request.POST['value']

        fig_path = os.path.join(temp_dir, col_name + '.png')
        if not os.path.exists(fig_path):
            gr = sb.distplot(current_frame[col_name]).get_figure()
            gr.savefig(fig_path, format="png")
            plt.close()

        # if number of temp files > MAX_TEMP_FIG, remove earliest
        temp_files = [os.path.join(temp_dir, f) for f in os.listdir(temp_dir)]
        fig_files = [f for f in temp_files if f.endswith('.png') == True]
        print(fig_files)
        if len(fig_files) > MAX_TEMP_FIG:
            _, f = min([(os.path.getctime(f), f) for f in fig_files])
            os.remove(f)
        print(header)

    return HttpResponse(open(fig_path, 'rb').read(), content_type="image/png")
