# Create a Python module that contains functions
# for common mathematical operations (e.g.,
# factorial, greatest common divisor). Write a script
# that imports this module and uses its functions.
import Math_module as m
number = 5
print(f"Factorial of {number}: {m.factorial(number)}")

num1 = 36
num2 = 60
print(f"GCD of {num1} and {num2}: {m.gcd(num1, num2)}")
