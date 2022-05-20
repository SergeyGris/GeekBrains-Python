from functools import wraps


def val_checker(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if (lambda x: x > 0)(arg) == True:
                result = func(arg)
                print(result)
                return result
            else:
                print(f'ValueError: wrong val {arg}')
                raise ValueError

    return wrapper
    # return _val_checker


@val_checker
def calc_cube(x):
    return x ** 3


calc_cube(5)
