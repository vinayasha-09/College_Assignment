#Write a program to Develop complete mini project using arrays, strings and functions.

# Uses arrays (lists), strings, and functions

roll_numbers = []
names = []
courses = []
marks = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    mark = input("Enter Marks: ")
    roll_numbers.append(roll)
    names.append(name)
    courses.append(course)
    marks.append(mark)
    print("Student added successfully!\n")

def display_students():
    if not roll_numbers:
        print("No student records found.\n")
    else:
        print("\n--- Student Records ---")
        for i in range(len(roll_numbers)):
            print(f"Roll: {roll_numbers[i]}, Name: {names[i]}, Course: {courses[i]}, Marks: {marks[i]}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in roll_numbers:
        i = roll_numbers.index(roll)
        print(f"Record found: Roll: {roll_numbers[i]}, Name: {names[i]}, Course: {courses[i]}, Marks: {marks[i]}\n")
    else:
        print("Record not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in roll_numbers:
        i = roll_numbers.index(roll)
        names[i] = input("Enter new Name: ")
        courses[i] = input("Enter new Course: ")
        marks[i] = input("Enter new Marks: ")
        print("Record updated successfully!\n")
    else:
        print("Record not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in roll_numbers:
        i = roll_numbers.index(roll)
        del roll_numbers[i]
        del names[i]
        del courses[i]
        del marks[i]
        print("Record deleted successfully!\n")
    else:
        print("Record not found.\n")

def highest_marks():
    if not marks:
        print("No records to evaluate.\n")
    else:
        max_mark = max(marks, key=int)
        i = marks.index(max_mark)
        print(f"Topper: Roll: {roll_numbers[i]}, Name: {names[i]}, Marks: {marks[i]}\n")

def menu():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
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
            highest_marks()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
