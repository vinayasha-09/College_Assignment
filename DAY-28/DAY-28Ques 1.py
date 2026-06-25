# Write a program to Create library management system.

library = {}  # Dictionary to store books

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    library[book_id] = {"Title": title, "Author": author}
    print("Book added successfully!\n")

def display_books():
    if not library:
        print("No books found.\n")
    else:
        print("\n--- Library Books ---")
        for book_id, info in library.items():
            print(f"ID: {book_id}, Title: {info['Title']}, Author: {info['Author']}")
        print()

def search_book():
    book_id = input("Enter Book ID to search: ")
    if book_id in library:
        print(f"Book found: ID: {book_id}, Title: {library[book_id]['Title']}, Author: {library[book_id]['Author']}\n")
    else:
        print("Book not found.\n")

def update_book():
    book_id = input("Enter Book ID to update: ")
    if book_id in library:
        title = input("Enter new Title: ")
        author = input("Enter new Author: ")
        library[book_id] = {"Title": title, "Author": author}
        print("Book updated successfully!\n")
    else:
        print("Book not found.\n")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    if book_id in library:
        del library[book_id]
        print("Book deleted successfully!\n")
    else:
        print("Book not found.\n")

def menu():
    while True:
        print("=== Library Management System ===")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
