import bcrypt
from app.db import get_connection
from app.users import insert_user, get_user
from app.schema import create_user_table
from hashing import hash_password, validate_password

def register_user(conn):
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    hashed = hash_password(password)
    insert_user(conn, name, hashed)
    print("User registered successfully.")

def login_user(conn):
    username = input('Enter your name: ')
    password = input('Enter your password: ')
    user = get_user(conn, username)
    if user and validate_password(password, user[2]):  # user[2] = password_hash
        return True
    return False

def main():
    conn = get_connection()
    create_user_table(conn)

    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            register_user(conn)
        elif choice == '2':
            if login_user(conn):
                print("Login successful.")
            else:
                print("Login failed.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()