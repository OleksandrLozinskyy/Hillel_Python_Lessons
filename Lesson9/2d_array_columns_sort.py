# Для генерации двухмерного массива и запроса данных от пользователя воспользуемся частью ДЗ из урока 6
import sys
from random import randrange

while True:
    column_count = input("Введите размер массива для генерации (column_count должен быть больше 5): ")
    if str(column_count) == 'q':
        sys.exit()
    elif not str(column_count).isdigit() or int(column_count) < 5:
        print('Введенное значение не удовлетворяет требованию. Значение должно быть целым числом больше 5.\n \
        Попробуйте еще раз или нажмите q для выхода.')
        continue
    else:
        break

print(f'Исходный массив будет иметь размер М*М - {column_count}*{column_count}')

column_count = int(column_count)

# Создаем исходный массив М*М
gen_arr = [[randrange(1, 50) for i in range(column_count)] for _ in range(column_count)]

# В случае необходимости можно раскомментировать и напечатать исходный массив
#print(gen_arr, '\n')


def print_array(arr):
    """
    Функция для красивой печати массива
    Печатаем элементы построчно, между элементами вставляем пробелы.
    Для того чтоб отступы были одинаковые, то разбиваем по количеству символов в элементе массива
    Для двух символьных добавляем по два пробела спереди, для односимвольных по три.
    По окончанию печати массива печатаем строку с суммами каждого столбца, также добавляем пробелы
    для соблюдения отступов
    """
    print()
    for i in range(column_count + 1):
        for j in range(column_count):
            print(f"{arr[i][j] : > 4}", end="")
        print()

def sum_and_sort_array_column(arr):
    """
    Функция сортировки значений в столбцах массива.
    Так как по условию задания в нечетных столбцах сортировка должна быть по возрастанию, а в четных по убыванию,
    то проверяем индекс столбца и разделяем код для сортировки.
    """

    # Подсчет сумм столбцов и добавление их элементом массива

    sum_list = []

    for j in range(column_count):
        column_sum = 0
        for i in range(column_count):
            column_sum += arr[i][j]
        sum_list.append(column_sum)
    arr.append(sum_list)

    # Печать несортированного массива с суммами столбцов
    print('\n')
    print('Несортированный массив с суммами столбцов', end='\n')
    print_array(arr)

    # Сортируем положение столбцов по возрастанию суммы

    for n in range(column_count - 1):
        for j in range(column_count - n - 1):
            if arr[column_count][j] > arr[column_count][j + 1]:
                arr[column_count][j], arr[column_count][j + 1] = \
                    arr[column_count][j + 1], arr[column_count][j]
                for i in range(column_count):
                    arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

    # Сортируем элементы в столбцах. В четных по убыванию, в нечетных по возрастанию

    for j in range(column_count):
        if j % 2 == 0:
            for n in range(column_count - 1):
                for i in range(column_count - n - 1):
                    if arr[i][j] < arr[i + 1][j]:
                        arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
        elif j % 2 > 0:
            for n in range(column_count - 1):
                for i in range(column_count - n - 1):
                    if arr[i][j] > arr[i + 1][j]:
                        arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
    # Печатаем результирующий отсортированный массив
    print('\n')
    print('Сортированный массив с суммами столбцов', end='\n')
    print_array(arr)


# Вызываем функцию сортировки и передаем ей как параметр сгенерированный массив

sum_and_sort_array_column(gen_arr)

