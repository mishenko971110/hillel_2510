'''
My little SQLAlchemy
Створення моделі даних: Створіть просту модель даних для системи управління студентами. 
Модель може містити таблиці для студентів, курсів та їх відношень. Кожен студент може бути 
зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та 
додає його до певного курсу. Переконайтеся, що ці зміни коректно відображаються у базі даних.
Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, 
зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, 
а також видалення студентів з бази даних. Можна використовувати будь яку ORM на Ваш вибір.
'''
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.dialects.sqlite import dialect
import random
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()


student_course_association = Table(
    "student_course", Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship("Course", secondary=student_course_association, back_populates="students")


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship("Student", secondary=student_course_association, back_populates="courses")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def filling_database():
    course_names = ["Math", "Physics", "Biology", "History", "Computer Science"]
    courses = [Course(name=name) for name in course_names]

    session.add_all(courses)
    session.commit()

    student_names = [f"Student {i}" for i in range(1, 21)]
    students = [Student(name=name) for name in student_names]

    for student in students:
        student.courses = random.sample(courses, random.randint(1, 3))
        session.add(student)

    session.commit()


def add_student(name, course_ids):
    new_student = Student(name=name)
    new_student.courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    session.add(new_student)
    session.commit()
    print(f"Added student {name} with courses {course_ids}")


def get_students_in_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        return [student.name for student in course.students]
    return []


def get_courses_of_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        return [course.name for course in student.courses]
    return []


def update_student_name(student_id, new_name):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"Updated student {student_id} name to {new_name}")


def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Deleted student {student_id}")


if __name__ == "__main__":
    session.query(Student).delete()
    session.query(Course).delete()
    session.commit()

    filling_database()
    
    add_student("Olivia Wild", [1, 2])
    print("Students in Math:", get_students_in_course("Math"))
    print("Courses of Student 1:", get_courses_of_student("Student 1"))

    update_student_name(1, "Updated Student 1")
    delete_student(2)
