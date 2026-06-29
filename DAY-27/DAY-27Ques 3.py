# Write a program to Create salary management system.

salaries = {}  # Dictionary to store salary records

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    salaries[emp_id] = {"Name": name, "Salary": salary}
    print("Employee salary record added successfully!\n")

def display_employees():
    if not salaries:
        print("No records found.\n")
    else:
        print("\n--- Salary Records ---")
        for emp_id, info in salaries.items():
            print(f"ID: {emp_id}, Name: {info['Name']}, Salary: {info['Salary']}")
        print()

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    if emp_id in salaries:
        print(f"Record found: ID: {emp_id}, Name: {salaries[emp_id]['Name']}, Salary: {salaries[emp_id]['Salary']}\n")
    else:
        print("Record not found.\n")

def update_salary():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id in salaries:
        new_salary = float(input("Enter new Salary: "))
        salaries[emp_id]["Salary"] = new_salary
        print("Salary updated successfully!\n")
    else:
        print("Record not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if emp_id in salaries:
        del salaries[emp_id]
        print("Record deleted successfully!\n")
    else:
        print("Record not found.\n")

def menu():
    while True:
        print("=== Salary Management System ===")
        print("1. Add Employee Salary Record")
        print("2. Display All Salary Records")
        print("3. Search Employee Salary Record")
        print("4. Update Employee Salary")
        print("5. Delete Employee Salary Record")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_salary()
        elif choice == "5":
            delete_employee()
        elif choice ==  "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()