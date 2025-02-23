# 1. Check if a number is positive and negative in Python

number = int(input("Enter the number: "))

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")


# 2. Python Program To Check Whether A Number Is Odd or Even

number = int(input("Enter the number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Python Program to Find the Sum of First N Natural Numbers

number = int(input("Enter the number: "))

sum = 0

for i in range(0, number + 1):
    sum += i
print(sum)

# OR

number = 8

sum = int((number * (number +1))/2)
print(sum)


# 4. Find the Sum of Numbers in a given Range in Python

num1 = int(input("Enter the First Number:"))
num2 = int(input("Enter the Second Number: "))
sum = 0

for i in range(num1, num2+1):
    sum+=i
print(sum)

