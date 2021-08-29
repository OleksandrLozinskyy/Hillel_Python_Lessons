"""
Модуль осуществляет сортировку последовательностей с помощью различных
алгоритмов.

    bubble_sort: функция сортировки переданного массива методом пузырька

    bubble_rock_sort: функция сортировки переданного массива методом камня

    insertion_sort: функция сортировки переданного массива методом вставки
"""

__all__ = ['bubble_sort', 'bubble_rock_sort', 'insertion_sort']
__author__ = 'Oleksandr Lozinskyi (lsash@mail.com)'


def bubble_sort(arr) -> list:
    """
    Функция осуществляет сортировку переданного массива методом пузырька

    :param arr: Принимает несортированный массив

    :return: Возвращает отсортированный массив arr в виде списка
    """

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 2, i - 1, -1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_rock_sort(arr) -> list:
    """
    Функция осуществляет сортировку переданного массива методом камня

    :param arr: Принимает несортированный массив

    :return: Возвращает отсортированный массив arr в виде списка
    """

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr) -> list:
    """"
    Функция осуществляет сортировку переданного массива методом вставки

    :param arr: Принимает несортированный массив

    :return: Возвращает отсортированный массив arr в виде списка
    """

    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1

        # Элементы отсортированного сегмента перемещаем вперед, если они больше
        # элемента для вставки

        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
        # Вставляем элемент
        arr[j + 1] = item_to_insert
    return arr