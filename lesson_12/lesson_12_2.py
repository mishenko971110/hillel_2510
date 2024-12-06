# Задано словник даних про автомобілі “виробник”: потужність двигуна (в кінських силах – к.с.) 
# і вартість легкових автомобілів. Скласти функцію, яка визначає середню вартість автомобілів, 
# у яких потужність двигуна перевищує 100 к. с.
# {
#     "Mersedes": [120, 120000],
#     "Audi": [100, 165000],
#     "VW": [75, 88000],
#     "Toyta": [90, 88000],
#     "GodLikeLanos": [450, 88000],
#     "Nissan": [110, 50000],
#     "Tesla": [300, 150000],
# }

def avg_price_of_filtered_cars(car_dict):
  car_prices = [car_info[1] for car_info in car_dict.values() if car_info[0] >= 100]
  return round(sum(car_prices) / len(car_prices), 2)