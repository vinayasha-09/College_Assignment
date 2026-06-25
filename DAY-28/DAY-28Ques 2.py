# Write a program to Create bank account system.2

bank_accounts = {}  # Dictionary to store accounts

def create_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    bank_accounts[acc_no] = {"Name": name, "Balance": balance}
    print("Account created successfully!\n")

def display_accounts():
    if not bank_accounts:
        print("No accounts found.\n")
    else:
        print("\n--- Bank Accounts ---")
        for acc_no, info in bank_accounts.items():
            print(f"Acc No: {acc_no}, Name: {info['Name']}, Balance: ₹{info['Balance']}")
        print()

def search_account():
    acc_no = input("Enter Account Number to search: ")
    if acc_no in bank_accounts:
        print(f"Account found: Acc No: {acc_no}, Name: {bank_accounts[acc_no]['Name']}, Balance: ₹{bank_accounts[acc_no]['Balance']}\n")
    else:
        print("Account not found.\n")

def deposit_money():
    acc_no = input("Enter Account Number: ")
    if acc_no in bank_accounts:
        amount = float(input("Enter amount to deposit: "))
        bank_accounts[acc_no]['Balance'] += amount
        print(f"₹{amount} deposited successfully. New Balance: ₹{bank_accounts[acc_no]['Balance']}\n")
    else:
        print("Account not found.\n")

def withdraw_money():
    acc_no = input("Enter Account Number: ")
    if acc_no in bank_accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount > bank_accounts[acc_no]['Balance']:
            print("Insufficient balance \n")
        else:
            bank_accounts[acc_no]['Balance'] -= amount
            print(f"₹{amount} withdrawn successfully. New Balance: ₹{bank_accounts[acc_no]['Balance']}\n")
    else:
        print("Account not found.\n")

def delete_account():
    acc_no = input("Enter Account Number to delete: ")
    if acc_no in bank_accounts:
        del bank_accounts[acc_no]
        print("Account deleted successfully!\n")
    else:
        print("Account not found.\n")

def menu():
    while True:
        print("=== Bank Account System ===")
        print("1. Create Account")
        print("2. Display All Accounts")
        print("3. Search Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Delete Account")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            display_accounts()
        elif choice == "3":
            search_account()
        elif choice == "4":
            deposit_money()
        elif choice == "5":
            withdraw_money()
        elif choice == "6":
            delete_account()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
