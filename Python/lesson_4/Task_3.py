from requests import get, utils
from datetime import date as DT

def currency_rates(url, valute):
    valute = valute.upper()
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date_left_border = int(content.index('Date="') + 6)
    date_right_border = int(content.index('" name'))
    day, month, year = content[date_left_border:date_right_border].split('.')
    date = DT(int(year), int(month), int(day))
    try:
        place = content.index(valute)
        value_left_border = int(content.index('<Value>', place) + 7)
        value_right_border = int(content.index('</Value>', place))
        value = content[value_left_border:value_right_border].replace(',', '.')
        currency = float(value)
    except ValueError:
        currency = None
    currency_with_date = [date, currency]
    print(currency_with_date)
    return currency

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_rates(url, 'USd')
currency_rates(url, "EuR")
currency_rates(url, "GBP")
currency_rates(url, "GBP2")
