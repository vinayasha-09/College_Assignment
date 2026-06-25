# Write a program to Create contact management system.

contacts = {}  # Dictionary to store contacts
                                          
def add_contact():
    phone = input("Enter Phone Number: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    contacts[phone] = {"Name": name, "Email": email}
    print("Contact added successfully!\n")

def display_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n--- All Contacts ---")
        for phone, info in contacts.items():
            print(f"Phone: {phone}, Name: {info['Name']}, Email: {info['Email']}")
        print()

def search_contact():
    phone = input("Enter Phone Number to search: ")
    if phone in contacts:
        print(f"Contact found: Phone: {phone}, Name: {contacts[phone]['Name']}, Email: {contacts[phone]['Email']}\n")
    else:
        print("Contact not found.\n")

def update_contact():
    phone = input("Enter Phone Number to update: ")
    if phone in contacts:
        name = input("Enter new Name: ")
        email = input("Enter new Email: ")
        contacts[phone] = {"Name": name, "Email": email}
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    phone = input("Enter Phone Number to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("=== Contact Management System ===")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
