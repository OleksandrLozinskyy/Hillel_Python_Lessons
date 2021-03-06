"""
    Написать функцию которая принимает на вход параметры : список чисел
    любой длины и число . Функция должна проверить, есть ли в списке 2 числа
    сумма которых эквивалентна числу переданному 2-ым параметром. Функция должна
    вернуть булево значение - результат работы функции.
    Для проверки вызвать 2 раза функцию с разными тестовыми примерами.

    Для того чтоб не складывать одно и тоже число само с собой необходимо объявить два указателя и
    проверять, что указатели не указывают на одно и тоже число в списке. Это позволит проверять списки
    с произвольными (повторяющимися) значениями. Например список [1, 2, 5, 4, 5, 2, 1] ()
"""


def find_sum(num, *args):
    num_list = args
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)):

            # Ниже я расписал проверки в два условия, хотя можно было и в одну строку, как в комментарии ниже
            # if i != j and num_list[i] + num_list[j] == num:
            #       return True
            if i != j:
                res_num = num_list[i] + num_list[j]
                if res_num == num:
                    return True
    return False


# Для создания тестовых списков воспользуемся генераторами, которые мы изучали ранее
test_lst1 = [i for i in range(0, 7)]

# Выводим на печать исходный список и применяем функцию передавая ей число и список.
print(test_lst1)
print(find_sum(10, *test_lst1))
print(find_sum(15, *test_lst1))

# Для создания тестовых списков воспользуемся генераторами, которые мы изучали ранее
test_lst2 = [i for i in range(0, 101, 5)]

# Выводим на печать исходный список и применяем функцию передавая ей число и список.
print(test_lst2)
print(find_sum(120, *test_lst2))
print(find_sum(196, *test_lst2))

test_lst3 = [1, 2, 5, 4, 5, 2, 1]

print(test_lst3)
print(find_sum(10, *test_lst3))
print(find_sum(8, *test_lst3))