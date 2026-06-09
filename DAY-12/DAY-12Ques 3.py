# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter number of terms: "))
print("Fibonacci series:", fibonacci(n))
      
             # OR

# Recursive function to find nth Fibonacci term
#def fib(n):
#  if n <= 1:
#        return n
#    else:
#        return fib(n-1) + fib(n-2)

#n = int(input("Enter number of terms: "))
#print("Fibonacci series:", [fib(i) for i in range(n)])
