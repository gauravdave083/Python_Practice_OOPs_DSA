# 1. Sum of Digits of a Number in Python

num = input("Enter Number: ")
sum = 0 

for i in num:
    sum = sum + int(i)

print(sum)


# 2. Reverse a Number in Python

num = input("Enter a number: ")
reversed_num = (str(num)[::-1])
print(reversed_num)

# OR

num = 1234
temp = num
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)


# Palindrome Program in Python

num = 1221
temp = num
reversed = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

if num == reverse:
    print('Palindrome')
else:
    print("Not a palindrome")