#   4. Reverse a String
#
#   Problem: Reverse a string using a loop.

str = str(input("Give here your input string: "))

reversed_str = ""

for char in str:
    reversed_str = char + reversed_str
    
print("This is your reversed string: ",reversed_str)