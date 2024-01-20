#создаём класс GroupJournal
class GroupJournal:
    def __init__(self, class_leader, subject, students):
        self.class_leader = class_leader
        self.subject = subject
        self.students = students

    def get_class_leader(self):
        return self.class_leader

    def set_class_leader(self, class_leader):
        self.class_leader = class_leader

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    def get_students(self):
        return self.students

    def set_students(self, students):
        self.students = students

# Создаем объекты класса GroupJournal
journal1 = GroupJournal("Иванов", "Математика", ["Алексей", "Мария"])
journal2 = GroupJournal("Петров", "Физика", ["Сергей", "Елена", "Дмитрий"])

# Показываем значения свойств объектов
print("Журнал 1:")
print("Классный руководитель:", journal1.get_class_leader())
print("Предмет:", journal1.get_subject())
print("Студенты:", journal1.get_students())

print("\nЖурнал 2:")
print("Классный руководитель:", journal2.get_class_leader())
print("Предмет:", journal2.get_subject())
print("Студенты:", journal2.get_students())

