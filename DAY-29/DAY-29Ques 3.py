# Write a program to Create menu-driven string operations system.

def string_system():
    while True:
        print("\n--- Menu Driven String Operations ---")
        print("1. Reverse string")
        print("2. Check palindrome")
        print("3. Count vowels and consonants")
        print("4. Find length of string")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting String System. Goodbye!")
            break

        s = input("Enter a string: ")

        if choice == 1:
            print("Reversed String:", s[::-1])

        elif choice == 2:
            if s == s[::-1]:
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")

        elif choice == 3:
            vowels = "aeiouAEIOU"
            v_count = sum(1 for ch in s if ch in vowels)
            c_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
            print(f"Vowels: {v_count}, Consonants: {c_count}")

        elif choice == 4:
            length = 0
            for _ in s:  # manual count without len()
                length += 1
            print("Length of string:", length)

        else:
            print("Invalid choice. Please try again.")

# Run the system
string_system()
