"""
Модифицированное решение. Функция подсчета среднего бала вынесена отдельно.
"""


def average(lst) -> float:
    """
    Функция подсчета среднего бала
    :param lst: Список балов для подсчета среднего значения
    :return: Средний бал округленный до 2 знаков после запятой
    """
    avg = 0
    count = 0

    for ele in lst:
        avg += float(ele)
        count += 1
    avg = round(avg / count, 2)
    return avg


def get_students(filename):

    avg_dict = {}

    with open(filename, 'r', encoding='utf-8') as in_file:
        for line in in_file.readlines():
            firstname, lastname, *score_lst = line.split()
            # Согласно условия задания переформатируем вывод ФИ
            full_name = ' '.join([lastname, (firstname[0] + '.')])
            avg_dict[full_name] = average(score_lst)

    # Выведем список студентов с низкой успеваемостью. Средний бал меньше 5
    for key in avg_dict.keys():
        if avg_dict[key] < 5:
            print('{:25s} {:.2f}'.format(key, avg_dict[key]))
    # Выведем средний бал по группе
    group_avg = average(avg_dict.values())
    print('{:25s} {:5s}'.format('Средний балл по группе :',
                                str(group_avg)))
    # Выводим список студентов и средний бал каждого студента в новый файл
    with open('src_15_1.txt', 'w', encoding='utf-8') as out_file:
        for key in avg_dict.keys():
            line = '{:25s} {:.2f}{:1s}'.format(key, avg_dict[key], '\n')
            out_file.write(line)


get_students('src_14.txt')
