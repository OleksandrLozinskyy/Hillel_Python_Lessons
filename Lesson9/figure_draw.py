n = int(input('Введите высоту фигуры в символах: '))

lst = [i for i in range(2 * n - 1, 0, -2)]

for i in range(1, n + 1):
    print(' ' * (lst[i - 1] - 1) + ' '.join('*' * lst[-i]) + ' ' * (lst[i - 1] - 1))

lst1 = [j for j in range(0, 4*n, 3)]
print(lst1)

