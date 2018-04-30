import json

def json2chart():
    with open('apps/chart/data.json') as f_in:
        my_data =(json.load(f_in))

    list_keyword = []
    list_date = []

    for k, v in my_data["error_by_keyword"].items():
        dict = {"label": k, "value": v}
        list_keyword.append(dict)

    for k, v in my_data["errors_by_date"].items():
        dict = {"label": k, "value": v}
        list_date.append(dict)

    str_keyword = """ {
        "chart": {
            "caption": "Keyword Column",
            "subCaption": "",
            "xAxisName": "keyword",
            "yAxisName": "count",
            "numberPrefix": "",
            "theme": "fint",
            "exportEnabled": "1",
            "exportTargetWindow": "_self",
            "exportFileName": "keyword_analytics"
        },
        "data": [
    """
    str_date = """ {
        "chart": {
            "caption": "Date Column",
            "subCaption": "",
            "xAxisName": "date",
            "yAxisName": "count",
            "numberPrefix": "",
            "theme": "fint",
            "exportEnabled": "1",
            "exportTargetWindow": "_self",
            "exportFileName": "date_analytics"
        },
        "data": [
    """

    str_keyword_pie = """ {
        "chart": {
            "caption": "Keyword Pie",
            "subCaption": "",
            "startingangle": "120",
            "showlabels": "0",
            "showlegend": "1",
            "enablemultislicing": "0",
            "slicingdistance": "15",
            "showpercentvalues": "1",
            "showpercentintooltip": "0",
            "plottooltext": "Keyword : $label Count : $datavalue",
            "theme": "fint",
            "exportEnabled": "1",
            "exportTargetWindow": "_self",
            "exportFileName": "keyword_analytics"
        },
        "data": [
    """
    str_date_pie = """ {
        "chart": {
            "caption": "Date Pie",
            "subCaption": "",
            "startingangle": "120",
            "showlabels": "0",
            "showlegend": "1",
            "enablemultislicing": "0",
            "slicingdistance": "15",
            "showpercentvalues": "1",
            "showpercentintooltip": "0",
            "plottooltext": "Date : $label Count : $datavalue",
            "theme": "fint",
            "exportEnabled": "1",
            "exportTargetWindow": "_self",
            "exportFileName": "date_analytics"
        },
        "data": [
    """

    for x in range(len(list_keyword)):
        str_keyword += str(list_keyword[x]) + ",\n"
        str_keyword_pie += str(list_keyword[x]) + ",\n"

    str_keyword = str_keyword.strip()[:-1] + "]\n}"
    str_keyword_pie = str_keyword_pie.strip()[:-1] + "]\n}"

    for x in range(len(list_date)):
        str_date += str(list_date[x]) + ",\n"
        str_date_pie += str(list_date[x]) + ",\n"

    str_date = str_date.strip()[:-1] + "]\n}"
    str_date_pie = str_date_pie.strip()[:-1] + "]\n}"

    return str_keyword, str_date, str_keyword_pie, str_date_pie
