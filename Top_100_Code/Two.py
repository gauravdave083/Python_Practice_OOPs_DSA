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


# 3. Leap Year

year = int(input("Enter the year: "))

if year%400 ==0 or year%4==0 and year%100!=0:
    print("Its a Leap Year")
else:
    print("Not a Leap Year")


# 4. Prime number

num = 11
flag = 0

for i in range(2, num):
    if num%i == 0:
        flag = 1
        break
if flag == 1:
    print("Not Prime")
else: 
    print("Prime")

