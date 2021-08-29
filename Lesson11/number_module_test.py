from workwithnumsandarrays import analisenumber as an

help(an)

get_num = int(input('Введите произвольное многозначное число(количество \
                    разрядов больше  2):'))

print('Данное число, содержит рядом стоящие одинаковые цифры?',
      an.adjacent_digits(get_num))
print('Данное число, имеет в составе одинаковые цифры?',
      an.same_numbers_in_row(get_num))
print(f'Все автоморфные числа от 1 до {get_num}')
print(an.is_automorth_number(get_num))
