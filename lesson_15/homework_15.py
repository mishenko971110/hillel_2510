# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).

# Необхідно реалізувати наступні вимоги:
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.


class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value < 0:
                raise ValueError("Сторона ромба повинна бути більшою за 0")
        elif name == 'angle_a':
            if value <= 0 or  value >= 180:
                raise ValueError("Кут повинен бути в межах від 0 до 180")
        super().__setattr__(name, value)
            
    def display_info(self):
        print(f"Довжина сторони a: {self.side_a}")
        print(f"Кут a (між сторонами): {self.angle_a}°")
        print(f"Кут b (суміжний): {self.angle_b}°")


try:
    rhombus1 = Rhombus(5, 60)
    rhombus2 = Rhombus(100, 120)
    #rhombus3 = Rhombus(12, 180)
    #rhombus4 = Rhombus(-12, 120)

    rhombus1.display_info()
    rhombus2.display_info()
    #rhombus3.display_info()
    #rhombus4.display_info()

except ValueError as e:
    print(e)
