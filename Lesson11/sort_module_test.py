import sortmodule as sm

help(sm)

test_arr = [2, 14, 3, 44, 18, 0, 22, 10, 7, 15, 28]

print('Исходный несортированный массив', test_arr)
print('Массив отсортирован методом пузырька', sm.bubble_sort(test_arr))
print('Массив отсортирован методом камня', sm.bubble_rock_sort(test_arr))
print('Массив отсортирован методом вставки', sm.insertion_sort(test_arr))