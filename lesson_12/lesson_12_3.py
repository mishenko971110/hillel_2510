"""Задача про оцінки студентів: Дані про студентів містять ім'я студента і список оцінок за семестр. 
Написати функцію, яка повертає список студентів у яких середній бал вище вказаний бал при запуску функції
students = [
    {"name": "John", "grades": [85, 90, 92]},
    {"name": "Jane", "grades": [78, 80, 85]},
    {"name": "Doe", "grades": [100, 100, 100]},
    {"name": "Smith", "grades": [65, 75, 70]}
]"""

def avg_mark(mark_list):
  return sum(mark_list) / len(mark_list)

def get_success_student(students, mark):
  students_list = []
  for student_info in students:
    if (avg_mark(student_info['grades']) > mark):
      students_list.append(student_info['name'])
  return students_list
