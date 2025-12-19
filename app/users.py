import sqlite3

# C - Create
def insert_user(conn, name, hashed_password):
    curr = conn.cursor()
    sql = "INSERT INTO users (user_name, password_hash) VALUES (?, ?)"
    params = (name, hashed_password)
    curr.execute(sql, params)
    conn.commit()

# R - Read
def get_all_users(conn):
    curr = conn.cursor()
    sql = "SELECT * FROM users"
    curr.execute(sql)
    users = curr.fetchall()
    return users

def get_user(conn, name_):
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE user_name = ?"
    param = (name_,)
    curr.execute(sql, param)
    user = curr.fetchone()
    return user

# U - Update
def update_password(conn, username, new_password):
    curr = conn.cursor()
    sql = "UPDATE users SET password_hash = ? WHERE user_name = ?"
    params = (new_password, username)
    curr.execute(sql, params)
    conn.commit()

# D - Delete
def delete_user(conn, user_name):
    curr = conn.cursor()
    sql = "DELETE FROM users WHERE user_name = ?"
    params = (user_name,)
    curr.execute(sql, params)
    conn.commit()