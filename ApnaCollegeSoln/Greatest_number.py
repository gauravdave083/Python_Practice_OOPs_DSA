## WAP to find the greatest of 3 numbers entered by the user.

# Prompt user for input
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Compare the numbers using if-else statements
if number1 >= number2 and number1 >= number3:
    greatest_number = number1
elif number2 >= number1 and number2 >= number3:
    greatest_number = number2
else:
    greatest_number = number3

# Print the result
print("The greatest number is:", greatest_number)