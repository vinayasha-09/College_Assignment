# Function to check Armstrong number.

def is_armstrong(num):
    digits = len(str(num))   # count digits
    total = 0
    
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    
    return num == total

n = int(input("Enter a number: "))
if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")

             # OR

#def is_armstrong(num):
#    return num == sum(int(digit) ** len(str(num)) for digit in str(num))

#n = int(input("Enter a number: "))
#print("Armstrong number" if is_armstrong(n) else "Not Armstrong number")
