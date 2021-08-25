"""
Даны числа a и b. Определите, сколько существует последовательностей из a нулей и
b единиц, в которых никакие два нуля не стоят рядом.
"""
num_a = int(input('Введите количество нулей: '))
num_b = int(input('Введите количество единиц: '))


def without_00(a, b):
    if a > b + 1:
        return 0
    if a == 0 or b == 0:
        return 1
    return without_00(a, b - 1) + without_00(a - 1, b - 1)


print('Ввод: ', num_a, num_b)
print('Вывод: ', without_00(num_a, num_b))
