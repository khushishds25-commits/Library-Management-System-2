# Library Management System
# Combined Assessment-I and Assessment-II

books = []
members = []


# ---------------- ADD BOOK ----------------
def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": book_name,
        "author": author
    }

    books.append(book)
    print("Book added successfully!")


# ---------------- DISPLAY BOOKS ----------------
def display_books():
    print("\n===== LIBRARY BOOKS =====")

    if len(books) == 0:
        print("No books available.")

    else:
        for book in books:
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("------------------------")


# ---------------- SEARCH BOOK ----------------
def search_book():
    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found!")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            return

    print("Book not found.")


# ---------------- UPDATE BOOK ----------------
def update_book():
    book_id = input("Enter Book ID to update: ")

    for book in books:
        if book["id"] == book_id:

            book["name"] = input("Enter New Book Name: ")
            book["author"] = input("Enter New Author Name: ")

            print("Book updated successfully!")
            return

    print("Book not found.")


# ---------------- REMOVE BOOK ----------------
def remove_book():
    book_id = input("Enter Book ID to remove: ")

    for book in books:
        if book["id"] == book_id:

            books.remove(book)
            print("Book removed successfully!")
            return

    print("Book not found.")


# ---------------- REGISTER MEMBER ----------------
def register_member():
    member_id = input("Enter Member ID: ")
    member_name = input("Enter Member Name: ")

    member = {
        "id": member_id,
        "name": member_name
    }

    members.append(member)

    print("Member registered successfully!")


# ---------------- DISPLAY MEMBERS ----------------
def display_members():
    print("\n===== LIBRARY MEMBERS =====")

    if len(members) == 0:
        print("No members registered.")

    else:
        for member in members:
            print("Member ID:", member["id"])
            print("Member Name:", member["name"])
            print("------------------------")


# ---------------- MAIN MENU ----------------
while True:

    print("\n================================")
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Remove Book")
    print("6. Register Member")
    print("7. Display Members")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        remove_book()

    elif choice == "6":
        register_member()

    elif choice == "7":
        display_members()

    elif choice == "8":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")