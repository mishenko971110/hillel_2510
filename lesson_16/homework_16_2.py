# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. 
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи 
# для площі та периметру. Властивості по типу 'довжина сторони' й т.д. повинні бути приватними, 
# та ініціалізуватись через конструктор. Створіть Декілька різних об'єктів фігур, та у циклі 
# порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass
    
    @abstractmethod
    def get_area(self):
        pass
    

class Square(Figure):
    def __init__(self, len_a):
        self.__len_a = len_a
    
    @property
    def figure_input_data(self):
        return self.__len_a
    
    def get_perimeter(self):
        return 4 * self.__len_a
    
    def get_area(self):
        return self.__len_a ** 2


class Triangle(Figure):
    def __init__(self, len_a, len_b, len_c):
        self.__len_a = len_a
        self.__len_b = len_b
        self.__len_c = len_c

    @property
    def figure_input_data(self):
        return self.__len_a, self.__len_b, self.__len_c
    
    def get_perimeter(self):
        return self.__len_a + self.__len_b + self.__len_c
    
    def get_area(self):
        p = self.get_perimeter() / 2
        s = (p * (p - self.__len_a) * (p - self.__len_b) * (p - self.__len_c)) ** (1 / 2)
        return s


class Trapeze(Figure):
    def __init__(self, len_a, len_b, len_c, len_d, len_h):
        self.__len_a = len_a
        self.__len_b = len_b
        self.__len_c = len_c
        self.__len_d = len_d
        self.__len_h = len_h

    @property
    def figure_input_data(self):
        return self.__len_a, self.__len_b, self.__len_c, self.__len_d, self.__len_h

    def get_perimeter(self):
        return self.__len_a + self.__len_b + self.__len_c + self.__len_d
    
    def get_area(self):
        return 0.5 * (self.__len_a + self.__len_b) * self.__len_h
        

figures = [
    Square(10),
    Triangle(3, 4, 5),
    Trapeze(5, 7, 8, 4, 3)
]

for figure in figures:
    print(f"\n{figure.__class__.__name__}:")
    print(f"Периметр: {figure.get_perimeter()}см")
    print(f"Площа: {figure.get_area()}см²")
