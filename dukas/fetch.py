import asyncio

from dukas.defines import URL_TEMP_DATE
from dukas.utils import date_range


def ticks_data(symbol, start, end):
    """
    :param symbol: symbol
    :param start: start date
    :param end: end date
    :return: ticks data for date range
    """
    dates = date_range(start, end)
    if not dates:
        return
    dates_data = []
    for date in dates:
        date_data = fetch_day(symbol, date)
        dates_data.extend(date_data)
    return dates_data


def day_tasks(symbol, date):
    """
    :param symbol: symbol
    :param date: date
    :return: create tasks for one day
    """
    date_string = URL_TEMP_DATE.format(symbol=symbol, year=date.year, month=date.month - 1, day=date.day)
    print(date_string)
    return [asyncio.ensure_future(
        get_file_stream(URL_TEMP.format(symbol=symbol, **url_info, hour=i))) for i in range(24)
    ]


def fetch_day(symbol, date):
    """
    :param symbol: symbol
    :param date: date
    :return: data for one day
    """
    loop = asyncio.get_event_loop()
    date_tasks = create_date_tasks(symbol, date)
    loop.run_until_complete(asyncio.wait(date_tasks))
    date_data = []
    for i in range(24):
        result = date_tasks[i].result()
        decom_data = decompress_lzma(result)
        if not decom_data:
            continue
        token_data = tokenize(decom_data)
        reform_data = format_data(token_data, date, i)
        date_data.extend(reform_data)
    return date_data