#ASSIGNMENT 5:Task 1 and Task 2 are combined.
# Task 1: Create a Dictionary of Student Marks
# Create dictionary of student names and marks
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 67,
    "Eva": 90
}

name = input("Enter the student's name: ")
# Retrieve marks or show error if not found
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
    
#Task 2: Demonstrate List Slicing 
#Create list of numbers from 1 to 10
numbers = list(range(1, 11))
print("\nOriginal List:", numbers)

#Extract first five elements
first_five = numbers[:5]

#Reverse the extracted elements
reversed_list = first_five[::-1]

print("Extracted first five elements:", first_five)
print("Reversed extracted list:", reversed_list)


