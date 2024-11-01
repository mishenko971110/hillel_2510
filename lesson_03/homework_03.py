alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = ''' \
    "Would you tell me, please, which way I ought to go from here?"\n \
    "That depends a good deal on where you want to get to," said the Cat.\n \
    "I don't much care where ——" said Alice.\n \
    "Then it doesn't matter which way you go," said the Cat.\n \
    "—— so long as I get somewhere," Alice added as an explanation.\n \
    "Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
alice_in_wonderland = ' \
    "Would you tell me, please, which way I ought to go from here?"\n \
    "That depends a good deal on where you want to get to," said the Cat.\n \
    "I don\'t much care where ——" said Alice.\n \
    "Then it doesn\'t matter which way you go," said the Cat.\n \
    "—— so long as I get somewhere," Alice added as an explanation.\n \
    "Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'

# task 03 == Виведіть змінну alice_in_wonderland на друк
print('Задачі №1-3')
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_sea_area = black_sea_area + azov_sea_area

print('\nЗадача №4')
print(f'Площа Чорного моря становить {black_sea_area} км2, а площа Азовського моря \
становить {azov_sea_area} км2. \nЧорне та Азовське моря разом займають \
{black_sea_area} + {azov_sea_area} = {total_sea_area} км2.')


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому - 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods_in_all_stores = 375291
total_goods_in_1_2_stores = 250449
total_goods_in_2_3_stores = 222950
total_goods_in_1_store = total_goods_in_all_stores - total_goods_in_2_3_stores
total_goods_in_2_store = total_goods_in_1_2_stores - total_goods_in_1_store
total_goods_in_3_store = total_goods_in_2_3_stores - total_goods_in_2_store

print('\nЗадача №5')
print(f'Мережа супермаркетів має 3 склади, де всього розміщено {total_goods_in_all_stores} товар.\n\
На першому та другому складах перебуває {total_goods_in_1_2_stores} товарів.\n\
На другому та третьому - {total_goods_in_2_3_stores} товарів.')
print(f'На 1 складі розміщено {total_goods_in_all_stores} - {total_goods_in_2_3_stores} = {total_goods_in_1_store} товарів.')
print(f'На 2 складі розміщено {total_goods_in_1_2_stores} - {total_goods_in_1_store} = {total_goods_in_2_store} товарів.')
print(f'На 3 складі розміщено {total_goods_in_2_3_stores} - {total_goods_in_2_store} = {total_goods_in_3_store} товарів.')


# task 06
"""
Михайло разом з батьками вирішили купити комп'ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп'ютера.
"""
count_months = 18
sum_per_month = 1179
computer_cost = count_months * sum_per_month

print('\nЗадача №6')
print(f'Михайло разом з батьками вирішили купити комп\'ютер, скориставшись послугою «Оплата частинами».\n\
Відомо, що сплачувати необхідно буде {count_months} місяців по {sum_per_month} грн/місяць.')
print(f'Вартість комп\'ютера складає {count_months} * {sum_per_month} = {computer_cost} грн.')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print('\nЗадача №7: \nЗнайди остачу від діленя чисел:')
print(f'a) остача від ділення числа 8019 на 8  = {8019 % 8}')
print(f'b) остача від ділення числа 9907 на 9  = {9907 % 9}')
print(f'c) остача від ділення числа 2789 на 5  = {2789 % 5}')
print(f'd) остача від ділення числа 7248 на 6  = {7248 % 6}')
print(f'e) остача від ділення числа 7128 на 5  = {7128 % 5}')
print(f'f) остача від ділення числа 19224 на 9 = {19224 % 9}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
count_pizza_l = 4
count_pizza_m = 2
count_juice = 4
count_cake = 1
count_water = 3

price_pizza_l = 274
price_pizza_m = 218
price_juice = 35
price_cake = 350
price_water = 21

sum_pizza_l = count_pizza_l * price_pizza_l
sum_pizza_m = count_pizza_m * price_pizza_m
sum_juice = count_juice * price_juice
sum_cake = count_cake * price_cake
sum_water = count_water * price_water

total_sum = sum_pizza_l + sum_pizza_m + sum_juice + sum_cake + sum_water

print('\nЗадача №8')
print('Іринка, готуючись до свого дня народження, склала список того, що їй потрібно замовити.')
print(f'Вона хоче придбати {count_pizza_l} великих піци за {price_pizza_l} грн. і витратити \
{count_pizza_l} * {price_pizza_l} = {sum_pizza_l} грн.')
print(f'Вона хоче придбати {count_pizza_m} середні піци за {price_pizza_m} грн. і витратити \
{count_pizza_m} * {price_pizza_m}= {sum_pizza_m} грн.')
print(f'Вона хоче придбати {count_juice} пачки соку за {price_juice} грн. і витратити \
{count_juice} * {price_juice} = {sum_juice} грн.')
print(f'Вона хоче придбати {count_cake} торт за {price_cake} грн. і витратити \
{count_cake} * {price_cake} = {sum_cake} грн.')
print(f'Вона хоче придбати {count_water} пляшок води за {price_water} грн. і витратити \
{count_water} * {price_water} = {sum_water} грн.')
print(f'Всього для її замовлення знадобиться \
{sum_pizza_l} + {sum_pizza_m} + {sum_juice} + {sum_cake} + {sum_water} = {total_sum} грн.')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
count_photos_per_page = 8
count_pages = total_photos / count_photos_per_page

print('\nЗадача №9')
print(f'Ігор займається фотографією. Він вирішив зібрати всі свої {total_photos} фотографії та вклеїти в альбом.')
print(f'На одній сторінці може бути розміщено щонайбільше {count_photos_per_page} фото.')
print(f'Ігорю знадобиться {total_photos} / {count_photos_per_page} = {count_pages} сторінок, щоб вклеїти всі фото.')


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
length = 1600
per_length = 100
gasoline = 9
tank_capacity = 48
total_gasoline = length / per_length * gasoline
times_to_visit_gas_station = total_gasoline // tank_capacity

print('\nЗадача №10')
print(f'Родина зібралася в автомобільну подорож із Харкова в Будапешт.')
print(f'Відстань між цими містами становить {length} км.')
print(f'Відомо, що на кожні {per_length} км необхідно {gasoline} літрів бензину.')
print(f'Місткість баку становить {tank_capacity} літрів.')
print(f'Для такої подорожі знадобиться {length} : {per_length} * {gasoline} = {total_gasoline} літрів бензину')
print(f'Родині необхідно заїхати на заправку під час цієї подорожі щонайменше \
{total_gasoline} : {tank_capacity} = {times_to_visit_gas_station} разів, кожного разу заправляючи повний бак')
