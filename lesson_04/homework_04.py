adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')
print('\nTask #1')
print(adwentures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', ' ')
print('\nTask #2')
print(adwentures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_list = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer_list)
print('\nTask #3')
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
#method 1
h_list = adwentures_of_tom_sawer.split('h')
h_count = len(h_list) - 1
print('\nTask #4')
print('Method #1\nКіл-ть h в тексті: ', h_count)

#method 2
h_count = adwentures_of_tom_sawer.count('h')
print('Method #2\nКіл-ть h в тексті: ', h_count)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
#method 1
word_list = adwentures_of_tom_sawer.split()
up_count = 0
for word in word_list:
    if word.istitle():
        up_count += 1
print('\nTask #5')
print('Method #1\nКіл-ть слів з великої літери: ', up_count)

#method 2
import re
rule = r'\b[A-Z][A-Za-z]*\b'
up_count = len(re.split(rule, adwentures_of_tom_sawer)) - 1
print('Method #2\nКіл-ть слів з великої літери: ', up_count)

#method 3
up_count = len(re.findall(rule, adwentures_of_tom_sawer))
print('Method #3\nКіл-ть слів з великої літери: ', up_count)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index = adwentures_of_tom_sawer.find('Tom')
if index != -1:
    index = adwentures_of_tom_sawer[index + 1:].find('Tom')
print('\nTask #6')
print(f'Позиція, на якій слово Tom зустрічається вдруге: {index}')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print('\nTask #7')
print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences_4 = adwentures_of_tom_sawer_sentences[3].lower()
print('\nTask #8')
print(adwentures_of_tom_sawer_sentences_4)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
start_str = 'By the time'
str_for_search = start_str.lower()
is_sentance = False

for sentance in adwentures_of_tom_sawer_sentences:
    print(sentance)
    if sentance.lower().startswith(str_for_search):
        is_sentance = True
        break

print('\nTask #9')
if is_sentance == True:
    print('В тексті є речення, яке починається з ', start_str)
else:
    print('В тексті немає речення, яке починається з ', start_str)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
index = len(adwentures_of_tom_sawer_sentences)
last_sentance = adwentures_of_tom_sawer_sentences[index - 1]
words_list = last_sentance.split()
words_count = len(words_list)
print('\nTask #10')
print(f'В останньому реченні {words_count} слова.')
