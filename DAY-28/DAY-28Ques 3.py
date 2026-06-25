# Write a program to Create ticket booking system.

tickets = {}  # Dictionary to store ticket records

def book_ticket():
    ticket_id = input("Enter Ticket ID: ")
    name = input("Enter Passenger Name: ")
    destination = input("Enter Destination: ")
    tickets[ticket_id] = {"Name": name, "Destination": destination}
    print("Ticket booked successfully!\n")

def display_tickets():
    if not tickets:
        print("No tickets found.\n")
    else:
        print("\n--- All Tickets ---")
        for ticket_id, info in tickets.items():
            print(f"Ticket ID: {ticket_id}, Name: {info['Name']}, Destination: {info['Destination']}")
        print()

def search_ticket():
    ticket_id = input("Enter Ticket ID to search: ")
    if ticket_id in tickets:
        print(f"Ticket found: ID: {ticket_id}, Name: {tickets[ticket_id]['Name']}, Destination: {tickets[ticket_id]['Destination']}\n")
    else:
        print("Ticket not found.\n")

def cancel_ticket():
    ticket_id = input("Enter Ticket ID to cancel: ")
    if ticket_id in tickets:
        del tickets[ticket_id]
        print("Ticket cancelled successfully!\n")
    else:
        print("Ticket not found.\n")

def menu():
    while True:
        print("=== Ticket Booking System ===")
        print("1. Book Ticket")
        print("2. Display All Tickets")
        print("3. Search Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            book_ticket()
        elif choice == "2":
            display_tickets()
        elif choice == "3":
            search_ticket()
        elif choice == "4":
            cancel_ticket()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
