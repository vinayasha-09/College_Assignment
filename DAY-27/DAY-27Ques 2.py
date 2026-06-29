# Employee Management System

employees = {}  # Dictionary to store employee records

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")
    employees[emp_id] = {"Name": name, "Department": department, "Salary": salary}
    print("Employee added successfully!\n")

def display_employees():
    if not employees:
        print("No records found.\n")
    else:
        print("\n--- Employee Records ---")
        for emp_id, info in employees.items():
            print(f"ID: {emp_id}, Name: {info['Name']}, Department: {info['Department']}, Salary: {info['Salary']}")
        print()

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    if emp_id in employees:
        info = employees[emp_id]
        print(f"Record found: ID: {emp_id}, Name: {info['Name']}, Department: {info['Department']}, Salary: {info['Salary']}\n")
    else:
        print("Record not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id in employees:
        name = input("Enter new Name: ")
        department = input("Enter new Department: ")
        salary = input("Enter new Salary: ")
        employees[emp_id] = {"Name": name, "Department": department, "Salary": salary}
        print("Record updated successfully!\n")
    else:
        print("Record not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Record deleted successfully!\n")
    else:
        print("Record not found.\n")

def menu():
    while True:
        print("=== Employee Management System ===")
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
