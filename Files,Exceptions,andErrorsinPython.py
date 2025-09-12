# Task 1: Read a File and Handle Errors

try:
    # Open file in read mode
    with open("sample.txt", "r") as file:
        print("File content:")
        for line in file:
            print(line.strip())   # strip() removes extra spaces/newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")


# Task 2: Write and Append Data to a File

# Step 1: Take user input and write to file
data = input("Enter some data to write into the file: ")
with open("output.txt", "w") as file:
    file.write(data + "\n")

# Step 2: Append additional data
extra_data = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(extra_data + "\n")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
