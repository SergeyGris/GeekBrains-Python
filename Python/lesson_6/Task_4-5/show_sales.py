from sys import argv
from os.path import join


def show_sales(*args):
    with open(join(".", "bakery.csv"), encoding="utf-8") as bakery:
        start, end = args
        n = 1
        for line in bakery:
            if end is None:
                if n >= start:
                    print(line.strip())
            else:
                if end >= n >= start:
                    print(line.strip())
            n += 1


end = None
start = 1
if len(argv) > 3:
    print('Введено некорректное число записей, повторите попытку')
    exit()
elif len(argv) >= 2:
    try:
        start = int(argv[1])
        if len(argv) > 2:
            end = int(argv[2])
    except ValueError:
        print('Введено некорректное число записей, повторите попытку')
        exit()
show_sales(start, end)
