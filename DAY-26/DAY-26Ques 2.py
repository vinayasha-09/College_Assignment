# Write a program to check voting eligibility.

def voting_eligibility():
    print("Welcome to the Voting Eligibility System!")
    
    # Take user input for age
    age = int(input("Enter your age: "))
    
    # Check eligibility
    if age >= 18:
        print("You are eligible to vote ")
    else:
        print("You are NOT eligible to vote ")
        print(f"You will be eligible after {18 - age} year(s).")

# Run the program
voting_eligibility()
