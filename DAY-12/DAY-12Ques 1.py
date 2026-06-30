#Write a program to Write function for palindrome.

def is_palindrome(num):
    temp = num
    rev = 0
    
    while temp > 0:
        digit = temp % 10       # extract last digit
        rev = rev * 10 + digit  # build reversed number
        temp //= 10             # remove last digit
    
    return num == rev

n = int(input("Enter a number: "))
if is_palindrome(n):
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")

             # OR
             
#def is_palindrome(num):
#    return str(num) == str(num)[::-1]

#n = int(input("Enter a number: "))
#if is_palindrome(n):
#    print(n, "is a palindrome")
#else:
#    print(n, "is not a palindrome")
