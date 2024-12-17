# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". 
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент", 
# який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть його середній бал.


class Student:
    def __init__(self, name, surname, age, avg_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_mark = avg_mark

    def change_avg_mark(self, new_mark):
        self.avg_mark = new_mark

    def print_student_info(self):
        print(f"{self.name} {self.surname} має середній бал {self.avg_mark}.")
        print(f"Студенту {self.age} років.")


student1 = Student("Олівер", "Томсон", 18, 88)
student1.change_avg_mark(99)

student1.print_student_info()
