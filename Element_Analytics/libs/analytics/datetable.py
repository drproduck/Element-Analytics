def generate_date_lookup():
    """ Generate a table to map dates """
    res = {}
    _month_lookup = {
    'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr' : '04',
    'May' : '05', 'Jun' : '06', 'Jul' : '07', 'Aug' : '08',
    'Sep' : '09', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12' }
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for m in month:
        for d in range(1, 32):
            o_date = m + " " + str(d).zfill(2)
            res[o_date] = _month_lookup[m] + "-" + str(d).zfill(2)
    return res

DATE_TABLE = generate_date_lookup()
