import re
from datetime import datetime, timedelta, date
import time


def valid_date(date_string):
    """
    return date from date string
    :param date_string: date string
    :return: date
    """
    date_string_number = re.sub('\D', '', date_string)
    try:
        date_res = datetime.strptime(date_string_number, '%Y%m%d').date()
    except ValueError:
        print("Not a valid date: '{}'.".format(date_string))
    else:
        return date_res


def date_range(start, end):
    """
    :param start: start date
    :param end: end date
    :return: dates from 'start' to 'end'
    """
    start = valid_date(start) if isinstance(start, str) else start
    end = valid_date(end) if isinstance(end, str) else end
    if start > end:
        return
    day_delta = timedelta(days=1)
    end += day_delta
    today = date.today()
    while start < end and start < today:
        yield start
        start += day_delta

if __name__ == '__main__':
    # for date in date_range('2015-12-21', '2016-12-21'):
    #     print(date)
    a = valid_date('20150808')
    print(time.mktime(a.timetuple()))
