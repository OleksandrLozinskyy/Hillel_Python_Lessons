import string
import random

filename = ''.join(random.choice(string.ascii_uppercase + string.digits
                   + string.ascii_lowercase) for _ in range(8)) + '.txt'

with open(filename, 'w', encoding='utf-8') as out_file:
    while True:
        user_input = input('Введите текст для записи в файл, для завершения '
                           'введите пустую строку: ')
        if user_input != '':
            line = user_input + '\n'
            out_file.write(line)
        else:
            out_file.close()
            break
