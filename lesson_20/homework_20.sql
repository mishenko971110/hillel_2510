'''
Створіть базу даних для інтернет-магазину з наступними таблицями:
products: таблиця для зберігання інформації про продукти, включаючи назву, опис, ціну тощо.
categories: таблиця для категорій продуктів.
products повинна мати зовнішній ключ на таблицю categories.
Напишіть SQL-скрипт для створення зазначених таблиць.
Внесіть декілька рядків даних в кожну таблицю
Виконайте JOIN-запит, який повертає інформацію про продукти та назву їх категорій
'''

CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO categories (name) VALUES 
    ('fruits'),
    ('vegetables'),
    ('berries'),
    ('other');

INSERT INTO products (name, price, description, category_id) VALUES 
    ('gold apple', 35.0, 'very tasty', 1),
    ('pineapple', 215.0, 'very tasty', 1),
    ('tomato', 107.0, 'no nitrats', 2),
    ('orange', 25.0, 'very tasty', 1),
    ('strawberry', 13.0, 'no nitrats', 3);

SELECT products.name AS product_name, 
       products.price, 
       products.description, 
       categories.name AS category_name
FROM products
INNER JOIN categories ON products.category_id = categories.category_id;
