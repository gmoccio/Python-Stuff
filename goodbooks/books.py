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

    print("\n1. Add to reading list")
    print("2. Read reviews")
    print("3. Exit")
    uinput = input("Enter number for selection: ")
    if uinput == "1":
        database.append_reading_list(user_id, book)
        print("Book added!")
        return
    elif uinput == "2":
        view_reviews = book['title']
        pull_reviews(view_reviews)
    elif uinput == "3":
        return



def pull_reviews(view_reviews):
    rows = database.read_reviews(view_reviews)
    if not rows:
        print("No reviews for this book yet!")
        return

    for row in rows:
        print(f"{row[0]} gave it {row[1]} stars")
        print(row[2])



def leave_review(user_id):
    rows = database.parse_readlist(user_id)

    if not rows:
        print("No books in reading list!")
        return

    for i, row in enumerate(rows, start=1):
        print(f"{i}. {row[0]}")

    uinput = int(input("Which book would you like to review? (enter number): "))
    book_title = rows[uinput - 1][0]
    stars = input("How many stars would you leave this book (1-5)?: ")
    review = input("Write your review: ")
    database.append_review_list(user_id, book_title, stars, review)
    print("Review Added!")
