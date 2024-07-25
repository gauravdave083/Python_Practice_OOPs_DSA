#   5. Find the First Non-Repeated Character
#
#   Problem: Given a string, find the first non-repeated character.

string = str(input("give your input string here: "))

for char in string:
    print(char)
    if string.count(char) == 1:
        print("Character not getting repeated first is: ",char) 
        break