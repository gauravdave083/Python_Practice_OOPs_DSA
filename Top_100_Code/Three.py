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


# 3. Palindrome Program in Python

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


# 4. Find the Nth Term of a Fibonacci Series in Python

def Fibonacci(n):
    if n < 2:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

n = 6
print(Fibonacci(n-1))


# 5. Whrite a program to print fibonacci series upto n terms in python

number = 10
n1, n2 = 0, 1

print("Fibonacci Series:", n1, n2, end=" ")

for i in range(2, number):
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()