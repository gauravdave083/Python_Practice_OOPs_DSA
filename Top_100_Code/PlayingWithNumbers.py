# Number is positive or not

number = 20

if number > 0:
    print("This number is positive")
elif number == 0:
    print("This number is 0")
else:
    print("Number is zero")



# Number is even or odd

number = 3

if number % 2 == 0:
    print("Number is positive")
else:
    print("Negative")



# First N natural numbers

num = 8
sum = 0

for i in range(1, num+1):
    sum += i 
print(sum)

print(int(num*(num+1)/2))



# Sum of N natural numbers
num1 = 2
num2 = 7

sum = 0

for i in range(num1, num2+1):
    sum+=i
print(sum)



# Greatest Of two Numbers

num1 = 61
num2 = 57

if num1 > num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")



# Greatest of three Number

num1, num2, num3 = 3, 4, 5

if num1 > num2 and num1 > num3:
    print(num1, "is greatest")
elif num2 > num1 and num2 > num3:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")



# Leap Year

year = 2020

