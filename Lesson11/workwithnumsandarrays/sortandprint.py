"""
    Пакет предназначен для генерации 2d массива по заданным пользователем
    параметрам. Позволяет производить суммирование значений элементов по
    столбцам, сортировку по возрастанию сумм столбцов и сортировку значений
    элементов в столбцах в зависимости от четности столбца. Нечетные столбцы
    сортируются по убыванию, четные по возрастанию
Методы пакета:
    create_array - создает исходный 2d массив
    sum_and_sort_array_column - считает суммы столбцов, сортирует массив
    print_array - печатает массив
"""
from random import randrange

__all__ = ["sum_and_sort_array_column", "print_array", "create_array"]
__author__ = 'Oleksandr Lozinskyi (lsash@mail.com)'


def create_array(column_count: int, rand_start: int, rand_end: int) -> list:
    """
     Метод создает 2d массив по параметрам задаваемым пользователем. Перечень
     параметров описан ниже

    :param column_count: Числовое значение, задает количество столбцов
    создаваемого массива

    :param rand_start: Числовое значение, начало диапазона генерируемых
    значений массива

    :param rand_end: Числовое значение, конец диапазона генерируемых значений
    массива

    :return: Возвращает 2d массив из column_count столбцов, значения в столбцах
    входят в диапазон rand_start < arr[i] < rand_end
    """

    print(f'Исходный массив будет иметь размер М*М - {column_count}* \
                                                     {column_count}')

    column_count = int(column_count)

    # Создаем исходный массив М*М

    gen_arr = [[randrange(rand_start, rand_end) for i in range(column_count)]
               for _ in range(column_count)]
    return gen_arr


def print_array(arr):
    """
    Функция для красивой печати массива
    Все элементы массива помещаются в поля размером 4 символа и центрируются по
    левому краю

    :arr - Входной 2d массив n * n элементов
    """

    column_count = len(arr[0])

    print()
    for i in range(column_count + 1):
        for j in range(column_count):
            print(f"{arr[i][j] : > 4}", end="")
        print()


def sum_and_sort_array_column(arr):
    """
    Метод сортировки значений в столбцах массива.
    Данный метод вычисляет значения суммы всех элементов для каждого столбца
    массива. Затем сортирует столбцы по возрастанию сумм. После выполнения
    данной сортировки значения в нечетных столбцах сортируются по возрастанию
    значений, в четных по убыванию. На печать выводятся несортированный и
    сортированный массивы.

    :arr - Входной 2d массив n * n элементов
    """

    column_count = len(arr[0])

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

    # Сортируем элементы в столбцах. В четных по убыванию, в нечетных по
    # возрастанию

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
