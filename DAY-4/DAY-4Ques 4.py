# Program to print Armstrong numbers in a range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Armstrong numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    total = 0
    digits = len(str(num))
    for digit in str(num):
        total += int(digit) ** digits
    if total == num:
        print(num)
      
            #OR

# Simple Armstrong numbers in a range

#start = int(input("Enter start: "))
#end = int(input("Enter end: "))

#print("Armstrong numbers between", start, "and", end, ":")

#for num in range(start, end + 1):
#    if num == sum(int(digit) ** len(str(num)) for digit in str(num)):
#        print(num)
