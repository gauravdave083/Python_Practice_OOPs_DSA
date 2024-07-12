# Print numbers from 1 to 100
for i in range(1, 101):
    print(i)


# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# List of elements
elements = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Print elements using a loop
for element in elements:
    print(element)


# Print numbers from 1 to 100. (use range)
for i in range (1, 101):
    print(i)



# WAP to find the factorial of first n numbers. (using for)

# Prompt user for input
n = int(input("Enter the number of numbers: "))

# Calculate the factorial of the first n numbers using a loop
factorials = []
for i in range(1, n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    factorials.append(factorial)

# Print the list of factorials
print("Factorials of the first", n, "numbers:")
for i, factorial in enumerate(factorials, start=1):
    print(f"{i}: {factorial}")