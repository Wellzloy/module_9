# import time
# import sys
#
# def func_gen_dec(precision):
#     def dec(func):
#         def wrapper(*args, **kwargs):
#             started_at = time.time()
#             result = func(*args, **kwargs)
#             ended_at = time.time()
#             elapsed = round(ended_at - started_at, precision)
#             print(f'Функция работала {elapsed} секунд(ы)')
#             return result
#         return wrapper
#     return dec
#
# @func_gen_dec(precision=6)
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return  len(str(total))
#
#
# sys.set_int_max_str_digits(10**5)
#
# # time_track_precision_6 = func_gen_dec(precision=10)
# # digits = time_track_precision_6(digits)
# result = digits(3141, 5926, 2718, 2818)
# print(result)

# # 1
#
# animal = 'мишка'
#
# def gen_repeat(n):
#
#     def repeat(animal):
#
#         return (animal[:2] + '_') * n + animal
#
#     return repeat
#
#
# test_1 = gen_repeat(1)
# test_2 = gen_repeat(2)
#
# print(test_1(animal))
# print(test_2(animal))
#
# # 2
#
# repetitions = [gen_repeat(n) for n in range(1, 4)]
# print(repetitions)
#
# result = [func(animal) for func in repetitions]
# print(result)
#
# # 3
# animals = ['зайка', 'мишка', 'бегемотик']
# fin_result = [func(x) for func in repetitions for x in animals]
# print(fin_result)

# 4
def memoize_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргументами = {args}, внутренняя память = {mem}')
        if args not in mem:
            result = f(*args)
            mem[args] = result
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена ранее, ответ = {mem[args]}'
    return wrapper()


@memoize_func
def func(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
