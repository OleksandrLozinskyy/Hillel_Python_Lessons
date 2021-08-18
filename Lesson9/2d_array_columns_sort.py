# Для генерации двухмерного массива и запроса данных от пользователя воспользуемся частью ДЗ из урока 6
from random import randrange

while True:
    column_count = input("Введите размер массива для генерации (column_count должен быть больше 5): ")
    if str(column_count) == 'q':
        break
    elif not str(column_count).isdigit() or int(column_count) <= 5:
        print('Введенное значение не удовлетворяет требованию. Значение должно быть целым числом больше 5.\n \
        Попробуйте еще раз или нажмите q для выхода.')
        continue
    else:
        break

print(f'Исходный массив будет иметь размер М*М - {column_count}*{column_count}')

column_count = int(column_count)
# Создаем пустой список для сумм столбцов
sum_lst = []
# Создаем исходный массив М*М
gen_arr = [[randrange(1, 50) for i in range(column_count)] for _ in range(column_count)]

# Считаем сумму столбца.
for n in range(len(gen_arr)):
    column_sum = 0
    for m in range(len(gen_arr[n])):
        column_sum += gen_arr[n][m]
    sum_lst.append(column_sum)

# print(gen_arr, '\n')


def print_array(arr, sum_lst):
    for j in range(column_count):
        for i in range(column_count):
            if len(str(gen_arr[i][j])) == 1 and j == 0:
                print('   ', gen_arr[i][j], end=' ')
            elif len(str(gen_arr[i][j])) == 2 and j == 0:
                print('  ', gen_arr[i][j], end=' ')
            if len(str(gen_arr[i][j])) == 1 and j > 0:
                print('   ', gen_arr[i][j], end=' ')
            elif len(str(gen_arr[i][j])) == 2 and j > 0:
                print('  ', gen_arr[i][j], end=' ')
        print('\n')
    for n in range(len(sum_lst)):
        if n == 0:
            print(' ',sum_lst[n], end='  ')
        else:
            print('', sum_lst[n], end='  ')
    print('\n')


def sort_array_column(arr):
    for item in range(column_count):
        lst = arr[item]

        if item % 2 == 0:
            for i in range(column_count - 1):
                for j in range(column_count - i - 1):
                    if lst[j] < lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        elif item % 2 > 0:
            for i in range(column_count - 1):
                for j in range(column_count - i - 1):
                    if lst[j] > lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]


print('\n\n')
print_array(gen_arr, sum_lst)
print('\n\n')
sort_array_column(gen_arr)
gen_arr.append(sum_lst)
print_array(gen_arr, sum_lst)
