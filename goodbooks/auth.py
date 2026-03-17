import database
import bcrypt

def login():
    while True:
        uinput = input("Login or Register?: ")
        if uinput == "register":
            username = input("Create username: ")
            password = input("Create password: " )
            hashedpw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            database.insert_user(username, hashedpw)
            print("Profile Created!")
        elif uinput == "login":
            username = input("Enter your username: ")
            password = input("Enter password: ")
            user_id = database.login_user(username, password)

            if user_id:
                print(f"Welcome {username}!")
                return user_id
            else:
                print("Incorrect username or password!")