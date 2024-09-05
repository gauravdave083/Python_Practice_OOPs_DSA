# sancha - object
# GUJIYA -easily bana lo

# Basic of object oriented programming




# # Basic Class And Object
# Problem: Create A Car class with attribute liie brand and model. Then create an instance of this  class


# --------------------------------------------------------------------------------------------------------------------- #


# A WAY TO WRITE

class Car:
    brand = None
    model = None

my_car = Car()     


# BETTER WAY TO WRITE 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyato", "Corrala")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)



