
#Calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Calculate the greatest common divisor of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
