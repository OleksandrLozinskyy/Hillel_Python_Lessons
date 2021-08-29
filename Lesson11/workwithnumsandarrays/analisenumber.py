"""
Данный модуль позволяет определить наличие одинаковых однозначных чисел в записи
многозначного числа. Числа могут находиться рядом, т.е идти последовательно или
же находиться на произвольной позиции в заданном пользователем числе.
Например наличие двух цифр 8 в числе 318028. А также узнать есть ли в многознач-
ном числе одинаковые рядом стоящие однозначные числа. Например цифра 1 в числе
201104.
Также данный модуль позволяет вывести в терминал все автоморфные числа от 1 до
числа введенного пользователем
"""

__all__ = ["adjacent_digits", "same_numbers_in_row", "is_automorth_number"]
__author__ = 'Oleksandr Lozinskyi (lsash@mail.com)'


def adjacent_digits(num: int) -> str:
    """
    Функция позволяет проверить наличие рядом стоящих одинаковых однозначных
    цифр в многозначном числе и вывести текстовый ответ.

    :param num: Многозначное число заданное пользователем

    :return: Возвращает "Да", если обнаружены рядом стоящие одинаковые
    однозначные числа и "Нет", если они не обнаружены
    """

    ret_value = ['Да', 'Нет']
    counter = 0
    n = 0
    lst = list(str(num))
    string_set = set(lst)

    if len(lst) != len(string_set):
        while n < (len(lst) - 1):
            if lst[n] == lst[n + 1]:
                counter += 1
            n += 1

    if counter > 0:
        return ret_value[0]
    else:
        return ret_value[1]


def same_numbers_in_row(num: int) -> str:
    """
    Функция позволяет проверить наличие одинаковых однозначных цифр в
    многозначном числе, стоящих на произвольных позициях и вывести текстовый
    ответ.

    :param num: Многозначное число заданное пользователем

    :return: Возвращает "Да", если обнаружены одинаковые однозначные числа и
    "Нет", если они не обнаружены
    """

    ret_value = ['Да', 'Нет']
    lst = list(str(num))
    string_set = set(lst)

    if len(lst) != len(string_set):
        return ret_value[0]
    else:
        return ret_value[1]


def is_automorth_number(num: int):

    """
    Функция возвращает все автоморфные числа от 1 до числа введенного
    пользователем. Натуральное число называется автоморфным, если оно равно
    последним цифрам своего квадрата.
    Например, 25 ** 2 = 625.

    :param num: Верхняя граница диапазона проверки на наличие автоморфных чисел

    :return: Печатает в консоль все автоморфные числа от 1 до числа введенного
    пользователем
    """
    for n in range(1, (num + 1)):
        result = n ** 2
        len_of_n = len(str(n))

        div = 10 ** len_of_n

        res = result % div

        if n == res:
            print(f'{n} * {n} = {n ** 2}')
