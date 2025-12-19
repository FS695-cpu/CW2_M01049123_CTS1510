import sqlite3 
import streamlit as st

def get_connection():
    return sqlite3.connect("your_database.db", check_same_thread=False)

conn = get_connection()




