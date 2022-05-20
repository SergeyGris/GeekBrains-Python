def type_logger(func):
    def wrapper(*args, **kwargs):
        print(f'Call for: {func.__name__}')
        rezult = func(*args, **kwargs)
        for arg in args:
            print(f'{arg}: {type(arg)}')

        for var, val in kwargs.items():
            print(f"'{var}' = {val}: {type(val)}")
        print(f'Rezult: {rezult}  type: {type(rezult)}')
        # return rezult

    return wrapper


@type_logger
def render_input(*args, **kwargs):
    return 1


@type_logger
def calc_cube(x):
    return x ** 3
