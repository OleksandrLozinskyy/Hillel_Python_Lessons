"""
Функция получает на вход имя файла в котором содержится список студентов и
оценки за определенный период. Из файла производится чтение и следующие
операции:
    - переформатирование представления "Имя Фамилия" в представление
    "Фамилия И."
    - подсчет среднего балла по каждому студенту
    - подсчет среднего балла группы
    - вывод студентов с низкой успеваемостью (бал ниже 5)
    - вывод средней успеваемости группы
    - сохранение в файл информации по группе в формате
        Фамилия И.  Ср.бал
"""


def get_students(filename):

    avg_dict = {}

    with open(filename, 'r', encoding='utf-8') as in_file:

        for line in in_file.readlines():
            firstname, lastname, *score_lst = line.split()

            full_name = ' '.join([lastname, (firstname[0] + '.')])

            score_sum = 0
            count = 0

            for score in score_lst:
                score_sum += int(score)
                count += 1

            avg_dict[full_name] = round(score_sum / count, 2)

    group_avg = 0
    count = 0
    # Выведем список студентов с низкой успеваемостью (бал < 5) и посчитаем
    # общий бал по группе и количество студентов.
    for key in avg_dict.keys():
        group_avg += avg_dict[key]
        count += 1

        if avg_dict[key] < 5:
            print('{:25s} {:.2f}'.format(key, avg_dict[key]))
    # Выведем средний бал по группе
    print('{:25s} {:5s}'.format('Средний балл по группе :',
                                str(round(group_avg / count, 2))))
    # Выводим список студентов и средний бал каждого студента в новый файл
    with open('src_14_1.txt', 'w', encoding='utf-8') as out_file:
        for key in avg_dict.keys():
            line = '{:25s} {:.2f}{:1s}'.format(key, avg_dict[key], '\n')
            out_file.write(line)


get_students('src_14.txt')
