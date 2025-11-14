import bcrypt

def hash_password(password):  # converts plain text (password) into hashed version
    password_bytes = password.encode('utf-8') # utf-8 converts password yo bytes
    salt = bcrypt.gensalt() #  bcrypt.gensalt() generates a salt 
    hashed = bcrypt.hashpw(password_bytes, salt) # password is hashed using the salt
    return hashed.decode('utf-8')

def validate_password(password, hashed): # checks if pw entered by user matches the one stored in the database
    password_bytes = password.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def register_user(username, password):  # Saves a new user with a hashed password
    hashed = hash_password(password)
    with open('users.txt', 'a') as f:
        f.write(f'{username},{hashed}\n')

def login_user(username, password):   # Reads stored users and checks if credentials match.
    try:
        with open('users.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue
                user, hash = parts
                if user == username:
                    return validate_password(password, hash)
    except FileNotFoundError:
        print("No users registered yet.")
    return False