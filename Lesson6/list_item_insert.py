"""Дан список целых чисел (можно сгенерировать при помощи генератора случайных
    чисел), число k и значение C.
    Необходимо вставить в список на позицию с индексом k значение C, сдвинув все
    элементы, с индексом большим k, вправо. Поскольку при этом количество
    элементов в списке увеличивается, в конец списка нужно будет добавить новый
    элемент (любое значение), используя метод append().

    - Вставку необходимо осуществлять уже в считанном списке, не делая этого
    при выводе и не создавая дополнительного списка.
    - Использовать метод insert() не разрешается."""

from random import randrange

range_input = input("Введите диапазон для генерации списка и количество элементов в списке (start, end, count): ")
range_lst = range_input.split(',')
range_lst = list(map(int, range_lst))

print('Исходный список будет иметь введенные Вами параметры:', range_lst)

gen_range = [randrange(range_lst[0], range_lst[1]) for i in range(range_lst[2])]
k_index = int(input(f"Введите индекс вставляемого элемента. Должно быть целочисленное значение от 0 до {range_lst[2]}: "))
k_value = int(input('Введите значение вставляемого элемента: '))
print('Вставляемый элемент будет иметь индекс и значение:', k_index, ',', k_value)

print('Исходный список: ', gen_range)

gen_range.append(' ')

for i in range(len(gen_range) - 1, k_index,  -1):
    gen_range[i] = gen_range[i - 1]
gen_range[k_index] = k_value

print(gen_range)