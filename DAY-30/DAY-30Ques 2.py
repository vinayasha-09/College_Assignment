# Write a program to Create mini library system.

book_ids = []
titles = []
authors = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    book_ids.append(book_id)
    titles.append(title)
    authors.append(author)
    print("Book added successfully!\n")

def display_books():
    if not book_ids:
        print("No books found.\n")
    else:
        print("\n--- Library Books ---")
        for i in range(len(book_ids)):
            print(f"ID: {book_ids[i]}, Title: {titles[i]}, Author: {authors[i]}")
        print()

def search_book():
    book_id = input("Enter Book ID to search: ")
    if book_id in book_ids:
        i = book_ids.index(book_id)
        print(f"Book found: ID: {book_ids[i]}, Title: {titles[i]}, Author: {authors[i]}\n")
    else:
        print("Book not found.\n")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    if book_id in book_ids:
        i = book_ids.index(book_id)
        del book_ids[i]
        del titles[i]
        del authors[i]
        print("Book deleted successfully!\n")
    else:
        print("Book not found.\n")

def menu():
    while True:
        print("=== Mini Library System ===")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
