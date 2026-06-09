# Function to check Perfect Number
def is_perfect(num):
    sum_of_divisors = 0
    
    # Find proper divisors (excluding the number itself)
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    
    return sum_of_divisors == num

n = int(input("Enter a number: "))
if is_perfect(n):
    print(n, "is a Perfect Number")
else:
    print(n, "is not a Perfect Number")
              

              # OR

#def is_perfect(num):
#    return num == sum([i for i in range(1, num) if num % i == 0])

#n = int(input("Enter a number: "))
#print("Perfect Number" if is_perfect(n) else "Not Perfect Number")
