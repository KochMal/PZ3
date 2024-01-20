class GroupJournal:
    def __init__(self, class_leader, subjects, students):
        self.class_leader = self.validate_class_leader(class_leader)
        self.subjects = self.validate_subjects(subjects)
        self.students = self.validate_students(students)

    def validate_class_leader(self, class_leader):
        if len(class_leader) > 100:
            raise ValueError("Имя классного руководителя не может превышать 100 символов")
        return class_leader

    def validate_subjects(self, subjects):
        if len(set(subjects)) != len(subjects):
            raise ValueError("Повторяющиеся предметы не допускаются")
        return subjects

    def validate_students(self, students):
        if len(set(students)) != len(students):
            raise ValueError("Повторяющиеся студенты не допускаются")
        return students

    def sort_subjects(self):
        self.subjects = sorted(self.subjects)

    def sort_students(self):
        self.students = sorted(self.students)

    def get_class_leader(self):
        return self.class_leader

    def set_class_leader(self, class_leader):
        self.class_leader = self.validate_class_leader(class_leader)

    def get_subjects(self):
        return self.subjects

    def set_subjects(self, subjects):
        self.subjects = self.validate_subjects(subjects)

    def get_students(self):
        return self.students

    def set_students(self, students):
        self.students = self.validate_students(students)

# Ввод данных для создания объектов класса GroupJournal
class_leader = input("Введите имя и фамилию классного руководителя: ")
subjects = input("Введите предметы через запятую: ").split(",")
students = input("Введите имена студентов через запятую: ").split(",")

# Создаем объекты класса GroupJournal с учетом ограничений предметной области
journal1 = GroupJournal(class_leader, subjects, students)

# Вывод свойств объектов
print("Журнал 1:")
print("Классный руководитель:", journal1.get_class_leader())
print("Предметы:", journal1.get_subjects())
print("Студенты:", journal1.get_students())