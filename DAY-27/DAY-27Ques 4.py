# Write a program to Create marksheet generation system.

marksheets = {}  # Dictionary to store student marksheets

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    subjects = int(input("Enter number of subjects: "))
    
    marks = []
    for i in range(subjects):
        m = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(m)
    
    total = sum(marks)
    percentage = total / subjects
    
    # Assign grade based on percentage
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"
    
    marksheets[roll] = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }
    print("Marksheet generated successfully!\n")

def display_marksheets():
    if not marksheets:
        print("No records found.\n")
    else:
        print("\n--- Marksheet Records ---")
        for roll, info in marksheets.items():
            print(f"Roll: {roll}, Name: {info['Name']}, Marks: {info['Marks']}, "
                  f"Total: {info['Total']}, Percentage: {info['Percentage']:.2f}%, Grade: {info['Grade']}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in marksheets:
        info = marksheets[roll]
        print(f"\n--- Marksheet ---\nRoll: {roll}, Name: {info['Name']}")
        print(f"Marks: {info['Marks']}")
        print(f"Total: {info['Total']}, Percentage: {info['Percentage']:.2f}%, Grade: {info['Grade']}\n")
    else:
        print("Record not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in marksheets:
        del marksheets[roll]
        print("Record deleted successfully!\n")
    else:
        print("Record not found.\n")

def menu():
    while True:
        print("=== Marksheet Generation System ===")
        print("1. Add Student Marksheet")
        print("2. Display All Marksheets")
        print("3. Search Student Marksheet")
        print("4. Delete Student Marksheet")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_marksheets()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
