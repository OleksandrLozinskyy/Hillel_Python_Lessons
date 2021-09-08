"""
Класс имплементирующий счетчик. Отсчет начинается от минимального значения
указанного пользователем и завершается на верхней границе заданной пользователем
Шаг счетчика составляет 1 (Можно наследовать данный класс и создать счетчик с
шагом задаваемым пользователем)
"""


class DigitalCounter:

    current = 0

    def __init__(self, min_value, max_value):
        """
        Инициализирует счетчик. При инициализации устанавливаются нижняя и
        верхняя границы.
        :param min_value: нижняя граница счетчика
        :param max_value: верхняя граница счетчика
        """
        self.current = min_value
        self.maximum = max_value

    def increase(self):
        if self.current < self.maximum:
            self.current += 1
            return self.current
        else:
            # вывод значения счетчика после достижения максимального значения
            # согласно условия задания
            # здесь можно вывести текст о достижении верхней границы либо
            # сбросить счетчик на минимальное значение
            return self.current


# Инициализация класса, вывод стартового значения счетчика, вызов функции
# инкремента с проверкой достижения верхней границы
counter = DigitalCounter(2, 7)
print(counter.current)
print(counter.increase())
print(counter.increase())
print(counter.increase())
print(counter.increase())
print(counter.increase())
# Верхняя граница достигнута на предыдущем шаге. Следующий шаг выводит
# максимальное значение без изменения
print(counter.increase())
