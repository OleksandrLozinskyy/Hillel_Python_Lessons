numb = int(input('Введите произвольное целое число: '))

for n in range(1, (numb + 1)):
    result = n ** 2
    len_of_result = len(str(result))
    len_of_n = len(str(n))

    div = 10 ** len_of_n

    res = result % div

    if n == res:
        print(f'{n} * {n} = {n ** 2}')
