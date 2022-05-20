from requests import get, utils
from decimal import Decimal

def currency_rates(url, valute):
    try:
        valute = valute.upper()
        response = get(url)
        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding=encodings)
        place = content.index(valute)
        value_left_border = int(content.index('<Value>', place) + 7)
        value_right_border = int(content.index('</Value>', place))
        value = content[value_left_border:value_right_border].replace(',', '.')
        currency=Decimal(value)
        print(currency)
        return currency
    except ValueError:
        print(None)
        return None

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_rates(url, 'USd')
currency_rates(url, "EuR")
currency_rates(url, "GBP")
currency_rates(url, "GBP2")
