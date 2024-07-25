#   3. Multiplication Table Printer
# 
#   Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Which table do you need till 10: "))

for i in  range(1, 11):
    if i == 5:
        continue           
    
    """ continue is use to skip """
    
    print(number, 'x', i, '=', number * i)