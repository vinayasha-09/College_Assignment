# # Write a program to Create student record management system.

students = {}  # Dictionary to store student records

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students[roll] = {"Name": name, "Course": course}
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No records found.\n")
    else:
        print("\n--- Student Records ---")
        for roll, info in students.items():
            print(f"Roll: {roll}, Name: {info['Name']}, Course: {info['Course']}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print(f"Record found: Roll: {roll}, Name: {students[roll]['Name']}, Course: {students[roll]['Course']}\n")
    else:
        print("Record not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new Name: ")
        course = input("Enter new Course: ")
        students[roll] = {"Name": name, "Course": course}
        print("Record updated successfully!\n")
    else:
        print("Record not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Record deleted successfully!\n")
    else:
        print("Record not found.\n")

def menu():
    while True:
        print("=== Student Record Management System ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")
