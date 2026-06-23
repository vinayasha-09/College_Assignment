# Write a program to Create ATM simulation.

def atm_simulation():
    balance = 1000  # Initial balance
    pin = 1234      # Example PIN

    print("Welcome to the ATM Simulation!")
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin != pin:
        print("Incorrect PIN ")
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Your balance is ₹{balance}")
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{balance}")
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance ")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully. New balance: ₹{balance}")
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
atm_simulation()
