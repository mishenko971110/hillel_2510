'''
Створіть базу даних для інтернет-магазину з наступними таблицями:
products: таблиця для зберігання інформації про продукти, включаючи назву, опис, ціну тощо.
categories: таблиця для категорій продуктів.
products повинна мати зовнішній ключ на таблицю categories.
Напишіть SQL-скрипт для створення зазначених таблиць.
Внесіть декілька рядків даних в кожну таблицю
Виконайте JOIN-запит, який повертає інформацію про продукти та назву їх категорій
'''
CREATE DATABASE internetstore;

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT,
    description VARCHAR(250),
    category INT REFERENCES categories(category_id)
);

CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO products (product_id, name, price, description, category) VALUES (1, 'gold apple', 35.0, 'very tasty', 1);
INSERT INTO products (product_id, name, price, description, category) VALUES (2, 'pineapple', 215.0, 'very tasty', 1);
INSERT INTO products (product_id, name, price, description, category) VALUES (3, 'tomato', 107.0, 'no nitrats', 2);

INSERT INTO categories (category_id, name) VALUES (1, 'fruits');
INSERT INTO categories (category_id, name) VALUES (2, 'vegetables');
