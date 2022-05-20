class IncorrectNumber(Exception): pass


num_lst = []
num = None


def num_valid(num):
    # i = 0
    # if num[0] == '-':
    #     i = 1
    # if num[i:].isdigit():
    #     return int(num)
    # else:
    #     raise IncorrectNumber
    try:
        return  int(num)
    except ValueError:
        raise NotNumberException(f"{num} - не целое число")


while num != 'stop':
    num = input('Введите число. Для остановки наберите "stop"')
    if num == 'stop':
        print('Программа завершена')
        break
    try:
        rez = num_valid(num)
    except IncorrectNumber:
        print('Неверное число. ', num_lst)
        continue
    num_lst.append(rez)
    print(num_lst)
