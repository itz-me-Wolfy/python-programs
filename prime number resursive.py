def is_prime(num, divisor=2):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % divisor == 0:
        return False
    if divisor * divisor > num:
        return True
    return is_prime(num, divisor + 1)

def display_primes(n, current=2):
    if current <= n:
        if is_prime(current):
            print(current)
        display_primes(n, current + 1)
num = int(input("Enter a positive integer (n): "))
print(f"Prime numbers from 2 to {num}:")
display_primes(num)
