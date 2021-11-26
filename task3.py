def type_logger(func):
    def wrapper(*args):
        calc = func(*args)
        print(f'{args[0]}: {type(args[0])}')
        return calc
    return wrapper
@type_logger
def calc_cube(x, *args):
   return x ** 3
area1 = calc_cube(5)
print(area1)
