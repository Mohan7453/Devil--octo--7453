#ASSIGNMENT 4:Task 1 and Task 2 are combined
#Task 1:Read a File and handle error data 
try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for line in file:
            print(line.strip())  # strip() removes extra newline characters
except FileNotFoundError:
    print("Error: The file 'Demo.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
# Task 2:Write and Append data to a File
# Step 1: Take user input and write it to a file
data = input("\nEnter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(data + "\n")
    print("Data successfully  written to output.txt")

# Step 2: Append additional data to the same file
more_data = input("\nEnter additional text to append: ")
print("Data successfully  written to output.txt")
with open("output.txt", "a") as file:
    file.write(more_data + "\n")

# Step 3: Read and display the final content of the file
print("\nFina content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
