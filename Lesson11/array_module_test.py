from workwithnumsandarrays import sortandprint as sp

# Выводим в консоль описание пакета, доступные методы, автора и тд.

help(sp)

# Пробуем пакет в действии. Создаем 2d массив с заданными параметрами, сортируем его и выводим на печать
arr = sp.create_array(7, 1, 50)
sp.sum_and_sort_array_column(arr)
