def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes
start = 10
end = 50
primes = find_primes_in_range(start, end)
print(f"Prime numbers between {start} and {end}: {primes}")
