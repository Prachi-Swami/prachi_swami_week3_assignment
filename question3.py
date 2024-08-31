# mplement a program that calculates the
# Fibonacci sequence up to a specified number
# using both iterative and recursive approaches.
# Calculate Fibonacci sequence up to a specified number iteratively
def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence
#Calculate the nth Fibonacci number recursively
def fibonacci_recursive(n):
 
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
num = 10
print(f"Fibonacci sequence up to {num} (iterative): {fibonacci_iterative(num)}")

print(f"Fibonacci sequence up to {num} (recursive): {[fibonacci_recursive(i) for i in range(num+1)]}")
