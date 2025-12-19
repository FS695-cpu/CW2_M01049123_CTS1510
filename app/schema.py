import sqlite3

def create_user_table(conn):
    curr = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    '''
    curr.execute(sql)
    conn.commit()