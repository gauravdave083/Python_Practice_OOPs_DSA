#WAP to check if a number is a multiple of 7 or not.

number = int(input("Enter the number: "))

def check():
    if number%7 == 0:
        print( number,"is divisible by 7")
    else:
        print( number,"is not divisible by 7")
        
check()