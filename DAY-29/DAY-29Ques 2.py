# Write a program to Create menu-driven array operations system.

def array_system():
    arr = []

    while True:
        print("\n--- Menu Driven Array Operations ---")
        print("1. Insert element")
        print("2. Delete element")
        print("3. Search element")
        print("4. Display array")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            element = int(input("Enter element to insert: "))
            arr.append(element)
            print(f"{element} inserted successfully.")

        elif choice == 2:
            element = int(input("Enter element to delete: "))
            if element in arr:
                arr.remove(element)
                print(f"{element} deleted successfully.")
            else:
                print("Element not found in array.")

        elif choice == 3:
            element = int(input("Enter element to search: "))
            if element in arr:
                print(f"{element} found at position {arr.index(element)}")
            else:
                print("Element not found in array.")

        elif choice == 4:
            print("Current Array:", arr)

        elif choice == 5:
            print("Exiting Array System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the system
array_system()
