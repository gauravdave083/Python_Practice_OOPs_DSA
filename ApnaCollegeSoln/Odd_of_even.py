def OddOrEven(number):
    if number % 2 == 0:
            return "Even"
    else: 
            return "Odd"
      
#Take input for the problem
number = int(input("Enter the number: "))
      
result = OddOrEven(number)
print(f"The number is {result}.")