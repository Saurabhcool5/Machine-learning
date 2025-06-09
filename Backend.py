#How backend works in python
# Backend is the part of the application that handles data processing, business logic, and database interactions.
import sqlite3

def connect_to_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
def insert_user(conn, name, email):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email) VALUES (?, ?)
    ''', (name, email))
    conn.commit()
def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users
    ''')
    return cursor.fetchall()
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE id = ?
    ''', (user_id,))
    return cursor.fetchone()
def update_user(conn, user_id, name, email):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users SET name = ?, email = ? WHERE id = ?
    ''', (name, email, user_id))
    conn.commit()
def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM users WHERE id = ?
    ''', (user_id,))
    conn.commit()
def close_connection(conn):
    conn.close()
# Example usage
if __name__ == "__main__":
    db_name = 'example.db'
    conn = connect_to_database(db_name)
    
    create_table(conn)

    insert_user(conn, 'Alice', 'alice@example.com')
    insert_user(conn, 'Bob', 'bob@example.com')

    users = get_all_users(conn)
    print("All users:")
    for user in users:
        print(user)

    user = get_user_by_id(conn, 1)
    print("User with ID 1:")
    print(user)

    update_user(conn, 1, 'Alice Smith', 'alice.smith@example.com')

    delete_user(conn, 2)

    close_connection(conn)
# This code demonstrates how to create a simple backend using SQLite in Python.
# It includes functions to connect to a database, create a table, insert, retrieve, update, and delete users.
# This is a basic example of how a backend can be implemented in Python using SQLite.
