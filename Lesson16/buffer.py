from random import randint


class Buffer:
    """
    Класс накопитель-агрегатор.
    Накапливает подаваемые на вход последовательности целых чисел. При
    достижении количества накопленных элементов равного пяти суммирует значения
    чисел последовательности и возвращает сумму. Буфер в котором накапливаются
    значения после суммирования и вывода суммы очищается.
    """

    def __init__(self):
        # конструктор без аргументов
        self.partial_list = []
        self.five_part_sum = 0

    def add(self, *a):
        # добавить следующую часть последовательности
        for ele in a:
            self.partial_list.append(ele)
            if len(self.partial_list) == 5:
                for j in self.partial_list:
                    self.five_part_sum += j
                # Вывод последовательности из 5 элементов перед выводом суммы.
                # Может быть закомментировано, так как не требуется условием
                print(self.get_current_part())
                print(f'Сумма 5 элементов последовательности: '
                      f'{self.five_part_sum}')
                self.partial_list.clear()
            self.five_part_sum = 0

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности
        # в порядке, в котором они были добавлены
        return self.partial_list


if __name__ == "__main__":
    num_of_nums = randint(1, 20)
    num_buffer = Buffer()
    print(f'Количество элементов передаваемых в буфер: {num_of_nums}')
    # Добавление элементов с помощью генератора
    num_buffer.add(*[randint(1, num_of_nums * 3) for i in range(num_of_nums)])
    print(f'Элементы в буфере на текущий момент: '  
          f'{num_buffer.get_current_part()}')
    # Ручное добавление элементов
    num_buffer.add(12, 18, 9)
    print(f'Элементы в буфере на текущий момент: '
          f'{num_buffer.get_current_part()}')