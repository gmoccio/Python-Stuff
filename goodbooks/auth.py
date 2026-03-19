import database
import bcrypt
import getpass

def login():
    while True:
        uinput = input("Login or Register?: ")
        if uinput == "register":
            username = input("Create username: ")
            password = getpass.getpass("Create password: " )
            hashedpw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            bio = input("Write a bio to describe yourself: ")
            pref_genres = input("What are your preferred genres?: ")
            database.insert_user(username, hashedpw, bio, pref_genres)
            print("Profile Created!")
        elif uinput == "login":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter password: ")
            user_id = database.login_user(username, password)

            if user_id:
                print(f"Welcome {username}!")
                return user_id
            else:
                print("Incorrect username or password!")