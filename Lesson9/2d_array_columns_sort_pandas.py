# Start off by importing the pandas module
import pandas
import sys
from random import randrange

while True:
    column_count = input("Введите размер массива для генерации (column_count должен быть больше 5): ")
    if str(column_count) == 'q':
        sys.exit()
    elif not str(column_count).isdigit() or int(column_count) <= 5:
        print('Введенное значение не удовлетворяет требованию. Значение должно быть целым числом больше 5.\n \
        Попробуйте еще раз или нажмите q для выхода.')
        continue
    else:
        break

print(f'Исходный массив будет иметь размер М*М - {column_count}*{column_count}')

column_count = int(column_count)

# Создаем исходный массив М*М
gen_arr = [[randrange(1, 50) for i in range(column_count)] for _ in range(column_count)]

for i in range(len(gen_arr)):
    if i % 2 == 0:
        gen_arr[i] = sorted(gen_arr[i], reverse=True)
    else:
        gen_arr[i] = sorted(gen_arr[i], reverse=False)

#print(gen_arr)
#print('\n\n')

# Clean data, create dataframe and calculate columns sum
arr_df = pandas.DataFrame(gen_arr)
totals_list = arr_df.sum(axis=1).tolist()

#print(totals_list)
#print('\n\n')

arr_df['Total'] = totals_list
arr_df = arr_df.transpose()

print(arr_df.to_string(index=False, header=False))

