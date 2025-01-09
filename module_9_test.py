# def get_russian_names():
#     return ['Ваня', 'Коля', 'Маша', ]
#
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry', ]
#
#
# name_getters = [get_russian_names, get_british_names]
#
# for name_getter in name_getters:
#     print(name_getter())
#

# get_russian_names()
# print(type(get_russian_names))
# print(get_russian_names.__name__)
# my_func = get_russian_names
# print(my_func())
# print(my_func.__name__)
def adder(args):
    res = 0
    for number in args:
        res += number
    return res


def multiplier(args):
    res = 1
    for number in args:
        res *= number
    return res


def process_numbers(numbers, function):
    result = function(numbers)
    print(f'Получилось {result}')


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

process_numbers(numbers=my_numbers, function=adder)
process_numbers(numbers=my_numbers, function=multiplier)