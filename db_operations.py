
# print("Hello World")


import sqlite3 
import pandas as pd 

def create_user_table(conn): 
    curr = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL) """
    curr.execute(sql)
    conn.commit()


def insert_user(conn,name,hash_password):
    curr = conn.cursor()
    sql = "INSERT INTO users (username,password_hash) VALUES(?,?)"
    parram = (name,hash_password)
    curr.execute(sql,parram)
    conn.commit()

def migrate_users():
    with open ('DATA/users.txt', 'r') as f: 
        users = f.readlines()

    for user in users: 
        name , hash = user.strip().split(',') 
        insert_user(conn,name,hash)  
    conn.close()  


def get_all_users(conn): 
    curr = conn.cursor() 
    sql = "SELECT * from users"
    curr.execute(sql) 
    users = curr.fetchall()
    conn.close()
    return (users)

def get_user(conn,name_):
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param = (name_,)
    curr.execute(sql,param)
    user = curr.fetchone()
    conn.close()
    return(user)


def migrate_datasets_matadata():
    data = pd.read_csv('DATA/datasets_metadata.csv')
    print(data.head(5))
    data.to_sql('datasets_metadata', conn, if_exists= 'append', index = False)
    conn.close()

def get_all_users_pandas():
    sql = 'SELEC * from datasets_metadata'
    data = pd.read_sql(conn)
    print(data) 

#General structure 

#INSERT,UPDATE,DELETE operations 
conn = sqlite3.connect('DATA/intelligence_platform.db')
curr = conn.cursor()
sql=""
parr =""
curr.execute(sql,parr)
conn.commit()
conn.close()


#GET DATA FROM TABLE 
conn = sqlite3.connect('DATA/intelligence_platform.db')
curr = conn.cursor()
sql=""
parr =""
curr.execute(sql,parr)
curr.fetchall()
curr.fetchone()
conn.close()