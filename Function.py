# Assignment 3
# Task 1 and Task 2 are combined
# Task 1 calculate factorial using function
def factorial(n):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
number=int(input("Enter a number: "))
result= factorial(number)
#calling the function and printing the result
print(f"The factorial of {number} is: {result}")

#Task 2 Using the math module for calculation
from math import *
num=int(input("Enter the number :"))
print("Square Root :",sqrt(num))
print("Sine :",sin(num))
print("Logarithm :",log(25))