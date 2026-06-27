# Write a program to Create mini employee management system.

emp_ids = []
names = []
departments = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    emp_ids.append(emp_id)
    names.append(name)
    departments.append(dept)
    print("Employee added successfully!\n")

def display_employees():
    if not emp_ids:
        print("No employee records found.\n")
    else:
        print("\n--- Employee Records ---")
        for i in range(len(emp_ids)):
            print(f"ID: {emp_ids[i]}, Name: {names[i]}, Department: {departments[i]}")
        print()

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    if emp_id in emp_ids:
        i = emp_ids.index(emp_id)
        print(f"Record found: ID: {emp_ids[i]}, Name: {names[i]}, Department: {departments[i]}\n")
    else:
        print("Record not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id in emp_ids:
        i = emp_ids.index(emp_id)
        names[i] = input("Enter new Name: ")
        departments[i] = input("Enter new Department: ")
        print("Record updated successfully!\n")
    else:
        print("Record not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if emp_id in emp_ids:
        i = emp_ids.index(emp_id)
        del emp_ids[i]
        del names[i]
        del departments[i]
        print("Record deleted successfully!\n")
    else:
        print("Record not found.\n")

def menu():
    while True:
        print("=== Mini Employee Management System ===")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
