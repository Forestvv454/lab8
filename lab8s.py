# Базовый класс образовательного учреждения
class Institution:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def show_info(self):
        print("Название:", self.name)
        print("Город:", self.city)

    def study(self):
        print("Обучение в образовательном учреждении")


# Первый наследник — школа
class School(Institution):
    def __init__(self, name, city, classes):
        super().__init__(name, city)
        self.classes = classes

    def study(self):
        print("Обучение школьников с", self.classes, "класса")


# Второй наследник — колледж
class College(Institution):
    def __init__(self, name, city, specialty):
        super().__init__(name, city)
        self.specialty = specialty

    def study(self):
        print("Обучение по специальности:", self.specialty)


# Третий наследник — университет
class University(Institution):
    def __init__(self, name, city, faculties):
        super().__init__(name, city)
        self.faculties = faculties

    def study(self):
        print("Количество факультетов:", self.faculties)


# Создаём объекты
school = School("Школа №1", "Москва", 1)
college = College("Технический колледж", "Казань", "Программирование")
university = University("Казанский университет", "Казань", 8)


# Выводим информацию
institutions = [school, college, university]

for institution in institutions:
    institution.show_info()
    institution.study()
    print()