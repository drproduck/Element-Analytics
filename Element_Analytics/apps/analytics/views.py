from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from Element_Analytics.settings import MEDIA_URL
from django.views.generic import FormView
from .forms import ParserRegexForm, LogToMatForm, ParserNameForm
from .models import Matrix
from Element_Analytics.settings import DOCUMENT_ROOT, BASE_DIR
from ..upload.models import LogFile
from django import forms

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apps.upload.models import User
import seaborn as sb
# import ray.dataframe as pdr
import libs.parser.logparser as parser
import itertools, functools

import datetime

STATIC_DIR = os.path.join(BASE_DIR, 'apps/analytics/static/analytics/')
frame = None
frame_path = None
MAX_TEMP_FIG = 5


def file_parser(file_path):
    parsed_file = parser.parse_file_parallel(file_path)
    parser.to_csv(parsed_file)


COMMON_ERROR_REGEX  = '(exception|warn|error|fail|unauthorized|timeout|refused|NoSuchPageException|[^0-9]404[^0-9]|[^0-9]401[^0-9]|[^0-9]505[^0-9])'


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

    def get_context():
        logtomatform = LogToMatForm()
        regexform = ParserRegexForm()
        # parserform = ParserNameForm()
        logtomatform.fields['log'].queryset = LogFile.objects.filter(user=user)
        log_list = LogFile.objects.filter(user=user)
        mat_list = Matrix.objects.filter(user=user)
        return {'logtomatform': logtomatform, 'regexform': regexform,
                               'log_list': log_list, 'mat_list': mat_list}
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':

        # if 'logtomatform' in request.POST:
        logtomatform = LogToMatForm(request.POST)
        if logtomatform.is_valid():
            log = logtomatform.cleaned_data['log']
            mat_name = logtomatform.cleaned_data['mat_name']
            save_path = get_user_log_dir(user.username, log.log_name, mat_name)
            log_path = log.get_filepath()

            if 'regexform' in request.POST:
                regexform = ParserRegexForm(request.POST, prefix='regex')
                if regexform.is_valid():
                    # parse the log by regex
                    regex_history = regexform.cleaned_data['regex']
                    processed = parse_by_regex(log_path, regex_history)

                    # save mat file
                    parser.to_csv(processed, save_path)
                    mat = Matrix(user, log, regex_history, save_path)
                    mat.save()

                    return redirect(mat)

            regex_history = logtomatform.cleaned_data['parser_name']
            processed = parser.parse_file_parallel(log_path)

            # save mat file
            parser.to_csv(processed, save_path)
            mat = Matrix(user=user, log=log, regex_history=regex_history, path=save_path, mat_name=mat_name)
            mat.save()
            return redirect(mat)
        else:
            print('Im here')

            context = get_context()

        return render(request, 'analytics/parser.djt',
                      context=context)

    else:
        context = get_context()
        return render(request, 'analytics/parser.djt',
                      context=context)


def MainView(request, log, mat):
    if request.POST:
        chosen_column = request.POST['header choice']
    global frame, frame_path
    matrix = Matrix.objects.get(user=request.user, mat_name=mat)
    frame_path = matrix.path
    headers = [fields.DATE, fields.NAME, fields.TYPE, fields.INFO, fields.MSSG]
    frame = pd.read_csv(frame_path, names=headers)
    error_col = make_error_col(frame[fields.MSSG])
    img_path, plot_name = make_plot(error_col)
    print(img_path)

    return render(request, 'analytics/mainpage.djt', {'name':mat, 'frame':frame, 'headers':headers,
                                                       'plot_name': plot_name})


def make_error_col(df):
    if frame is None: raise Exception('Not good')
    err_col = df.str.extract(COMMON_ERROR_REGEX, expand=False)
    err_col = err_col.replace(np.nan, 'no error')
    return err_col


def make_plot(col, kind='bar'):
    # date = date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M");
    plot_name = col.name+'_'+kind+'.png'
    img_path = os.path.join(STATIC_DIR, plot_name)
    if os.path.exists(img_path):
        return img_path, plot_name
    assert type(col) is pd.Series
    plot = col.value_counts(dropna=False).plot(kind=kind)
    fig = plot.get_figure()
    plt.savefig(img_path, transparent=True, bbox_inches='tight')
    plt.close(fig)
    return img_path, plot_name


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
