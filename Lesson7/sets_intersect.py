"""
1. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно
    как в первом списке, так и во втором.
    - Примечание. Эту задачу на python можно решить в одну строчку.

Также как и в предыдущей задаче для генерации списков воспользуемся генераторами из прошлых ДЗ
Решение будет одной строчкой, после подготовки списков
"""

from random import randrange

range1_input = input("Введите диапазон для генерации списка и количество элементов в списке (start, end, count): ")
range1_lst = range1_input.split(',')
range1_lst = list(map(int, range1_lst))
range2_input = input("Введите диапазон для генерации списка и количество элементов в списке (start, end, count): ")
range2_lst = range2_input.split(',')
range2_lst = list(map(int, range2_lst))
print('Исходный список 1 будет иметь введенные Вами параметры:', range1_lst)
print('Исходный список 2 будет иметь введенные Вами параметры:', range2_lst)

gen_range1 = [randrange(range1_lst[0], range1_lst[1]) for i in range(range1_lst[2])]
gen_range2 = [randrange(range2_lst[0], range2_lst[1]) for i in range(range2_lst[2])]

# Выведем на печать сгенерированные списки и результирующий set для удобства проверки. Для решения не требуется,
# В окончательном варианте может быть удалено или закомментировано по желанию.
print(gen_range1)
print(gen_range2)
print(set(gen_range1).intersection(set(gen_range2)))

# Подготовительные работы закончены, можем приступать к решению

print(len(set(gen_range1).intersection(set(gen_range2))))