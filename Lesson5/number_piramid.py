entered_num = input('Input number from 3 to 9: ')
passed_number = entered_num.isdigit()  # Проверяем что введенные символы цифры

if not passed_number:
    if entered_num[0] == '-' and entered_num[1:].isdigit():
        print(f'Введенное значение должно быть положительным числом. Работа приложения завершена')
    elif entered_num.find('.') >= 0 and (entered_num.replace('.', '', 1)).isdigit():
        print(f'Введенное значение не должно быть дробным. Попробуйте еще раз!')
    elif entered_num[0] == '-' and entered_num.find('.') >= 1 and (entered_num[1:].replace('.', '', 1)).isdigit():
        print(f'Введенное значение не должно быть отрицательным и дробным. Попробуйте еще раз!')
    else:
        # В случае, если введен текст или символы, выводим сообщение об ошибке и завершаем работу
        print('Введено не число! Работа приложения завершена')
elif passed_number:
    entered_num = int(entered_num)  # Так как ранее мы проверили, что введенные значения цифры, то переводим его в число
    if entered_num in range(3, 10):
        for i in range(1, entered_num + 1):
            row = ''  # Инициализируем пустую строку
            for count in range(1, i):
                # В цикле заполняем строку по возрастанию дописывая значения в конец строки
                row += str(count)
            for count in range(i, 0, -1):
                # В цикле заполняем строку по убыванию дописывая значения в конец строки
                row += str(count)
            # Печатаем сформированную строку
            print(row)
    else:
        print('Введено число за пределами диапазона! Работа приложения завершена')

