# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". 
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу 
# "Студент", який дозволяє змінювати середній бал студента. Виведіть інформацію про 
# студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, avg_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_mark = avg_mark

    def change_avg_mark(self, new_avg_mark):
        self.avg_mark = new_avg_mark

    def print_student_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Прізвище: {self.surname}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.avg_mark}")


student1 = Student("Олівер", "Томсон", 18, 88)

print("\nІнформація про студента до зміни балу:")
student1.print_student_info()

student1.change_avg_mark(99)

print("\nІнформація про студента після зміни балу:")
student1.print_student_info()
