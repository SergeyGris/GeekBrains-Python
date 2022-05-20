class ZeroDevError(Exception): pass

def dev_func(x,y):
    if y!=0:
        return x/y
    else:
        raise ZeroDevError

num_lst=[-1,0,1,2]
for num in num_lst:
    for dev in num_lst:
        try:
            rez=dev_func(num,dev)
        except ZeroDevError:
            rez='Деление невозможно! Деление на ноль'
        finally:
            print(f'{num}/{dev}={rez}')
