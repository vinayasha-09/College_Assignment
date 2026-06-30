# Write a program to Create inventory management system.

def inventory_system():
    inventory = {}

    while True:
        print("\n--- Menu Driven Inventory Management ---")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. Search Item")
        print("5. Display Inventory")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            name = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory[name] = {"quantity": qty, "price": price}
            print(f"{name} added successfully.")

        elif choice == 2:
            name = input("Enter item name to update: ")
            if name in inventory:
                qty = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))
                inventory[name] = {"quantity": qty, "price": price}
                print(f"{name} updated successfully.")
            else:
                print("Item not found.")

        elif choice == 3:
            name = input("Enter item name to delete: ")
            if name in inventory:
                del inventory[name]
                print(f"{name} deleted successfully.")
            else:
                print("Item not found.")

        elif choice == 4:
            name = input("Enter item name to search: ")
            if name in inventory:
                print(f"{name} → Quantity: {inventory[name]['quantity']}, Price: {inventory[name]['price']}")
            else:
                print("Item not found.")

        elif choice == 5:
            if inventory:
                print("\n--- Current Inventory ---")
                for item, details in inventory.items():
                    print(f"{item} → Quantity: {details['quantity']}, Price: {details['price']}")
            else:
                print("Inventory is empty.")

        elif choice == 6:
            print("Exiting Inventory System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the system
inventory_system()

