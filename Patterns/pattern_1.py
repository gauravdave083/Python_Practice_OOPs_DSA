#   use nested loop wherever possible
#   For loop + while loop

"""
1. Solid Square Pattern
Create a solid square of asterisks

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

"""

#    CODE

n = 5

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ") 
    print()