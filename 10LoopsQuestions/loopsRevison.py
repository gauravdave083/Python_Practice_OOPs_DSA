# PRINT HELLO 100 Times: 

def printHello(n):
    for i in range(n+1):
        print("Hello")

n = 100
printHello(n)

# Print numbers from 1 to 100

i = 1
while i <=100:
    print(i)
    i +=1

# Print numbers from 100 to 1

i = 100
while i >= 1:
    print(i)
    i -= 1

# Print multiplication table off a number n

n = 3
i = 1
while i <=10:
    print(n, " * ", i, " = ", n*i)
    i += 1

# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx <= len(nums):
    print(idx*idx)
    idx += 1

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 36
i = 0

while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    i += 1