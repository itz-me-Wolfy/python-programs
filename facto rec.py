def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        
        return n * factorial(n - 1)

 
n = int(input("Enter a positive integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
