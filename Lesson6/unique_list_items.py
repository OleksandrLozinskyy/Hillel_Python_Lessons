"""    Даны два списка чисел (можно сгенерировать при помощи генератора случайных
    чисел). Посчитайте, сколько уникальных чисел содержится одновременно как в
    первом списке, так и во втором.

    Примечание. Эту задачу можно решить в одну строчку.
    (+ 5 балов если задача решена в одну строчку)"""

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

print(len(list(x for i, x in enumerate(gen_range1 + gen_range2) if i == (gen_range1 + gen_range2).index(x))))

