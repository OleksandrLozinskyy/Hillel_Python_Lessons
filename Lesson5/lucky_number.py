from random import randint

chance = 0  # Количество попыток
lucky_number = randint(1, 100)  # Загаданное число

while True:
    user_number = input('Введите загаданное число: ')  # Значение введенное пользователем
    chance += 1  # Увеличиваем значение счетчика, после каждого ввода
    if not user_number.isdigit():  # Проверяем, если введены не цифры, ругаемся и пропускаем шаг
        print('Вы ввели не число')
        continue
    elif int(user_number) not in range(1, 101):  # Если все же введены цифры, проверяем вхождение в диапазон
        print('Вы ввели число за пределами диапазона игры')  # Если не входит в диапазон, ругаемся и пропускаем шаг
        continue

    if int(user_number) > lucky_number:  # Пользователь ввел значение больше загаданного
        print('Загаданное число меньше')
    elif int(user_number) < lucky_number:  # Пользователь ввел значение меньше загаданного
        print('Загаданное число больше')
    elif int(user_number) == lucky_number:
        print(f'Вы угадали! Загаданное число {lucky_number}, количество использованных попыток {chance}')
        break
