from sys import argv
from os.path import join


def edit_sales(*args):
    with open(join(".", "bakery.csv"),'r+', encoding="utf-8") as bakery:
        number, edition = args
        n=1
        while n!=number:
           bakery.readline()
           n+=1
        edit_line = bakery.tell()
        bakery.readline()
        left_lines_list=bakery.readlines()
        bakery.seek(edit_line)
        bakery.truncate()
        bakery.write(f'{edition}\n')
        for line in left_lines_list:
            bakery.write(line)
# argv=[0,1,1]
_,number,edition=argv
number=int(number)
edition=float(edition)
edit_sales(number,edition)
