entered_num = input('Input number from 3 to 9: ')
passed_number = entered_num.isdigit()  # Проверяем что введенные символы цифры

if passed_number:
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

else:
    # В случае, если введено не число, выводим сообщение об ошибке и завершаем работу
    print('Введено не число! Работа приложения завершена')
