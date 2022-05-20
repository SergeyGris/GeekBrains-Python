from utils import currency_rates

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_rates(url, 'USd')
currency_rates(url, "EuR")
currency_rates(url, "GBP")
currency_rates(url, "GBP2")