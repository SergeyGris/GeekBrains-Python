from requests import get, utils


def currency_rates(url, *args):
    valute_lst=args[0]
    num_of_valutes = len(valute_lst)
    for i in range(num_of_valutes):
        valute = valute_lst[i].upper()
        response = get(url)
        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding=encodings)
        try:
            place = content.index(valute)
            value_left_border = int(content.index('<Value>', place) + 7)
            value_right_border = int(content.index('</Value>', place))
            value = content[value_left_border:value_right_border].replace(',', '.')
            currency = float(value)
        except ValueError:
            currency = 'Неверно указана валюта'
        print(f"{valute}: {currency}")
        # return currency
