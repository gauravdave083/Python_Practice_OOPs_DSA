# 1. Find the greatest of two numbers in python

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greatest of two numbers")
else: 
    print(num2, "is greatest of two numbers")


# 2. Find the Greatest of te three numbers in python

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num2 > num3:
    print(num1, "is greatest")
elif num2 > num1 and num2 > num3:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")