from utils_2 import currency_rates
from sys import argv
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
if len(argv)==1:
    print('Не введена валюта =(')
else:
    valute=argv[1:]
    currency=currency_rates(url, valute)
