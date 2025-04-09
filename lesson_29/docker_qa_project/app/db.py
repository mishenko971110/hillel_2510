import os
import psycopg2

DB_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DB_URL)

def init_db():
    """Створює таблицю users, якщо її немає"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INT NOT NULL
                )
            """)
            conn.commit()

def insert_user(name, age):
    """Додає користувача"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id", (name, age))
            conn.commit()
            return cur.fetchone()[0]

def get_users():
    """Отримує всіх користувачів"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            return cur.fetchall()

def update_user(user_id, name, age):
    """Оновлює дані користувача"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
            conn.commit()

def delete_user(user_id):
    """Видаляє користувача"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
