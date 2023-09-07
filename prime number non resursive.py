def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes(n):
    if n < 2:
        print("There are no prime numbers in the specified range.")
        return

    print("Prime numbers from 2 to", n, "are:")
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")
 
num = int(input("Enter a positive integer (n): "))
 
display_primes(num)
