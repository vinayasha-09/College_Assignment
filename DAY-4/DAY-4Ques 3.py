# Program to check Armstrong number

num = int(input("Enter a number: "))
sum = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

              #OR
#num = int(input("Enter a number: "))
#total = 0
#for digit in str(num):
#    total += int(digit) ** len(str(num))

#if total == num:
#    print("Armstrong number")
#else:
#    print("Not Armstrong number")
