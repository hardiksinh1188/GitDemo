# Task 1: Check if a Number is Even or Odd

# Taking input from the user
num = int(input("Enter an integer: "))

# Checking even or odd using if-else
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")





# Task 2: Sum of Integers from 1 to 50

# Initialize sum
total_sum = 0

# Using for loop to calculate sum
for i in range(1, 51):
    total_sum += i

# Display the result
print("The sum of integers from 1 to 50 is:", total_sum)
