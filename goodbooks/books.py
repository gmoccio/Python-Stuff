import requests
import database
import main

def search_book(title):
    url = "https://openlibrary.org/search.json"
    params = {
        "q": title,
        "limit": 5
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not data["docs"]:
        return None
    

    book = None
    for doc in data["docs"]:
        if doc.get("number_of_pages_median"):
            book = doc
            break
    if not book:
        book = data["docs"][0]
    
    info = {
        "title":    book.get("title", "N/A"),
        "author":   book.get("author_name", "N/A")[0],
        "pages":    book.get("number_of_pages_median", "N/A"),
        "published":    book.get("first_publish_year", "N/A"),
    }
    return info


def search_menu(user_id):
    title = input("Enter book Title: ")
    book = search_book(title)

    if not book:
        return

    print(f"\n {book['title']}")
    print(f"    Author: {book['author']}")
    print(f"    Pages: {book['pages']}")
    print(f"    Published: {book['published']}")

    uinput = input("Add to reading list? (yes/no): ")
    if uinput == "yes":
        database.append_reading_list(user_id, book)
        print("Book added!")
        main.main_menu(user_id)
