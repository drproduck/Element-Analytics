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
            "caption": "Keyword analytics",
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
            "caption": "Date analytics",
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

    for x in range(len(list_keyword)):
        str_keyword += str(list_keyword[x]) + ",\n"

    str_keyword = str_keyword.strip()[:-1] + "]\n}"

    for x in range(len(list_date)):
        str_date += str(list_date[x]) + ",\n"

    str_date = str_date.strip()[:-1] + "]\n}"

    return str_keyword, str_date
