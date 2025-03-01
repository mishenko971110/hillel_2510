# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_number_generator(N):
    for num in range(0, N + 1, 2):
        yield num

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b
