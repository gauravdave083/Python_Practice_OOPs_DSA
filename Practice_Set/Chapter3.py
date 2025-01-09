# Question 1

UserName = str(input("User Name : "))
print("Good Afternoon", UserName)



# Question 2

letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

Name = str(input("Enter Name: "))
Date = str(input("Enter the date: "))

print(letter.replace("<|Name|>", Name).replace("<|Date|>", Date))


# Question 3

name = " harry  is a  good  boy and"

print(name.find("  "))

