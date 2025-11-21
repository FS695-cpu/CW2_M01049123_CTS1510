from log_hash import register_user,login_user

def main():
    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            username = input("create a username: ")
            password = input("create a password: ")
            register_user(username, password)
            print("User registered successfully.")
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login_user(username, password):
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


