from sys import argv
from os.path import join


def add_sale(sale):
    with open(join(".", "bakery.csv"), 'a', encoding="utf-8") as bakery:
        sale_str = str(sale)
        bakery.write(f'{sale_str}\n')

len_argv=len(argv)
if len_argv < 1:
    print('Не введена сумма, повторите попытку')
else:
    for sale in range(1, len_argv):
        try:
            float(argv[sale])
        except ValueError:
            print(f'Введено неверное значение "{argv[sale]}", должно быть число')
            continue
        add_sale(argv[sale])
