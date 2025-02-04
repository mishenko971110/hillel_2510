# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseNumListIterator:
    def __init__(self, num_list):
        self.num_list = num_list
        self.index = len(num_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.num_list[self.index]


# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbersIterator:
    def __init__(self, N):
        self.N = N
        self.current = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.N:
            raise StopIteration
        return self.current
