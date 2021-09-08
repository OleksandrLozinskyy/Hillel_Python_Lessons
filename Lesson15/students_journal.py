class Student:
    grades = []

    def __init__(self, firstname, lastname, age, sex):
        """
        Инициализирует экземпляр класса передаваемыми значениями
        :param firstname: Имя
        :param lastname: Фамилия
        :param age: Возраст
        :param sex: Пол
        """
        self.grades = []
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def add_grade(self, grade: int):
        self.grades.append(grade)

    def average(self) -> float:
        """
        Функция для подсчета среднего балла успеваемости студента.
        Работает только в случае, если у студента больше 1 оценки
        :return: Возвращает средний балл студента
        """
        avg_grade = 0
        count = 0
        if len(self.grades) > 1:
            for grade in self.grades:
                avg_grade += grade
                count += 1
            avg_grade = round(avg_grade / count, 2)
        elif len(self.grades) == 1:
            avg_grade = round(float(self.grades[0]), 2)

        return avg_grade

    # Здесь толерантно было бы добавить функцию по смене пола, но ее тут нет )))


class Group:
    journal = []

    def __init__(self, group_name):
        """
        Инициализируем экземпляр класса Group. При инициализации задаем название
        группы и пустой журнал для группы.
        :param group_name: Название группы
        """
        self.group_name = group_name
        self.journal = []

    def add_student(self, student: Student):
        self.journal.append(student)

    def remove_student(self, student: Student):
        self.journal.remove(student)

    def print_journal(self):
        print(f'Журнал группы "{self.group_name}"', end='\n\n')
        if len(self.journal) > 0:
            for stud in self.journal:
                print('{:20s}{:^5d}{:^5s}'.format(' '.join([stud.firstname,
                                                            stud.lastname]),
                                                  stud.age, stud.sex), end='')
                if len(stud.grades) > 0:
                    for grade in stud.grades:
                        print('{:^3d}'.format(grade), end='')
                    print('{:^7.2f}'.format(stud.average()), end='\n')
                else:
                    print('Оценок пока нет', end='\n')
        else:
            print('Журнал Вашей группы пуст.')
        print('\n')


# Создаем студентов
student1 = Student('Martin', 'Luter', 24, 'M')
student2 = Student('Janna', 'Dark', 22, 'F')
student3 = Student('Oleksandr', 'Lozinskyi', 43, 'M')
student4 = Student('Ivan', 'Petrov', 22, 'M')

# Создаем группы
group1 = Group('Python Introduction')
group2 = Group('Python Advanced')

# Добавляем студентов в группы. Вторую группу умышленно оставляем пустую
group1.add_student(student1)
group1.add_student(student2)
group1.add_student(student3)
group1.add_student(student4)

# Так как первая группа у нас уже учится, то добавляем успеваемость студентам
student1.add_grade(10)
student1.add_grade(8)
student1.add_grade(9)

student2.add_grade(7)
student2.add_grade(10)
student2.add_grade(9)

student4.add_grade(10)

# Выводим журналы успеваемости обеих групп
group1.print_journal()
group2.print_journal()
