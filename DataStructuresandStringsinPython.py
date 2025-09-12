# Task 1: Dictionary of Student Marks

# Step 1: Create a dictionary
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eva": 88
}

# Step 2: Ask user for a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks if student exists
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")


# Task 2: List Slicing

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_list = first_five[::-1]

# Step 4: Print results
print("Extracted first five elements:", first_five)
print("Reversed list:", reversed_list)
