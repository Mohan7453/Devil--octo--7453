# Assignment 2
# Task 1 and Task 2 are combined
# Task 1 check if a number is even or odd using if-else
num=int(input("Enter the number :"))
if(num %2 !=0):
      print(num,"is an odd number.")
else:
      print(num,"is an even number.")
      
#Task 2 sum of integers frm 1 to 50 using a loop
total_sum = 0
# Loop through numbers from 1 to 50
for number in range(1, 51):
    total_sum += number  
# Display the final sum
print("The sum of numbers from 1 to 50 is:", total_sum)

      




