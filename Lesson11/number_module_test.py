from workwithnumsandarrays import analisenumber as an


help(an)

get_num = int(input('Введите произвольное многозначное число(количество разрядов больше  2):'))

print('Данное число, содержит рядом стоящие одинаковые цифры?', an.adjacent_digits(get_num))
print('Данное число, имее1т в составе одинаковые цифры?', an.same_numbers_in_row(get_num))