import sqlite3
import bcrypt


def get_connection():
    database = sqlite3.connect("goodbooks.db")
    cursor = database.cursor()
    return database, cursor

def create_tables():
    database, cursor = get_connection()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
            )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reading_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_title TEXT,
            book_author TEXT,
            book_length INT,
            publish_date INT,
            FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_title TEXT,
            stars INTEGER,
            review_text TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)

    database.commit()

def insert_user(username, hashedpw):
    database, cursor = get_connection()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashedpw))
    database.commit()

def login_user(username, password):
    database, cursor = get_connection()
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username, ))
    row = cursor.fetchone()
    if row and bcrypt.checkpw(password.encode(), row[1]):
        return row[0]
    return None
    

def append_reading_list(user_id, book):
    database, cursor = get_connection()
    cursor.execute("INSERT INTO reading_list (user_id, book_title, book_author, book_length, publish_date) VALUES (?, ?, ?, ?, ?)", (user_id, book['title'], book['author'], book['pages'], book['published']))
    database.commit()

def view_readlist(user_id):
    database, cursor = get_connection()
    cursor.execute("SELECT book_title, book_author, book_length, publish_date FROM reading_list WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    for i, row in enumerate(rows, start=1):
        print(f"{i}.  {row[0]}")
        print(f"    Author:     {row[1]}")
        print(f"    Pages:      {row[2]}")
        print(f"    Published:  {row[3]}")

def parse_readlist(user_id):
    database, cursor = get_connection()
    cursor.execute("SELECT book_title, book_author, book_length, publish_date FROM reading_list WHERE user_id = ?", (user_id,))
    return cursor.fetchall()

def append_review_list(user_id, book_title, stars, review):
    database, cursor = get_connection()
    cursor.execute("INSERT INTO reviews (user_id, book_title, stars, review_text) VALUES (?, ?, ?, ?)", (user_id, book_title, stars, review))
    database.commit()