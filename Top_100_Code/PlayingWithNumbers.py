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

year = 2022

if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("leap Year")
else:
    print("Not a Leap Year")



# Prime Number

num = 3
flag = 0
for i in range(2,num):
    if num%i == 0:
        flag == 1
        break
if flag == 1:
    print("Not Prime")
else:
    print("Prime")



# Sum of Digits of a Number

num = input("Enter a number: ")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)

#------------------OR--------------------

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # find last digit
        n //= 10         # assign n
    return total

print(sum_of_digits(472))




# Reverse A Number

num = 1234
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)



# Number Palindrom Or Not

num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

if num == reverse:
    print("palindrome")
else:
    print("not palindrome")