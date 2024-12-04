"""    
   Біометрична авторизація. Функція виконує авторизацію на підставі отриманого списка словників даних та словника, отриманого з іншої функції від користувача.
      Параметри користувача: id - int, name - str, second_name - str, age - int
      Якщо дані від користувача співпадають з єталонними даними - користувач отримує повний доступ. Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
      Функція повертає рівень доступу: full, read-only, forbidden

  # варіант вхідних значень
  database_users = [
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
    {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
  ]
  # варіанти user_input :
  {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
  {"id": 1, "name": "John", "second_name": "Joi", "age": 30}
  {"id": 1, "name": "John", "second_name": "Joi", "age": 25}
"""

database_users = [
  {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
  {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
]


def check_count_true(user_data, database_data):
  count_true = 0
  if user_data['name'] == database_data['name']:
    count_true += 1
  if user_data['second_name'] == database_data['second_name']:
    count_true += 1
  if user_data['age'] == database_data['age']:
    count_true += 1
  return count_true


def get_level_access(input_data):
  for db_user in database_users:
    if input_data['id'] == db_user['id']:
      count_true = check_count_true(input_data, db_user)
      if count_true == 3:
        return 'full'
      elif count_true == 2:
        return 'read-only'
      else:
        return 'forbidden'
