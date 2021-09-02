def sum_or_concat():
    """
    Функция получает два аргумента и конвертирует их в число. В случае если один
    из аргументов не является числом обрабатываем исключительную ситуацию и
    приводим оба аргумента к строке и конкатенируем их.
    """

    try:
        num_a = input('Введите первое значение: ')
        num_b = input('Введите второе значение: ')
        num_a = int(num_a)
        num_b = int(num_b)
    except ValueError as err:
        ret_str = ' '.join(map(str, (num_a, num_b)))
        print(f'Результирующая строка a + b: {ret_str}')
    else:
        sum_ab = num_a + num_b
        print(f'Сумма введенных чисел {num_a} + {num_b}: {sum_ab}')


sum_or_concat()

