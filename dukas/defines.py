URL_TEMP_DATE = 'https://www.dukascopy.com/datafeed/{symbol}/{year}/{month:02d}/{day:02d}/'
URL_TEMP_HOUR = '{hour:02d}h_ticks.bi5'
HOURS_LIST = [URL_TEMP_HOUR.format(hour=i) for i in range(24)]
TRY_HOUR_ATTEMPTS = 4

TIMEFRAME_RULE_DICT = {
    'M1': '1T',
    'M5': '5T',
    'M15': '15T',
    'M30': '30T',
    'H1': '1H',
    'H4': '4H',
    'D1': '1D',
    'W1': '1W-SUN',
    'MN': '1MS'
}

