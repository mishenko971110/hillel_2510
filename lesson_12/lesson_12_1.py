"""
1) Розробіть функцію is_palindrome, яка приймає рядок і повертає True, якщо 
рядок є паліндромом (читається однаково зліва направо і справа наліво) та False 
в іншому випадку. Напишіть тести для перевірки роботу функції на різних вхідних текстах.
"""

def is_palindrome(entered_text):
  text_list = list(entered_text.lower())
  return text_list == text_list[::-1]
