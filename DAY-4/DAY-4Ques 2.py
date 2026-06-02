# Program to find nth Fibonacci term

n = int(input("Enter the term number (n): "))

a, b = 0, 1

if n == 1:
    print("Fibonacci term at position", n, "is", a)
elif n == 2:
    print("Fibonacci term at position", n, "is", b)
else:
    for i in range(3, n + 1):
        a, b = b, a + b
    print("Fibonacci term at position", n, "is", b)