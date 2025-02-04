# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        print(f"[LOG] Виклик: {self.func.__name__}({args}, {kwargs}) -> {result}")
        return result

    def __getattr__(self, attr):
        return getattr(self.func, attr)


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції
class ExceptionHandler:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Виникла помилка у {self.func.__name__}: {e}")
            return None

    def __getattr__(self, attr):
        return getattr(self.func, attr)
