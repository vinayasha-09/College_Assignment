# write a program to check whather the no. is palindrome or not

num = input("Enter a number: ")
if num == num[::-1]:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")