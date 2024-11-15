# Порахувати кількість унікальних символів в строці. 
# Якщо їх більше 10 - вивести в консоль True, інакше - False. 
# Строку отримати за допомогою функції input()

str = input('Input a string for check: ')
count_uniq = len(set(str.lower()))

if count_uniq > 10:
    print(True)
else:
    print(False)
