''' 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

arg_1 = int(input('Введите 1 число'))
arg_2 = int(input('Введите 2 число'))


def dev(arg_1, arg_2):  # Дмитрий почему pycharm подчеркивает arg_1 and arg_2 ?
    try:
        res = arg_1 / arg_2
    except(ZeroDivisionError, ValueError):
        return 'Поделили на 0 или ввели строку'
    return res


print(dev(arg_1, arg_2))
