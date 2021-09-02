def sum_or_concat():
    """
    Функция получает два аргумента и конвертирует их в число. В случае если один
    из аргументов не является числом обрабатываем исключительную ситуацию и
    приводим оба аргумента к строке и конкатенируем их.
    """
    num_a = input('Введите первое значение: ')
    num_b = input('Введите второе значение: ')

    try:
        num_first = int(num_a)
        num_second = int(num_b)
    except ValueError:
        ret_str = ' '.join(map(str, (num_a, num_b)))
        print(f'Результирующая строка a + b: {ret_str}')
    else:
        sum_ab = num_first + num_second
        print(f'Сумма введенных чисел {num_first} + {num_second}: {sum_ab}')


sum_or_concat()
