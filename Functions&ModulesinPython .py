# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage
num = 5
print(f"Factorial of {num} is: {factorial(num)}")



import math

# Ask user for input
num = float(input("Enter a number: "))

# Perform calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)   # log base e
sine_value = math.sin(num)    # input is in radians

# Display results
print(f"Square root of {num} is: {square_root}")
print(f"Natural logarithm of {num} is: {natural_log}")
print(f"Sine of {num} radians is: {sine_value}")
