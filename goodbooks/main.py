import database
import auth
import books

def main():
    database.create_tables()
    user_id = auth.login()
    main_menu(user_id)


def main_menu(user_id):
    while True:
        print("\nWhat would you like to do?: ")
        print("1. Search books")
        print("2. View reading list")
        print("3. Review read books")
        print("4. quit")
        uinput = input("Enter choice: ")
        if uinput == "1":
            books.search_menu(user_id)
        elif uinput == "2":
            database.view_readlist(user_id)
        elif uinput == "3":
            books.leave_review(user_id)
        elif uinput == "4":
            break

if __name__ == "__main__":
    main()