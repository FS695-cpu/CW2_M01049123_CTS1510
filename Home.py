import streamlit as st
from hashing import hash_password, validate_password
from app.db import get_connection
from app.users import insert_user, get_user
conn = get_connection()
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title= 'Home',
    page_icon='',
    layout='wide' 
)

st.title('Welcome to the Main Page ') 

if 'logged_in' not in st.session_state: 
    st.session_state['logged_in'] = False 



tab_login, tab_register = st.tabs(['Login Status', 'Register'])

with tab_login: 
    login_username = st.text_input('Username',key='login_username')
    login_password = st.text_input('Password', type='password', key= 'login_=assword')

    if st.button('Log In'):
        user = get_user(conn, login_username)
        if user and validate_password(login_password, user[2]):  # user[2] = password_hash
            st.session_state['logged_in'] = True
            st.success('Login Sucessful')
            st.switch_page_page('pages/1_Dashboard.py')
        st.session_state['logged_in'] = False
            




with tab_register: 
    register_username = st.text_input('New Username')
    register_password = st.text_input('New Password', type='password')

    if st.button('Register'):
        hashed = hash_password(register_password)

        insert_user(conn, register_username, hashed)
        st.session_state['logged_in'] = False 
        st.success('Registration succesful. Please Log in.')

st.write(st.session_state)

