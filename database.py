import sqlite3

def connect():
    conn = sqlite3.connect("inventory.db")
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, category, quantity, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, category, quantity, price)
        VALUES (?, ?, ?, ?)
    ''', (name, category, quantity, price))
    conn.commit()
    conn.close()

def get_all_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def delete_product(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_product(id, name, category, quantity, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products
        SET name=?, category=?, quantity=?, price=?
        WHERE id=?
    ''', (name, category, quantity, price, id))
    conn.commit()
    conn.close()

def search_product(keyword):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products
        WHERE name LIKE ? OR category LIKE ?
    ''', (f"%{keyword}%", f"%{keyword}%"))
    products = cursor.fetchall()
    conn.close()
    return products

def low_stock_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE quantity < 10")
    products = cursor.fetchall()
    conn.close()
    return products

create_table()